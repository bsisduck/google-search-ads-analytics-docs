---
title: "March 2023 Google SEO office hours"
source_url: "https://developers.google.com/search/help/office-hours/2023/march?hl=en"
product: "Google Search Central"
section: "Help & FAQ"
language: en
scraped_date: 2026-06-08
doc_id: "search-central/help/office-hours/2023/march.md"
---
March 2023 Google SEO office hours
==================================

This is the transcript for the March 2023 edition of the [Google SEO Office Hours](/search/help/office-hours). For site-specific help,
we recommend posting your question in the [Google Search Central Help Community](https://support.google.com/webmasters/community).

How to best update the results for my site?
-------------------------------------------

**John**: Bob asks us: How to best update the SEO results? I pointed a URL to a new WordPress site, but the search results are blending the previous site and the new site.

Hi Bob, there is nothing special that you need to do when updating a website. As Google reprocesses your current website, it will update automatically. There are, however, a few things that you could do. Ideally, when changing the URLs of a website, such as when you remove pages or fold them together, your old URLs should redirect to the new ones. This helps users and search engines. If that's not possible, they should either return a `404` or a `410` result code. I double-checked your site and you're doing this already. If there are pages you urgently need to remove, you can submit these for [removal in Search Console](https://support.google.com/webmasters/answer/9689846). Finally, looking at your site, it feels like the [titles](/search/docs/appearance/title-link) and the [descriptions](/search/docs/appearance/snippet) could be improved. For example, you could put the location, the city and state names, into the titles to make it easier for people to recognize.

How does Google recognize WEBP images?
--------------------------------------

**Gary**: Sam is asking: How does Google recognize WEBP images? Through file extensions or the format of the image itself?

This is an interesting question. Pretty much with all content types, we are actually looking at the content type header in the HTTP response. Images are no different. The image format is actually not learned from the file extension, but rather the content type header the server sends. We may also use other methods to learn what format the image is, but the HTTP header is generally already enough.

Handling the 'could not determine the prominent video' error
------------------------------------------------------------

**Lizzi**: Jimmy is asking: How do I solve the 'Google could not determine the prominent video on the page' error in Search Console?

Hey, Jimmy. So [Search Console](https://search.google.com/search-console/about)shows you a list of affected Pages for this message. So I would take a look at a few of those pages to see if it makes sense to fix. It may be that this is working as intended, based on how you designed the page, and that's totally okay. Prominent means that the video is within view when the page first loads. This is also known as "above the fold". And the video should be appropriately sized, so not too small and not too large. The[video indexing report documentation](https://support.google.com/webmasters/answer/9495631) has more details on this, so you can check that out.

Is one language in two markets seen by Google as duplicate content?
-------------------------------------------------------------------

**John**: Mark asks: It seems having one language on two markets might be seen by Google as duplicate content. How do we work around that?

That's a great question, Mark. This comes up from time to time. There is no duplicate content penalty and no penalty in a case like this. However, you may still be seeing some effects. If the sites have pages with the same content in the same language, then it can happen that we treat one of these pages as a duplicate and pick the other as a canonical. This is on a per page basis. Then when you search for a generic piece of text, we'll only show one of those pages because the other is the same. If you use `hreflang` annotations, we can still swap out the URLs in Search. However, Search Console reports primarily on the canonical URLs. So it might look like we're ignoring the other version. In short, it can be a bit confusing for reporting, but it will still work. To be extra safe, you could show a banner when a user from another country visits to guide them to their appropriate version.

Is it better to use .com for my Dutch website, or .nl?
------------------------------------------------------

**Gary**: Jelle is asking: I have a Dutch website with a .nl domain and recently bought the .com domain as well. Is it better for SEO to use the .com domain for my Dutch website, or the .nl?

Well, big topic, but if at all possible, I'd stay on the .nl version of your domain name. For one, a site move can come with risks. So you generally only want to do them if you really have no other choice. And the second thing is that the .nl version is a very direct signal to all search engines that the site is local to the Netherlands. You don't get that benefit from from the .com domains.

How do I move large number of indexed pages?
--------------------------------------------

**Lizzi**: Anonymous is asking: How do I move large number of indexed pages to another site?

Okay, this sounds like an adventure. Try to minimize your room for errors and isolate the change that you're doing. Don't do any other big changes, like site re-architecture or redesigning. Focus on moving the URLs only, as they are, and make sure to redirect them. Make a list of all the URLs before and after, to monitor that you're redirecting the traffic correctly. We have some [documentation on site moves](/search/docs/crawling-indexing/site-move-with-url-changes) that have more info on what to check to make sure your site move is successful. Good luck!

Will crawl requests in the Search Console cover Google's AdsBot crawling?
-------------------------------------------------------------------------

**John**: Ellen asks: Will crawl requests in the Search Console cover Google's AdsBot crawling? Because we noticed some examples provided by the Search Console Crawler request our product URLs from Merchant Center.

Hi Ellen, and yes, the [crawl stats in Search Console](https://support.google.com/webmasters/answer/9679690) include AdsBot as well. You should see it listed separately in the Googlebot Type section. This is included here because AdsBot uses the same infrastructure as search Googlebots and it's limited through the same crawl rate mechanisms.

How does Google update an indexed URL?
--------------------------------------

**Gary**: Shannon is asking: How does Google update an indexed URL that is returned from search?

Well, Google updates the URL in its index once it is crawled and reprocessed. So we go out with Googlebot, we crawl the URL and then we pass it on to our indexer. And that will probably reprocess that URL. Depending on the popularity of the URL, this may take some time, but we do get there eventually.

Can `hreflang` be read and understood across several sitemaps?
--------------------------------------------------------------

**Lizzi**: Frederick is asking: Can `hreflang` be read and understood across several sitemaps, or do you need all URLs sharing same language in the same sitemap? So one sitemap for DE, for CH, and for AT?

You can do either approach, whichever is easier for you to manage. I would check out our [documentation on cross-site sitemap submission](/search/docs/crawling-indexing/sitemaps/build-sitemap#cross-submit) and the [`hreflang` documentation](/search/docs/specialty/international/localized-versions). There's more info on there about what you need to make this happen and depending on the approach you pick and submission method.

Can I massively request the re-indexing?
----------------------------------------

**John**: Martyna asks: Can I massively request the re-indexing of all products in the shop in Search Console?

Hi Martyna. Unfortunately, there's no button to push to request reprocessing of a whole website. Instead, this is something that happens automatically over time. You can tell us about pages which have changed, using a sitemap file, and most e-commerce setups do this for you. You can also use a [Merchant Center feed](https://support.google.com/merchants/answer/7439882), if it's a matter of product or price updates. If there are individual pages that you'd like to have updated faster, you can do this with the [URL inspection tool](https://support.google.com/webmasters/answer/9012289) in Search Console, where you can request re-indexing. If there are pages you urgently need to have removed, you can also do that in Search Console. In practice, all of this should work automatically if you're using a good e commerce setup.

Why does Google show a URL to be a duplicate of another URL?
------------------------------------------------------------

**Gary**: Lori's asking about duplicate URLs: Google is showing a URL to be a duplicate of another URL, why?

Well, if you sign in into Search Console, the data you get can shed a light on why a particular URL is considered duplicate. But just to blindly answer, we consider two URLs to be duplicate because they were at one point duplicate, or at least near duplicates. You can use your favorite search engine to search for our [documentation on fixing canonicalization issues](/search/docs/crawling-indexing/consolidate-duplicate-urls) for tips on fixing your problem.

Is the `<strong>` tag beneficial for our website?
-------------------------------------------------

**Lizzi**: Varinder is asking: Is the `<strong>` tag beneficial for our website or not, and what's the difference between the `<b>` tag and `<strong>` tag?

Good question. Both the `<b>` tag and the `<strong>` tag are ways that you can specify that text is important, but they're not the same. The `<strong>` tag should be used for things that are more intensely important, urgent, or serious in nature, like a warning. The way I like to remember the difference is that strong is a stronger form of bold.

Why is my specific website not being indexed?
---------------------------------------------

**John**: Hamza submitted a question saying: Please check my robots.txt file. I want to know why my website is not being indexed.

Hi Hamza. You included a copy of your site's robots.txt file in the submission. It included a link to the feed that you're submitting as a sitemap file. So I took a quick look at your site. The good news is that your robots.txt file is not holding your site back. The bad news is that there's very little on your site that I suspect is worth indexing for search. It's not a technical issue. It's a free download type site and it's mostly video and music descriptions with affiliate download links. The text seems to be copied from other sites. My honest recommendation would be to delete the site and to start over with a topic that you're passionate about, and where you have existing knowledge that you can share. If you'd prefer to focus on technical details, then maybe work together with someone who has a content, but who needs technical help. Hope that helps.

Are site: changes a sign of a core ranking system update?
---------------------------------------------------------

**Gary**: Jason is asking: Are drastic changes in site: search results, a tell-tale sign of a core ranking system update?

Good question. Easy answer. No.

Can Google crawl text in images for the best SEO?
-------------------------------------------------

**Lizzi**: Bartu asks: I uploaded an image to my website. It also has text in it. Can Google crawl into that text in the image for the best SEO?

Well, Google can usually extract text from images via OCR. It's better if you provide that information via `alt` text for that image, so we can better understand the context of your image. Not only is it helpful for your readers that might be visiting your site via a screen reader, but it gives you more opportunities to explain how your image relates to the rest of the content on your page.

Does Google's page speed algorithm take into account viewports optimized for speed?
-----------------------------------------------------------------------------------

**John**: Nick asks: Does Google's page speed algorithm take into account web pages that have had their viewport content optimized for speed, rather than the whole page? Sometimes it might not be possible to load the whole page within acceptable time parameters.

Hi Nick. When it comes to search, we use the [core web vitals](https://web.dev/articles/vitals) as a part of how we measure [page experience](/search/docs/appearance/page-experience). The core web vitals include the [largest contentful paint, or LCP,](https://web.dev/articles/lcp) which is probably the closest to your mention of the page loading time. The LCP metric reports the render time of the largest image or text block visible within the viewport, relative to when the page first started loading. I suspect this covers your concern. For more information, we have documentation on the core web vitals and there's a [web vitals discussion group](https://groups.google.com/g/web-vitals-feedback), if you have detailed questions.

Is there any issue for Googlebot in the Arabic region?
------------------------------------------------------

**Gary**: Mirela is asking: Is there any coverage issue for Googlebot in the Arabic region that could affect indexation? GSC can fetch our sitemap.

Well, there are many many reasons why Google couldn't catch a sitemap. But by far the most common is related to the quality of the feed, or more precisely the pages that were sent us through that feed. Keep in mind that a sitemap is not actually required to appear in Search. So just keep doing what you're doing and the problem may go away, as our algorithms reassess the content of your site.

If I have DE, AT and CH sites on my domain - should I then mark DE with `hreflang` 'de'?
----------------------------------------------------------------------------------------

**Lizzi**: Okay, we have another question from Frederick: If I have DE, AT and CH sites on my domain - should I then mark DE with `hreflang` 'de' (not 'de-de'), as it's the most important market for me?

You could do either 'de' or 'de-de'. It depends on your goals and if you need to target by country. If, for example, you're okay with the users in Switzerland landing on your .de country site, then it's fine to just use 'de'.

If Googlebot finds an unlaunched, password-protected website, how does the website get recrawled?
-------------------------------------------------------------------------------------------------

**John**: Leah asks: If Googlebot searchs an unlaunched website that has password access, how does the website get recrawled after the `401` error code? Our site was not launched and hidden behind a password. There was a Googlebot crawl attempt performed in November, but it was blocked. I'm curious how to get the site crawled again.

Hi Leah. I took a quick look at the site you mentioned and it looks like we're crawling it normally now. And, that's the way it should be happening. Locking a staging site away with a password is a common and a recommended practice. In this and in other cases, such as when your server goes down or a page disappears, our systems will retry from time to time. You'll see this in Search Console as crawl errors. When things become accessible, we'll try to to pick up and index the pages again. And if you remove something for good, then those occasional crawl errors are normal and not a cause for alarm.

How can we generate app-store site links?
-----------------------------------------

**Gary**: Olivia is asking: Hi, Search Console team. I noticed some media websites have a site link pointing to the iOS or Google Play App Stores. For example, The Washington Post or Times UK. How can we generate this kind of site links? Thank you.

Well, I'm not from the Search Console team, I'm from the Search team, but I think I can answer this. It's generally coming from the knowledge graph. Once your mobile app is associated with your website, for example, [deep linking](https://developer.android.com/training/app-links) or providing the website in the app stores, from where we can learn, the app may show up in our results in some form. Sometimes as an app result, sometimes as a site link.

Is it allowed to add one structured data inside another type of structure data?
-------------------------------------------------------------------------------

**Lizzi**: Prabal is asking: Is it allowed to add one structured data inside another type of structure data? For example, adding carousel structured data inside Q & A structured data.

Yep. Nesting your structure data can help us understand what the main focus of the page is. For example, if you put recipe and review at the same level, it's not as clear as telling us that the page is a recipe with a nested review. This means that the primary purpose of the page would be a recipe and that the review is a smaller component of that. As a tip, always check the specific feature [documentation](/search/docs/appearance/structured-data/search-gallery) to see if there's any more notes about combining various structure data types. Right now, the only [supported carousel features](/search/docs/appearance/structured-data/carousel) are course, movie, recipe, and restaurant.

Why does Google not show local business map results for some queries?
---------------------------------------------------------------------

**Gary**: Tyson is asking: For the search term 'wedding invitations', Google no longer shows local business map results. Why?

The kind of search features we show for different queries is a very dynamic business and it depends on many factors, such as user location, and data quality may come back eventually. You don't have to worry about it, really.

How does Google define a page that has soft-404 errors?
-------------------------------------------------------

**Lizzi**: Rajeev is asking: How does Google define a page that has soft-404 errors, despite Google's soft-404 error guidelines?

Hey Rajeev. Soft-404 errors usually appear when there's some kind of error happening. For example, if it's missing some resource that should be loading on the page but isn't, which ends up looking very similar to a `404` page. Or it could be that some error string is appearing when the resource fails to load. You can check out Googlebot's view of the page with the [URL inspection tool](https://support.google.com/webmasters/answer/9012289) and see if it looks alright. In your case, if it's a job search results page, then ideally there would be a list of jobs on that page and not an error message for "no jobs found", because the widget failed to load or something. However, if there really are no jobs found, then this page shouldn't really be indexed. Sometimes the soft-404 error is working as intended, and as you noted, you can ignore the error in Search Console if that's the case.

If a company offers different services, is it better to have two websites?
--------------------------------------------------------------------------

**Gary**: Adrian is asking: If a company offers different services, for example, language courses and IT courses, is it better off to have two websites or the same one in terms of SEO?

Well, I'd argue this is largely a business decision rather than a SEO decision. Depending on the setup, having two websites may incur substantial maintenance costs that may outweigh the benefit two separate domains can bring. If that's not an issue, having a different website for your users in different regions or different categories of courses that you provide is sometimes helpful, especially if it's a localized website. So for example, if you are providing a version for iOS users or English-speaking users and the German speaking users, in those cases especially users tend to click more easily on your website and stick around your website more.

What does 'This URL is not allowed for a sitemap at this location' mean?
------------------------------------------------------------------------

**Lizzi**: Zain is asking: What does the error mean for an XML `hreflang` sitemap that says - 'This URL is not allowed for a sitemap at this location'? I submitted `hreflang` for both country sites through sitemap submission, but got errors and I'm unsure how to troubleshoot.

Hey Zain. Make sure you're verified for both of the country sites in Search Console and check to make sure that the URL is in at a higher level than wherever the sitemap is stored. If you're still having an issue, you can check out the [troubleshooting sitemap's guidance in the Search Console Help Center](https://support.google.com/webmasters/answer/7451001#zippy=%2Cerror-list) or post in the [forums](https://goo.gle/sc-forum) with more details about your sitemap and the URL that's not working. Hope that helps.

Why do organic searches display a different image than the main image?
----------------------------------------------------------------------

**Gary**: Martina is asking: Why organic searches display a different image next to the link than the main image for the linked product?

The images within Google Search results are not necessarily the main image of the page, but rather the image that's the most relevant to the user's query, based on the signals we have for that particular image.

What are the implications of using an infinite scroll with no numbered pagination?
----------------------------------------------------------------------------------

**John**: Adam asks: What are the implications of using an infinite scroll with no numbered pagination links on an e-commerce site?

Hi Adam. One of the difficulties with infinite scroll in terms of Google Search is that search engines need to do the scrolling in order to see the next segment of content. In practice, at Google, this is done through a technique called "viewport expansion", where we render a page like a very long phone. However, this isn't particularly efficient and it can mean that we don't see the infinite content you might have. Because of that, it's strongly recommended that you have some pagination links in addition to any infinite scrolling that you might do. Pagination allows search engines to explicitly access specific pages, making it easier to index as much as possible. For e-commerce sites, we have more about this in our [Search Central documentation](/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading).
