---
title: "May 2023 Google SEO office hours"
source_url: "https://developers.google.com/search/help/office-hours/2023/may?hl=en"
product: "Google Search Central"
section: "Help & FAQ"
language: en
scraped_date: 2026-06-08
doc_id: "search-central/help/office-hours/2023/may.md"
---
May 2023 Google SEO office hours
================================

This is the transcript for the May 2023 edition of the [Google SEO Office Hours](/search/help/office-hours). For site-specific help,
we recommend posting your question in the [Google Search Central Help Community](https://support.google.com/webmasters/community).

If a domain gets penalized does it affect the links that are outbound from it?
------------------------------------------------------------------------------

**Duy:** Kholizio asked: if a domain gets penalized does it affect the links that are outbound from it?

I assume by 'penalize' you mean that the domain was demoted by our spam algorithms or [manual actions](https://support.google.com/webmasters/answer/9044175). In general, yes, we don't trust links from sites we know are spam. This helps us maintain the quality of our anchor signals.

Are results generated differently in the various URL testing tools?
-------------------------------------------------------------------

**Martin:** Ellen Edmands is asking: Are results in the [URL Inspection Tool](https://support.google.com/webmasters/answer/9012289) rendered html tab and Rich Results Testing Tool rendered html tab generated differently?

Generally speaking, they are generated the same way. However, there are two ways these might be created: Using the [indexing pipeline when using the "View crawled page" tab](https://support.google.com/webmasters/answer/9012289#using_the_tool) in Google Search Console or using [live test](https://support.google.com/webmasters/answer/9012289#test_live_page) in Google Search Console or the live test in [Rich Results testing tool](https://search.google.com/test/rich-results). The live tests both skip caching to provide a current glimpse into how the current version of the page will be rendered. So it is without caching, and without caching timeouts can happen that will affect the rendered output. Depending on where these timeouts happen, or if these timeouts happen, you might get different rendered HTML. But the way these are created are using the exact same paths through our infrastructure.

Is doing off page SEO submissions to directory & social bookmarking sites worth it?
-----------------------------------------------------------------------------------

**Gary:** Shantanu was asking: Is doing off page SEO submissions to directory and social bookmarking sites worth it?

I like this question because it reminds me of the times when I was doing SEO 15 years ago! In short, I wouldn't waste my time with directory submissions and social bookmarking. You're likely wasting time on things that are not going to help at all.

Why are collection pages excluded as noindex on my site?
--------------------------------------------------------

**John:** Why are collection pages excluded as noindex on my site?

I took a look at the site that you mentioned to double-check. In short, it's particularly the paginated category pages on your site, and they do have a [`noindex` robots `<meta>` tag](/search/docs/crawling-indexing/block-indexing). For things like this, I'd check the exact URL specified in Search Console. The short way to check is to open the page in a browser, and use view-source, then search for "robots" to find robots `<meta>` tags, and 'googlebot' to find Googlebot `<meta>` tags. Some pages may have multiple of these. In your case, I noticed you have two separate robots `<meta>` tags, and the second one has the `noindex`. In advanced cases, you'd want to use the [mobile emulation in Chrome](https://developer.chrome.com/docs/devtools/device-mode) and use Inspect Element in the developer tools to look at the loaded DOM, or to use Search Console's Inspect URL feature. In this particular case, I suspect it's a plugin or setting in your site's ecommerce platform that does this, and maybe it's ok for you like this anyway.

Links to my site appear to be coming from Russian websites. How do I block these links?
---------------------------------------------------------------------------------------

**Duy:** Somebody asked: Links to my site appear to be coming from Russian websites - how do I block these links? I believe they want to harm my site by making them lose ranking in search.

Our algorithms generally do a very good job at recognizing and ignoring spammy or garbage links on the internet. In some cases there can be a lot of them. You shouldn't really worry about them and just let our systems do their job and focus on improving your website.

Does the backend of a website matter for ranking?
-------------------------------------------------

**Martin:** Eshragh is asking: Does the backend of a website matter for ranking? For example does it matter if we are using WordPress or a custom made CMS or any specific programming language to render HTML?

No, it generally doesn't matter. However, the performance and behavior of it does though. For instance, if your server is particularly slow then that can have some impact on ranking.

Do you plan to allow more than one site name for snippets?
----------------------------------------------------------

**John:** Madeleine asks: Do you plan to allow more than one Site Name for snippets (for example for the root domain AND subdomains)?

In our documentation about site names, we mention that this is currently only for the domain name, and not for subdomains. I can't promise future changes. With some changes, the team involved tends to start on one part of the problem, evaluate how it's working out, and then expand from there. We really can't promise anything future-looking though.

Should it take over six months to index my 16,000 pages?
--------------------------------------------------------

**Gary:** Tom Baker is asking: should it take over six months to index my 16,000 pages? I see an increase of maybe 5 to 15 per week and I find this slow.

How fast a site is indexed depends on a bunch of things, but the most important one is the quality of the site, followed by its popularity on the internet. Once you ensured that your content is the highest quality you can possibly make, try to run some social media promos perhaps so you get people to start talking about your site. That will likely help.

For permalinks, is it better with contractions to have "-will-not-" vs. "-wont-" in the URL?
--------------------------------------------------------------------------------------------

**John:** Michael asks: For permalinks, is it better with contractions to have "-will-not-" vs. "-wont-" in the URL? "Wont" actually has another meaning, but in general is there a best practice for don't "-do-not-" vs. "-dont-"?

It doesn't matter. Generally speaking, words in URLs have a minimal effect on Search. My only recommendation would be to be consistent, so that you don't accidentally link to the same page in different ways. Also, since the effect is minimal, and since changing URLs across a site is a pretty big change, I would not, or wouldn't, recommend changing a site's URLs only for a vague SEO promise you might have read somewhere.

Does it make it hard for Googlebots to crawl and index an image if it is having many levels in the image URL?
-------------------------------------------------------------------------------------------------------------

**Martin:** Aman is asking: Does it make it hard for Googlebots to crawl and index an image if it is having many levels in the image URL? For instance, `https://www.abc.com/ab/cd/content/category/image/hires/imagefilename.jpg`

Well, good news is no, it doesn't.

A lot of spam backlinks point to my website, how to stop them?
--------------------------------------------------------------

**Gary:** Anonymous is asking: A lot of spam backlinks point to my website, how to stop them?

Easy: you ignore them. The internet is a huge place and you likely get links which are from its not-so-nice corners. We've been dealing with such links for 25 years and we've gotten pretty good at ignoring them. So I'd just ignore them. If they really bother you, you can use the [disavow tool in Search Console](https://support.google.com/webmasters/answer/2648487).

Is it possible that Google Search Console shows me wrong queries?
-----------------------------------------------------------------

**John:** Alexis asks: Is it possible that Google Search Console shows me wrong queries?

[Performance data](https://support.google.com/webmasters/answer/7576553) in Search Console is collected when your site is shown for specific queries. The data is not theoretical, it's based on what was shown to users when they searched. When I see data there which I don't understand, I try to narrow the report's settings down to find the specifics. Was it only in a certain country? Or perhaps a specific search type? Was it perhaps something in a very short window of time? Sometimes it's possible to reproduce the search results shown given these specifics, but it can also be something that either isn't shown anymore, or that is only visible from time to time. Sometimes these are fun puzzles, and sometimes you just have to accept that you currently can't reproduce it.

Full HTML page via server side rendering for search engines & client-side rendering for users. Is this OK?
----------------------------------------------------------------------------------------------------------

**Martin:** Madeleine is asking: We deliver the full HTML of a page via server side rendering (SSR) for all search engine bots and use client-side rendering for the user. Is this a suitable solution in terms of JavaScript SEO?

That's an approach we call [dynamic rendering](/search/docs/crawling-indexing/javascript/dynamic-rendering). It adds complexity to your setup and maintenance efforts, but if it works for you, it's fine to do it. We don't encourage it for new projects, because of the complexity cost it adds on the side of website owners too. It's not an optimal solution but if it works, I don't see a reason to change it.

How important are descriptive file names for images?
----------------------------------------------------

**Gary:** Al G. is asking: How important are descriptive file names for images?

Good question! They're generally helpful a little, but if you have many images, say millions, at one point you'll have to consider whether that benefit is worth it. If you just have a few here and there, yeah, have good filenames, but you probably shouldn't bother once you have a truckload of them. Also check out our [images SEO best practices](/search/docs/appearance/google-images).

What's the best way to get your traffic up after a redesign?
------------------------------------------------------------

**John:** Next up is: What's the best way to get your traffic up after a redesign?

There are a lot of different ways to do redesigns. Some sites are essentially completely new after a redesign, with new URLs and completely new page structures. In cases like that, you'd need to treat it more like a [site move](/search/docs/crawling-indexing/site-move-with-url-changes), and include redirects, otherwise you might see an immediate drop after relaunching. In your case, it looks like the decline is more slowly over time. To me, that suggests that the redesign isn't primarily the issue, but rather that search, the web, or users have changed their behavior or expectations over time. That's usually less of a technical issue, and more about understanding the world around your site, and working to improve your site to match. It's not always easy, sorry!

Does Googlebot for organic search crawling render every page crawled? If not, how often does this happen?
---------------------------------------------------------------------------------------------------------

**Martin:** Jason is asking: Does Googlebot for organic search crawling render every page crawled? If not, how often does this happen?

Yes and no. Not every page we crawl gets rendered. For example, a crawl that leads to a `404` error page won't get rendered. Every page that is fine when we crawl it, gets rendered.

Can it hurt to have schema markup on a page that is invalid?
------------------------------------------------------------

**Gary:** Matthias is asking: Can it hurt to have schema markup on a page that is invalid? (e.g. [`product` markup](/search/docs/appearance/structured-data/product) without `offer` / `review` / `aggregateRating`)

Short answer is no. The long answer is also no, because if we can't parse it, we just won't use it. That might mean that you'll miss out on some search features like [rich attributes under your snippets](/search/docs/appearance/structured-data/search-gallery) though.

How to change from a redirect `302` to a redirect `301`?
--------------------------------------------------------

**John:** Hazim asks: How to change from a redirect `302` to a redirect `301`?

This is something you'd have to look at with your site's hoster or domain registrar. However, the good news is that Google search does recognize long-standing temporary redirects as permanent ones, so this isn't something that's critical for your site at the moment. It's good to use the theoretically correct redirect, but Search tries to work with whatever you have too, as long as it's a redirect.

Does extensive boilerplate content harm the website?
----------------------------------------------------

**Gary:** Anan is asking: Hi, does extensive boilerplate content harm the website? I'm not referring to contact info, privacy policy, etc. Thanks.

Generally no, extensive boilerplate should not have much of an effect on your website's presence in Search. That said, you might want to think about how users perceive that extensive boilerplate; there's a chance they might not like it at all.

How do I prevent Googlebot from calling an expensive external API when rendering the JavaScript on a page?
----------------------------------------------------------------------------------------------------------

**Martin:** Matthew is asking: How do I prevent Googlebot from calling an expensive external API when rendering the Javascript on a page?

You can disallow the API via [robots.txt](/search/docs/crawling-indexing/robots/intro) - but beware: If you use client-side rendering and the content of the page depends on these APIs, then Googlebot needs to access the API to see the content. Otherwise your pages would not have that content when Googlebot looks at them. For external third-party URLs where you cannot use robots.txt to disallow access, you could conditionally load these APIs in your JavaScript and skip it when Googlebot requests the page.

Is there any certain method to change domain names without losing SEO rankings?
-------------------------------------------------------------------------------

**Gary:** D.ray from mu.se is asking: Is there any certain method to change domain names without losing SEO rankings?

A well executed site move, which includes domain changes, shouldn't result in lasting traffic loss, so yes: there is a method to change a domain name without losing rankings. Check out our [documentation about site moves](/search/docs/crawling-indexing/site-move-with-url-changes); we've also linked to other expertly crafted guides from others.

My brand favicon was uploaded over a month ago. However, on Google my webflow favicon is still there?
-----------------------------------------------------------------------------------------------------

**John:** Josh asks: My brand favicon was uploaded over a month ago. However, on Google my webflow favicon is still there. Do you know how to resolve this so it's my brand one that I uploaded previously?

We have a [help document about favicons](/search/docs/appearance/favicon-in-search), I would go through that and check the details there. I would also make sure that the old favicon is both no longer on or linked from your site, and ideally, that you redirect the old file to the new one. In short, make sure that everything is consistent, and that there's no room for misinterpretation by search engines. Past that, sometimes these changes take a while to be visible, a month should be enough, but if you find other things to fix, I'd give it a bit more time to catch up. And finally, outside of Google, Glenn Gabe has put together a fantastic [guide on troubleshooting favicon issues](https://www.gsqi.com/marketing-blog/favicon-problems-google-search/), you might find some more tips there.

What if a website writes posts in multiple languages (translated by hand), what is the best practice to divide the content?
---------------------------------------------------------------------------------------------------------------------------

**Gary:** V is asking: What if a website writes posts in multiple languages (translated by hand), what is the best practice to divide the content?

That's really up to you. Whether you use URL parameters like our help center, say `?hl=ja`, or you put the language code in the URL path, it doesn't matter from a search perspective. Just make sure you have a unique URL for every language version.

Does Google accept links in dropdowns?
--------------------------------------

**John:** Michał asks: Does Google accept links such as `<select><option value="https://www.examplepage.com">Page</option>` ? Is that something that works?

We would not treat this as a link, but we might recognize the URL and crawl it separately. If you want something to be treated as a link, then you should make sure that it is a normal link. We recently published guidelines on making links, so if your web developer has questions about what's supported, I'd send them there. As an aside, this combination of HTML wouldn't necessarily work as a link in the browser either, it could be used in a dropdown for a form instead.

Robots.txt unreachable in Google Search Console. Why?
-----------------------------------------------------

**Gary:** Aslam Khan is asking, well, actually, stating: Robots.txt unreachable in Google Search Console.

If Search Console is reporting [unreachable robots.txt](https://support.google.com/webmasters/answer/1067240) issue with your property, your site or server has an issue and you'll have to fix it if you want to see your site in Google Search. There's nothing we can do about this on our side, really. The first thing I'd check is the firewall rules for your server. See if there's anything weird going on in the block rules, then move to the server configuration files. If you don't know how to do this yourself, open a support ticket with your hosting provider and they can help you most likely.

If a sitemap has hreflang URLs mentioned, how do properties like `<lastmod>` or `<priority>` affect it?
-------------------------------------------------------------------------------------------------------

**John:** Carlos asks: If a sitemap has hreflang URLs mentioned, how do properties like `<lastmod>` or `<priority>` affect it?

When the hreflang annotations are specified in a sitemap file, you're essentially referring to other URLs. This needs to be confirmed on all URLs of the hreflang set. However, understanding when to crawl a URL is different. For crawling, among other things, we look at the attributes for that specific URL, for example its last modification date. It can happen, for example, that one language version changes independently, perhaps due to a translation fixes. That said, even the last modification date is just a very rough signal among other signals, it alone does not guarantee that a page will be recrawled soon. Also worth noting, crawling more does not mean that a page ranks better, so you don't need to try to force a higher crawl frequency.

Should I block affiliate links in robots.txt or lift disallow and prevent affiliate links from being indexed?
-------------------------------------------------------------------------------------------------------------

**Gary:** Nick van Schaik is asking: Should I block affiliate links in robots.txt (to manage crawl budget) or lift disallow and prevent affiliate links from being indexed (by using `noindex` tag)?

Blocking affiliate links in robots.txt seems sensible. Although we're also pretty good at recognizing and ignoring them ourselves, with a robots.txt disallow you're in control and you might indeed save some crawl budget much easier.
