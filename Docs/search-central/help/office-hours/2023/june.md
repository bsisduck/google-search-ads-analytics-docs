---
title: "June 2023 Google SEO office hours"
source_url: "https://developers.google.com/search/help/office-hours/2023/june?hl=en"
product: "Google Search Central"
section: "Help & FAQ"
language: en
scraped_date: 2026-06-08
doc_id: "search-central/help/office-hours/2023/june.md"
---
June 2023 Google SEO office hours
=================================

This is the transcript for the June 2023 edition of the [Google SEO Office Hours](/search/help/office-hours). For site-specific help,
we recommend posting your question in the [Google Search Central Help Community](https://support.google.com/webmasters/community).

Our syndicated version appears in Google Discover despite using canonical links. Why?
-------------------------------------------------------------------------------------

**John:** Beth asks: We allow our content to be syndicated. However, many times the syndicated version appears in Google Discover despite using canonical links. How can we avoid this?

Well, this is timely. We just recently expanded our [guidance for syndicated content](/search/docs/crawling-indexing/canonicalization-troubleshooting#syndicated-content) to help cover this. The `link rel=canonical` is a signal which helps us with canonicalization, as a hint. If your content is being syndicated, and you don't want the syndicated versions to appear at all in Search, we recommend making sure that the syndicated versions also include a [`noindex` robots `meta` tag](/search/docs/crawling-indexing/block-indexing). This blocks them from appearing in Search, while still allowing users to access the page normally.

Is it OK for 2 domains with different TLDs target the same country for the same keywords?
-----------------------------------------------------------------------------------------

**Gary:** Sagar is asking: Is it okay for 2 domains with different TLDs target the same country for the same keywords?

My gut reaction is whether this would be confusing for your users: two domains each having presumably the same content might be confusing. From a policy perspective this might also seem like search result manipulation, I'd check out [Google's spam policies](/search/docs/essentials/spam-policies).

Do Lighthouse JavaScript warnings have any influence on page rating or ranking?
-------------------------------------------------------------------------------

**Martin:** Arnd is asking: If Lighthouse JavaScript warnings for [libraries with known security vulnerabilities](https://developer.chrome.com/docs/lighthouse/best-practices/no-vulnerable-libraries) do have any influence on page rating or ranking?

Hi Arnd, thanks for the question. No. Generally that doesn't have any input on ranking. However, it is a really bad idea to ignore security warnings and issues. I highly recommend you fix these as soon as possible.

How do I block Googlebot from crawling a specific section of a web page?
------------------------------------------------------------------------

**John:** Sean asks: How do I block Googlebot from crawling a specific section of a web page? On the product pages, we have an also bought section. This often contains small add-ons that are not a big part of our website.

The short version is that you can't block crawling of a specific section on an HTML page. There are two similar things though: you can use the `data-nosnippet` HTML attribute to prevent text from appearing in a search snippet, or you could use an `iframe` or JavaScript whose source is [blocked by robots.txt](/search/docs/crawling-indexing/robots/intro). Using a robotted `iframe` or JavaScript file is usually not a good idea, since it can cause problems in crawling and indexing that are hard to diagnose and resolve. If this is just for content that's reused across your pages, I wouldn't worry about it—there's no need to block Googlebot from seeing that kind of duplication.

I submitted a sitemap but it's not showing in search results. Why?
------------------------------------------------------------------

**Gary:** Someone's asking: I submitted a sitemap but it's not showing in search results.

I'm assuming that you are talking about the URL, in which case I would remind you that [sitemaps](/search/docs/crawling-indexing/sitemaps/overview) are a way to tell search engines where your content is, but that's pretty much all. It won't guarantee that the URLs you supplied will be crawled, and it definitely doesn't guarantee they will be indexed. Both depend on the quality of the content and its relative popularity on the internet.

Why does structured data show errors on Google but not schema.org?
------------------------------------------------------------------

**Martin:** Corey is asking: Why does structured data show errors on Google but not schema.org? Google Search Console is showing errors for invalid enum value in field "returnFees" but our schema.org test says no error. Please advise.

Thanks for the question Corey. [schema.org](https://schema.org) is an open and vendor-independent entity that defines the data types and attributes for structured data. Google, as a vendor however, might have specific requirements for some attributes and types in order to use the [structured data in product features](/search/docs/appearance/structured-data/search-gallery), such as our rich results in Google Search. So while just leaving out some attributes or using some type of values for an attribute is fine with schema.org, vendors such as Google and others might have more specific requirements in order to use the structured data you provide to actually enhance features and products.

Does the integration of security headers such as for HSTS have a ranking influence?
-----------------------------------------------------------------------------------

**John:** Arnd asks: Does the integration of security headers such as for HSTS have a ranking influence?

No, the [HSTS header](https://web.dev/articles/enable-https#hsts) does not affect Search. This header is used to tell users to access the HTTPS version directly, and is commonly used together with redirects to the HTTPS versions. Google uses a process called [canonicalization](/search/docs/crawling-indexing/canonicalization) to pick the most appropriate version of a page to crawl and index—it does not rely on headers like those used for HSTS. Using these headers is of course great for users though.

Does Google do any kind of comparisons between current and previous XML sitemap versions?
-----------------------------------------------------------------------------------------

**Gary:** Bill is asking: Does Google do any kind of comparisons between current and previous XML sitemap versions to see what's new or what's been removed from a site?

The absolute answer is yes, we will not reprocess a sitemap that hasn't changed since it was last crawled, but that's just a software optimization to not waste resources. As soon as you change something in your sitemap, be that a URL element or lastmod, the sitemap will be parsed again and generally reprocessed. That doesn't mean that the URLs will be surely crawled, they are subject to the quality evaluations like any other URL. Also worth noting that if you remove a URL from the sitemap (because it doesn't exist anymore perhaps), that doesn't mean it's automatically going to be dropped from the index, or even prioritized for crawling so it can be dropped sooner.

What is the difference between an XML sitemap and HTML? I have an error message in Search Console.
--------------------------------------------------------------------------------------------------

**John:** Maro Samy asks: What is the difference between an XML sitemap and HTML, and what is the resolution of this case in Search Console when it says "your sitemap appears to be an HTML page. Please use a supported sitemap format instead"?

This is an unfortunate consequence of using pretty much the same name for both the XML file as well as for the HTML page. A HTML sitemap can be helpful for users, it's more like a higher level map. An XML sitemap is only for crawlers, it's a file made for robots. To add my personal opinion, a HTML sitemap is often a sign that your website's navigation is too confusing, so I might try to fix that instead of creating a sitemap page.

How does Google treat structured data with parsing errors?
----------------------------------------------------------

**Gary:** Animesh is asking: How does Google treat structured data with parsing errors?

It doesn't. If some structured data doesn't parse, we can't extract the information that it may contain, so it's just ignored.

Are numbers in the URL bad for SEO? Are they a bad idea to include in the URL?
------------------------------------------------------------------------------

**John:** Are numbers in the URL bad for SEO? Are they a bad idea to include in the URL?

No. Numbers in URLs are not bad. Use numbers, use letters, use non-latin letters, or even unicode symbols if you want. The only thing I'd avoid in URLs is temporary identifiers that change every time you visit a page, since this makes crawling very hard and confusing.

Why is my website URL blocked?
------------------------------

**Gary:** Claudio is asking: Why is my website URL blocked?

It is not, it's well and happy, just not ranking. I'd check out our [SEO starter guide](/search/docs/fundamentals/seo-starter-guide) to get an idea what you'll need to do to get liftoff, and then get more tips from other reputable SEO focused sites and people, like [Moz](https://moz.com/beginners-guide-to-seo) and [Aleyda Solis](https://www.aleydasolis.com/en/seo-resources-tools/) respectively.

"Index Bloat"—is that a real thing that impacts Google crawling and indexing?
-----------------------------------------------------------------------------

**John:** "Index Bloat"—is that a real thing that impacts Google crawling and indexing?

I'm not aware of any concept of index bloat at Google. Our systems don't artificially limit the number of pages indexed per site. I'd just make sure that the pages which you're providing for indexing are actually useful pages, but that's independent of the number of pages your site has.

How do I block Googlebot from even touching my site reliably and permanently?
-----------------------------------------------------------------------------

**Gary:** Someone's asking: How do I block Googlebot from even touching my site reliably and permanently? Not for a few months or something like that, but forever.

The simplest way is [robots.txt](/search/docs/crawling-indexing/robots/intro): if you add a `disallow: /` for the `Googlebot` user agent, Googlebot will leave your site alone for as long you keep that rule there. If you want to block even network access, you'd need to create firewall rules that load our IP ranges into a deny rule. You can get the list of our IP addresses following our [documentation about verifying Googlebot](/search/docs/crawling-indexing/verifying-googlebot).

Can an SEO company get a Google approved badge?
-----------------------------------------------

**John:** Michael asks: Can an SEO company get a Google approved badge?

I'm not aware of a Google SEO certification. There are certifications for certain products, like for Google Ads, but I'm not aware of one for SEO. For official certifications, I'd double-check the source directly, rather than to take someone's word for it.

Can having multiple navigation menus hurt SEO performance?
----------------------------------------------------------

**Gary:** Anonymous is asking: Can having multiple navigation menus hurt SEO performance? A main menu with all the most important categories of the site and "secondary" menus to enhance categories related to brand extensions.

It's highly unlikely that having multiple navigation menus will have any effect on your site's SEO performance.

I tried to get HTML and ASPX pages to index but only a few HTML pages got indexed. Help!
----------------------------------------------------------------------------------------

**John:** I tried to get HTML and ASPX pages to index and only a few HTML pages got indexed. I need help!

From our side, there's nothing special with these file endings. URLs with these endings can be normal HTML pages, and we can index them. Hiding the ending does not change anything for Google's systems. For general questions about crawling and indexing, I'd recommend checking out our [help community](https://support.google.com/webmasters/community)—folks there can be super-helpful.

I see two results from the same domain but different web pages, the second one is slightly indented. Why?
---------------------------------------------------------------------------------------------------------

**Gary:** Shin is asking: I see two results from the same domain but different web pages, the second one is slightly indented. What is that?

They are called [host groups](/search/docs/appearance/visual-elements-gallery#host-group)! You can't really influence them with markup, but it's a tell that you have more than 1 page that can rank well for a certain query. You might want to consolidate those two pages if possible? You can learn more about host groups in our [visual element gallery](/search/docs/appearance/visual-elements-gallery).

Is a fake Googlebot allowed? It mentions the official URL but is on a different IP address?
-------------------------------------------------------------------------------------------

**John:** Arnd asks: Is a fake Googlebot allowed? It mentions the official URL but is on a different IP address?

Unfortunately, anyone can specify any user agent name, and it happens that scripts use a Googlebot user agent name in an attempt to appear legitimate. We publish the [IP ranges that Googlebot uses](/search/docs/crawling-indexing/verifying-googlebot#use-automatic-solutions), as well as a way to confirm that requests are legitimate, in our documentation. In your particular case, the IP address maps back to Hetzner Online, a hoster in Germany. If you're seeing many requests like this, it might be worth contacting their abuse department.

Is there a way to disavow IP addresses instead of domain names?
---------------------------------------------------------------

**Gary:** Muhammad is asking: Is there a way to disavow IP addresses instead of domain names?

No, there isn't.

What is the purpose of using NOODP generally found in Blogger?
--------------------------------------------------------------

**John:** What is the purpose of using NOODP generally found in Blogger?

That's a blast from the past! Google has not used this robots `meta` tag in ages. It goes back to the [DMOZ open directory project](https://en.wikipedia.org/wiki/DMOZ), where sites were listed with a short description. The `meta` tag told search engines to ignore that description. The Open Directory Project or ODP does not exist anymore, and this `meta` tag has no effect. It also doesn't cause problems, so leaving it is fine too.

Does "main content" mean that the video has to be the absolute first element on the page?
-----------------------------------------------------------------------------------------

**Gary:** Frederick is asking: Since April 13, a video has to be the main content of the page if a thumbnail should show in SERPs. Does "main content" mean that the video has to be the absolute first element on the page?

No. Think about the users' perspective: they end up on your page and then they have to actively look for the video instead of having it in their face right away. The former is pretty confusing and that's why we're looking for videos that are the main content: basically "in your face". If you look at the large video sites such as Vimeo or YouTube, then you can get a sense of what our algorithms are looking for.
