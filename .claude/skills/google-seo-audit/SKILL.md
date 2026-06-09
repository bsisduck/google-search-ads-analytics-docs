---
name: google-seo-audit
version: 0.3.0
description: >-
  This skill should be used when the user asks to "audit my page/site/repo",
  "scan for SEO", "check structured data / rich results", "is my page
  Google-ready", "SEO audit", "Google scanner", or wants prioritized, cited
  recommendations to improve a page in Google Search. It runs a full multi-agent
  SEO / discoverability audit of a web page - a live URL OR a local .html file in
  the current repo - grounded in the local Google documentation knowledge base
  (the google-search-ads-analytics-docs skill): it spawns one subagent per audit
  dimension and produces a scored report with fixes that cite the official Google
  docs (source_url).
---

# Google SEO Audit - multi-agent page audit

Audits a page across every Google-discoverability dimension and returns a
**scored report with prioritized, cited recommendations**. Every recommendation
must be grounded in the local corpus via the **`google-search-ads-analytics-docs`** skill
(`.claude/skills/google-search-ads-analytics-docs/search.py`) and cite a Google `source_url`.

## Fast path - the Workflow

For a thorough, adversarially-verified audit, run the bundled **`seo-audit`**
workflow (Workflow tool), saved at `.claude/workflows/seo-audit.js`. It implements
the four phases below and **scales agents to the work - no fixed cap**:
**Snapshot -> Verify** (one agent per dimension) **-> Refute** (adversarial
verifiers per finding, false positives dropped) **-> Synthesize** (`AUDIT-<page>.md`).
Pass the target as args (URL or local path); optional `{ refuters: N }` raises the
adversarial panel size. If the Workflow tool isn't available, do the same steps
manually with the Task tool, below.

## Step 1 - Pick the target(s)
- A live page: pass the URL.
- **This repo (default when the user says "my page/repo"):** find local pages
  with `Glob "**/*.html"` (ignore `.venv/`, `node_modules/`). The repo's page is
  `app/index.html`. Audit each found page.

## Step 2 - Snapshot (deterministic, run once per target)
Use a per-target output file so multiple pages don't clobber each other:
```bash
.venv/bin/python3 .claude/skills/google-seo-audit/fetch_page.py <url-or-path> --out /tmp/snap-<page-slug>.json
```
Produces a JSON of: status/headers/HTTPS, title, meta description, meta robots,
canonical, viewport (mobile), lang + hreflang, H1/heading outline, word count,
images+missing-alt, JSON-LD structured data (types + a parse-OK flag - **not**
schema validation; the structured-data agent must still verify required props),
Open Graph, analytics/ads tags (GA4/GTM/Ads), and robots.txt (remote only).

## Step 3 - Fan out the audit (one subagent per dimension)
Spawn the dimensions **in parallel** (Task tool, or the Workflow). Give each agent
the snapshot JSON and tell it to **consult `google-search-ads-analytics-docs` first** - run
`.venv/bin/python3 .claude/skills/google-search-ads-analytics-docs/search.py "<topic>"` (and
`--doc <doc_id>` to resolve a citation), then read the matched files - and cite
`source_url` on every finding. Dimensions:

1. **Crawlability & Indexing** - HTTP status, redirects, `meta robots` /
   `X-Robots-Tag`, canonical, robots.txt, sitemap. KB: `crawling-indexing/*`.
2. **On-page SEO & Content** - title (len/uniqueness), meta description,
   exactly one H1, heading hierarchy, content depth, helpful-content signals.
   KB: `fundamentals/seo-starter-guide`, `creating-helpful-content`,
   `appearance/snippet`, `appearance/title-link`.
3. **Structured Data & Rich Results** - JSON-LD presence, valid types, required
   props, rich-result eligibility. KB: `appearance/structured-data/*`.
4. **Page Experience & Core Web Vitals** - HTTPS, HSTS, mobile viewport,
   intrusive-interstitial risk, CWV considerations. KB: `appearance/page-experience`,
   `appearance/core-web-vitals`, `crawling-indexing/mobile/*`.
5. **International (hreflang)** - `lang`, hreflang alternates, locale handling
   (only if the page is multilingual). KB: `specialty/international/*`.
6. **Measurement & Tagging** - GA4/gtag, GTM, Google Ads conversion, GA4
   events/Measurement Protocol readiness. KB: `google-analytics/*`,
   `google-ads-help/*`.

Each finding: `{check, verdict: pass|warn|fail, evidence, recommendation,
severity: high|medium|low, citation_url}`.

## Step 4 - Synthesize the report
Aggregate into `AUDIT-<page>.md`:
- **Score**: each dimension 0-100; overall = average (call out fails).
- **Executive summary** (3-5 lines).
- **Prioritized fixes**: a table sorted by severity -> effort, each with the
  concrete change and a `source_url` citation.
- **Per-dimension findings** (pass/warn/fail with evidence).
- Be honest: don't invent issues; mark "N/A" where a dimension doesn't apply
  (e.g. hreflang on a single-language page).

## Notes
- Requires the project venv (`.venv/bin/python3`) with Scrapling, and the
  `google-search-ads-analytics-docs` skill present for grounding.
- Local files can't show HTTP-level signals (status/headers/HTTPS/robots.txt) -
  flag those as "deployment-dependent, verify on the live URL".

## Safety
- **Authorization:** only audit pages you own or are explicitly authorized to
  test. `fetch_page.py` issues a normal browser-like GET to the target and its
  `/robots.txt`; do not point it at internal/private hosts you don't control
  (it has no SSRF allow-list - it fetches whatever URL you pass).
- **No credentials, no writes to the target.** The snapshot is read-only and is
  written only to the local `--out` JSON (or stdout). Nothing is sent anywhere
  except the HTTP GET to the page being audited.
