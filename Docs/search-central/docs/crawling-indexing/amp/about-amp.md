---
title: "Understand how AMP works in search results"
source_url: "https://developers.google.com/search/docs/crawling-indexing/amp/about-amp?hl=en"
product: "Google Search Central"
section: "Docs / Crawling & Indexing"
language: en
scraped_date: 2026-06-08
doc_id: "search-central/docs/crawling-indexing/amp/about-amp.md"
---
Understand how AMP works in search results
==========================================

Google Search indexes [AMP](/amp)
pages to provide a fast, reliable web experience. When an AMP page is available, it can be
featured on mobile search as part of rich results and carousels. While AMP itself isn't a
ranking factor,
[speed is a ranking factor](/search/blog/2018/01/using-page-speed-in-mobile-search)
for Google Search. Google Search applies the same standard to all
pages, regardless of the technology used to build the page. For more information on the
benefits of using AMP, see the
[AMP Project success stories](https://amp.dev/success-stories/).

When users select an AMP page, Google Search retrieves the page from the
[Google AMP Cache](/amp/cache), enabling a variety of load optimizations that often
make these pages appear instantly, such as prerendering. Currently, AMP pages on desktop aren't
served from the Google AMP Cache/AMP Viewer.
[Canonical](/search/docs/crawling-indexing/consolidate-duplicate-urls) AMP Pages behave
like standard results.

Initial display in Search results
---------------------------------

AMP pages can appear in Google Search as a [rich result](/search/docs/appearance/structured-data/search-gallery),
just like other pages on the web. To help Google better understand your page, you can add
[structured data](/search/docs/appearance/structured-data/intro-structured-data) to your page. It's
important to note that Google doesn't guarantee that adding
structured data will enable a rich result in Search results. For more information, refer to the
[Structured Data General Guidelines](/search/docs/guides/sd-policies).

If you have duplicate pages for the same content, place the same structured
data on all page duplicates, not just on the canonical page. For more information on placement,
see the [Structured Data General
Guidelines](/search/docs/guides/sd-policies#location).

AMP pages can also appear as Web Stories. Learn more about how to
[enable Web Stories on Google Search](/search/docs/appearance/enable-web-stories).

After users click AMP content
-----------------------------

When users click your AMP content in Google Search, AMP content may be shown in one of two ways:

* **[Google AMP Viewer](#about-google-amp-viewer)**: At the top of the Google AMP
  Viewer, the domain of your content is displayed so that users understand who published
  it.
* **[Signed exchange](#about-signed-exchange)**: A technology that allows the browser to treat a document
  as belonging to your
  [Origin](https://en.wikipedia.org/wiki/Same-origin_policy).

![An illustration that compares how AMP content can be displayed. The first image shows AMP content displayed in the Google AMP Viewer. The callouts point out the Google AMP Viewer URL and the Original AMP Source bar. The second image shows navigation using signed exchange. The callouts point out the website's URL and more space for the website.](/static/search/docs/images/amp07-signed-exchange.png)

### About the Google AMP Viewer

The Google AMP Viewer is a hybrid environment where you can collect data about the user in
browsers that support the Google AMP Viewer. The Google AMP Viewer may render when our systems
determine it can provide a helpful user experience, especially in situations where swiping
through content is expected. Data collection by Google is governed by Google's
[privacy policy](https://www.google.com/policies/privacy/). As an AMP page publisher
whose content is displayed in the Google AMP Viewer, your data collection is governed by your
privacy policy. Because you choose the behaviors and vendor integrations in your AMP page, you
are responsible for fulfilling the compliance obligations that result from those choices.

### About signed exchange

A signed exchange allows you to use first party cookies to customize content and measure
analytics. Your page appears under your URL instead of the `google.com/amp` URL.
Google Search prioritizes linking to content as signed exchange over using the Google AMP
Viewer in browsers that support signed exchange. To provide users with results in this format,
you must publish AMP content as a signed exchange in addition to the regular AMP HTML format.
Currently, signed exchange is only supported in Google Search for rich results and basic
results, not carousels. To learn more about setting up signed exchange for AMP pages, visit
[Serve AMP using Signed Exchanges](https://amp.dev/documentation/guides-and-tutorials/optimize-and-measure/signed-exchange).
