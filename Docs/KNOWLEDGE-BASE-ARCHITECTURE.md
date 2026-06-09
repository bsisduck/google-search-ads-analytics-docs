---
title: "Knowledge Base Architecture Decision — jak mapować korpus dla agenta AI"
type: decision-record
date: 2026-06-05
corpus: "Docs/ (302 plików Markdown, ~4.5MB, PL: Google Search/SEO, Search Console, Ads, GA4)"
method: "5-agent web-grounded research workflow (28 cytowanych źródeł) + adversarial verification"
---

# Decision: Knowledge Base Mapping for the Polish Google Docs Conversational Agent

## 1. TL;DR Recommendation

Build a **Claude Agent Skill that wraps index-first file search (grep/glob over the 17 README maps and the URL-mirrored Markdown tree), and add a lightweight local vector sidecar as a *recommended* fallback — not optional — because of Polish inflection.** This corpus is almost a textbook case for agentic file search: 302 files, single-user scale, reference-heavy content that demands verbatim citations (JSON-LD, tables, status codes), and it is *already pre-built* for navigation (URL-mirroring directories, 17 README tables-of-contents, YAML frontmatter with `source_url`). Each ~4-5K-token file fits whole in context, so the agent locates 1-5 files and reads them intact — maximum citation precision, zero chunk-mangling, zero embedding drift, and instant freshness on edits. The one proven weak spot is that heavily-inflected Polish defeats literal grep (verified live: nominative `dane strukturalne` = 0 hits while the files plainly exist; `indeksowanie` = 140 files vs `indeksować` = 87). That single fact is what turns the vector sidecar from "nice-to-have" into "build it in phase 2." Full RAG-as-backbone and GraphRAG are both over-engineered for this scale and query mix.

## 2. Decision Matrix

| Criterion | File-search | RAG (layered) | Knowledge-Graph | Skill (grep) | **Hybrid (Skill + sidecar)** |
|---|---|---|---|---|---|
| Setup cost | Very Low | Med | High | Low | **Low** |
| Maintenance | Low | Low | High | Low | **Low** |
| Answer precision | Very High | High | High | High | **Very High** |
| Multi-hop reasoning | High (reasoning loop) | Med (top-k loses doc context) | **Very High** | Med-High | **High** |
| Cost ($/query) | Med (multi-step loop) | **Low** (cheap top-k) | High (build) / Med (LazyGraphRAG) | Med | Low-Med |
| Portability | High | Low (DB + pipeline) | Very Low | **Very High** (git folder) | High |
| Recall on inflected Polish | **Low** ⚠️ | High (multilingual embed) | Med | **Low** ⚠️ | **High** ✅ |
| Fit for THIS corpus | Strong | Good (but heavy) | Weak | Strong | **Strongest** ✅ |

Legend: the two ⚠️ cells are the decisive differentiator — pure-lexical approaches share the Polish recall gap that the hybrid closes with a small sidecar.

## 3. Recommended Architecture (phased)

**WHY this fits:** 302 files / ~1.2-1.4M tokens is too big for one context window (so you genuinely need *retrieval*) but far too small to justify standing up a vector DB as the primary backbone or doing LLM entity-extraction for a graph. The corpus's three assets — URL-mirrored tree, 17 README map-of-content files, and `source_url` frontmatter — are precisely the navigation layer agentic search depends on, and they make every answer cite the exact original Google page. Single-user scale means no multi-tenant, access-control, or index-maintenance pressure that would tip the scales toward heavy RAG.

**Phase 0 — Finish the foundation (highest leverage, do first)**
- Complete YAML frontmatter on **all 302 files** (today only ~32/319 have it). `title / source_url / product / section / doc_id` is what makes both routing and citation trustworthy — without it some answers cite a derived path instead of the canonical Google URL.
- Enrich the 17 README descriptions with **synonyms and alternate phrasings** (this is a cheap, direct mitigation for the lexical-recall problem before any vector work).

**Phase 1 — MVP: the Skill (ship this, it answers ~70-80% of queries)**
- Write one `SKILL.md` whose **description** covers SEO / Search Console / Google Ads / GA4 in Polish (so the agent auto-triggers it), and whose **body is a retrieval playbook**:
  1. Read the root `Docs/README.md` map first.
  2. Open the relevant section README to pick candidate files by topic.
  3. Grep for exact terms — **use word stems, not full inflected Polish phrases** (e.g. `strukturaln`, `indeksow`, not `dane strukturalne`); exact English tech tokens (`canonical`, `hreflang`, `Measurement Protocol`, JSON-LD property names, HTTP codes) grep cleanly.
  4. Read 1-5 candidate files whole.
  5. Cite `source_url` from frontmatter.
- Bundle a small **frontmatter-aware ranking helper script** (e.g. `search.py` that scores files by title/section/keyword hits and resolves `doc_id → source_url`). Its code never enters context — only its output does — making retrieval deterministic and token-cheap.
- Optionally add a root `llms.txt` (you effectively already have it in `Docs/README.md`) as the single compact map the agent loads first.

**Phase 2 — Add the vector sidecar (recommended, not optional, because of Polish)**
- Stand up a **local file-based index** — LanceDB / SQLite-vec / Chroma — no server, no ops.
- Section-level chunks (Markdown-aware so tables/JSON-LD stay intact), a **strong multilingual embedding model validated on Polish** (this is the single biggest quality risk — test it before trusting it), BM25 + dense vectors fused with **RRF**, optional cross-encoder reranker on the top-k shortlist.
- The agent calls the sidecar **only when grep returns nothing or the question is conceptual/paraphrased**. Make this escalation rule explicit in `SKILL.md` so the dual-path design doesn't waste turns.
- Re-index on corpus change (small corpus → fast, infrequent job).

This is "do the simplest thing that works," with a single targeted addition for the one verified failure mode. Backend-agnostic: the same `SKILL.md` can later be re-pointed at any retriever without throwing work away.

## 4. When to Upgrade

Concrete signals that justify escalating beyond the hybrid:

- **→ Promote vector/hybrid RAG to primary path** when: real usage logs show grep+index *missing* relevant docs on >~20% of natural-language Polish queries even after frontmatter/synonym enrichment; **OR** the corpus grows by an order of magnitude (thousands of files) or loses its clean README/URL structure; **OR** query volume becomes high enough that the multi-step agentic loop's per-query token/latency cost dominates (Milvus reports ~40%+ token savings switching such loops to vector search).
- **→ Add a lightweight relations layer (NOT full GraphRAG)** when: observed traffic shows **frequent multi-hop, cross-product questions** ("I changed my sitemap, why isn't my product rich result showing — trace the chain", "how do GA4, Ads, and Search Console fit together end-to-end"). Derive edges cheaply from the **existing internal hyperlinks + frontmatter (section/product)** first, or pilot **LazyGraphRAG** (indexing cost ≈ vector RAG) for the global-question subset only.
- **Avoid full Microsoft GraphRAG entirely** unless multi-hop synthesis becomes the *dominant* query shape — its 6-8x indexing premium, ~10-14 week build, and high re-indexing cost against frequently-changing Google docs are not justified here. Link analysis shows a shallow hub-and-spoke structure, so an extracted graph would mostly re-encode hyperlinks the docs already carry.

## 5. What to Discuss With Your AI Agent

1. **Stem-search discipline:** "When you grep Polish, always search word stems (`strukturaln`, `indeksow`), and try 2-3 morphological variants before concluding a topic is absent." — directly counters the verified inflection gap.
2. **Navigation order:** "Read the README maps and frontmatter *first*; use blind full-text grep only as a second step." The maps, not raw grep, are the reliable routing layer (setext headings also mean `^#` heading-grep won't enumerate sections).
3. **Escalation rule:** "If grep returns zero hits OR the question is conceptual/paraphrased, call the vector sidecar." Make the grep-vs-vector boundary explicit so the agent doesn't burn turns.
4. **Citation contract:** "Always cite the `source_url` from frontmatter, and quote tables/JSON-LD verbatim from the whole file — never paraphrase code examples."
5. **Multi-hop handling:** "For cross-product questions (GA4 ↔ Ads ↔ Search Console), read multiple section READMEs and follow internal links rather than relying on a single search."
6. **Frontmatter completeness as a gate:** "Flag any answer where the matched file lacks frontmatter, so I know the metadata rollout is incomplete there."
7. **Multilingual embedding validation:** "Before we trust the sidecar, run an eval set of real Polish questions and confirm the embedding model's recall — this is our biggest quality risk."

## 6. Key Citations

- Agentic search over RAG (precision, simplicity, freshness, privacy): https://vadim.blog/claude-code-no-indexing
- Anthropic Agent Skills & progressive disclosure (table-of-contents → chapters → appendix; filesystem context "effectively unbounded"): https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- Skills best practices (domain-specific org, grep-over-reference-files pattern, ToC for long files): https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- Effective context engineering ("just-in-time" retrieval, hybrid strategies, "do the simplest thing that works"): https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- llms.txt spec (H1 + summary + H2 link-lists; why context windows force a map): https://llmstxt.org/
- Contextual Retrieval (200K-token prompt-stuff threshold; contextual+BM25+rerank cuts retrieval failure up to 67%): https://www.anthropic.com/news/contextual-retrieval
- Hybrid BM25 + vector (exact-token strength for `gtag.js` / JSON-LD / status codes): https://www.pinecone.io/learn/hybrid-search-intro/
- Polish lexical retrieval is harder than English; recommends BM25 + multilingual embeddings + reranker: https://arxiv.org/pdf/2305.19840
- Cost critique of grep-only retrieval (semantic blindness, ~40%+ token savings via vectors): https://milvus.io/blog/why-im-against-claude-codes-grep-only-retrieval-it-just-burns-too-many-tokens.md
- LazyGraphRAG / GraphRAG cost reality (full GraphRAG ~1000x vector RAG indexing; graphs only for multi-hop/global queries): https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/
