---
title: "AMP on Google Search guidelines"
source_url: "https://developers.google.com/search/docs/crawling-indexing/amp?hl=en"
product: "Google Search Central"
section: "Docs / Crawling & Indexing"
language: en
scraped_date: 2026-06-08
doc_id: "search-central/docs/crawling-indexing/amp/index.md"
---
AMP on Google Search guidelines
===============================

All of our [guidelines](https://support.google.com/webmasters/answer/40349)
for making a site Google-friendly also apply to AMP. This document covers additional
guidelines that are specific to AMP on Google Search. To learn more about AMP on Google
Search, read our [developer guide](/search/docs/crawling-indexing/amp/about-amp).

* Your AMP page must follow the [AMP
  HTML specification](https://www.ampproject.org/docs/reference/spec.html). If you're just getting started, learn how to
  [create
  your first AMP HTML page](https://www.ampproject.org/docs/get_started/create.html).
* Users must be able to experience the same content and complete the same actions on AMP
  pages as on the corresponding canonical pages, where possible.
* Your AMP URL scheme makes sense to the user.
  For instance, if your canonical page is `example.com/giraffes`,
  host the AMP somewhere like `amp.example.com/giraffes` or
  `example.com/amp/giraffes`, rather than at `test.com/giraffes`.
  This is because when users click a link to your AMP page from Google Search, the AMP URL
  is visible to the user in the browser (like any web page), and showing a URL that is
  completely unrelated to your main website can be confusing to users.
* Your AMP page must be [valid](https://search.google.com/test/amp)
  so that your pages work as expected for users and can be included in AMP-related features.
  Pages with invalid AMP will not be eligible for some Search features.
* If you add structured data to your page, make sure that you follow our
  [structured data policies](/search/docs/appearance/structured-data/sd-policies).

Additional AMP topics
---------------------

The following topics describe how to work with AMP and how it works in Google Search.

| Topics | |
| --- | --- |
| [Understand how AMP works in search results](/search/docs/crawling-indexing/amp/about-amp) | Learn how AMP appears in Google Search results. |
| [Enhance AMP content for Google Search](/search/docs/crawling-indexing/amp/enhance-amp) | Learn how to enhance and monitor your AMP pages. |
| [Validate AMP content for Google Search](/search/docs/crawling-indexing/amp/validate-amp) | This article contains tips and pointers about how to validate AMP pages. |
| [Remove your AMP pages from Google Search](/search/docs/crawling-indexing/amp/remove-amp) | Learn how to remove your AMP pages from Google Search. |

FAQs
----

### Are AMP pages mobile-only?

No. Since AMP pages can be viewed on all device types, build your AMP pages with
[responsive
design](https://www.ampproject.org/docs/guides/author-develop/responsive_amp).

### How does AMP look on desktop?

AMP pages display equally well on both mobile and desktop screens. If AMP supports all the
functionality that you need, you might consider creating your pages as
[standalone
AMP pages](https://www.ampproject.org/docs/guides/deploy/discovery#what-if-i-only-have-one-page) to support both desktop and mobile visitors for the same page. However, AMP
on desktop doesn't get search-specific features in Google Search results.
