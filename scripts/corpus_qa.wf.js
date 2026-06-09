export const meta = {
  name: 'corpus-qa',
  description: 'Multi-agent QA of the English Google-docs corpus: one agent per content directory verifies language, title quality, completeness, and clean extraction; synthesize a QA report.',
  phases: [
    { title: 'QA', detail: 'one agent per content directory checks its pages' },
    { title: 'Report', detail: 'aggregate issues into QA-REPORT.md' },
  ],
}

const dirs = [
  "Docs/google-ads-help", "Docs/google-analytics/collection-app", "Docs/google-analytics/collection-ga4",
  "Docs/google-analytics/measurement-protocol", "Docs/google-analytics/support", "Docs/search-central/case-studies",
  "Docs/search-central/crawling-docs/crawlers-fetchers", "Docs/search-central/crawling-docs/robots-txt",
  "Docs/search-central/docs", "Docs/search-central/docs/advanced/guidelines", "Docs/search-central/docs/appearance",
  "Docs/search-central/docs/appearance/structured-data", "Docs/search-central/docs/crawling-indexing",
  "Docs/search-central/docs/crawling-indexing/amp", "Docs/search-central/docs/crawling-indexing/javascript",
  "Docs/search-central/docs/crawling-indexing/mobile", "Docs/search-central/docs/crawling-indexing/robots",
  "Docs/search-central/docs/crawling-indexing/sitemaps", "Docs/search-central/docs/essentials",
  "Docs/search-central/docs/fundamentals", "Docs/search-central/docs/monitor-debug",
  "Docs/search-central/docs/monitor-debug/search-operators", "Docs/search-central/docs/monitor-debug/security",
  "Docs/search-central/docs/specialty/ecommerce", "Docs/search-central/docs/specialty/explicit",
  "Docs/search-central/docs/specialty/international", "Docs/search-central/help",
  "Docs/search-central/help/office-hours", "Docs/search-central/help/office-hours/2022",
  "Docs/search-central/help/office-hours/2023", "Docs/search-central/help/office-hours/2024",
  "Docs/search-console-help",
]

const ISSUE = {
  type: 'object',
  properties: {
    dir: { type: 'string' },
    checked: { type: 'number' },
    issues: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          path: { type: 'string' },
          problem: { type: 'string' },
          severity: { type: 'string', enum: ['high', 'medium', 'low'] },
        },
        required: ['path', 'problem', 'severity'],
      },
    },
  },
  required: ['dir', 'checked', 'issues'],
}

phase('QA')
const raw = await parallel(dirs.map(d => () => agent(
  `You QA the English Google-documentation pages in directory "${d}".\n` +
  `List its *.md files (ignore README.md). For each, read the YAML frontmatter and the body (Read / head / sed / grep).\n` +
  `Flag a file ONLY if it has a real problem:\n` +
  `- HIGH: body not English (Polish/other), or contains CAPTCHA / "unusual traffic" / "/sorry/" text, or truncated/near-empty (<300 chars real content), or frontmatter language != "en".\n` +
  `- MEDIUM: title missing or a slug like "Answer 12345"; or body mostly nav/boilerplate.\n` +
  `- LOW: minor leftover chrome ("Skip to main content", feedback widget) or broken markdown table.\n` +
  `Be precise and conservative - verbatim Google docs are expected; do not invent issues. Return checked count and issues (empty if clean).`,
  { label: `qa:${d.replace('Docs/', '')}`, phase: 'QA', schema: ISSUE, agentType: 'general-purpose' }
)))
const results = raw.filter(Boolean)

phase('Report')
const flat = results.flatMap(r => (r.issues || []).map(i => ({ ...i, dir: r.dir })))
const checked = results.reduce((s, r) => s + (r.checked || 0), 0)
const high = flat.filter(i => i.severity === 'high')
await agent(
  `Write a QA report to QA-REPORT.md using the Write tool.\n` +
  `Corpus: English Google docs. Directories QA'd: ${dirs.length}. Files checked: ${checked}. Issues: ${flat.length} (HIGH ${high.length}).\n` +
  `Issues JSON:\n${JSON.stringify(flat).slice(0, 12000)}\n` +
  `Format: one-line summary; "High-priority (fix now)" table (path | problem) if any; then medium/low grouped. If no issues, state the corpus passed QA cleanly. Concise.`,
  { label: 'qa-report', phase: 'Report', agentType: 'general-purpose' }
)
return { directories: dirs.length, files_checked: checked, issues: flat.length, high: high.length, high_list: high.slice(0, 40) }
