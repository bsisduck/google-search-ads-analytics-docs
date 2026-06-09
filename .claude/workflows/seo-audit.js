export const meta = {
  name: 'seo-audit',
  description: 'Multi-agent SEO/discoverability audit grounded in the Google docs KB: snapshot a page, fan out one auditor per dimension, adversarially refute every finding, then synthesize a scored, cited report. Scales agents with the work — no fixed cap.',
  phases: [
    { title: 'Snapshot', detail: 'extract page signals with fetch_page.py' },
    { title: 'Verify', detail: 'one agent per SEO dimension audits the snapshot, grounded in the docs KB' },
    { title: 'Refute', detail: 'adversarial verification — try to refute each finding; drop false positives' },
    { title: 'Synthesize', detail: 'aggregate surviving findings into a scored AUDIT report' },
  ],
}

// args: a URL or local .html path (string), or { target, refuters }
const target = (typeof args === 'string' ? args : args?.target) || 'app/index.html'
const REFUTERS = (typeof args === 'object' && args?.refuters) || 2   // adversarial verifiers per finding
const slug = target.replace(/^https?:\/\//, '').replace(/[^a-zA-Z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 60) || 'page'
const snapPath = `/tmp/snap-${slug}.json`

const SNAP_SCHEMA = { type: 'object', properties: { snapshot_path: { type: 'string' }, summary: { type: 'string' } }, required: ['snapshot_path'] }
const FINDINGS_SCHEMA = {
  type: 'object',
  properties: {
    dimension: { type: 'string' },
    score: { type: 'number' },
    findings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          check: { type: 'string' },
          verdict: { type: 'string', enum: ['pass', 'warn', 'fail'] },
          evidence: { type: 'string' },
          recommendation: { type: 'string' },
          severity: { type: 'string', enum: ['high', 'medium', 'low'] },
          citation_url: { type: 'string' },
        },
        required: ['check', 'verdict', 'severity'],
      },
    },
  },
  required: ['dimension', 'score', 'findings'],
}
const VERDICT_SCHEMA = { type: 'object', properties: { real: { type: 'boolean' }, reason: { type: 'string' } }, required: ['real'] }

// ----- Phase 1: snapshot -----
phase('Snapshot')
const snap = await agent(
  `Extract SEO signals for target "${target}".\n` +
  `Run: .venv/bin/python3 .claude/skills/google-seo-audit/fetch_page.py "${target}" --out ${snapPath}\n` +
  `(fall back to python3 if no venv but scrapling is installed). Then confirm the file exists and return its path + a one-line summary.`,
  { label: 'snapshot', phase: 'Snapshot', schema: SNAP_SCHEMA, agentType: 'general-purpose' }
)
const snapshot = snap?.snapshot_path || snapPath

// ----- Phase 2+3: per-dimension audit -> adversarial refute (pipelined) -----
const DIMENSIONS = [
  { key: 'crawl-indexing', focus: 'HTTP status, redirects, meta robots / X-Robots-Tag, robots.txt, sitemap', kb: 'crawling-indexing/*' },
  { key: 'onpage', focus: 'title (length/uniqueness), meta description, exactly one H1, heading hierarchy, content depth, helpful-content signals', kb: 'fundamentals/seo-starter-guide, creating-helpful-content, appearance/title-link, appearance/snippet' },
  { key: 'structured-data', focus: 'JSON-LD presence, valid @type, required properties, rich-result eligibility', kb: 'appearance/structured-data/*' },
  { key: 'canonical', focus: 'canonical correctness, duplicate/alternate URLs, parameter handling', kb: 'crawling-indexing/canonicalization' },
  { key: 'performance', focus: 'HTTPS, HSTS, mobile viewport, intrusive interstitials, Core Web Vitals', kb: 'appearance/page-experience, appearance/core-web-vitals, crawling-indexing/mobile/*' },
  { key: 'hreflang', focus: 'lang attribute, hreflang alternates, locale handling (only if multilingual)', kb: 'specialty/international/*' },
  { key: 'links-assets', focus: 'crawlable links (href), image alt text, blocked CSS/JS assets', kb: 'crawling-indexing/links-crawlable, appearance/google-images/*' },
  { key: 'measurement', focus: 'GA4/gtag presence, GTM, Google Ads conversion, GA4 events / Measurement Protocol readiness', kb: 'google-analytics/*, google-ads-help/*' },
]

const auditOne = (d) => agent(
  `You audit the **${d.key}** dimension of a web page for Google Search.\n` +
  `1) Read the snapshot JSON at ${snapshot}.\n` +
  `2) GROUND every finding in the local Google docs — run:\n` +
  `   .venv/bin/python3 .claude/skills/google-search-ads-analytics-docs/hybrid.py "<topic>"\n` +
  `   (or: python3 .claude/skills/google-search-ads-analytics-docs/search.py "<topic>" if no venv)\n` +
  `   then Read the top matched file(s) and cite their source_url.\n` +
  `Focus: ${d.focus}. Relevant KB: ${d.kb}.\n` +
  `Return findings (check/verdict/evidence/recommendation/severity/citation_url) and a 0–100 score. ` +
  `Be honest; if a dimension does not apply, return one finding with verdict "pass" and evidence "not applicable".`,
  { label: `verify:${d.key}`, phase: 'Verify', schema: FINDINGS_SCHEMA }
)

const refuteOne = (res) => {
  if (!res || !res.findings) return Promise.resolve(res)
  const actionable = res.findings.filter(f => f.verdict !== 'pass')
  if (!actionable.length) return Promise.resolve(res)
  return parallel(actionable.flatMap(f =>
    Array.from({ length: REFUTERS }, (_, i) => () =>
      agent(
        `Adversarially REFUTE this SEO finding for the "${res.dimension}" dimension:\n${JSON.stringify(f)}\n` +
        `Check it against the snapshot at ${snapshot} and the Google docs KB ` +
        `(.claude/skills/google-search-ads-analytics-docs/search.py "<topic>"). ` +
        `Is it actually true AND actionable per official Google guidance? ` +
        `Default real=false if the evidence is weak, the citation does not support it, or it isn't really a problem.`,
        { label: `refute:${res.dimension}:${(f.check || '').slice(0, 16)}#${i + 1}`, phase: 'Refute', schema: VERDICT_SCHEMA }
      )
    )
  )).then(votes => {
    let vi = 0
    const survivors = []
    for (const f of res.findings) {
      if (f.verdict === 'pass') { survivors.push(f); continue }
      const fv = votes.slice(vi, vi + REFUTERS).filter(Boolean); vi += REFUTERS
      if (fv.filter(v => v.real).length >= Math.ceil(REFUTERS / 2)) survivors.push(f)
    }
    return { ...res, findings: survivors }
  })
}

const audited = (await pipeline(DIMENSIONS, auditOne, refuteOne)).filter(Boolean)

// ----- Phase 4: synthesize -----
phase('Synthesize')
const report = await agent(
  `Write the final SEO audit for "${target}" to AUDIT-${slug}.md using the Write tool.\n` +
  `Audited, refuted-clean per-dimension results:\n${JSON.stringify(audited).slice(0, 12000)}\n\n` +
  `Report:\n` +
  `- Title + executive summary (3–5 lines).\n` +
  `- Overall score (average of dimension scores) + a per-dimension score table.\n` +
  `- Prioritized fixes table sorted by severity then effort: each row = concrete change + source_url citation.\n` +
  `- Per-dimension findings (pass/warn/fail with evidence).\n` +
  `Cite a Google source_url on every recommendation; mark N/A dimensions explicitly.`,
  { label: 'synthesize', phase: 'Synthesize', agentType: 'general-purpose' }
)

log(`SEO audit complete → AUDIT-${slug}.md`)
return { target, report_file: `AUDIT-${slug}.md`, dimensions: audited.length, refuters_per_finding: REFUTERS, summary: report?.slice?.(0, 400) }
