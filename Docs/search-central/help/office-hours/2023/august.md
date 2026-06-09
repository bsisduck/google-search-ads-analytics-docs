---
title: "August 2023 Google SEO office hours"
source_url: "https://developers.google.com/search/help/office-hours/2023/august?hl=en"
product: "Google Search Central"
section: "Help & FAQ"
language: en
scraped_date: 2026-06-08
doc_id: "search-central/help/office-hours/2023/august.md"
---
August 2023 Google SEO office hours
===================================

This is the transcript for the August 2023 edition of the [Google SEO Office Hours](/search/help/office-hours). For site-specific help,
we recommend posting your question in the [Google Search Central Help Community](https://support.google.com/webmasters/community).

How many URLs can a sitemap index file have?
--------------------------------------------

**John:** I am confused about how many URLs a sitemap index file can have?

An XML sitemap file can have up to 50,000 URLs and that also applies for sitemap index files. Sitemap index files only include other sitemap files. Check out our [sitemap documentation](/search/docs/crawling-indexing/sitemaps/overview) for more information.

Does setting ARIA attributes improve SEO?
-----------------------------------------

**John:** Michał asks: Does Google see and consider ARIA-label name and other ARIA label accessibility attributes? Does setting ARIA attributes improve SEO?

There's no inherent SEO advantage to making a website look like it has accessibility features. Instead, use accessibility features for accessibility reasons. There are enough users that rely on these features to make it worthwhile, even without any direct SEO effect. Instead of artificially using [accessibility](https://web.dev/learn/accessibility) features like [ARIA-labels](https://web.dev/learn/accessibility/aria-html), use them properly.

Should I redirect canonicalized "domain/en" to "domain," or is being canonicalized enough already?
--------------------------------------------------------------------------------------------------

**John:** Hakan asks: Should I redirect canonicalized "domain/en" to "domain"? Or is being canonicalized enough already?

There is no SEO advantage to be gained here, but it's useful to be consistent. If the version without language code is the default version and the same as one of the language codes, then you can set it as the [`x-default` in `hreflang`](/search/docs/specialty/international/localized-versions#xdefault). Being consistent with [canonicalization](/search/docs/crawling-indexing/canonicalization) and internal linking will also usually result in that version being selected as the canonical. This makes it easier for your work, since it's more consistent for tracking. It doesn't have an SEO effect though.

Do the elements of the link after a hashtag (`#`) in the URL affect how it's displayed in the search results?
-------------------------------------------------------------------------------------------------------------

**John:** Michel asks: Do the elements of the link after a hashtag (`#`) in the URL affect how it's displayed in the search results?

Usually, no. That thing is called a [fragment](https://www.w3.org/DesignIssues/Fragment.html) and it's used to link to a specific part of the content of a page. Google Search looks at the whole page, though, so it's usually ignored, but might be useful to help users jump to the relevant part of the page directly. There are URLs where we figure out that the fragment has been used to display different content, but it's very rare and not a recommended practice and usually Google Search will ignore URL fragments.

Why is my site not ranking despite low competition and good SEO?
----------------------------------------------------------------

**John:** Why is my site not ranking despite low competition and good SEO? I have a sitemap, indexed pages, updated content, backlinks and on-page optimization. But my site is still not in the top 200 results for my keywords.

I see this kind of question often. Google tends to focus on various technical aspects when it comes to talking about SEO, but you need to do more. A good way to think about this is to compare it to the offline world. When it comes to books, does a good cover photo, a reasonable sentence length, few misspellings, and a good topic mean that a book will become a best-seller? Or as a restaurant, does using the right ingredients and cooking in a clean kitchen mean you'll get a lot of customers? Technical details are good to cover well, but there's more involved in being successful.

How can I see if my newly bought site has a penalty?
----------------------------------------------------

**John:** Anton asks: How can I see if my newly bought site has a penalty?

You can see the current status of [manual actions in Search Console](https://support.google.com/webmasters/answer/9044175), once you've [verified ownership of the site](https://support.google.com/webmasters/answer/9008080). This information is visible to all verified owners. Manual actions that have expired or which are resolved are not listed there. When a manual action is resolved, the effect generally goes away fairly quickly. Keep in mind that our algorithms can also react to significant [quality issues](/search/docs/fundamentals/creating-helpful-content) without a manual action being involved.

Is it OK to use `product` rich snippets for real estate properties?
-------------------------------------------------------------------

**John:** Igor asks: Is it OK to use `product` rich snippets for real estate properties?

I checked with the team on this. When it comes to Google Shopping, If you look at the [unsupported content Merchant Center help article](https://support.google.com/merchants/answer/6150006), it lists immovable objects, like real-estate, as being unsupported. In practice, what will happen in cases like this is that we'd just ignore it. Using product structured data for real-estate isn't seen as abuse, but it also has no effect. My recommendation would be to use [structured data which has a visible effect](/search/docs/appearance/structured-data/search-gallery), such as using [`product` structured data](/search/docs/appearance/structured-data/product) for things which can be shown as products in search.

Can `hreflang` be used to link similar content targeting different countries, even if not direct translations?
--------------------------------------------------------------------------------------------------------------

**John:** Alex asks: Can `hreflang` be used to link content that is very similar but targeted at different countries, even if they aren't direct translations? For example, a company might sell chocolate candy in multiple countries, but their ingredients might vary.

Yes, you can. `Hreflang` is for alternate language or regional versions. It's not specifically for localization, though it can be. For more information on `hreflang`, I'd check out the [documentation on international websites](/search/docs/specialty/international).

Can we use a white font, but on a colored background?
-----------------------------------------------------

**John:** Zaid asks: Can we use a white font, but on a colored background?

Sure. Just make sure it has good contrast, so your users can actually read it.

Does the use of an `<article>` HTML tag have an impact on Google?
-----------------------------------------------------------------

**John:** Carlos asks: Does the use of an `<article>` HTML tag have an impact on Google? Is it better to put the content of a product listing page in an `<article>` tag?

The `<article>` HTML element does not have any particular effect in Google Search. This is similar to lots of other kinds of HTML tags. There's so much more to using HTML than just Google Search though! Sometimes there are accessibility or semantic reasons to use a specific kind of markup, so don't only focus on SEO.

On our website we have a mix of relative and absolute links. Is this a problem for SEO?
---------------------------------------------------------------------------------------

**John:** Markus asks: On our website we have a mix of relative and absolute links. Is the mix a problem for SEO?

Search engines look at links like a browser would, so there would be no difference here. If you're curious about links in general, you can check out our [link best practices documentation](/search/docs/crawling-indexing/links-crawlable).

For the structured data on a French website, should we write the opening days in English or French?
---------------------------------------------------------------------------------------------------

**John:** Bastien asks: For the structured data on a French website, should we write the opening days in the English language or French Language for a French website?

Great question! For most text-based structured data, you should match what you show to users on the page. However, some structured data uses so-called enumerated fields, which means you need to specify it exactly. This is the case for `dayOfWeek` data, which must list the names of the days in English, as documented in the [schema.org specification](https://schema.org/DayOfWeek). In short, even if your site is in another language and you show the opening hours in that language, then for structured data you would use the names in English.

Is this IP address a Google crawler?
------------------------------------

**John:** Fan asks: Is the IP address (lists example) a Google crawler? Our website received a huge traffic volume today from this.

No, that IP address is not from Google. One way to check is to do a reverse DNS lookup for the IP address, to get the hostname, and then to look up the hostname to confirm the IP address. We have this covered in our [verifying Googlebot documentation](/search/docs/crawling-indexing/verifying-googlebot). Another way to get an approximation is to use one of the online whois services, and to check the registration details there. In this case, it maps to a Hong Kong based cloud provider. Unfortunately, some scrapers use [Googlebot user-agents](/search/docs/crawling-indexing/overview-google-crawlers) in an attempt to trick sites. It's fine to block these from our point of view.

Does Google treat certain tags as a signal that the website is attempting to give a good UX?
--------------------------------------------------------------------------------------------

**John:** Hans asks: Does Google treat link `prefetch`, `prerender`, `dns-prefetch`, etc. tags as a signal that the website is attempting to give its visitors a good user experience?

When these things are used correctly so that your users benefit from a better experience, this will be reflected in real user metrics for the [Core Web Vitals](/search/docs/appearance/core-web-vitals) and as such be considered by Search as well. What matters for Google is not that a website is attempting to give users a good page experience, but rather if it is actually giving users a good page experience. Make sure that what you implement is functional.

Why does the Google cache page show a 404 error for my site?
------------------------------------------------------------

**John:** Why does the [Google cache page](/search/docs/monitor-debug/search-operators/web-search-cache) show a 404 error for my site?

So there can be many reasons for this, and we've talked about this in the past a few times already. Generally the cache doesn't matter at all when it comes to indexing. It's not a technical SEO tool. [Use Search Console](https://support.google.com/webmasters/answer/9012289) if you want to diagnose the status of a URL.

Online gambling websites appearing on our domain that originate from Google's smartphone crawlers. Help!
--------------------------------------------------------------------------------------------------------

**John:** Dylan asks: It seems that Google's crawler is confused or being tricked. We have a bunch of online gambling websites appearing on our domain that appear to originate from Google's smartphone crawlers.

The important thing to keep in mind is that Google doesn't make up content for indexing. It uses what your site provides. If you're seeing online gambling content in the search results for your site and your site isn't about online gambling, that's still what your server is providing. If you didn't place that content there yourself, then it's very likely that your server, or something in your infrastructure, was hacked. Resolving the hack and securing the site properly can be hard, so if this is your first time, it's good to get help from others. Recognizing this can be tricky. I recommend setting up a [Google Alert](https://www.google.com/alerts) for a site-query for your domain together with keywords often used on spammy or hacked content, such as those around pharmaceuticals or gambling. We have more [tips on handling hacked sites](https://web.dev/articles/hacked), I hope that helps!
