---
title: "April 2023 Google SEO office hours"
source_url: "https://developers.google.com/search/help/office-hours/2023/april?hl=en"
product: "Google Search Central"
section: "Help & FAQ"
language: en
scraped_date: 2026-06-08
doc_id: "search-central/help/office-hours/2023/april.md"
---
April 2023 Google SEO office hours
==================================

This is the transcript for the April 2023 edition of the [Google SEO Office Hours](/search/help/office-hours). For site-specific help,
we recommend posting your question in the [Google Search Central Help Community](https://support.google.com/webmasters/community).

Website.com/eu or a separate website per country?
-------------------------------------------------

**John:** Nissa asked: When expanding a website into the EU, can I use website.com/eu as the subdirectory with multiple `hreflang` (`en-fr`, `en-de`, `en-nl`, etc)? Or do I need a separate website per country? (all english, in euros)

Yes, you can do that. [`Hreflang` annotations](/search/docs/specialty/international/localized-versions) are per-page, and you can apply multiple annotations to the same page. In your case, you could either specify the list of countries in English that apply to that page, or you could use just the language, `en`, to mark it as the generic English version, and annotate the other English versions appropriately. In any case, I'd still back this up with a dynamic banner that displays for users from a "wrong" country, to help guide them to the best-possible experience.

When I search for something included in my sitemap it's not showing an indexed post, why?
-----------------------------------------------------------------------------------------

**Gary:** Someone's asking: when I search for something included in my sitemap it's not showing an indexed post. It says only one page and page 2, but there are approximately 200 pages on my website. What should I do first?

First, keep in mind that google doesn't index every single URL on the internet. It would be great if we could, but it's just not feasible. But to answer your question more specifically, I'd check if the URLs are actually accessible to Googlebot, you can do this with the [Search Console URL inspection tool](https://support.google.com/webmasters/answer/9012289). If so, remember that the URLs that Google tends to index are those that are of high quality; check out our documentation on developers.google.com/search, we have quite a few documents about what we perceive as [high quality content](/search/docs/fundamentals/creating-helpful-content).

Does Google use product-specific third-party review & rating data for Rich Results?
-----------------------------------------------------------------------------------

**Lizzi:** Mike T is asking: does Google use product specific third-party review and rating data for Rich results?

For products, this is ok. The reviews need to be visible on the page somewhere, so make sure people can easily find and read the reviews about the product, and make sure it's relevant to that product page. Product reviews should be about an individual product and not a category of items. Our [documentation on review snippets](/search/docs/appearance/structured-data/review-snippet) has more info on this.

I have a site that is flagged in Google. How do I find out why it doesn't appear in SERPS?
------------------------------------------------------------------------------------------

**Gary:** David is asking: I have a site that is flagged in Google. How do I find out why it doesn't appear in search results? Search Console has nothing to report. Site is indexed but pretty much not ranking for anything.

If the URL was "flagged" by Google, then you would [see it in Search Console](https://support.google.com/webmasters/answer/9044175). Otherwise if our automated systems rank your URL lower than before, you probably need to check out our documentation about [content quality](/s/results/search/docs?q=quality%20content), and you can find that documentation at [developers.google.com/search](/search) .

Does using a URI for a thesaurus term work for SEO?
---------------------------------------------------

**John:** The next question I have is does using a URI for a thesaurus term work for SEO?

This question specifically mentioned the [NALT thesaurus](https://agclass.nal.usda.gov/), which is for the US National Agricultural Library, where there are URIs defined for specific items. At the moment, this is not something that Google Search supports. It is, however, fine to use these annotations if they're valuable to your site outside of Google. Our Search developer documentation lists the [structured data which Google supports](/search/docs/appearance/structured-data/search-gallery) through rich results.

Failed robots.txt file is unreachable when trying to index in Search Console URL inspector tool, why?
-----------------------------------------------------------------------------------------------------

**Gary:** Someone's asking about failed robots.txt files, which return with unreachable errors when trying to use [Search Console URL inspection tool](https://support.google.com/webmasters/answer/9012289).

The [robots.txt unreachable error](https://support.google.com/webmasters/answer/1067240) is fairly common and it's always down to your site's settings to solve it, there's nothing Google can do about it. Check your firewall settings, or other network components that steer traffic and have a configurable allowlist, check your CDN also if you use one for blocked IPs, and if all fails, check with your hosting provider. Also, you don't have to submit your robots.txt file for indexing; it wouldn't do anything at all.

If I delete several old indexed HTML landing pages, should I redirect 404s to the homepage?
-------------------------------------------------------------------------------------------

**Lizzi:** Pete is asking: if I delete several old indexed HTML landing pages. Should I redirect 404s to the homepage?

Maybe? It really depends on the content on those landing pages: would it matter to a user to land on the home page instead, or would it be confusing? 404s are a normal part of the internet, and sometimes a `404` status code is the best course of action if there's really not a good replacement for whatever was on the old landing page. For example, given the following scenario: there's an old landing page about purchasing aquariums, but the new home page reflects the business's new focus on high-end cat trees. `404` is probably a better approach there.

How do I delete an old website from Google Search?
--------------------------------------------------

**Gary:** Nick is asking: how do I delete an old website from Google Search.

If you are moving to a new domain, please please please [redirect your old site](/search/docs/crawling-indexing/301-redirects) to the new one instead of just deleting the old site. It's pretty likely that your old site has collected some valuable signals over time and you don't want to throw that away. If you already redirected, it may take a few weeks, occasionally a few months to see all your old URLs replaced by the new ones in Search.

Bad URLs discovered on my site. Will it affect the way my site is crawled?
--------------------------------------------------------------------------

**John:** Alex asked: if a poorly coded ad that ran on my site has resulted in 1.2 million bad URLs being discovered by Google in just a few days. Is this a problem for me? Will it affect the way my site is crawled?

The context mentions that the ad used a relative path, so a crawler would have tried to follow the links. Overall, our systems try to recognize and handle these kinds of incidents -- you're not the first one to create a ton of irrelevant URLs accidentally. That said, it can happen that this temporarily increases the overall crawling, resulting in a higher load on the server, until things back down again, perhaps after a few weeks, depending on the situation. The fact that these URLs do not get indexed won't cause problems for Search, neither for indexing of other URLs nor for any quality assessment. Having a lot of unindexed URLs is fine.

Is using `410` for Googlebot & `200` for users OK?
--------------------------------------------------

**Gary:** Wolfgang is asking: would it be ok from Google perspective to provide HTTP status code `410` to Googlebot and status code `200` to users for SEO irrelevant URLs which are massively crawled or will this be considered cloaking?

Cloaking status codes is generally a pretty bad idea and I would strongly advise against it. When you have multiple serving conditions, eventually something will go wrong and your site may even fall out of search results, depending what went wrong. If you need to remove something from Search specifically, you can just add a [`noindex` robots meta tag](/search/docs/crawling-indexing/block-indexing) to the specific pages; it's much easier and so much safer than setting up weird serving conditions.

How does Google handle `308` status code compared to `301`?
-----------------------------------------------------------

**Lizzi:** Riccardo is asking: how does Google handle `308` status code compared to `301`?

We treat these as the same (they are both "moved permanently"): Googlebot treats `308` as equivalent to `301`, and these codes are strong signals that the [redirect](/search/docs/crawling-indexing/301-redirects) should be canonical.

How to increase indexing speed on Google Search Console?
--------------------------------------------------------

**Gary:** Shailesh is asking: indexing on Google search console is very, very slow. There are many items that are pending for indexing. How to increase the speed for that?

How much of your website Google indexes depends on how much of your site Googlebot can access and the quality of the content on your pages. The higher the quality, the more your site Google might index. If you want to learn more, check out our documentation at [developers.google.com/search](/search)

My website is not appearing in Google Search. What should I do?
---------------------------------------------------------------

**John:** Melissa asked: my website is not appearing in Google searches. I'm not sure what else I need to do? Help!

Hi Melissa! I took a look at the URL you mentioned, and unfortunately, it's one that we haven't even seen at all. This makes it really tough for us to discover, and to index. Apart from encouraging others to mention your website, you can also add the website to [Search Console](https://search.google.com/search-console/about), [submit a sitemap file](/search/docs/crawling-indexing/sitemaps/build-sitemap), and take individual pages, like the homepage, to [submit for indexing](/search/docs/crawling-indexing/ask-google-to-recrawl) directly. Hope that helps.

Why is "Wifi" and "Wi-Fi" not considered the same by Google?
------------------------------------------------------------

**Gary:** Anonymous is asking: why are "Wifi" and "Wi-Fi" not considered the same by Google?

Good question! "Wifi" and "Wi-fi" with a dash are treated ballpark the same by Google, however since people are using the two interchangeably, we surface slightly different results for the two, but always trying to closer match the users' spelling. But from a pure understanding perspective Google does equate "Wifi" to "Wi-fi" with a dash.

Missing structured data snippets for `ratingValue` & `reviewCount` - bad for SEO?
---------------------------------------------------------------------------------

**Lizzi:** Ren asks: pages are missing structured data for `ratingValue` and the value in property `reviewCount`. This is only for pages with 0 reviews. Is it hurting our SEO?

Hey, Ren, It's not a problem if the `reviewCount` is zero; this is normal for new product pages that don't have reviews just yet, and therefore this property is often empty or set to zero initially. This just means that there's also nothing for Google to show in the rich result; if there's no rating, we just wouldn't be able to show any star information at all.

Can my site be deleted from SERP for one certain keyword?
---------------------------------------------------------

**Gary:** Kamil is asking: Is there a way that my site was deleted from SERP for one certain keyword? We were 1st and now we are absent completely. Page is in the index.

It's really uncommon that you would completely lose rankings for just one keyword. Usually you just get out-ranked by someone else in search results instead if you did indeed disappear for this one particular keyword. First I would check if that's the case globally. Ask some remote friends to search for that keyword and report back. If they do see your site then it's just a "glitch in the matrix". If they don't, then next I would go over my past actions to see if I did anything that might have caused it. Have I changed my internal link structure or page layout or acquired more links or if I use the disavow tool and so on each of these may have some effect on ranking. So going through them is probably going to help.

Why did my request in the outdated info tool get denied?
--------------------------------------------------------

**John:** The next question I have here is the webmaster has made changes to an initial article. I submitted a request through the [outdated info tool](https://support.google.com/webmasters/answer/7041154), but it got denied.

Hi there! I took a look at the page that you mentioned in the context link in our tools. This tool is specifically meant for cases where the page continues to exist, but something specific was removed from the page, sometimes that's a name or a phone number. The tool will only accept requests where we can determine that the text was removed, and where the text was still indexed. In this case, the text was no longer indexed, so there's nothing for the tool to do, so it rejected the requests. Essentially, that means you're all set!

Migrated domain to Google Domains: How long will it take to appear in Search?
-----------------------------------------------------------------------------

**Gary:** Anonymous is asking: how long until recently migrated domain to [Google Domains](https://domains.google/) appears on Google Search?

It largely depends on the site itself how long it takes to replace the old site's URLs with new ones in Search. It can be anywhere between a few days and many months, and it's usually faster for higher quality sites.

How can you optimize your recipe structured data to make it eligible for rich results?
--------------------------------------------------------------------------------------

**Lizzi:** Koen is asking: how can you optimize your Recipe structured data in order to make it eligible for rich snippets? Does it matter if all optional attributes are '`null`'? This Recipe does not have a '`Name`' and '`Image`' for every step.

To make your site eligible for recipe rich results, you need to add the required properties (they're listed in a separate table in the [recipe documentation](/search/docs/appearance/structured-data/recipe)). `Image` and `name` of the recipe are required, so you should focus on filling those out and making sure they're not empty. If the optional properties are empty, that can be ok, as these are nice to have. It just means that we might not be able to show additional enhancements for that rich result; for example, if you don't specify the `cookTime`, then Google may not be able to show that part of the rich result. The same goes for reviews of the recipe, which is oftentimes empty until someone reviews the recipe (this is fine, just nothing to show until there's a review for that recipe). It's also ok not to have `name` and `image` for every step: first of all, this is only recommended if you're trying to optimize for recipes on the Google Assistant (which is known as "Guided Recipes" in our documentation) and if it makes sense to name your steps. Sometimes this doesn't make sense if the steps are already pretty short (for example, you don't really need to use `name` to shorten "preheat the oven to 350" to just "preheat", but that may make sense if you recipe has lots of subsections and complex things).

My site's description shows spam not from my site, why?
-------------------------------------------------------

**Gary:** Anonymous is asking: My site's description shows spam not from my site.

Unfortunately this is usually a sign that your site was hacked. Head to our friends over web.dev and search for their [hacked topics](https://web.dev/articles/hacked), it's not easy but it's certainly possible to clean up your site and secure it better.
