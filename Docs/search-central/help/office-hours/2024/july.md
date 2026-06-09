---
title: "July 2024 Google SEO office hours"
source_url: "https://developers.google.com/search/help/office-hours/2024/july?hl=en"
product: "Google Search Central"
section: "Help & FAQ"
language: en
scraped_date: 2026-06-08
doc_id: "search-central/help/office-hours/2024/july.md"
---
July 2024 Google SEO office hours
=================================

How does Google handle incremental CMS migration and `hreflang`?
----------------------------------------------------------------

**John:** Corinna asks: We are migrating to a new CMS. We will have some pages in the old CMS for months, some in the new CMS without an `hreflang` connection. Can Google handle this? What about ranking as an international brand?

It's somewhat common to have an incremental migration, and not have everything lined up from the start. When it comes to missing markup, like structured data or `hreflang`, if it's not on the page yet, it won't be taken into account. Once you fully upgrade the site and the markup returns, then it can be taken into account again. For `hreflang`, there are always multiple pages involved. If some of them don't have the markup yet, then that connection just won't be taken into account. A transition like this is not great, your site will be affected appropriately when the site is incomplete, but it won't cause longer-term issues. There's more on [managing international websites](/search/docs/specialty/international/managing-multi-regional-sites).

What non-search features does GoogleOther crawling support?
-----------------------------------------------------------

**Gary:** Anne is asking: What non-search features does GoogleOther crawling support?

This is a very topical question, and I think it is a very good question. Besides what's in the public I don't have more to share. [GoogleOther is the generic crawler](/search/docs/crawling-indexing/overview-google-crawlers#googleother) that may be used by various product teams for fetching publicly accessible content from sites. For example, it may be used for one-off crawls for internal research and development. Historically [Googlebot](/search/docs/crawling-indexing/overview-google-crawlers#googlebot-smartphone) was used for this, but that kinda makes things murky and less transparent, so we launched GoogleOther so you have better controls over what your site is crawled for. That said GoogleOther is not tied to a single product, so opting out of GoogleOther crawling might affect a wide range of things across the Google universe; alas, not Search, search is only Googlebot.

Why did my site's products disappear in rich result snippets on Google Search?
------------------------------------------------------------------------------

**John:** I used to have my site's products appear in rich result snippets on Google's homepage, but after a sitemap issue, they disappeared. Despite following Google's schema guidelines, they haven't reappeared. Can Google provide more detailed guidance on getting products to show in homepage rich snippets?

It's hard to say without seeing specifics. My recommendation for a situation where you're not sure which part of a site is causing a technical issue like this would be to get help from experienced folks. They'll often know of common issues, and be able to check for them efficiently. That could be someone from your hosting platform, a trusted consultant, or someone from the [help forums](https://support.google.com/webmasters/community). Good luck! (Also see our [`Product` structured data documentation](/search/docs/appearance/structured-data/product).)

When a user searches Google in Korean, does a com.kr or .com domain do better?
------------------------------------------------------------------------------

**Gary:** Taegyu Kim is asking: When a Korean person searches Google in Korean, does a com.kr domain or a .com domain do better?

Good question. Generally speaking the local domain names, in your case .kr tend to do better because Google Search promotes content local to the user. That's not to say that a .com domain can't do well, it can, but generally .kr has a little more benefit, albeit not too much. If the language of a site matches the user's query language, that probably has more impact than the domain name itself. There's more on [managing international websites](/search/docs/specialty/international/managing-multi-regional-sites).

What's the impact of a huge expansion of our product portfolio on SEO performance?
----------------------------------------------------------------------------------

**John:** Michael asks: What's the impact of a huge expansion of our product portfolio on SEO Performance, for example going from 10,000 to products to 100,000?

I don't think you have to look for exotic explanations. If you grow a website significantly, in this case, by a factor of 10, then your website will overall be very different. By definition, the old website would only be 10% of the new website. This means it's only logical to expect search engines to re-evaluate how they show your website. It's basically a new website after all. It's good to be strategic about changes like this, I wouldn't look at it as being primarily an SEO problem.

How do I remove old pages from Google's search results?
-------------------------------------------------------

**Gary:** Will is asking: Hi, I have launched a new site recently and Google still references some links from the previous site. I'd like to remove them from search results. How can I do this?

This is normal. Think about it this way: people may call a product or entity by its old name for a long time after the name was changed. I still call [Search Console "Webmaster Tools"](/search/blog/2015/05/announcing-google-search-console-new) because I can't let go. Google Search is a reflection of what people seem to want, so sometimes it can't let go of old names as easily.

How do I remove all the indexing errors under the "page indexing" report?
-------------------------------------------------------------------------

**John:** How to remove all the indexing errors under "page indexing" report?

Gary on my team (hi Gary!) has put together a few LinkedIn posts on this theme. I'll link to them for you. (Update: I was wrong - but the [post about 404 errors](https://www.linkedin.com/posts/garyillyes_404-not-found-errors-are-not-to-be-afraid-activity-7210899528328097792-vU7C) is somewhat related.) The short answer is that you don't have to fix all issues that are reported. Many issues will be expected - for example, if you remove a part of a website. Other issues will be normal, for example, that search engines just don't index everything on a website. If you're curious about specific kinds of reported issues, I'd recommend posting in the [help forum](https://support.google.com/webmasters/community) to get insights from other site owners.

Is it possible to get an API link to status.search.google.com/summary?
----------------------------------------------------------------------

**Gary:** Sanjay is asking: Is it possible to get an API link to [status.search.google.com/summary](https://status.search.google.com/summary)

Well, this is your lucky day! You can grab the [RSS file](https://status.search.google.com/en/feed.atom) and the [history JSON](https://status.search.google.com/incidents.json) linked from every page of the status dashboard to grab the data we have! From there on, you can build whatever you like.

How do I increase the number of product snippets in Google Search Console?
--------------------------------------------------------------------------

**John:** Refat asks: How to increase the number of product snippets in Search Console?

It's not really clear to me what exactly you mean, perhaps it would be useful to chat with folks in the help forum about it. If you're asking about [`product` rich results](/search/docs/appearance/structured-data/product), these are tied to the pages that are indexed for your site. And that's not something which you can change by force. It requires that the page be indexed, that the page has valid structured data on it, and that our systems have determined that it's worth showing this structured data. Our `product` structured data documentation has more. However! There's also the possibility to [submit a feed to your merchant center account](https://support.google.com/merchants/answer/7439058), to show products there. This is somewhat separate, and has different requirements which I'll link to. Often a CMS or platform will take care of these things for you, which makes it a bit easier.

I manage a lot of sites on Google Search Console, can I have unlimited index requests?
--------------------------------------------------------------------------------------

**Gary:** Jivko is asking: Hey I manage a lot of sites on Google Search Console, can I have unlimited index requests?

Well, no.

A word confusion is affecting my website's visibility! Can you guide me on this SEO issue?
------------------------------------------------------------------------------------------

**John:** My brand is being confused with a common English word in Google's search results, affecting my website's visibility. Can you guide me on this SEO issue?

These kinds of suggestions will resolve themselves over time, as our systems recognize that users are looking for your site, and not accidentally misspelling a common word. Depending on the specifics, this can take many months. There's no shortcut available.

Is there an HTML markup or tag to tell Google to ignore text parts?
-------------------------------------------------------------------

**Gary:** Someone is asking: Is there an HTML markup or tag to tell Google to ignore/not-value text parts?

The short answer is that there's no tag or annotation you could use for this. One hacky way to achieve what you want is to inject into the page the weird tags that you don't want indexed with JavaScript and [disallow crawling](/search/docs/crawling-indexing/robots/create-robots-txt) that JavaScript. If we can't fetch it, we can't see it.

Can recipe schema for structured data be used for non-edible recipes?
---------------------------------------------------------------------

**John:** Andy asks: I'd like to know if the [recipe schema for structured data](/search/docs/appearance/structured-data/recipe) can be used for non-edible recipes such as deodorant or washing machine powder?

No. Our [structured data guidelines](/search/docs/appearance/structured-data/sd-policies#relevance) are very clear in this regard. I don't recommend misusing the markup for other purposes.

Can the Google team help transfer SEO rankings from one previous domain to the new domain?
------------------------------------------------------------------------------------------

**Gary:** Someone's asking: Can the Google team help transfer SEO rankings from one previous domain to the new domain?

No, but YOU can. See our [site migration guidelines](/search/docs/crawling-indexing/site-move-with-url-changes) for the not so secret method!

How can I tell if someone has been actively optimizing my site's SEO?
---------------------------------------------------------------------

**John:** If I have an agency that is managing our organic SEO on a monthly basis, how can I tell if anyone has been actively optimizing? I have a suspicion that the agency has not been optimizing our site for years.

This is a great question. When we worked with an SEO agency for some of the Search Central content, we had regular meetings to discuss the work that they did, to look at reports about the site's progress, and to discuss any upcoming work. This did require a bit more time, both from them and from us, but I found it very insightful. I think it helps to lightly understand the kind of work that an agency would do, so that you can confirm that they're doing what you expect them to do, and even then there's a component of trust involved. We have a page about [hiring an SEO](/search/docs/fundamentals/do-i-need-seo) which has some insights, and there's our [SEO starter guide](/search/docs/fundamentals/seo-starter-guide), which can explain a bit more. And also, perhaps some folks from the SEO industry can comment on how they'd help a client understand how they're spending their time.

How do I perform a `noindex` tag to Google's search engine?
-----------------------------------------------------------

**Gary:** Someone's asking: How to perform `noindex` tag to Google's search engine?

I imagine this is about how to apply a `noindex robots meta` tag. The `noindex` rule is applied to individual pages (or other resources) on your site. If you want to add a `noindex` rule to your HTML pages, you would add a `robots meta tag` with a `noindex` value in the page's HTML head element. We have [extensive documentation about these controls](/search/docs/crawling-indexing/block-indexing), check it out!

Can you use product variant structured data on a site that has many incomplete product configurator variants?
-------------------------------------------------------------------------------------------------------------

**John:** André asks: Can we use product variant structured data for a website that has a product configurator for 3 million variants but no price output?

Well, yes, you can use structured data markup even in cases where you don't have all required fields. But also, our systems would likely ignore such markup since we'd consider it incomplete. In your case, I don't think the [product variant markup](/search/docs/appearance/structured-data/product-variants) would be suitable for over 3 million variants, so I'd try to find ways to focus the markup on variations that you'd commonly offer.

Will Google spiders crawl links in an RSS feed that is embedded on a web page?
------------------------------------------------------------------------------

**Gary:** Chaz is asking: Will Google spiders crawl links in an RSS feed that is embedded on a web page?

Yes, Google may use RSS feeds that are referenced on your site to discover your new URLs. Kinda like sitemaps. See our [sitemaps documentation](/search/docs/crawling-indexing/sitemaps/overview); we mention RSS there.

I updated my logo for the SEO of my website but there hasn't been any changes yet on Google, why?
-------------------------------------------------------------------------------------------------

**John:** Hi, I just wanted to ask and fix an issue in where I updated my logo for the SEO for my website on Thursday, yet there hasn't been any changes yet when I checked on Google, is there any way to fix this?

New logos are cool, and in this case, I assume you mean the favicon. Since favicons tend not to change that quickly, our systems generally don't refresh them that often. I'd make sure you've updated all the relevant files - sometimes there are multiple favicons marked up and in separate files - and then just give it more time. Check out our [favicon documentation](/search/docs/appearance/favicon-in-search) for more.

Is the SEO starter guide accurate with regards to heading order?
----------------------------------------------------------------

**Gary:** Matt is asking: I recently read on the [SEO starter guide](/search/docs/fundamentals/seo-starter-guide) that "Having headings in semantic order is fantastic for screen readers, but from Google Search perspective, it doesn't matter if you're using them out of order." Is this correct because an SEO tool told me otherwise.

We update our documentation quite frequently to ensure that it's always up to date. In fact the SEO starter guide was [refreshed just a couple months back](/search/blog/2024/02/ssg-gets-a-makeover) to ensure it's still relevant, so what you read in the guide is as accurate as it can get. Also, just because a non-Google tool tells you something is good or bad, that doesn't make it relevant for Google; it may still be a good idea, just not necessarily relevant to Google.

Does the Google Account used to verify a domain on GSC have to match the owner of a new Google site?
----------------------------------------------------------------------------------------------------

**John:** Does the Google Account used to verify a domain on Google Search Console have to match the owner of a new Google site?

[Search Console verification](https://support.google.com/webmasters/answer/9008080) is so that you have access to the data and settings that are relevant for your website. For Google, it doesn't matter who has verified ownership of the website. That said, from an organizational point of view, it seems like a bad practice to rely on employees' personal accounts to manage the company web presence. But again, for Search Console and Google Search, that doesn't matter. That's up to you.

Does blocking crawl or indexing on a URL cancel the linking power from external and internal links?
---------------------------------------------------------------------------------------------------

**John:** Clement asks: Does blocking crawl or indexing on a URL cancel the linking power from external and internal links?

I'd look at it like a user would. If a page is not available to them, then they wouldn't be able to do anything with it, and so any links on that page would be somewhat irrelevant. If you want a page to be easily discovered, make sure it's linked to from pages that are indexable and relevant within your website. It's also fine to block indexing of pages that you don't want discovered, that's ultimately your decision, but if there's an important part of your website only linked from the blocked page, then it will make search much harder.

How should I organize my sitemap files?
---------------------------------------

**John:** Hi, Gary. I have a number of sitemaps from my site. How can I organize them?

[I am not a cat](https://www.google.com/search?q=i+am+not+a+cat&hl=en), sorry. I am also not Gary, sorry. When it comes to sitemap files, you can organize them however you want. The [limits are documented](/search/docs/crawling-indexing/sitemaps/build-sitemap#general-guidelines), I think it's 50,000 pages per sitemap file. If you're generating them automatically, I'd just fill them up.
