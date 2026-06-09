#!/usr/bin/env bash
# Create the Python venv and install dependencies for the semantic/hybrid
# retrieval, the model daemon, and the SEO-audit page scanner.
# (Lexical search needs none of this - it's stdlib-only.)
#
#   ./setup.sh
#
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"

PY="${PYTHON:-python3}"
if [ ! -d .venv ]; then
  "$PY" -m venv .venv
fi
./.venv/bin/pip install --upgrade pip >/dev/null
./.venv/bin/pip install -r requirements.txt

echo
echo "Done. Quick check:"
echo "  python3 .claude/skills/google-search-ads-analytics-docs/search.py \"robots.txt\" --no-content"
echo "  ./.venv/bin/python3 .claude/skills/google-search-ads-analytics-docs/hybrid.py \"dane strukturalne produktu\""
echo
echo "Optional speed-up (load models once, ~sub-second queries):"
echo "  ./.venv/bin/python3 scripts/serve_models.py   # leave running"
