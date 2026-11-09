"""
Check that two Ubergraph backends give the same validation results.

Runs generate_class_graph_template (the step that sends all the Ubergraph
queries) on ASCT+B tables once per backend, writes every output in a sorted,
diff-friendly form, and reports which outputs differ. Use it after changing a
query or ubergraph_subset.py, to confirm the local subset journal still holds
everything the queries need.

A backend is "remote" (the public SPARQL endpoint), "local" (the default subset
journal) or a path to a journal, e.g. the full Ubergraph journal
(https://ubergraph.apps.renci.org/downloads/current/ubergraph.jnl.gz, 79 GB
uncompressed). Compare against the remote endpoint only when it runs the same
Ubergraph release as the journal (see the Last-Modified date of the dump).

Usage (from src/):
  python compare_ubergraph_backends.py ../resources/ASCT-b_tables/Kidney.json [more tables...] \\
      [--a local] [--b remote] [--out ../ubergraph/compare]

The validation_date_* columns (run timestamps) are left out of the comparison.
"""
import argparse
import contextlib
import filecmp
import hashlib
import io
import json
import os

import pandas as pd
from rdflib import BNode, Graph

from ccf_tools import parse_asctb
from template_generation_tools import generate_class_graph_template

OUTPUT_NAMES = ['class_template', 'no_valid_template', 'error_log', 'annotations', 'indirect_error_log',
                'report_r', 'strict_log', 'has_part_log', 'ub_subs_t', 'cl_subs_t', 'image_report',
                'sec_graph', 'log_dict']


def use_backend(backend):
  """Point UberonGraph (created inside generate_class_graph_template) at a backend."""
  if backend in ('local', 'remote'):
    os.environ['UBERGRAPH_BACKEND'] = backend
    if backend == 'local':
      os.environ.pop('UBERGRAPH_JOURNAL', None)
  else:
    os.environ['UBERGRAPH_BACKEND'] = 'local'
    os.environ['UBERGRAPH_JOURNAL'] = os.path.abspath(backend)


def graph_lines(graph):
  """N-Triples lines with stable blank-node labels: a hash of each blank node's
  outgoing triples (in these graphs blank nodes are owl:Axiom annotations)."""
  outgoing = {}
  for s, p, o in graph:
    if isinstance(s, BNode) and not isinstance(o, BNode):
      outgoing.setdefault(s, []).append(f'{p.n3()} {o.n3()}')
  labels = {b: '_:h' + hashlib.sha1('\n'.join(sorted(v)).encode()).hexdigest()[:16] for b, v in outgoing.items()}
  def n3(term):
    return labels.get(term, '_:unlabelled') if isinstance(term, BNode) else term.n3()
  return sorted({f'{n3(s)} {n3(p)} {n3(o)} .' for s, p, o in graph})


def normalise(value):
  """Sort lists and dict keys recursively so JSON dumps are order-independent."""
  if isinstance(value, dict):
    return {k: normalise(v) for k, v in sorted(value.items())}
  if isinstance(value, (list, set, tuple)):
    return sorted((normalise(v) for v in value), key=lambda v: json.dumps(v, sort_keys=True, default=str))
  return value


def dump_outputs(table, out_dir):
  os.makedirs(out_dir, exist_ok=True)
  with contextlib.redirect_stdout(io.StringIO()):  # the query code prints every query
    ccf_tools_df, *_, log_dict = parse_asctb(table)
    results = generate_class_graph_template(ccf_tools_df, log_dict)
  for name, value in zip(OUTPUT_NAMES, results):
    path = os.path.join(out_dir, name)
    if isinstance(value, pd.DataFrame):
      value = value.drop(columns=[c for c in value.columns if str(c).startswith('validation_date')]).astype(str)
      rows = sorted(value.to_csv(index=False, header=False).splitlines())
      text, path = '\n'.join([','.join(map(str, value.columns))] + rows), path + '.csv'
    elif isinstance(value, Graph):
      text, path = '\n'.join(graph_lines(value)), path + '.nt'
    else:
      text, path = json.dumps(normalise(value), indent=1, sort_keys=True, default=str), path + '.json'
    with open(path, 'w', encoding='utf-8') as f:
      f.write(text + '\n')


def main():
  parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
  parser.add_argument('tables', nargs='+', help='ASCT+B table JSON files')
  parser.add_argument('--a', default='local', help='first backend (default: local)')
  parser.add_argument('--b', default='remote', help='second backend (default: remote)')
  parser.add_argument('--out', default='../ubergraph/compare', help='where to write the outputs')
  args = parser.parse_args()

  differing = 0
  for table in args.tables:
    name = os.path.splitext(os.path.basename(table))[0]
    dirs = []
    for side, backend in (('a', args.a), ('b', args.b)):
      use_backend(backend)
      dirs.append(os.path.join(args.out, side, name))
      print(f'{name}: running against {backend}', flush=True)
      dump_outputs(table, dirs[-1])
    files = sorted(os.listdir(dirs[0]))
    _, mismatch, errors = filecmp.cmpfiles(dirs[0], dirs[1], files, shallow=False)
    for f in mismatch + errors:
      print(f'  DIFFERS: {f} (diff {os.path.join(dirs[0], f)} {os.path.join(dirs[1], f)})')
    print(f'{name}: {len(files) - len(mismatch) - len(errors)}/{len(files)} outputs identical')
    differing += len(mismatch) + len(errors)
  raise SystemExit(1 if differing else 0)


if __name__ == '__main__':
  main()
