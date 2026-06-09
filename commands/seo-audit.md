---
description: Run a multi-agent SEO/discoverability audit of a page (URL or local .html), grounded in the Google docs KB, and write a scored cited report.
argument-hint: "[url-or-path]"
---

Run a thorough SEO audit of: **$ARGUMENTS** (default to `app/index.html`, or any `*.html` in this repo, if no target is given).

Use the `google-seo-audit` skill. For a deep, adversarially-verified pass, drive it as a multi-agent workflow:

1. **Snapshot** - extract page signals with `fetch_page.py`.
2. **Verify** - spawn one auditor agent per dimension (crawl-indexing, onpage, structured-data, canonical, performance, hreflang, links-assets, measurement). Each grounds findings in the docs KB (`google-search-ads-analytics-docs`) and cites a Google `source_url`.
3. **Refute** - spawn adversarial verifiers per finding; drop false positives.
4. **Synthesize** - write `AUDIT-<page>.md`: overall + per-dimension scores, prioritized fixes with citations.

If the Workflow tool is available, run the bundled `seo-audit` workflow (it implements exactly this, scaling agents to the work). Only audit pages you own or are authorized to test.
