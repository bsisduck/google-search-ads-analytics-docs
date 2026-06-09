export const meta = {
  name: 'docs-research',
  description: 'Deep multi-agent research over the Google docs knowledge base: decompose the question, hybrid-retrieve and read top docs per sub-question, adversarially verify each claim against its cited source_url, then synthesize one cited answer.',
  phases: [
    { title: 'Decompose', detail: 'break the question into independent sub-questions' },
    { title: 'Retrieve', detail: 'hybrid-retrieve and read top docs per sub-question' },
    { title: 'Verify', detail: 'adversarially check each claim against its cited source_url' },
    { title: 'Synthesize', detail: 'write the final cited answer' },
  ],
}

// args: the research question (string) or { question }
const question = (typeof args === 'string' ? args : args?.question) || ''
if (!question) { log('docs-research: no question provided in args'); return { error: 'no question' } }

const SUBQ_SCHEMA = { type: 'object', properties: { subquestions: { type: 'array', items: { type: 'string' } } }, required: ['subquestions'] }
const ANSWER_SCHEMA = {
  type: 'object',
  properties: {
    subquestion: { type: 'string' },
    answer: { type: 'string' },
    claims: { type: 'array', items: { type: 'object', properties: { claim: { type: 'string' }, source_url: { type: 'string' } }, required: ['claim', 'source_url'] } },
  },
  required: ['subquestion', 'answer'],
}
const VERDICT_SCHEMA = { type: 'object', properties: { supported: { type: 'boolean' }, note: { type: 'string' } }, required: ['supported'] }

phase('Decompose')
const dec = await agent(
  `Break this question into 2-5 independent sub-questions answerable from official Google docs ` +
  `(Search/SEO, Search Console, Google Ads, GA4). Question: "${question}". Return only the sub-questions.`,
  { label: 'decompose', phase: 'Decompose', schema: SUBQ_SCHEMA }
)
const subs = (dec?.subquestions || [question]).slice(0, 6)

const retrieve = (sub) => agent(
  `Answer this sub-question from the local Google docs KB: "${sub}".\n` +
  `Run: .venv/bin/python3 .claude/skills/google-search-ads-analytics-docs/hybrid.py "${sub}"\n` +
  `(or python3 .claude/skills/google-search-ads-analytics-docs/search.py "${sub}" if no venv), ` +
  `Read the top 1-3 matched files whole, and answer with claims each tied to a source_url. Quote code/tables verbatim.`,
  { label: `retrieve:${sub.slice(0, 24)}`, phase: 'Retrieve', schema: ANSWER_SCHEMA }
)

const verify = (res) => {
  if (!res || !res.claims || !res.claims.length) return Promise.resolve(res)
  return parallel(res.claims.map(c => () =>
    agent(
      `Verify this claim against its cited Google doc. Claim: "${c.claim}". Cited source_url: ${c.source_url}.\n` +
      `Use .claude/skills/google-search-ads-analytics-docs/search.py --doc to resolve the doc, Read it, and confirm. ` +
      `supported=false if the page does not actually state this.`,
      { label: `verify:${(c.claim || '').slice(0, 24)}`, phase: 'Verify', schema: VERDICT_SCHEMA }
    ).then(v => ({ ...c, supported: v?.supported !== false }))
  )).then(claims => ({ ...res, claims }))
}

const answered = (await pipeline(subs, retrieve, verify)).filter(Boolean)

phase('Synthesize')
const final = await agent(
  `Write a single, well-structured answer to: "${question}".\n` +
  `Use these verified sub-answers (drop unsupported claims):\n${JSON.stringify(answered).slice(0, 12000)}\n` +
  `Cite the Google source_url inline for every factual statement. If the corpus does not cover something, say so plainly.`,
  { label: 'synthesize', phase: 'Synthesize' }
)

return { question, subquestions: subs.length, answer: final }
