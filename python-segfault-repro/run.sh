#!/usr/bin/env bash
# Usage: ./run.sh   (needs Linux x86_64, Python >= 3.11)
set -u
python3 -m venv .venv && .venv/bin/pip -q install kson-lang==0.4.0
for f in repro.py no_crash_workaround.py; do
  for i in 1 2 3 4 5; do .venv/bin/python -I "$f" >/dev/null 2>&1; echo -n "$? "; done
  echo "<- $f (139 = segfault)"
done
.venv/bin/python -X faulthandler -I repro.py 2>&1 | head -8
