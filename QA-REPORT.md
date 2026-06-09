# Corpus QA Report (English migration)

Multi-agent QA of the English Google-docs corpus: 32 content directories audited by
one agent each (33 agents total), then synthesized.

## Audit

- **Files checked:** 458 (incl. section indexes)
- **Issues found:** 64 (23 HIGH, plus medium/low)

| Severity | Finding | Count |
|---|---|---|
| HIGH | `language: pl` frontmatter on English bodies (GA4 / Measurement Protocol pages whose source URL carried trailing params) | 23 |
| MEDIUM | Non-descriptive titles - boilerplate `On this page` / `Note` / `Tip` (Google Ads) or section-heading / `Page Summary` (GA4) used as title | ~30 |
| LOW | Leftover UI chrome - Google's injected "Page Summary" AI-summary widget (Spark icon + AI bullets), `outlined_flag`, and trailing support-assistant / search-nav fragments | ~11 |

## Remediation (all resolved)

1. **Language:** set `language: en` corpus-wide (the corpus is fully English); fixed the
   detection in `enhance_frontmatter.py` (`"hl=pl" in url` rather than `endswith`).
2. **AI-summary widget:** stripped Google's "Page Summary" widget (Spark icon -> AI bullets)
   and stray UI tokens from all bodies - it is injected UI, not source documentation. Folded
   into `enhance_frontmatter.py` (`strip_summary_widget`) so re-scrapes stay clean.
3. **Titles:** re-derived 34 mis-titled pages from the page `<title>` via Firecrawl metadata
   (e.g. `Page Summary` -> `Set up events`; `On this page` -> `Multiply conversions with Performance Max`).

## Post-fix verification

| Check | Result |
|---|---|
| `language: pl` files | 0 |
| Page Summary / `outlined_flag` / Spark chrome | 0 |
| Boilerplate titles (`On this page`/`Note`/`Tip`/`Page Summary`) | 0 |
| `scripts/validate.py` (links / dups / error pages / tiny files) | PASSED (0 issues) |

The reusable QA workflow lives at `scripts/corpus_qa.wf.js`.
