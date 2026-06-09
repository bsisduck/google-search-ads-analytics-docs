---
title: "Google Search crawling and indexing FAQ"
source_url: "https://developers.google.com/search/help/crawling-index-faq?hl=en"
product: "Google Search Central"
section: "Help & FAQ"
language: en
scraped_date: 2026-06-08
doc_id: "search-central/help/crawling-index-faq.md"
---
Google Search crawling and indexing FAQ
=======================================

This article brings together answers to the questions about crawling and indexing that we at
Google hear most often.

How do I get my site into Google?
---------------------------------

[Crawling](/search/docs/fundamentals/how-search-works#crawling) and [indexing](/search/docs/fundamentals/how-search-works#indexing)
are processes that take some time and rely on many factors. In general, we cannot make
predictions or guarantees about when or if your URLs will be crawled or indexed. When
looking at your site's indexing in Search Console, make sure that you have both the "www" and the
"non-www" versions (like "www.example.com" and "example.com") verified. Keep in mind that while a
[sitemap file](/search/docs/crawling-indexing/sitemaps/overview) can help us learn about
your site, it does not guarantee indexing or increase your site's ranking.

Learn how to [get your site on Google](/search/docs/fundamentals/get-on-google).

Why isn't my site indexed?
--------------------------

In general, the most common reason that a site is not indexed is because it's just too new; be
patient and [ask Google to crawl and index it](/search/docs/crawling-indexing/ask-google-to-recrawl).

Here are the other common reasons why a website or parts of a website might not be indexed yet:

* A website might not be well connected through multiple links from other sites on the web.
* The design of the website might make crawling and indexing difficult. Maybe the site
  itself is even explicitly [blocking crawling or indexing](/search/docs/crawling-indexing/control-what-you-share)?
* Perhaps it was temporarily unavailable when we attempted to crawl? You might find
  [crawl errors](https://support.google.com/webmasters/answer/7440203)
  in Search Console in this case.
* Verify that the website complies with our [Search Essentials](/search/docs/essentials)
  and hasn't been [hacked](/search/docs/monitor-debug/security/malware)
  or otherwise modified by a third party.
* In very rare cases, it might be that content previously hosted on a domain name is
  causing issues. In this case, you may wish to submit a
  [reconsideration request](https://support.google.com/webmasters/answer/35843)
  detailing the change of content and ownership.
* If the website recently moved to a different address, make sure that you follow our
  [guidelines for moving a site](/search/docs/crawling-indexing/site-move-with-url-changes).
* It's possible that a previous owner or someone else with access to the website
  [requested removal through Search Console](https://support.google.com/webmasters/answer/156412). You can cancel these requests by using the
  [Removals Tool](https://support.google.com/webmasters/answer/9689846).

For more information, check out [Why is my page missing from Google Search?](https://support.google.com/webmasters/answer/7474347).

I have the same content available on two domains. How do I tell Google
that the two domains are the same site?
--------------------------------------------------------------------------------------------------------------

Use a `301` redirect to direct traffic from the alternative domain (example2.org) to your
preferred domain (example.com). This tells Google to always look for your content in one
location, and is the best way to ensure that Google (and other search engines) can crawl
and index your site correctly. Ranking signals (such as PageRank or incoming links) will
be passed appropriately across `301` redirects. If you're changing domains, read about the
[best practices for making the move](/search/docs/crawling-indexing/site-move-with-url-changes).

Do I have duplicate content? Am I being penalized for it? What should I do about it?
------------------------------------------------------------------------------------

Generally, duplicate content is **not** a violation of
[Google's spam policies](/search/docs/essentials/spam-policies). For more
information, read our article on
[Demystifying the "duplicate content penalty"](/search/blog/2008/09/demystifying-duplicate-content-penalty).
If you're still concerned or want to know more, read these articles:

* [Dealing with duplicate content](/search/blog/2006/12/deftly-dealing-with-duplicate-content)
* [Duplicate content caused by URL parameters](/search/blog/2007/09/google-duplicate-content-caused-by-url)
* [Duplicate content caused by scrapers](/search/blog/2008/06/duplicate-content-due-to-scrapers)
* [Reunifying duplicate content on your website](/search/blog/2009/10/reunifying-duplicate-content-on-your)
* [Duplicate content and multiple site issues](/search/blog/2009/09/duplicate-content-and-multiple-site)
* [Define a canonical page for similar or duplicate pages](/search/docs/crawling-indexing/consolidate-duplicate-urls)
* [Handling cross-domain duplication](/search/blog/2009/12/handling-legitimate-cross-domain)

Is it better to use subfolders or subdomains?
---------------------------------------------

You should choose whatever is easiest for you to organize and manage. From an indexing
and ranking perspective, Google doesn't have a preference.

Does validating my site's code (with a tool such as the W3C validator) help my
site's ranking in Google?
--------------------------------------------------------------------------------------------------------

No, at least not directly. However, cleaning up your HTML makes your site
[render better in a
variety of browsers](/search/docs/advanced/guidelines/browser-compatibility) and more accessible.

I'm using a hosting service for my site that uses frames,
"masked redirects", or "masked forwarding". Will this affect my site's crawling, indexing,
or ranking?
----------------------------------------------------------------------------------------------------------------------------------------------------------------

We recommend always hosting your content directly using your domain name. Using a
forwarding service that uses frames will generally make crawling, indexing, and ranking
of your content using your domain name impossible.

I changed some text on my pages. Why isn't it updated in search results?
------------------------------------------------------------------------

Crawling and indexing of pages within a website can take some time. While there's no
way to force an update, here are some tips that may help to speed this process up:

* Ask Google to [recrawl your URLs](/search/docs/crawling-indexing/ask-google-to-recrawl).
* If you are using a [sitemap file](https://sitemaps.org/), make
  sure to update the [last modification date](https://www.sitemaps.org/protocol.html).
* If your site's content is indexed with multiple URLs, [resolving the duplicate content issue within your site](/search/blog/2009/10/reunifying-duplicate-content-on-your)
  will generally allow crawlers to find updated content quicker.

My website uses pages made with PHP, ASP, CGI, JSP, CFM, etc. Will these still get indexed?
-------------------------------------------------------------------------------------------

Yes! Provided these technologies serve pages that are visible in a browser, without
special plugins installed or enabled, Google will generally be able to crawl, index,
and rank them without problems. We have no preference; they're all equivalent in terms
of crawling, indexing, and ranking, as long as we can crawl them.

I recently purchased a domain
that was previously associated with a spammy website. What can I do to make sure that
spammy history doesn't affect my site now?
--------------------------------------------------------------------------------------------------------------------------------------------------------------

[Verify your site in Search Console](https://support.google.com/webmasters/answer/9008080),
then check to see if there's a manual action in the
[Manual Actions report](https://support.google.com/webmasters/answer/9044175).
