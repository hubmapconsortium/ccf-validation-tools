"""
Filter Ubergraph's N-Quads dump (ubergraph.nq.gz) down to the UBERON/CL/PCL
subset queried by uberongraph_tools.py, writing one N-Triples file per target
named graph:

  ontology.nt      -> <http://reasoner.renci.org/ontology>      triples about UBERON/CL/PCL terms
                                                                 (labels, subClassOf, IC, ...)
  redundant.nt     -> <http://reasoner.renci.org/redundant>     inferred edges between UBERON/CL/PCL terms
  nonredundant.nt  -> <http://reasoner.renci.org/nonredundant>  non-redundant edges between them
  union.nt         -> <http://purl.org/ccf/ubergraph-subset/union>
                      everything else the FROM-less queries (labels, images, annotations,
                      ontology versions) read from the union of all graphs: term triples from
                      the per-ontology graphs, owl:Axiom annotations on terms, annotation
                      property declarations, and uberon/cl/pcl owl:versionInfo.

Triples pointing to blank nodes (OWL restrictions) are dropped; no query uses them.

The dump is written by Blazegraph from its SPOC index, so all lines with the
same subject are contiguous. Blocks are cut at subject boundaries, which lets
each block be processed independently in a single pass (decompression with
rapidgzip, filtering in worker processes over shared memory).

Usage: python ubergraph_subset.py <ubergraph.nq.gz> <out dir> [--workers N] [--threads N]
"""
import argparse
import os
import sys
import time
from concurrent.futures import FIRST_COMPLETED, ProcessPoolExecutor, wait
from multiprocessing import shared_memory

try:
  import rapidgzip
except ImportError:  # pragma: no cover - much slower fallback
  rapidgzip = None
  import gzip

OBO = b'<http://purl.obolibrary.org/obo/'
TERM_PREFIXES = (OBO + b'UBERON_', OBO + b'CL_', OBO + b'PCL_')
G_ONTOLOGY = b'<http://reasoner.renci.org/ontology>'
G_REDUNDANT = b'<http://reasoner.renci.org/redundant>'
G_NONREDUNDANT = b'<http://reasoner.renci.org/nonredundant>'
ANNOTATED_SOURCE = b'<http://www.w3.org/2002/07/owl#annotatedSource> '
AP_DECLARATION = (b' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> '
                  b'<http://www.w3.org/2002/07/owl#AnnotationProperty> ')
VERSION_INFO = b' <http://www.w3.org/2002/07/owl#versionInfo> '
ONTOLOGY_IRIS = (OBO + b'uberon/uberon-base.owl>', OBO + b'cl/cl-base.owl>', OBO + b'pcl/pcl-base.owl>')
OUTPUTS = ('ontology', 'redundant', 'nonredundant', 'union')

BLOCK = 64 * 1024 * 1024
SLACK = 16 * 1024 * 1024  # room for a subject group carried over to the next block


def split_quad(line):
  """(s, p, o, g) tokens of an N-Quads line without its trailing ' .'."""
  s, p, rest = line.split(b' ', 2)
  o, g = rest[:-2].rsplit(b' ', 1)
  return s, p, o, g


def triple(s, p, o):
  return b'%s %s %s .' % (s, p, o)


def line_at(data, pos):
  """Return (start, end) of the line containing pos; end excludes the newline."""
  start = data.rfind(b'\n', 0, pos) + 1
  end = data.find(b'\n', pos)
  return start, (len(data) if end < 0 else end)


def subject_group(data, start):
  """Return (start, end) of the run of lines sharing the subject of the line at `start`."""
  subject = data[start:data.index(b' ', start)] + b' '
  gs = start
  while gs > 0:
    prev = data.rfind(b'\n', 0, gs - 1) + 1
    if data.startswith(subject, prev):
      gs = prev
    else:
      break
  ge = start
  while ge < len(data) and data.startswith(subject, ge):
    nl = data.find(b'\n', ge)
    ge = len(data) if nl < 0 else nl + 1
  return gs, ge


def find_all(data, needle):
  pos = data.find(needle)
  while pos >= 0:
    yield pos
    pos = data.find(needle, pos + len(needle))


def filter_block(data):
  out = {k: [] for k in OUTPUTS}

  # 1. Lines whose subject is a UBERON/CL/PCL term.
  for prefix in TERM_PREFIXES:
    starts = [0] if data.startswith(prefix) else []
    starts += [p + 1 for p in find_all(data, b'\n' + prefix)]
    for start in starts:
      end = data.find(b'\n', start)
      s, p, o, g = split_quad(data[start:(len(data) if end < 0 else end)])
      if o.startswith(b'_:'):
        continue
      if g == G_ONTOLOGY:
        out['ontology'].append(triple(s, p, o))
      elif g == G_REDUNDANT or g == G_NONREDUNDANT:
        if o.startswith(TERM_PREFIXES):
          out['redundant' if g == G_REDUNDANT else 'nonredundant'].append(triple(s, p, o))
      else:
        out['union'].append(triple(s, p, o))

  # 2. Subject groups: owl:Axiom blank nodes annotating a term, and annotation properties.
  seen = set()
  def emit_group(pos, keep_blank_objects):
    start, _ = line_at(data, pos)
    gs, ge = subject_group(data, start)
    if gs in seen or data.startswith(TERM_PREFIXES, gs):  # term subjects are handled above
      return
    seen.add(gs)
    for line in data[gs:ge].splitlines():
      s, p, o, g = split_quad(line)
      if keep_blank_objects or not o.startswith(b'_:'):
        out['union'].append(triple(s, p, o))

  for prefix in TERM_PREFIXES:
    for pos in find_all(data, ANNOTATED_SOURCE + prefix):
      start, _ = line_at(data, pos)
      if data.startswith(b'_:', start):
        emit_group(pos, True)
  for pos in find_all(data, AP_DECLARATION):
    emit_group(pos, False)

  # 3. Source ontology versions.
  for pos in find_all(data, VERSION_INFO):
    start, end = line_at(data, pos)
    s, p, o, g = split_quad(data[start:end])
    if s in ONTOLOGY_IRIS:
      out['union'].append(triple(s, p, o))

  return {k: b'\n'.join(v) + b'\n' for k, v in out.items() if v}


_BUFFERS = None


def _init_worker(names):
  global _BUFFERS
  _BUFFERS = [shared_memory.SharedMemory(name=n) for n in names]


def _work(index, length):
  return filter_block(bytes(_BUFFERS[index].buf[:length]))


def subject_boundary(data):
  """Length of the prefix of `data` that ends at a subject boundary (complete groups only)."""
  last_nl = data.rfind(b'\n')
  if last_nl < 0:
    return 0
  last_start = data.rfind(b'\n', 0, last_nl) + 1
  subject = data[last_start:data.index(b' ', last_start)] + b' '
  if data.startswith(subject):
    return last_nl + 1  # one giant group; shouldn't happen, but never stall
  first = data.find(b'\n' + subject)
  return first + 1


def open_dump(path, threads):
  if rapidgzip is not None:
    return rapidgzip.open(path, parallelization=threads)
  print('rapidgzip not installed; falling back to (slow) gzip', file=sys.stderr)
  return gzip.open(path, 'rb')


def main():
  parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
  parser.add_argument('dump', help='ubergraph.nq.gz')
  parser.add_argument('out_dir')
  parser.add_argument('--workers', type=int, default=max(1, (os.cpu_count() or 2) - 1))
  parser.add_argument('--threads', type=int, default=max(1, os.cpu_count() or 1),
                      help='decompression threads')
  args = parser.parse_args()
  os.makedirs(args.out_dir, exist_ok=True)

  started = time.time()
  n_buffers = args.workers * 2
  buffers = [shared_memory.SharedMemory(create=True, size=BLOCK + SLACK) for _ in range(n_buffers)]
  files = {k: open(os.path.join(args.out_dir, k + '.nt'), 'wb') for k in OUTPUTS}
  counts = dict.fromkeys(OUTPUTS, 0)
  total = 0

  def collect(future):
    for k, chunk in future.result().items():
      files[k].write(chunk)
      counts[k] += chunk.count(b'\n')

  try:
    with open_dump(args.dump, args.threads) as dump, \
         ProcessPoolExecutor(args.workers, initializer=_init_worker,
                             initargs=([b.name for b in buffers],)) as pool:
      free = list(range(n_buffers))
      pending = {}
      tail = b''
      while True:
        if not free:
          done, _ = wait(pending, return_when=FIRST_COMPLETED)
          for future in done:
            free.append(pending.pop(future))
            collect(future)
        chunk = dump.read(BLOCK)
        data = tail + chunk
        cut = subject_boundary(data) if chunk else len(data)
        if cut > BLOCK + SLACK:
          raise RuntimeError('subject group larger than buffer slack')
        tail = data[cut:]
        if cut:
          index = free.pop()
          buffers[index].buf[:cut] = data[:cut]
          pending[pool.submit(_work, index, cut)] = index
          total += cut
        if not chunk:
          break
      for future in pending:
        collect(future)
  finally:
    for f in files.values():
      f.close()
    for b in buffers:
      b.close()
      b.unlink()

  elapsed = time.time() - started
  print(f'{total / 1e9:.1f} GB of N-Quads in {elapsed:.0f}s; triples written: {counts}')


if __name__ == '__main__':
  main()
