---
name: google-search-ads-analytics-docs
version: 2.0.0
description: >-
  This skill should be used when the user asks about Google Search (SEO), Google
  Search Console, Google Ads, or Google Analytics 4 (GA4) - including SEO,
  crawling/indexing, robots.txt, sitemaps, structured data / rich results,
  Search Console reports (index coverage, performance, Core Web Vitals), Google
  Ads campaigns/conversions, or GA4 data collection (gtag.js, events, Measurement
  Protocol). It answers from a local English knowledge base of official Google
  documentation in Docs/ and returns precise, cited answers with the original
  Google source_url.
---

# Google Search / Ads / Analytics docs - knowledge base

A curated, validated corpus of **304 official Google documentation pages** under
`Docs/`, covering four products. Provide **precise, cited** answers; do not guess
when the answer is in the corpus.

## What's inside
- `Docs/README.md` - master map (start here).
- `Docs/<section>/README.md` - 17 section indexes (tables of contents).
- `index.json` (bundled) - every doc's `title`, `section`, `product`, `source_url`.
- `search.py` (bundled) - frontmatter-aware ranking search (stdlib).

Products: **Google Search Central** (SEO/crawling/indexing/structured-data),
**Search Console** (reports), **Google Ads** (campaigns/conversions),
**Google Analytics 4** (collection gtag.js + Measurement Protocol).

## Retrieval playbook - follow in order

1. **Search first.** Best quality is **hybrid** (lexical + semantic, RRF-fused -
   eval: 96% recall@5). Needs the repo venv:
   ```bash
   .venv/bin/python3 .claude/skills/google-search-ads-analytics-docs/hybrid.py "<the user's question>"
   ```
   Fast when the daemon runs (`.venv/bin/python3 scripts/serve_models.py`).
   **Stdlib fallback (no venv):** `python3 .claude/skills/google-search-ads-analytics-docs/search.py
   "<terms>"` - lexical, stem-aware, ~0.4s, works anywhere.
   All return ranked docs with `title`, `path`, `source_url`, `snippet`.

   Examples: `"block a page from indexing"`, `"product structured data with price and rating"`,
   `"submit a sitemap"`, `"track GA4 events with gtag.js"`, `"google ads conversion tracking"`.

2. **Read the top 1-5 files whole** with the Read tool (each is ~4-5K tokens and
   fits in context). Read complete files - never answer from the snippet alone.
   Quote tables and JSON-LD/code examples **verbatim**; do not paraphrase code.

3. **Cite** the `source_url` from the result for every claim, e.g.
   *(source: https://developers.google.com/search/docs/...)*.

4. **If `search.py` returns nothing useful, OR the question is conceptual /
   paraphrased** (lexical match is weak), use the **semantic fallback**:
   ```bash
   python3 .claude/skills/google-search-ads-analytics-docs/vec_search.py "<the user's question>"
   ```
   It embeds the query (multilingual model) and returns the closest docs even when
   wording differs. Then read the top files whole and cite `source_url` as above.
   (Requires the repo venv with `sentence-transformers`.)

5. **Last resort**, navigate manually: read `Docs/README.md` -> the relevant
   section `README.md` -> pick candidates; or `grep`/`Glob` over `Docs/` for exact
   terms and technical tokens (`hreflang`, `canonical`, `robots.txt`, `gtag`,
   JSON-LD props, HTTP codes). Prefer `search.py`/`hybrid.py`, which rank for you.

## Deep research (Workflow)

For a multi-part or research-style question, run the bundled **`docs-research`**
workflow (Workflow tool): it decomposes the question, hybrid-retrieves and reads
top docs per sub-question, **adversarially verifies each claim against its cited
source_url**, then synthesizes one cited answer. It scales agents to the number of
sub-questions and claims - no fixed cap. Saved at `.claude/workflows/docs-research.js`.

## Rules
- **Whole-file reads + verbatim code.** Precision over brevity.
- **Always cite `source_url`.** If a matched doc has no `source_url` (only the
  authored `KNOWLEDGE-BASE-ARCHITECTURE.md`), say so.
- **Language:** the corpus is Polish (a few help pages are English). Answer in the
  user's language; quote source text as-is.
- **Don't invent** Google behavior that isn't in the corpus; if it's genuinely
  missing, say the corpus doesn't cover it.

## Notes
- The corpus is validated: 0 broken links, 0 duplicates, 0 error pages; every
  file carries YAML frontmatter (`title`, `source_url`, `section`, ...).
- Two retrieval paths: **`search.py`** (lexical, stem-aware, stdlib - primary) and
  **`vec_search.py`** (semantic, embeddings - fallback for fuzzy/conceptual queries;
  rebuild with `scripts/build_embeddings.py`). See `Docs/KNOWLEDGE-BASE-ARCHITECTURE.md`.
- Helper usage variants:
  `search.py "query" --top 5` - `--no-content` (faster, metadata-only) -
  `--doc <doc_id>` (resolve one doc's citation + head).
