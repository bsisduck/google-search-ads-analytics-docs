---
title: "Google Search's guidance on using generative AI content on your website"
source_url: "https://developers.google.com/search/docs/fundamentals/using-gen-ai-content?hl=en"
product: "Google Search Central"
section: "Docs / SEO Fundamentals"
language: en
scraped_date: 2026-06-08
doc_id: "search-central/docs/fundamentals/using-gen-ai-content.md"
---
Google Search's guidance on using generative AI content on your website
=======================================================================

Generative AI can be particularly useful when researching a topic, and to add structure to
original content. However, using generative AI tools or other similar tools to generate many pages
without adding value for users may violate [Google's spam policy on scaled content abuse](/search/docs/essentials/spam-policies#scaled-content).
If you're using generative AI content on your website, **make sure your work meets the
standards of the [Search Essentials](/search/docs/essentials) and our
[spam policies](/search/docs/essentials/spam-policies#scaled-content).**

You might find value in looking at the [Search Quality Raters guidelines](https://static.googleusercontent.com/media/guidelines.raterhub.com/en//searchqualityevaluatorguidelines.pdf)
on how to evaluate both scaled content abuse (section 4.6.5) and main content created with little
to no effort, little to no originality, and little to no added value (section 4.6.6). These
guidelines are not a guide to ranking first in Google; they're used by our
[search raters](https://support.google.com/websearch/answer/9281931)
to help evaluate the performance of our [various search ranking systems](/search/docs/appearance/ranking-systems-guide),
and their ratings don't directly influence ranking.

### Focus on accuracy, quality, and relevance

When creating content for the web, focus on accuracy, quality, and relevance, especially when
automatically generating the content. This includes metadata like [`<title>` elements](/search/docs/appearance/title-link),
[meta description elements](/search/docs/appearance/snippet),
[structured data](/search/docs/appearance/structured-data/intro-structured-data), and
[alternate texts for images](/tech-writing/accessibility/self-study/write-alt-text),
which can appear in Search results.

For structured data, also ensure compliance with the [general guidelines](/search/docs/appearance/structured-data/sd-policies),
the specific policies for the individual search features, and [validate the markup](/search/docs/appearance/structured-data/sd-policies)
to ensure eligibility for [Search features](/search/docs/appearance/structured-data/search-gallery).

### Give users context

Sharing [information about how a piece of content was created](/search/docs/fundamentals/creating-helpful-content#how-the-content-was-created)
can help give your readers more context. If you're automatically generating content, consider
adding information on how your content was created in a way that makes sense for your audience,
such as by providing more background information on how automation was used and adding
[image metadata](/search/docs/appearance/structured-data/image-license-metadata#add-metadata).

For ecommerce sites, Google Merchant Center has [policies for AI-generated content](https://support.google.com/merchants/answer/14743464).
In particular, AI-generated images must contain metadata using the IPTC `DigitalSourceType`
[`TrainedAlgorithmicMedia`](https://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia)
metadata. AI-generated product data such as title and description attributes must be specified
separately and labeled as AI-generated.

For more, see our [FAQs in our blog post on AI-generated content](/search/blog/2023/02/google-search-and-ai-content).
