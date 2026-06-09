---
title: "December 2023 Google SEO office hours"
source_url: "https://developers.google.com/search/help/office-hours/2023/december?hl=en"
product: "Google Search Central"
section: "Help & FAQ"
language: en
scraped_date: 2026-06-08
doc_id: "search-central/help/office-hours/2023/december.md"
---
December 2023 Google SEO office hours
=====================================

This is the transcript for the December 2023 edition of the [Google SEO Office Hours](/search/help/office-hours). For site-specific help,
we recommend posting your question in the [Google Search Central Help Community](https://support.google.com/webmasters/community).

How to index the contents of an `iframe` when using an `iframe`?
----------------------------------------------------------------

**John:** Are there any meta tags required to ensure that the contents of an `iframe` are associated with the page using the `iframe` and not the original page.

Great question, thanks! Let's assume a primary page is embedding a sub-page with an `iframe` element. In general, our systems would try to associate the sub-page's content as a part of the primary page for indexing, but it's not guaranteed, since both pages are normal HTML pages on their own too. If you want to make sure that the sub-page is only ever indexed as a part of the primary page, you can use a combination of [`noindex`](/search/docs/crawling-indexing/block-indexing) + [`indexifembedded`](/search/blog/2022/01/robots-meta-tag-indexifembedded) robots `meta` tags on the sub-page. On the other hand, if you want to make sure that the sub-page is never indexed as a part of the primary page, you can use the appropriate [`x-frame-options`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options) in the HTTP header to prevent embedding via `iframe` elements.

Is hierarchical or flat structure better?
-----------------------------------------

**Gary:** Ido is asking: Which category structure: hierarchical or flat structure for my website?

I think this largely depends on the site's size. For a large site it's likely better to have a hierarchical structure; that will allow you to do funky stuff on just one section, and will also allow search engines to potentially treat different sections differently, especially when it comes to crawling. For example, having a /news/ section for newsy content and /archives/ for old content would allow search engines to crawl /news/ faster than the other directory. If you put everything in one directory, that's hardly possible.

How do I tell Googlebot not to search for links in JavaScript?
--------------------------------------------------------------

**Martin:** Mateusz is asking: I would like to ask how to tell Googlebot not to search for links in selected `<script>` tags for JSON or JavaScript.

Well Mateusz, consider disallowing crawling on these URLs that you don't want crawled clearly in your [robots.txt file](/search/docs/crawling-indexing/robots/intro). Googlebot does not make a request to the JavaScript file, it doesn't see the content and thus not any URLs that it might consider for crawling later on.

I built a site on Core MVC and moved it to HTTPS, why is it not indexing?
-------------------------------------------------------------------------

**John:** Panos asks: I built a new site on Core MVC and moved it to HTTPS and I have problems with indexing the new pages.

Hi Panos, I took a look at your site and how it's indexed. It looks like your site is indexed without the www subdomain, so if you explicitly look for the www version of your site, you won't find much. If you look for the domain alone, such as [site:domain.com](https://www.google.com/search?q=site:domain.com), then you'll find it indexed.

What is the recommendation for non-English page URLs?
-----------------------------------------------------

**Gary:** Kai is asking: What is the recommendation for non-English page URLs? Would it be better to have English language in the slug or use Chinese characters?

It doesn't matter all that much, but using the [language of the content also in the URLs](/search/docs/specialty/international/managing-multi-regional-sites#use-language-specific-urls) can be helpful sometimes for Google Search and for users.

What does the `<meta name="prerender-status-code" content="404">` code do for Googlebot?
----------------------------------------------------------------------------------------

**Martin:** Martin is asking: What does Googlebot do when it finds `<meta name="prerender-status-code" content="404">`?

Well Martin, that's easy to say, Googlebot currently ignores that status code. I guess this is coming from a single page application that is client-side rendered and you want to avoid `soft 404s`, in that case consider adding [`<meta name="robots" content="noindex">`](/search/docs/crawling-indexing/block-indexing) or redirect to a page where the server responds with the `404` status code. For more information on that, see [our documentation at developers.google.com/search](/search/docs/crawling-indexing/block-indexing).

With a new UI/UX, is it better to change everything all at once?
----------------------------------------------------------------

**John:** Anjaney asks: We're preparing to launch a new website design for my company, involving UI/UX improvements and new pages. Is it better to change the page design one at a time?

One complexity is that a relaunch can mean so many different things, from just shifting a website to a new server and leaving everything else the same, to changing domain names and all of the content as well. First, you need to be absolutely clear what's changing on the website. Ideally map out all changes in a document, and annotate which ones might have SEO implications. If you're changing URLs, we have some great guidance on [handling site migrations](/search/docs/crawling-indexing/site-move-with-url-changes) in our documentation. If you're changing the content or the UI, of course that will affect SEO too. If you're unsure about the effects, I'd strongly recommend getting help from someone more experienced - it's easy to mess up a bigger revamp or migration in terms of SEO, if it's done without proper preparation. Even with everything done properly, I get nervous when I see them being done. Fixing a broken migration will take much more time and effort than preparing well. In any case, good luck!

What is the SEO impact of using double slashes in a URL?
--------------------------------------------------------

**Gary:** Ricardo is asking: What is the SEO impact of using double slashes in a URL, such as in "https://www.example.us//us/shop"?

From a puritan perspective, that's not an issue. If you look at [RFC 3986, section 3](https://datatracker.ietf.org/doc/html/rfc3986#section-3.3), the forward slash is a separator and is OK to appear in the URL path as many times as you like, even repeatedly. From a usability perspective it's probably not the greatest idea, and it may also confuse some crawlers.

How can I fix the problem "Video outside the viewport" in Google Search Console?
--------------------------------------------------------------------------------

**Martin:** Igor's asking: How can I fix the problem "Video outside the viewport" in [Google Search Console](https://search.google.com/search-console/about)?

Consider someone searching for a video, landing on a page where they have to scroll to find that video that they just looked for, they're not going to be super happy. The easiest way to fix this problem is to move the video to the top of the page, so people will see it when they land on the page and then actually see the video so that avoids this error and hopefully answers your question. Note: after recording this, we've announced some changes to consider: [Video mode now only shows pages where video is the main content](/search/blog/2023/12/video-is-the-main-content).

How to deal with changed product image URLs that are now hosted on another server?
----------------------------------------------------------------------------------

**John:** Product image URLs are changed and now hosted on another server. How can I tell Google to transfer the current image rank to a new URL?

Well, the easy part is that you just have to update the image elements to point to the new image URLs. I also recommend taking the step to [redirect the old image URLs](/search/docs/crawling-indexing/301-redirects) to the new ones. Keep in mind that images tend to be recrawled less-frequently, so changing image URLs is going to take a bit of time to be reprocessed across all of the search systems. Also check out our [image SEO best practices](/search/docs/appearance/google-images).

My site had a lot of `404` pages, is it a problem?
--------------------------------------------------

**Gary:** Amani is asking: My site had a lot of `404` pages, which I requested to be removed, after a few published articles.

[`404` errors are part of the web](/search/blog/2011/05/do-404s-hurt-my-site). They're fine to have on your site and you shouldn't be afraid of them. The only thing you probably want to look out for is whether a page that YOU consider important is suddenly `404` then I would fix them, but otherwise I wouldn't worry about them.

My site returns HTTP `200` status for `404` pages, is that a soft-404 or cloaking?
----------------------------------------------------------------------------------

**Martin:** Martin is asking: The site returns HTTP `200` status for `404` pages. Is it considered a [soft-404](/search/docs/crawling-indexing/http-network-errors) or cloaking? How bad is this?

Well Martin, it is usually considered a soft-404 and it's not cloaking and you're not on the highway for SEO heck because of this, but it's still undesirable. There are a few ways to avoid this as you usually can set the `404` status on the client-side rendered application. You can still configure a router on your server to always respond with `404` and then use JavaScript redirects to point Googlebot to a page that actually gives them a `404` status code. Alternatively, you can use JavaScript to dynamically add a robots `meta` tag with the value of [`noindex`](/search/docs/crawling-indexing/block-indexing) to avoid these pages from ending up in the index. We have information on this in our [JavaScript documentation on developers.google.com/search](/search/docs/crawling-indexing/javascript/javascript-seo-basics).

How can I recrawl my website after changes?
-------------------------------------------

**John:** Anne Marie asks: How can I recrawl my website so that my students would find the new information?

Hi Anne Marie. Search engines are happy to replace content if you make it clear to them what has happened. For example, if you update a page, make sure that you're bringing that to attention by mentioning it prominently in your website. Or, if you're moving content from one page to another, make sure the old page has a redirect to the new one. In both of these cases, if users go to the old content, they will also be shown the new content, so even if it takes a bit for search engines to figure it all out, your users will get the new content regardless. Hope that helps!

Can the sitemap file link itself?
---------------------------------

**Gary:** El Oueryaghly is asking: Can [the sitemap file](/search/docs/crawling-indexing/sitemaps/overview) link itself or will the sitemap page itself be indexed?

Yes, but it's pointless to force the sitemap indexed. It doesn't hurt your site, but it will also not do any good. If you're worried about it getting indexed or you want to remove it efficiently from search results, add a [`noindex` `x-robots-tag`](/search/docs/crawling-indexing/block-indexing) HTTP header to it.

Is it bad to see a large increase in `404` errors from API paths?
-----------------------------------------------------------------

**Martin:** Evan is asking: On our websites we've recently been seeing a really large increase in `404` errors, based on Google picking up API paths in our raw JSON and crawling them. Is this something we should be worried about?

Hey Evan. No, you don't need to be worried about it. But if you want to avoid Googlebot crawling these URLs, feel free to [use robots.txt to disallow crawling](/search/docs/crawling-indexing/robots/intro) on them. When Googlebot finds URLs somewhere it usually crawls to check if there's content that could be useful to index and show to users. If we get a `404` doing that, well, then it's not going to be useful for users and not going to end up in the index.

Why doesn't my business show up in the search results?
------------------------------------------------------

**John:** Chuck asks: Why doesn't my service based business show up in the search results? My business doesn't show up while searching "snow removal" or "de-ice" in my town, which is one of my listed service areas.

Hey Chuck. I took a look around to try to find your business. On the one hand, the name of your business - whiteout - makes it somewhat hard to find in search because it's such a common word. If you search specifically for the business name, it will show the [Google Business Profile](https://www.google.com/business/) on the side, which is a great way to be present for users. Additionally, you seem to have a Facebook profile that might be your homepage, but it's not really referenced from your other business listings, so it's hard for our systems to discover and index it. My recommendation would be to make sure that you're linking to your website from your various business profiles, so that it's easier to find.

If a PDF ranks in the SERPs, can the user download it, and be redirected to the site?
-------------------------------------------------------------------------------------

**Gary:** Nichole is asking: If a PDF ranks in the SERPs, can the user download the PDF then be redirected to the site where the PDF is found?

To the best of my knowledge you can't do that with PDFs. BUT! You can place a link in the top of the PDF and ask the user to go to your site.

Is accessibility important for ranking?
---------------------------------------

**Martin:** Simon's asking: Is accessibility important for ranking? Thinking about Page Speed Insights interpretation specifically.

Well accessibility isn't exactly important for ranking but for your users some accessibility features such as [image `alt` attribute](/search/docs/appearance/google-images#descriptive-alt-text%20descriptive-titles-captions-filenames) is actually really useful information for Googlebot. But in general you want to build a website that is helpful and useful to your users and to reach as many of them as possible, you probably want to take accessibility into account. It is a very important feature of the web platform.

Why is buying links from third-party websites bad?
--------------------------------------------------

**John:** Rakesh asks: Buying links from third-party websites is one of the violations on Google webmasters. On what basis is that?

Hi Rakesh, nothing has changed with regards to paid links in a really, really long time. I'd recommend reading our [spam policies](/search/docs/essentials/spam-policies#link-spam), especially the section on link spam. If you have additional questions about this, I'd post in our [help community](https://support.google.com/webmasters/community), where you can discuss this with other experts.

Can I do more than reporting paid backlink?
-------------------------------------------

**Gary:** Anonymous is asking: I have reported thousands of paid backlink reports with no noticeable enforcement by Google. How can I help Google act on these reports?

First of all, thank you for reporting those bad links! Keep in mind that we're using those reports to improve our algorithms in general and we don't take individual actions on them. You can read more about this in our blog post on [handling search quality issues](/search/blog/2023/06/reporting-search-quality-issues).

Why is Google indexing URLs with `noindex` and blocked by robots.txt?
---------------------------------------------------------------------

**Martin:** Alvaro is asking: I have URLs with `noindex` and blocked by robots.txt. Few weeks ago, I saw Google was indexing them. What can have happened?

Well Alvaro if you [block crawling via robots.txt](/search/docs/crawling-indexing/robots/intro), Googlebot cannot make a request to these URLs and thus does not see the `noindex`. So allowing crawling for URLs that you don't want indexed helps in this case because we can make a request and see that they are not supposed to be indexed.

Why does my site's impressions decrease despite having updated according to trends?
-----------------------------------------------------------------------------------

**John:** Teemoes asks: Why does the website's impressions continuously decrease even though I have continuously updated new products according to trends? There are no warnings or penalties for my website.

Unfortunately there's more to online success than just adding more pages. On the one hand, it's important that things which you add actually bring new & unique value to the web. On the other hand, it's important that your site overall is unique, compelling, of high quality, and also brings value to the web in ways that users recognize. None of this is trivial, it can take a lot of hard work to figure out what to focus on, where to expand, and where to simplify. And sometimes, it is possible to commit no mistakes and still not win. In short: there is no simple secret to online success.

How do I remove my content from Google's index?
-----------------------------------------------

**Gary:** Pam is asking: How do I remove content from Google index on my website?

The easiest way is to just delete it on your site and wait until Google recrawls and reprocesses its URLs. You can also add a [`noindex`](/search/docs/crawling-indexing/block-indexing) robots directive. Or just use the [removals tool in Search Console](https://support.google.com/webmasters/answer/9689846). You should check out our docs because we have plenty of documentation about this.

Are company-owned blogs eligible to be included in Google News?
---------------------------------------------------------------

**John:** Are company-owned blogs eligible to be included in the Google News feed?

I can't speak directly for Google News, since I work on Search, which is somewhat separate, but looking at [their content policies](https://support.google.com/news/publisher-center/answer/6204050), I don't see anything specific to company blogs. If you're curious if this is an option or not, I'd recommend asking in the [News publisher help community](https://support.google.com/news/publisher-center/community). And, if you're curious whether your pages are already being shown in Google News, I'd check out the [performance reports in Search Console](https://support.google.com/webmasters/answer/7576553).

How does Google handle special characters in the search results?
----------------------------------------------------------------

**Gary:** Gilles is asking: How Google handles special characters like the superscript 'ᵉ' in search results?

Okay, I think this is the first time I get this question in 20 years. It's a super interesting question and thank you for that. Well, if those characters are not displayed correctly in search results that is most likely caused by a mismatch of what Google's algorithms detected as character encoding for your page versus what you meant to use. You should specify the encoding in your HTML using a `meta` element and its `charset` attribute, especially if you're using "funky characters" in your HTML. If the character encoding is not specified, Google will try to detect it, but getting it right is actually a huge undertaking, and it's very very difficult in most of the cases anyway. So yeah, if we are not displaying something correctly in the search results try to specify the character encoding and see if that fixes the issue.

Why is the Search Console position different from the search results?
---------------------------------------------------------------------

**John:** Luke asks: Why is the GSC position significantly different than the SERP search results?

[Search Console's performance data](https://support.google.com/webmasters/answer/7576553) is not theoretical, it's based on what was actually shown in the search results. However, search can be very dynamic, so it can sometimes be hard to reproduce what was shown. My general recommendation is to try to use the filters in Search Console to work out the most likely variation of how it was shown, for example, which country, and then to try to reproduce it. That said, because of the dynamic nature of search, you might not always be able to reproduce it.

Can I arrange SEO directly with Google for free?
------------------------------------------------

**Gary:** Anonymous is asking: Can I arrange SEO directly with Google for free?

No.

Why is Google still showing our closed business website?
--------------------------------------------------------

**John:** Our business is closed but Google is still showing website results.

If you're seeing your old website, you can [request removal of it in Search Console](https://support.google.com/webmasters/answer/9689846). If it's an older Business Profile, you can [mark it as closed](https://support.google.com/business/answer/10417060) in their tool.

With SEO reporting, should I trust Google Analytics or Search Console?
----------------------------------------------------------------------

**John:** Lin asks: With SEO reporting, should I trust GA4 or Search Console? And what're the differences between both?

While both Google Analytics and Search Console give you information on users, it's collected very differently, so it's worth looking at both independently. The [Search Console help center](https://support.google.com/webmasters/answer/7576553#data_discrepancies) has more information on some of the differences, if you're curious.

Can a URL contain periods?
--------------------------

**John:** Can a URL contain periods as part of a SKU as long as not immediately after each other?

Many sites choose to rewrite these kinds of characters, but keeping them is technically fine from Google Search's point of view.

How to know if my SEO is perfect?
---------------------------------

**John:** Charan asks: How to know if my SEO is perfect? Are there any tools, apps or websites available for it?

Sorry to disappoint, Charan, but your SEO is not perfect. In fact, no SEO is perfect. The internet, search engines, and how users search is always changing, so SEO will evolve over time as well. This includes both technical elements, like structured data, as well as considerations around quality. Just because you can't do perfect SEO shouldn't discourage you though!
