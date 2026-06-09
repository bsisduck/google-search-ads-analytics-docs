---
title: "July 2023 Google SEO office hours"
source_url: "https://developers.google.com/search/help/office-hours/2023/july?hl=en"
product: "Google Search Central"
section: "Help & FAQ"
language: en
scraped_date: 2026-06-08
doc_id: "search-central/help/office-hours/2023/july.md"
---
July 2023 Google SEO office hours
=================================

This is the transcript for the July 2023 edition of the [Google SEO Office Hours](/search/help/office-hours). For site-specific help,
we recommend posting your question in the [Google Search Central Help Community](https://support.google.com/webmasters/community).

Issues with my website appearing on Google. Help!
-------------------------------------------------

**John:** Shimmy asks: Hi there, I am having an issue with having my website appear on Google, and this is the site and they specify the URL.

Hi Shimmy, I took a look at your website. Unfortunately, when Googlebot crawls the site with a smartphone user-agent, the site returns a `403` HTTP status code. This tells us that there's nothing to index, so we don't index anything. To check that, you can use Google Search Console's [URL inspection tool](https://support.google.com/webmasters/answer/9012289).

What is less harmful: millions of `404` error pages or `301` redirects?
-----------------------------------------------------------------------

**Gary:** Someone's asking: What is less harmful: having millions of `404` error pages or millions of `301` redirects, where sold product pages redirect to the parent listing page?

`404` status codes are completely harmless, and so are `301`. You need to decide what's better for your scenario for and fly with that.

What URL format and declared canonical is the most optimal for an ecom site's category pages to get indexed?
------------------------------------------------------------------------------------------------------------

**Martin:** Ksenia's asking: What URL format and declared canonical is the most optimal for an ecom site's category pages to get indexed? Would it depend on Client Side Rendering (CSR) or Server Side Rendering (SSR)?

Canonicalisation looks at the recommendation of the site owner through the link rel canonical tag as well as how well a URL is linked from other places on the web and a bunch of other aspects. If you can canonicalise a shorter URL, that's great. If you can't, that's not a problem. You can build CSR applications in many different ways, supporting shorter URLs but none of this impacts indexing, so I wouldn't worry too much. Also there is no difference in canonicalisation for CSR or non-CSR sites.

Why does my search results only show prices in USD when my site has other currencies? I tested with a VPN.
----------------------------------------------------------------------------------------------------------

**John:** My search results only show prices in USD. When I test with the help of the search results, the price currency remains the same everywhere, even though my site shows other currencies, even if I am connected to VPN I still have the same issue.

Thanks for providing an example page! I took a look, and your website seems to change the currency and price depending on where the user is from. Since we mostly crawl from the US, this means that we just see the price as you'd show it to users there, which is in US dollars. To show multiple currencies in search, you need to have separate URLs per currency, and to show the price in that currency to all users of that page.

I purchased a domain name and tested it, and it comes up with a `404` error. Why?
---------------------------------------------------------------------------------

**Gary:** Gwendolyn is asking: I purchased a domain name for $12/yr. I tested it and it comes up with a `404` error.

So for your domain to show up in Google's search results it will need to be hosted by a hosting company. That can be even something like Wordpress.com or Wix.com or Blogger, where you associate your domain name with a location of your content. Then you just start creating high quality content and you're generally good to go.

How do I avoid Google selecting incorrect canonical URLs from another country domain according to Search Console?
-----------------------------------------------------------------------------------------------------------------

**Martin:** Luisa is asking: Google selects incorrect canonical URLs from another country domain according to Search Console, although `hreflang` attributes are correctly assigned. How can this problem be avoided?

Canonicalisation and hreflang are intertwined but slightly different concepts. With hreflang, you basically told Google "these pages are the same, but in different languages and/or regions", canonicalisation then makes a decision on which one to be the "main" URL in our index. If you create a group of pages with roughly the same content, but in different languages or for different regions, canonicalisation will still pick a main URL, but other URLs can and will show up in the search results, depending on the user's language and region. In your specific example, users in Germany are likely to see the .de domain, even if the .at or .ch domain is selected as the canonical. What makes this a bit trickier is, that Austrian and German pages probably are very, very similar in their content - so this might not always work 100%, so it's a good idea to let people choose which region they prefer to look at, should the selection be off.

I searched for my website on Google and found links which were written in Chinese. I want to delete them.
---------------------------------------------------------------------------------------------------------

**John:** Mohamed asks: When I tried to search for my website on Google I found many links which were written in Chinese, and now I want to delete those links permanently.

Search reflects what websites publicly show users. If there are links from Chinese language websites that are publicly accessible, which allow crawling and indexing, then Google may pick those up. Using the [disavow links](https://support.google.com/webmasters/answer/2648487) tool can tell Google that you don't want them taken into account for ranking, but it won't remove them from the web, or from our systems. Having links from websites in other languages is fine. And, assuming these are random spammy links that you just don't care about, you don't need to do anything with them, you can just ignore them.

How do I change my website address from an old domain to a new domain?
----------------------------------------------------------------------

**Gary:** Someone's asking: How do I change my website address from old domain to just new domain?

Fortunately there are hundreds if not thousands of guides on the internet on how to do a site move. Even we have a [guide about how to do site migrations](/search/docs/crawling-indexing/site-move-with-url-changes).

How can the content in a product page be unique when different sellers offer the exact same product?
----------------------------------------------------------------------------------------------------

**Martin:** Someone asks us: How can the content in a product page be unique when different sellers offer the exact same product?

To be unique, you can offer your own perspective, a genuine review or test you did of the product or things you found to be useful to know about the product, outside of the default product text and specifications issued by the manufacturer, for example.

How can we separate the report on Google Search Console based on the subdomain?
-------------------------------------------------------------------------------

**John:** Reina asks: How can we separate the report on Google Search Console based on the subdomain?

Yes! You can [verify subdomains](https://support.google.com/webmasters/answer/9008080) in Search Console, you can also verify subdirectories there. If you have the domain verified, then you can just add those subsections without needing to do anything special for verification. As with all new sites in Search console, depending on the report, it might take a few days for data to start appearing.

Can a lot of `404` pages lead to negative effects?
--------------------------------------------------

**Gary:** Can a big amount of `404` pages in GSC lead to negative effects of rankings of status `200` pages?

No.

How can I get Google Discover to come back?
-------------------------------------------

**Martin:** Siamak Ahadi is asking: No longer in Google Discover... What to do to come back?

[Discover](/search/docs/appearance/google-discover) is an organic feature that goes with the demand and habits of users. So there's no easy answer on how to bring Discover traffic back. Generally, content that is indexed and meets our content guidelines can be included in Discover. But as Discover traffic is hard to predict and will ebb and flow.

What is the schema type for an affiliate site?
----------------------------------------------

**John:** Shihabur asks: What is the schema type for an affiliate site?

First off, affiliate sites are fine, but making sure your website provides helpful, user-first content is the foundation you should be building on. There is no special structured data that you can use to signal that a website is an affiliate of another website. It's fine to monetize your website with affiliate links. Our guidance is to [label these affiliate links](/search/docs/crawling-indexing/qualify-outbound-links) accordingly, using either `rel=nofollow` and or `rel=sponsored`, so that search engines know that they're affiliate links.

How do I create a good robots.txt?
----------------------------------

**Gary:** Someone's asking: Bonjour, je ne sait pas comment créé un bon robot.txt? Or in English: Hi, how do I create a good robots.txt?

There's no general "good robots.txt". A good robots.txt fits your specific needs. For example, you might not want to allow crawling your internal search results (good), or you want to allow crawling a specific JavaScript file. It all depends on your website and how it's set up. We do have [documentation about robots.txt files](/search/docs/crawling-indexing/robots/create-robots-txt) on developers.google.com/search though, check it out!

Can you explain how Google uses quality raters to review and rate sites?
------------------------------------------------------------------------

**Martin:** Geoffrey: Can you explain how Google uses quality raters to review and rate sites. Does it only happen after a penalty, or is it routine for quality raters to review your site?

Quality raters technically look at individual websites, but don't change the live rating. We use responses from raters to evaluate changes, but they don't directly impact how our search results are ranked. You can learn more about this at [goo.gle/quality-raters](https://goo.gle/quality-raters).

GSC is showing 1 million "pages with redirects" despite a site migration a year ago. Why?
-----------------------------------------------------------------------------------------

**John:** Robin asks: Our website went through a site migration about a year ago. To this day Search Console shows us about 1 million "pages with redirect". Is there anything we can or should do?

That can be perfectly normal. Google's systems sometimes like to remember old URLs for a long time. That's not a sign of a problem, as long as these older URLs are still redirecting, that's all fine. You don't need to get them out of Google's memory - and you can't do that anyway. Over time, they generally drop out step by step. Any recent performance change you might be seeing would be unrelated to the older site-move.

My website domain is not showing when you search on Google. Why?
----------------------------------------------------------------

**Gary:** Eugene is asking: My website domain is not showing when you search on Google. Why?

I looked at your website and I strongly suggest that you verify it in [Search Console](https://search.google.com/search-console/about) and look for hints there. It's probably an easy fix once you're in your Search Console account.

Our domain is used only for email accounts. How can I stop it appearing in Google search results?
-------------------------------------------------------------------------------------------------

**Martin:** Amanda is asking: Our domain is used only for email accounts. How can I stop it appearing in Google search results?

Well if you're only using it for emails, then you don't really have content that could show up in search results. If you care about Googlebot not making requests to your domain, you can [use robots.txt](/search/docs/crawling-indexing/robots/intro) to block it from accessing any URL on your domain. That does not necessarily prevent the pages from showing up in Google search results. To do that, you'd have to use a [robots meta-tag or HTTP header](/search/docs/crawling-indexing/robots-meta-tag) and set to "`noindex`". If you don't even have a website on the domain and just use it for email, then there's nothing for Googlebot to see in the first place and it won't show up in search results anyway.

SC says my site's crawled by Googlebot desktop. What is preventing the migration to mobile index?
-------------------------------------------------------------------------------------------------

**John:** Pottier asks: Hello, in Search Console, my site is displayed to be crawled by the Googlebot desktop. I would like to know, if possible, what is preventing the migration of my site to the mobile index?

Most likely, your site is already in mobile first indexing. To double-check, you can go to the [crawl stats in Search Console](https://support.google.com/webmasters/answer/9679690), and check the crawler types mentioned there. If the smartphone Googlebot is the most common crawler type, then you're all set. Essentially all sites are being crawled and indexed with their mobile versions now, the handful of ones which are only crawled with a desktop crawler are those which essentially do not work at all with mobile devices.

Could the query string in `hreflang` give mixed signals to Google in any way?
-----------------------------------------------------------------------------

**Gary:** VT is asking: Could the query string in `hreflang` give mixed signals to Google in any way? For example, in: `<link rel="alternate" hreflang="en-us" href="https://www.domain.us?setContextLanguageCode=en-us" >`

Easy: this shouldn't cause big issues. I can't promise it won't cause issues at all though: you need to be consistent with these things, otherwise you might get some [canonicalization](/search/docs/crawling-indexing/canonicalization) surprises.

What is the effect of website form design and form position in SEO ranking?
---------------------------------------------------------------------------

**Martin:** Somnath Halder's asking: What is the effect of website form design and form position in SEO ranking?

Forms don't play a special role in ranking. It's content like any other content and as such the visual design doesn't matter much, but where you place it on the site might give Google an idea of the importance of the content. If you are using overlays for your forms, be aware that this might have an [impact on user experience](/search/docs/appearance/avoid-intrusive-interstitials) on your site.

Would removing pages improve crawlability and indexability?
-----------------------------------------------------------

**John:** Would deindexing and aggregating 8M used products into 2M unique indexable product pages help improve crawlability and indexability (Discovered - currently not indexed problem)?

It's impossible to say. I'd recommend reviewing the [large site's guide to crawl budget](/search/docs/crawling-indexing/large-site-managing-crawl-budget) in our documentation. For large sites, sometimes crawling more is limited by how your website can handle more crawling. In most cases though, it's more about overall website quality. Are you significantly improving the overall quality of your website by going from 8 million pages to 2 million pages? Unless you focus on improving the actual quality, it's easy to just spend a lot of time reducing the number of indexable pages, but not actually making the website better, and that wouldn't improve things for search.

Should a global company use .ai as their GTLD or is it considered by Google as a ccTLD?
---------------------------------------------------------------------------------------

**Gary:** Danielle Ross is asking: Should a global company use the .ai domain as their GTLD or is it considered by Google as a ccTLD for the country of Anguilla?

As of early June, 2023, we treat [.ai as a gTLD in Google Search](/search/docs/specialty/international/managing-multi-regional-sites#generic-domains), so yeah, you can use it for your global presence!

I want to clear all "Not Found (404)" errors in Search Console. How?
--------------------------------------------------------------------

**John:** Ghanshyam asks: I want to clear all "Not Found(404)" errors in Search Console.

There's no setting to clear out errors shown in Search Console. These are collected and updated automatically over time as we crawl your website. Also, `404` errors are not a problem. It's expected that all websites return `404` for pages which do not exist. This is actually a good thing.

We need your professional advice with our website ranking!
----------------------------------------------------------

**Gary:** Someone's asking: We need your professional advice with our website ranking. Can we have a meeting on this? Let us know what time and date that will be convenient.

First, thank you for wanting to meet us! But no, the Search team doesn't offer private help meetings for any reason, you will have to follow the same path that everyone else takes. If you want to know what that path is, check out our documentation at [developers.google.com/search/help](/search/help)

How do I request indexing of my publication in Google Scholar?
--------------------------------------------------------------

**John:** Rijul Chaturvedi: How to request indexing of my recent publication in a top journal on Google Scholar. I do not have my own website as I am just a PhD student. (They linked to an author profile page)

This is something that comes up from time to time. I looked at the URL you specified. Confusingly, the same content is available on a number of URLs, and we indexed one of the other versions instead. One way to find this is to open the page, copy some text from it, and to search for that text, rather than the URL. Also, make sure that the page is accessible to users who aren't logged in. In any case, I bookmarked your paper on social companionship with conversational agents and am curious to read through it!

Are best practices for redirects on files like PDF, video and image URLs the same as web page URLs?
---------------------------------------------------------------------------------------------------

**Gary:** Phillip is asking: Do best practices for redirects apply the same for PDF URLs, video URLs and image URLs the same as if it was a web page URL?

Yes, other file types, including binary files like videos and PDFs can be redirected the same way you would redirect web pages.

Will `hreflang` tags (used on a small section of a website) be used as an international targeting signal?
---------------------------------------------------------------------------------------------------------

**John:** Toby asks: If `hreflang` tags are correctly implemented, but only on a section of a website (ie. just european subfolders), will they still be used as an international targeting signal?

hreflang is done on a per-page basis, so it's fine if just a part of your site uses them. I would, however, double-check that seeing the wrong pages in search is actually a problem before spending a lot of time implementing `hreflang`. Also, keep in mind that you can [implement `hreflang` with a sitemap file](/search/docs/specialty/international/localized-versions#sitemap) too. In other words, if you can't edit the pages themselves, you could still specify `hreflang` annotations for them. Check out our documentation for more.
