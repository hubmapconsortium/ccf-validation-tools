#!/usr/bin/env bash
# Build ubergraph-subset.jnl: a small Blazegraph journal with just the parts of
# Ubergraph that the CCF validation queries (ubergraph_tools.py) use.
#
# Usage: build_ubergraph_subset.sh <output.jnl> [<work dir>]
#
#  1. download Ubergraph's N-Quads dump (resumable, retried; ~4 GB)
#  2. filter it to UBERON/CL/PCL with ubergraph_subset.py (one N-Triples file per graph)
#  3. load each file into its named graph with blazegraph-runner
#
# The output is written atomically, so a failed build leaves an existing journal intact.
# Set KEEP_DUMP=1 to keep the downloaded dump in the work dir.
set -euo pipefail

SRC_DIR="$(cd "$(dirname "$0")" && pwd)"
OUT="${1:?usage: build_ubergraph_subset.sh <output.jnl> [<work dir>]}"
WORK="${2:-$(dirname "$OUT")/subset-build}"
UBERGRAPH_NQ_URL="${UBERGRAPH_NQ_URL:-https://ubergraph.apps.renci.org/downloads/current/ubergraph.nq.gz}"
RUNNER="${BLAZEGRAPH_RUNNER:-$SRC_DIR/tools/blazegraph-runner-1.7/bin/blazegraph-runner}"
PYTHON="${PYTHON:-python}"
export JAVA_OPTS="${JAVA_OPTS:--Xmx4G}"

mkdir -p "$WORK" "$(dirname "$OUT")"
DUMP="$WORK/ubergraph.nq.gz"

remote_size() {
  curl -sfIL --retry 5 "$UBERGRAPH_NQ_URL" | tr -d '\r' | awk 'tolower($1) == "content-length:" { n = $2 } END { print n }'
}
local_size() { stat -c %s "$DUMP" 2>/dev/null || echo 0; }

echo "[$(date +%T)] downloading $UBERGRAPH_NQ_URL"
EXPECTED="$(remote_size || true)"
for attempt in $(seq 1 20); do
  if [ -n "$EXPECTED" ] && [ "$(local_size)" = "$EXPECTED" ]; then
    break  # complete (a resumed request for a finished file returns HTTP 416)
  fi
  if curl -fL --silent --show-error --retry 10 --retry-all-errors --retry-delay 10 -C - -o "$DUMP" "$UBERGRAPH_NQ_URL" \
      && { [ -z "$EXPECTED" ] || [ "$(local_size)" = "$EXPECTED" ]; }; then
    break
  fi
  [ "$attempt" = 20 ] && { echo "giving up downloading $UBERGRAPH_NQ_URL" >&2; exit 1; }
  echo "download attempt $attempt incomplete ($(local_size) of ${EXPECTED:-?} bytes); resuming..." >&2
  sleep 15
  if [ -z "$EXPECTED" ]; then EXPECTED="$(remote_size || true)"; fi
done
ls -l "$DUMP"

echo "[$(date +%T)] filtering"
"$PYTHON" "$SRC_DIR/ubergraph_subset.py" "$DUMP" "$WORK"
[ -n "${KEEP_DUMP:-}" ] || rm -f "$DUMP"

echo "[$(date +%T)] loading"
rm -f "$OUT.tmp"
load() {
  "$RUNNER" --journal="$OUT.tmp" --informat=ntriples load --graph="$2" "$WORK/$1.nt" > "$WORK/load-$1.log" 2>&1 \
    || { cat "$WORK/load-$1.log"; exit 1; }
}
load ontology http://reasoner.renci.org/ontology
load redundant http://reasoner.renci.org/redundant
load nonredundant http://reasoner.renci.org/nonredundant
load union http://purl.org/ccf/ubergraph-subset/union
mv "$OUT.tmp" "$OUT"
rm -f "$WORK"/*.nt "$WORK"/load-*.log
echo "[$(date +%T)] done"
ls -lh "$OUT"
