#!/usr/bin/env bash
# Install the two Claude Code skills globally (~/.claude/skills) so they work from
# any project. Idempotent. Rewrites the global SKILL.md command paths to absolute
# and writes a config.json pointing back to this repo's Docs/ corpus.
#
#   ./install-skills.sh
#
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS="$HOME/.claude/skills"
DOCS_SKILL="google-search-ads-analytics-docs"
AUDIT_SKILL="google-seo-audit"

mkdir -p "$SKILLS"
for name in "$DOCS_SKILL" "$AUDIT_SKILL"; do
  src="$REPO/.claude/skills/$name"
  dst="$SKILLS/$name"
  [ -d "$src" ] || { echo "missing $src" >&2; exit 1; }
  rm -rf "$dst"
  cp -R "$src" "$dst"
  rm -f "$dst/vec/.daemon.json"          # machine-specific, never copy
  # Rewrite command paths in the global SKILL.md to absolute (the agent's cwd is
  # the user's project, not this repo).
  sed -i.bak \
    -e "s#\.venv/bin/python3#$REPO/.venv/bin/python3#g" \
    -e "s#scripts/serve_models.py#$REPO/scripts/serve_models.py#g" \
    -e "s#scripts/build_embeddings.py#$REPO/scripts/build_embeddings.py#g" \
    -e "s#\.claude/skills/$DOCS_SKILL/#$SKILLS/$DOCS_SKILL/#g" \
    -e "s#\.claude/skills/$AUDIT_SKILL/#$SKILLS/$AUDIT_SKILL/#g" \
    "$dst/SKILL.md"
  rm -f "$dst/SKILL.md.bak"
done

# Corpus resolver for the global docs skill (no machine path is ever committed -
# it's generated here, on the user's machine).
cat > "$SKILLS/$DOCS_SKILL/config.json" <<EOF
{
  "root": "$REPO",
  "note": "Absolute path to the repo containing Docs/. Update if the repo moves, or set env GOOGLE_SAA_DOCS_ROOT."
}
EOF

echo "Installed skills to $SKILLS:"
echo "  - $DOCS_SKILL   (corpus root: $REPO)"
echo "  - $AUDIT_SKILL"
echo
echo "Lexical search works with system python3 (no deps)."
echo "For semantic/hybrid + the audit scanner, run ./setup.sh first."
