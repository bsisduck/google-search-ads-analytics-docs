---
title: "August 2024 Google SEO office hours"
source_url: "https://developers.google.com/search/help/office-hours/2024/august?hl=en"
product: "Google Search Central"
section: "Help & FAQ"
language: en
scraped_date: 2026-06-08
doc_id: "search-central/help/office-hours/2024/august.md"
---
August 2024 Google SEO office hours
===================================

My website is in English and Swahili. The English pages are almost always indexed but not the Swahili ones, why?
----------------------------------------------------------------------------------------------------------------

**John:** My website has English and Swahili pages, the English pages are almost always indexed but not the Swahili ones. Is there any bias from Swahili language?

For the most part, we treat content similarly regardless of the language used on the page. However, they're separate pages, so you need to make sure that they're linked from the rest of your website. A good way to help localized pages in terms of indexing is to cross-link the various language versions. That way, if the English version is well-known, we'll see the links to the other language versions and potentially use them too. This would be in addition to using [`hreflang`](/search/docs/specialty/international/localized-versions). Our [international sites guidance](/search/docs/specialty/international) has a lot of information which you might find useful too!

Can using a lot of `nofollow` or `noindex` tags signal to Google that the site has many low quality pages?
----------------------------------------------------------------------------------------------------------

**Martin:** Anan is asking: Can a lot of internal links with `nofollow` tags or many pages with [`noindex`](/search/docs/crawling-indexing/block-indexing) tags signal to Google that the site has many low-quality pages?

No, it doesn't signal low-quality content to us, just that you have [links you're not willing to be associated with](/search/docs/crawling-indexing/qualify-outbound-links). That might have many reasons - you're not sure where the link goes, because it is user-generated content (in which case consider using `rel=ugc` instead of `rel=nofollow`) or you don't know what the site you're linking to is going to do in a couple of years or so, so you mark them as `rel=nofollow`.

My website has a lot of 404s. Would I lose my site's rankings if I don't redirect them?
---------------------------------------------------------------------------------------

**John:** Mariya asks: My website has a lot of 404s. Would I lose my site's rankings if I don't redirect them?

First off, the 404s wouldn't affect the rest of your site's rankings. Redirects can play a role in dealing with old pages, but not always. For example, if you have a genuine replacement product, such as a new cup that functionally replaces a cup which is no longer produced, then redirecting is fine. On the other hand, if you just have similar pages, then don't redirect. If the user clicked on your site in search of a knife, they would be frustrated to only see spoons. It's a terrible user-experience, and doesn't help in search. Instead, return an `HTTP 404` result code. Make a great 404 page. Maybe even make a 404 page that explains why spoons are superior to knives, if you can make that argument. Just don't blindly redirect to a similar page, a category page, or your homepage. If you're unsure, don't redirect. Accept that [404s are fine](/search/blog/2011/05/do-404s-hurt-my-site), they're a normal part of a healthy website.

When using an image from a CDN, does the response speed determine whether the image appears in Search?
------------------------------------------------------------------------------------------------------

**Martin:** Seonsoo is asking: When a crawler pulls an image from a CDN (content distribution network), does the response speed determine whether the image appears in the search results?

No, the image will appear or not appear for a variety of reasons - one out of many is if we already have this image indexed from another domain, but users will thank you if your images load quickly. Some CDNs have additional features, like dynamically resizing or optimizing compression based on what the user's browser supports, so CDNs can have a few benefits besides speed.

I no longer have access to SC. How do I remove URLs so that after my domain expires, a new owner can't misuse it?
-----------------------------------------------------------------------------------------------------------------

**John:** I am the site owner and I can't login into Search Console because my hosting and my site database has been deleted. I want to remove all the URLs so that after my domain expires, a new owner can't misuse it.

This is an interesting question that I don't think we've run across yet. The data in Search Console is not tied to users, so anyone who verifies the site later on will see that data. There's no way to reset the data shown there, so you'd have to prevent the domain name from expiring. The advantage of this process is that you can re-verify your site in Search Console without any data-loss. To remove all content from search for a site that's already removed from the server, you can use [domain verification for Search Console](https://support.google.com/webmasters/answer/9008080#domain_name_verification) and submit a temporary site [removal request](https://support.google.com/webmasters/answer/9689846). This doesn't remove the site in the index, but will prevent it from being shown for a period of time. If you're selling the domain name, it would be nice to tell the new owner of this removal request, so that they can cancel it if needed.

Can multiple subdomains for various markets with the same content rank specifically for the intended markets?
-------------------------------------------------------------------------------------------------------------

**Martin:** I have a website with different subdomains for various markets with pages that contain the same content. How can I make sure that these rank specifically for the market mentioned in the subdomain?

If it's the same content, it's the same content. If there's variations due to the country, you can tell Google Search that by using `hreflang`` - for example in Germany, Austria and Switzerland, where the content might be similar but currencies and prices might differ, you can use hreflang to suggest to show a certain variation in a certain country. But just because you have regional subdomains or subfolders doesn't make the content unique and show up for specific regions. Check out our [international sites guidance](/search/docs/specialty/international) for more.

My rich results show the wrong currency. Can you help me resolve this issue?
----------------------------------------------------------------------------

**John:** Craig asks: My rich results show the wrong currency. Can you help me resolve this issue please?

Often this is a side-effect of Google's systems seeing the page as being mostly duplicate. For example, if you have almost exactly the same content on pages for Germany and Switzerland, our systems might see the pages as being duplicates, even if there's a different price shown. One approach is to make sure the pages are not that similar. Another approach can be to try to use the [Merchant Center feeds](https://support.google.com/merchants/answer/7439058) for pricing information, instead of using structured data on the page. I'm curious to see what you work out - if you get a chance, feel free to drop me a note on LinkedIn!

How do I mitigate targeted scraping and performance issues?
-----------------------------------------------------------

**Martin:** Anonymous is asking: Our website is experiencing significant disruptions due to targeted scraping by automated software, leading to performance issues, increased server load, and potential data security concerns. Despite IP blocking and other preventive measures, the problem persists. What can we do?

This sounds like somewhat of a distributed denial-of-service issue if the crawling is so aggressive that it causes performance degradation. You can try identifying the owner of the network where the traffic is coming from, thank "their hoster" and send an abuse notification. You can use [WHOIS](https://en.wikipedia.org/wiki/WHOIS) information for that, usually. Alternatively, CDNs often have features to detect bot traffic and block it and by definition they take the traffic away from your server and distribute it nicely, so that's a win. Most CDNs [recognize legitimate search engine bots](/search/docs/crawling-indexing/verifying-googlebot) and won't block them but if that's a major concern for you, consider asking them before starting to use them.

On Search Console I have a shopping tab, but my website is not an online shop. How can I fix it?
------------------------------------------------------------------------------------------------

**John:** On Search Console I have a shopping tab, but my website is not an online shop. How can I fix it?

Thanks for asking! There's nothing you need to do in a case like this. Our systems have recognized some product-related information on some of your pages, which is why we suggest this to you in Search Console. It doesn't mean that our systems assume your website is an online shop, and even if that were the case, there's no downside to that. This is just a way of showing you some options that might be useful for you.

Could a YouTube video and the exact same text or content on the same web page be flagged as duplicate content?
--------------------------------------------------------------------------------------------------------------

**Martin:** If I create a YouTube video and then take that exact text or content and place it on a web page, could Google flag that web page or site for duplicate content?

No, one is a video and the other one is text content, and that would be unique content! It's also not a bad idea, some users (like me) might prefer a text version and others might not be able to use a video version of the content in the first place due to bandwidth or visual constraints.

How can we ensure proper prices are displayed in organic text results for products on a retail website?
-------------------------------------------------------------------------------------------------------

**John:** Chaz asks: How can we ensure proper prices are displayed in organic text results for products on a retail website?

I'd recommend using the [Merchant Center feeds](https://support.google.com/merchants/answer/7439058), if you can. There are ways to submit pricing information in Merchant Center which don't require a lot of work, so I'd check that out. If you can't find ways to resolve this, please drop us a note in the [help forums](https://support.google.com/webmasters/community) with the details needed to reproduce the issue that you're seeing.

Would aggregated reviews from a specific service via structured data for products in our shop impact our SEO?
-------------------------------------------------------------------------------------------------------------

**Martin:** Can we use aggregated reviews from a specific service and feed it to Google via structured data for products on our shop. Would this negatively affect SEO? Asks Sumit Ponia.

No. If you check our documentation on the [technical guidelines for reviews](/search/docs/appearance/structured-data/review-snippet#guidelines), you'll see we specifically have a guideline against that ("Don't aggregate reviews or ratings from other websites"), so it means your pages won't anymore be eligible for review rich results if you do that.

Does Google crawl subfolders in a URL path which don't have pages? Would it be a problem?
-----------------------------------------------------------------------------------------

**John:** Does Google crawl subfolders in a URL path, which don't have pages? Would it be a problem?

Great question, I've seen variations of this over time. It's common to have URLs with paths that don't actually exist. Google's systems generally don't just try variations of URLs out, they rely on links to [discover new URLs](https://www.youtube.com/watch?v=JuK7NnfyEuc). This means that unless you're linking to those subdirectories, most likely Google wouldn't learn about them and try them. That said, even if Google were to try them and they return a 404, that's totally fine! Having pages on your site return 404 when they're not used is expected, and not a sign of a problem.

Why does Google crawl our hacked pages even after a year?
---------------------------------------------------------

**Martin:** Narayan Patel asks: Why does Google crawl our hacked pages after a year, where those pages are 404 and deleted.

Well, it takes a while until Googlebot will give up. Sometimes people remove pages by mistake, sometimes hacked pages come back with legitimate content after a while. Googlebot does not want to miss out on that - and who knows - maybe there are links somewhere on the internet pointing at these pages, too. The good news is that this doesn't hurt your site in Google Search and eventually Googlebot will move on.

I'm based in France, but I want to target the US market with my online shop. Should I change anything in SC?
------------------------------------------------------------------------------------------------------------

**John:** Victoria asks: Hello, I'm based in France and I want to target the US Market with my online shop. Should I change anything on my Search Console settings?

The geotargeting setting no longer exists in Search Console, so there's nothing that you can or need to change there. The main thing that comes to mind is that you might want to consider using a generic top level domain like a .com, if you're currently using a country-specific top level domain like .fr. We have more about how to [work with international websites](/search/docs/specialty/international) in our documentation, if you're keen. For online stores, I'd also check the [Merchant Center documentation](https://support.google.com/merchants/).

I run website audits. Some suggested things that weren't stated in the Search Central docs. Does it matter for SEO?
-------------------------------------------------------------------------------------------------------------------

**Martin:** Ekin is asking: I run several free website audits. Some of them suggested me things that were never mentioned in the Search Central documentation. Do these things matter for SEO?

A lot of audits don't specifically focus on SEO, and those that don't still mention outdated or downright irrelevant things, unfortunately. For example, "text to code ratio" is not a thing - Google Search doesn't care about it. "CSS/JS not minified" is suboptimal for your users because you are shipping more data over the wire, but it doesn't have direct implications on your SEO. It is a good practice though.

I'm having issues with indexing since updating our WordPress Plugins. Help!
---------------------------------------------------------------------------

**John:** I'm having issues with indexing since updating our WordPress Plugins.

I can't speak for WordPress plugins, but it's important to keep in mind that a content management system like WordPress, and any plugins or themes that you install, can significantly change how your website is presented to users and search engines. Settings there can block or break search completely. If you're uncertain and seeing issues after making changes there, I'd recommend getting help from someone who has worked with the specific systems that you're working on, who can help to diagnose issues and guide you to appropriate settings.

Do UTMs in a link with the medium referral remove the SEO value of a backlink?
------------------------------------------------------------------------------

**Martin:** Do UTMs in a link with the medium referral remove the SEO value of a backlink?

No, it doesn't, but you should canonicalise on the target page of that link to the URL without the [UTM parameter](https://support.google.com/analytics/answer/10917952).

How can Software as a Service (SAAS) companies ensure their login page appears in their sitelinks?
--------------------------------------------------------------------------------------------------

**John:** How can Software as a Service companies ensure their login page appears in their sitelinks?

You don't have direct control over what's shown in [sitelinks](/search/docs/appearance/sitelinks). These are essentially normal web results. However, there are a few things you can do with login pages. First off, if you have content behind a login page, redirect logged-out users to the login page and let search engines see that. Secondly, make sure your login page is indexable, don't use [`noindex`](/search/docs/crawling-indexing/block-indexing), and don't [block crawling with robots.txt](/search/docs/crawling-indexing/robots/intro). If you do those things, then your login page will be seen as a normal page on your site, and can be indexed accordingly.

What is the SEO impact of leaving user comments unanswered under blog posts?
----------------------------------------------------------------------------

**Martin:** Josh is asking: What is the SEO impact of leaving user comments unanswered under blog posts?

None. It's text on your pages. Google Search doesn't check if you answered a comment or not. Text is either there or it isn't.

Why does my robots.txt file show as a soft 404 in Google Search Console while it is visible to users?
-----------------------------------------------------------------------------------------------------

**John:** Visal asks: My robots.txt file is showing as a soft 404 in Google Search Console while it is visible to users, why does that happen?

This one's easy. That's fine, you don't need to do anything. The robots.txt file generally doesn't need to be indexed. It's fine to have it seen as a [soft 404](/search/blog/2010/06/crawl-errors-now-reports-soft-404s).

It looks like I am missing the `X-Robots-Tag`. How do I resolve this issue?
---------------------------------------------------------------------------

**Martin:** Eric is asking: It looks like I am missing `X-Robots-Tag`. How do I resolve this issue?

Not a problem. The [`X-Robots-Tag` HTTP header](/search/docs/crawling-indexing/robots-meta-tag#xrobotstag) or the `robots` meta-tag are only relevant if you want Google Search or other search engines to treat a page differently, for example: If you want a page excluded from the index, you can use the `X-Robots-Tag` HTTP header or `robots` meta tag to tell search engines about that. If you don't have one, the page will just be treated like any other page and, most importantly, can be indexed.

How can I fix a "page with a redirect" issue? I have international websites. They use Geo IP redirects.
-------------------------------------------------------------------------------------------------------

**John:** Aneeta asks: How can I fix the "page with a redirect" issue? I have international websites targeting USA, China, Japan and Korea. They use Geo IP redirects. I added `hreflang`. But, when I check the China website in Search Console, I get the error that the "Page is not indexed: Page with redirect". How do I fix this? Can all sites be indexed in Google.

Geo-IP redirects are when a website automatically redirects users in specific regions to their local pages. These can cause significant issues with search engines, as their crawlers would also be redirected. This prevents them from seeing the other local versions of your pages. Anecdotally, these redirects are also annoying to me, and probably many other users. Instead of redirects, we recommend showing banners to users on other country versions, and allowing them to click to their local versions as needed. We have more on this in our [documentation](/search/docs/specialty/international).

If the law for calculating the circumference of a circle is 2πR, then the condition for the existence of a real circle…
-----------------------------------------------------------------------------------------------------------------------

**Martin:** Msb asks: If the law for calculating the circumference of a circle is 2πR, then the condition for the existence of a real circle is the number π, and this number is not real because it is infinite, and therefore there is no real circle in nature, and every circle in nature ends at a certain precision, and real circles exist in our minds and hearts only.

I...my...what? Good point but please don't make me question my model of reality.

I changed my website a year ago and did a lot of work on SEO. Should this be affecting my website's traffic by now?
-------------------------------------------------------------------------------------------------------------------

**John:** Leonard asks: I changed my website a year ago and did a lot of work on SEO. Should this be affecting my website's traffic by now?

It's tricky to say much here. I don't know what specifically you did to work on SEO, and I don't know if that would have resulted in significant changes. There are many best practices which have minimal effect on the day-to-day performance of a website. For example, having a clean page structure helps search engines to better understand the content on a page, but it might not necessarily result in immediate search ranking or traffic changes. The most effective elements of SEO will vary across websites, it takes a lot of experience to go from a long checklist of possible items to a short prioritized list of critical items. Your experience here will grow over time as you practice. I recommend getting input from others, and practicing by helping with challenges that others post in [help forums](https://support.google.com/webmasters/community). Good luck!

Bad actors are trying to make our site appear untrustworthy by sending fake traffic to my site. Help!
-----------------------------------------------------------------------------------------------------

**Martin:** Fabio is asking: Do I have to be concerned about bad actors trying to make our site appear untrustworthy by sending spam or fake traffic to my site? Since site trustworthiness is binary.

It's not really binary and just by sending traffic from questionable sources to a site, that won't be "tainted". If a site itself does shady things, such as spam, malware, sure, that's a problem, but nobody gets to choose or control where traffic or links are coming from, so that's not something Google Search will look at to judge a website's trustworthiness.

Will modifying the page meta title and description affect the current rankings?
-------------------------------------------------------------------------------

**John:** Will asks: We have a website with satisfying ranks and now our product added new features. We need to modify the page meta title & description, does that affect the current rankings?

Yes, or better, maybe. Changing things like titles or headings on pages can result in changes in Search. Similarly, changing the `meta description` on a page can result in changes with how the snippet of a page is shown in Search. This is expected, and usually something that SEOs or site-owners focus on in an attempt to improve things in search.

How do I increase my Google Search Console property limit without making multiple accounts?
-------------------------------------------------------------------------------------------

**John:** How do I increase my Google Search Console property limit? We run a digital agency and want to avoid making multiple accounts.

It's great to hear that your agency is growing, but unfortunately it's not possible to increase those limits in Search Console. Sorry!
