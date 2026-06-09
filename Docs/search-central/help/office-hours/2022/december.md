---
title: "December 2022 Google SEO office hours"
source_url: "https://developers.google.com/search/help/office-hours/2022/december?hl=en"
product: "Google Search Central"
section: "Help & FAQ"
language: en
scraped_date: 2026-06-08
doc_id: "search-central/help/office-hours/2022/december.md"
---
December 2022 Google SEO office hours
=====================================

This is the transcript for the December 2022 edition of the [Google SEO Office Hours](/search/help/office-hours). For site-specific help,
we recommend posting your question in the [Google Search Central Help Community](https://support.google.com/webmasters/community).

How to reduce my site from 30,000 products to 2,500?
----------------------------------------------------

**Alan:** Vertical Web asks, my old site is going from 30,000 products down to 2,500. I will generate 400,000 `301` redirects. Is it better to start on a clean URL and redirect what needs to be redirected to the new site or do it on an old URL?

We generally recommend keeping your existing domain name where possible. We support redirecting to a new domain name as Google will recognize the `301` permanent redirect and so understand your content is moved. However, there's greater risk of losing traffic, if a mistake is made in the migration project, it is fine to clean up old pages and either have them return a `404` or redirect to new versions, even if this affects lots of pages on your site.

Does Google ignore links to a page that was a `404`?
----------------------------------------------------

**Gary:** Sina is asking, it's been formerly asserted that Google ignores links to a `404` page. I want to know whether links to that page will still be ignored when it is no longer `404`.

Well, as soon as a page comes back online, the links will be counted again to that page after the linking pages have been recrawled and the fillings have been deemed still relevant by our systems.

Do speed metrics other than Core Web Vitals affect my site's rankings?
----------------------------------------------------------------------

**John:** If my website is failing on the Core Web Vitals, but performs excellently on GTMetrix speed test, does that affect my search rankings?

Well, maybe. There are different ways to test speed, different metrics, and there's testing either [on the user side or in a lab](https://web.dev/articles/lab-and-field-data-differences). My recommendation is to read up on the different approaches and to work out which one is appropriate for you and your website.

Why doesn't Google remove all spam?
-----------------------------------

**Duy:** Somebody asked, why does Google not remove spam web pages?

Well, over the years we blogged about several spam specific algorithms that either demote or remove spam results completely. One such example is [SpamBrain](/search/blog/2022/04/webspam-report-2021#spambrain:-our-most-effective-solution-against-spam), our artificial intelligence system that's very good at catching spam. Sometimes for some queries where we don't have any good results to show, you might still see low quality results. If you see spam sites are still ranking, please continue to send them to us using the [spam report form](/search/docs/advanced/guidelines/report-spam). We don't take immediate manual actions on user spam reports, but we do actually use the spam reports to monitor and improve our coverage in future spam updates. Thank you so much.

Do too many `301` redirects have a negative effect?
---------------------------------------------------

**John:** Lisa asked. I create `301` redirects for every `404` error that gets discovered on my website. Do too many `301` redirects have a negative effect on search ranking for a website? And if so, how many is too many?

You can have as many redirecting pages as you want, millions is fine if that's what you need or want. That's said, focus on what's actually a problem so that you don't create more unnecessary work for yourself. It's fine to have `404` pages and to let them drop out of search, you don't need to redirect. Having `404` errors listed in Search Console is not an issue, if you know that those pages should be returning `404`.

How does Google determine what is a product review?
---------------------------------------------------

**Alan:** John asks, how does Google determine what is a product review for the purposes of product review updates? If it's affecting non-product pages, how can site owners prevent that?

Check out our Search Central documentation on [best practices for product reviews](/search/docs/specialty/ecommerce/write-high-quality-reviews), for examples of what we recommend, including in product reviews. It is unlikely that a non-product page would be mischaracterized as a product review. And it is unlikely that it would have a significant effect on ranking, even if it was. It's more likely to be other ranking factors or algorithm changes that has impacted the ranking of your page.

Should I delete my old website when I make a new one?
-----------------------------------------------------

**John:** I bought a Google domain that came with a free web page. I now decided to self-host my domain, and I wanted to know if I should delete my free Google page. I don't want to have two web pages.

If you set up a domain name for your business and have since moved on to a new domain, you should ideally redirect the old one to the new domain, or at least delete the old domain. Keeping an old website online when you know that it's obsolete is a bad practice and can confuse both search engines and users.

Should paginated pages be included in an XML sitemap?
-----------------------------------------------------

**Alan:** Should paginated pages such as `/category?page=2` be included in an XML sitemap? It make sense for me, but I almost never see it.

You can include them, but assuming each category page has a link to the next category page that may not be much benefit, we will discover the subsequent pages automatically. Also, since subsequent pages are for the same category, we may decide to only index the first category page on the assumption that the subsequent pages are not different enough to return separately in search results.

My site used to be hacked, do I have to do something with the hacked pages?
---------------------------------------------------------------------------

**John:** Nacho asks, we were hacked early in 2022 and still see Search Console `404` error pages from spammy pages created by the hacker. These pages were deleted from our database. Is there anything else that I should do?

Well, if the hack is removed, if the security issue is resolved, and if the pages are removed, then you're essentially all set. These things can take a while to disappear completely from all reports, but if they're returning `404`, that's fine.

Does Google care about fast sites?
----------------------------------

**Alan:** Tarek asks, does Google care about fast sites?

Yes. Google measures Core Web Vitals for most sites, which includes factors such as site speed, and Core Web Vitals is used as a part of the page experience ranking factor. While it's not something that overrides other factors like relevance, it is something that Google cares about and equally important users care about it too.

Can Google follow links inside a menu that shows on `mouseover`?
----------------------------------------------------------------

**Lizzi:** Abraham asks, can Google follow links inside a menu that appears after a `mouseover` on an item?

Hey, Abraham. Great question. And yes, Google can do this. The menu still needs to be visible in the HTML and the links need to be crawlable, which means they need to be proper `A` tags with an `href=` attribute. You can use the URL inspection tool in Google Search Console to see how Google sees the HTML on your site, and check to see if the menu links are there. Hope that helps.

Why did reporting shift between my mobile and desktop URLs?
-----------------------------------------------------------

**John:** Luki asked, we use sub-domains for desktop and mobile users. We found a strange report in Search Console in early August where the desktop performance has changed inversely with the mobile performance. And the result is that our traffic has decreased.

For the technical aspect of the indexing and reporting, shifting to the mobile version of a site is normal and expected. This happens with mobile first indexing and can be visible in reports if you look at the host names individually. However, assuming you have the same content on mobile and desktop, that wouldn't affect ranking noticeably. If you're seeing ranking or traffic changes, they would be due to other reason.

Does having many redirects affect crawling or ranking?
------------------------------------------------------

**Gary:** Marc is asking, do many redirects, let's say twice as many as actual URLs, affect crawling or ranking in any way?

Well, you can have as many redirects as you like on your site overall, there shouldn't be any problem there. Just make sure that individual URLs don't have too many hops in the redirect chains, if you are chaining redirects, otherwise you should be fine.

Can I use an organization name instead of an author's name?
-----------------------------------------------------------

**Lizzi:** Anonymous is asking, when an article has no author, should you just use `organization` instead of `person` on author markup? Will this have a lesser impact on results?

It's perfectly fine to list an organization as the author of an article. We say this in our [article structured data documentation](/search/docs/appearance/structured-data/article#author-bp). You can specify an organization or person as an author, both are fine. You can add whichever one is accurate for your content.

What can we do if someone copies our content?
---------------------------------------------

**Duy:** Somebody asked a competitor's copying all of our articles with small changes. In time, it ranks higher than us. DMCA doesn't stop them or seem to lower their ranking. What else can we do, their site has more authority.

If the site simply scrapes content without creating anything of original value, that's clearly a violation of our [spam policies](/search/docs/essentials/spam-policies), and you can report them to us using our [spam report form](/search/docs/advanced/guidelines/report-spam) so that we can improve our algorithms to catch similar sites. Otherwise, you can start a thread on our [Search Central Help community](https://goo.gle/sc-forum), so product experts can advise on what would be some of the possible solutions. They would also be able to escalate to us for further assessment.

Do URL, page title, and `H1` tag have to be the same?
-----------------------------------------------------

**Lizzi:** Anonymous is asking: URL, page title, and `H1` tag. Do they have to be the same?

Great question, and no, they don't need to be exactly the same. There's probably going to be some overlap in the words you're using. For example, if you have a page that's titled "How to Knit a Scarf", then it probably makes sense to use some of those words in the URL too, like `/how-to-knit-a-scarf` or `/scarf-knitting-pattern`, but it doesn't need to be a word for word match. Use the descriptive words that make sense for your readers and for you when you're maintaining your site structure and organization. And that'll work out for search engines as well.

Is redirecting through a page blocked by robots.txt a valid way to prevent passing PageRank?
--------------------------------------------------------------------------------------------

**John:** Sha asks, is redirecting through a page blocked by robots.txt still a valid way of preventing links from passing PageRank?

If the goal is to prevent signals from passing through a link, it's fine to use a redirecting page that's blocked by robots.txt.

Why is my site flagged as having a virus?
-----------------------------------------

**Alan:** Some pages in my website collect customer information, but my site is always reported as being infected via a virus or deceptive by Google. How can I avoid this happening again without removing those pages?

Your site might have been infected by a virus without you knowing it. Check out [web.dev/request-a-review](https://web.dev/articles/request-a-review) for instructions on how to register your site in [Search Console](https://search.google.com/search-console/about), check for security alerts, then request Google to review your site again after removed any malicious files. Some break-ins hide themselves from the site owner so they can be hard to track down

Is there any way to get sitelinks on search results?
----------------------------------------------------

**Lizzi:** Rajath is asking, is there any way to get sitelinks on SERPs?

Good question. One thing to keep in mind is that there's not really a guarantee that sitelinks or any search feature will show up. [Sitelinks](/search/docs/appearance/visual-elements-gallery#text-result) specifically only appear if they're relevant to what the user was looking for, and if it'll be useful to the user to have those links. There are some things that you can do to make it easier for Google to show sitelinks. However, like making sure you have a logical site structure, and that your titles, headings, and link text are descriptive and relevant. There's more on that in our [documentation on sitelinks](/search/docs/appearance/sitelinks), so I recommend checking that out.

Does having two hyphens in a domain name have a negative effect?
----------------------------------------------------------------

**John:** My site's domain name has two hyphens. Does that have any negative effect on its rankings?

There's no negative effect from having multiple dashes in a domain.

How important are titles for e-commerce category pages pagination?
------------------------------------------------------------------

**Alan:** Bill asks, how important are unique page titles for e-commerce category product listing page pagination? Would it be helpful to include the page number in the title?

There is a good chance that including the page number in your information about a page will have little effect. I would include the page number if you think it's gonna help users understand the context of a page. I would not include it on the assumption it'll help with ranking or increasing the likelihood of the page being indexed.

Is it better to post one article a day, or many a day?
------------------------------------------------------

**John:** Is it better for domain ranking to regularly post one article every day or to post many articles every day?

So here's my chance to give the SEO answer: it depends. You can decide how you want to engage with your users on the downside, that means there's no absolute answer for how often you should publish. On the upside, this means that you can decide for yourself.

What is the main reason for de-indexing a site after a spam update?
-------------------------------------------------------------------

**Gary:** Faiz Ul Ameen is asking what is the main reason for de-indexing of sites after the Google spam update?

Well, glad you asked. If you believe you were affected by the Google Spam update, you have to take a really, really deep look on your content and, considerably improve it. Check out our spam policies, and read more about the [Google spam update on Search Central](/search/updates/spam-updates).

Can Google read infographic images?
-----------------------------------

**John:** Zaid asks, can Google read infographic images? What's the best recommendation there?

While it's theoretically possible to scan images for text, I wouldn't count on it when it comes to web search. If there's text that you want your pages to be recognized for, then place that as text on your pages. For infographics, that can be in the form of captions and `alt` texts, or just generally, well, you know, text on the page.

Is it possible to remove my site completely if it was hacked?
-------------------------------------------------------------

**Gary:** Anonymous is asking whether it's possible to completely remove a site from Google Search, because it has been hacked and leads to thousands of invalid links.

Well, first and for foremost, sorry to hear that your site was hacked. Our friends at web.dev have [great documentation](https://web.dev/explore/secure) about how to prevent this from happening in the future, but they also have documentation about how to clean up after a hack. To answer your specific question, you can remove your site from search by serving a `404` or similar status code, or by adding `noindex` rules to your pages. We will need to recrawl your site to see the status codes and `noindex` rules. But that's really the best way to do it.

Why does my Search Console miss a period of data?
-------------------------------------------------

**John:** I'm missing months of data from my domain property on Search Console, from April 2022. It connects directly to August 2022. What happened?

This can happen if a website loses verification in Search Console for a longer period of time. Unfortunately, there is no way to get this data back. One thing you could try, however, is to verify a different part of your website and see if it shows some of the data there.

How can I deindex some bogus URLs?
----------------------------------

**Gary:** Anonymous is asking, I want to deindex some bogus URLs.

There's really only a handful ways to deindex URLs: removing the page and serving a `404` or 410 or similar status code. Or by adding a `noindex` rule to the pages and allowing Googlebot to crawl those pages. These you can all do on your own site. You don't need any specific tool. But Googlebot will need to recrawl those pages to see the new statuses and rules. If we are talking about only a couple pages, then you can request indexing of these pages in Search Console.

Why is some structured data detected only in the schema validator?
------------------------------------------------------------------

**Lizzi:** Frank asks, why is some structured data markup detected on the schema validator, but not on Google's rich result test?

Hey Frank. This is a really common question. These tools are actually measuring different things. I think you're referencing the [schema.org Markup Validator](https://validator.schema.org/), which is checking if your syntax in general is correct, whereas the [Rich Result Test](https://search.google.com/test/rich-results) is checking if you have markup that may enable you to get a rich result in Google Search. It doesn't actually check every type that's on schema.org, it only checks those that are listed in the list of [structured data markup that Google supports](/search/docs/appearance/structured-data/search-gallery), which is about 25 to 30 features, so it's not fully comprehensive of everything that you'd see on schema.org, for example.

Do you have people who can make a website for me?
-------------------------------------------------

**John:** Do you have people that I can work with to create a functioning site?

Unfortunately no. We don't have a team that can create a website for you. If you need technical help, my recommendation would be to use a hosted platform that handles all of the technical details for you. There are many fantastic platforms out there now, everything from [Blogger](https://www.blogger.com/) from Google, to [Wix](https://www.wix.com/), or [Squarespace](https://www.squarespace.com/), [Shopify](https://www.shopify.com/), and many more. They all can work very well with search and usually they can help you to get your site off the ground.

Why are some sites crawled and indexed faster?
----------------------------------------------

**Gary:** Ibrahim is asking why are some websites crawled and indexed faster than others?

This is a great question. Much of how fast a site is crawled and indexed depends on how the site is perceived on the internet. For example, if there are many people talking about the site, it's likely the site's going to be crawled and indexed faster. However, the quality of the content also matters a great deal. A site that's consistently publishing high quality content is going to be crawled and indexed faster.

Why do Google crawlers get stuck with a pop-up store selector?
--------------------------------------------------------------

**Alan:** Why do Google crawlers get stuck with a pop-up store selector?

It can depend on how the store selector is implemented in HTML. Google follows `a href` links on a page. If the selector is implemented in JavaScript, Google might not see that the other stores exist, and so might not find the product pages for those stores.

How can I verify my staging site in Search Console?
---------------------------------------------------

**Gary:** Anonymous is asking if we have a staging site that is allow-listing only specific developer's IP addresses, if we upload a Search Console HTML file, which I suppose is the verification file, will Search Console be able to verify that site?

Well, the short answer is no. To remove your staging site from Search, using the [removal tool for site owners](https://support.google.com/webmasters/answer/9689846) first you need to ensure that Googlebot can actually access the site, so you can verify it in Search Console. We publish our [list of IP addresses](/search/docs/crawling-indexing/verifying-googlebot) on Search Central. So you can use that list to allow-list the IPs that belong to Googlebot so it can access the verification file. Then you can use the removal tool to remove the staging site. Just make sure that the staging site in general is serving a status code that suggests it cannot be indexed such as `404` or `410`.

How can I get a desktop URL indexed?
------------------------------------

**John:** How can we get a desktop URL indexed? The message Search Console says page is not indexed because it's a page with a redirect. We have two separate URLs for our brand, desktop and mobile.

With [mobile first indexing](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing), that's normal. Google will focus on the mobile version of a page. There's nothing special that you need to do about that, and there's no specific trick to index just the desktop version.

Is it possible to report sites for stolen content?
--------------------------------------------------

**Lizzi:** Christian is asking, is it possible to report sites for stolen content, such as text, original images, that kind of thing?

Yes, you can report a site. Do a search for "DMCA request Google", and use the "[report content on Google](https://support.google.com/legal/troubleshooter/1114905)" troubleshooter to file a report.

Is adding Wikipedia links a bad practice?
-----------------------------------------

**John:** Is adding Wikipedia links to justify the content a bad practice?

Well, I'd recommend adding links to things that add value to your pages. Blindly adding Wikipedia links to your pages doesn't add value.

Is there any difference if an internal link is under the word "here"?
---------------------------------------------------------------------

**Lizzi:** Gabriel is asking, is there any difference if an internal link is under the word "here" or if it is linked in a keyword?

Hey Gabriel, good question. It doesn't matter if it's an internal link to something on your site or if it's an external link pointing to something else, "here" is still bad link text. It could be pointing to any page and it doesn't tell us what the page is about. It's much better to use words that are related to that topic so that users and search engines know what to expect from that link.

Why does my news site's traffic go up and down?
-----------------------------------------------

**Gary:** Niraj is asking, I follow the same pattern of optimization, but my news website traffic is up and down.

Well, for most sites it's actually normal to have periodic traffic fluctuations. For example, seasonality effects e-commerce sites quite a bit. For news sites, specifically user interest in the topics you cover can cause fluctuations, but all in all, it is normal and not something that you have to worry about usually.

Is changing the URL often impacting my SEO performance?
-------------------------------------------------------

**John:** Is changing the URL often impacting my SEO performance? For example, a grocery site might change a URL from `/christmas/turkey-meat` to `/easter/turkey-meat`. The page is the same, the URL is just changed with a redirect.

I wouldn't recommend constantly changing URLs. At the same time, if you must change your URLs, then definitely make sure to redirect appropriately.

How does freshness play a role in ranking seasonal queries like Black Friday deals?
-----------------------------------------------------------------------------------

**Alan:** How does freshness play a role in ranking? For seasonal queries like Black Friday deals, it makes sense to update frequently as news or deals are released, but what about something less seasonal?

You may decide to update a Black Friday deals page frequently to reflect the latest offers as they come out. Remember, however, that Google does not guarantee how frequently a page will be reindexed, so not all of the updates are guaranteed to be indexed. Also, a good quality page that does not change much may still be returned in search results if we think it's content is still relevant. I would recommend focusing on creating useful content and not spending too much time thinking about how to make static pages more dynamic.

Is there a way to appeal SafeSearch results?
--------------------------------------------

**John:** Adam asks, is there a way to appeal SafeSearch results? I work with a client that has been blocked from their own brand term while resellers and affiliates are still appearing.

So first off, I think it's important to realize that SafeSearch is not just about adult content. There's a bit of nuance involved there, so it's good to review the documentation. Should you feel that your website is ultimately incorrectly classified, there's a review request link in an article called "[SafeSearch and your website](/search/docs/crawling-indexing/safesearch)" in the Search developer documentation.

How can I update my site's brand name?
--------------------------------------

**Lizzi:** Danny is asking. My site name is in search is reflecting the old domain's brand name, even with structured data and metatags. What else can I do to update this information?

Hello, Danny. The [site name documentation](/search/docs/appearance/site-names#troubleshooting-common-issues) has a troubleshooting section with a list of things to check that's more detailed than what I can cover here. You want to make sure that your site name is consistent across the entire site, not just in the markup. And also check any other versions of your site and make sure that those are updated too, for example, `http` and `https`. If you're still not having any luck, go to the [Search Console help forum](https://goo.gle/sc-forum) and make posts there. The folks there can help.

When migrating platforms, do URLs need to remain the same?
----------------------------------------------------------

**John:** Aamir asks, while migrating a website from Blogger to WordPress, do the URLs need to be the same, or can I do a bulk `301` redirect?

You don't need to keep the URLs the same. With many platform migrations, that's almost impossible to do. The important part is that all old URLs redirect to whatever specific new URLs are relevant. Don't completely redirect from one domain to the home page of another. Instead, redirect on a per URL basis.

How much do I have to do to update an algorithmic penalty?
----------------------------------------------------------

**Duy:** Johan asked if a website gets algorithmically penalized for thin content, how much of the website's content do you have to update before the penalty is lifted?

Well, it's generally a good idea to clean up low quality content or spammy content that you may have created in the past. For algorithmic actions, it can take us several months to reevaluate your site again to determine that it's no longer spammy.

How can I fix long indexing lead times for my Google-owned site?
----------------------------------------------------------------

**John:** Vinay asks, we've set up Google Search Console for a Google owned website where the pages are dynamically generated. We'd like to get insights into what we should do to fix long indexing lead times.

Well, it's interesting to see someone from Google posting here. As you listeners might know, my team is [not able to give any Google sites SEO advice](https://www.youtube.com/watch?v=t46OTdKmbyE) internally, so they have to pop in here like anyone else. First off, as with any bigger website, I'd recommend [finding an SEO agency](/search/docs/fundamentals/do-i-need-seo) to help with this holistically. Within Google, in the marketing organization, there are folks that work with external SEO companies, for example. Offhand, one big issue I noticed was that the website doesn't use normal HTML links, which basically makes crawling it a matter of chance. For JavaScript sites, I'd recommend checking out the [guidance in our documentation](/search/docs/crawling-indexing/javascript/javascript-seo-basics) and our videos.

How does the helpful content system determine that visitors are satisfied?
--------------------------------------------------------------------------

**Duy:** Joshua asked, how exactly does the helpful content system determine whether visitors feel they've had a satisfying experience?

We published a pretty comprehensive article called "[What creators should know about Google's August 2022 helpful content update](/search/blog/2022/08/helpful-content-update)" where we outline the type of questions you can ask yourself to determine whether or not you're creating helpful content for users. Such as, are you focusing enough on people first content? Are you creating content to attract search users using lots of automation tools? Did you become an expert on a topic overnight and created many articles seemingly out of nowhere? Personally, I think not just SEOs, but digital marketers, content writers, and site owners should be familiar with these concepts in order to create the best content and experience for users.

Should we `404` or `noindex` pages created by bots on our website?
------------------------------------------------------------------

**John:** Ryan asks, bots have swarmed our website and caused millions of real URLs with code tacked on to be indexed on our website through a vulnerability in our platform. Should we `404` of these pages or `noindex` them?

Either using a `404` HTTP result code or a [`noindex` robots metatag](/search/docs/crawling-indexing/block-indexing) is fine. Having these on millions of pages doesn't cause problems. Depending on your setup. You could also use robots.txt to disallow crawling of those URLs. The effects will linger in Search Console's reporting for a longer time, but if you're sure that it's fixed, you should be all set.

Will adding a single post in Spanish to my English site affect my search rankings?
----------------------------------------------------------------------------------

**Lizzi:** Bryan asks if my site is all in English and I add a single post in Spanish, will that affect search rankings?

Hey, Bryan. Sure. That's totally fine. It's not going to harm your search rankings. I also recommend checking out our guide to [managing multilingual websites](/search/docs/specialty/international/managing-multi-regional-sites) as there's a lot more to cover when you're thinking about publishing content in multiple languages.

Do all penalties show up in Search Console?
-------------------------------------------

**Duy:** Stepan asked, in Google Search Console there exists a section called Manual Actions. Does Google show all penalties there and always notify domain owners when a domain is hit with some penalties?

We have manual actions, which are issued by human reviewers and algorithmic actions, which are driven entirely by our spam algorithms such as Spambrain. We only communicate manual actions to site owners through Search Console. You can search for [manual actions report](https://support.google.com/webmasters/answer/9044175). There's a page there that lists a lot of information to help you understand more about our different types of manual actions, as well as how to file a reconsideration request when you receive and already address the manual action.

Will SEO decline? Should I study something different?
-----------------------------------------------------

**John:** Caroline asks, will SEO decline in favor of SEA and SMA? I'm starting my internship and need to know if I better redirect my path or continue on my way and specialize myself in accessibility.

I'm not quite sure what SMA is, but regardless, there are many critical parts that lead to a website's and a business' success. I definitely wouldn't say that you shouldn't focus on SEO, but at the same time, it's not, well, the answer to everything. My recommendation would be to try things out. Find where your passions and your talents lie, and then try more of that. Over the years things will definitely change, as will your interests. In my opinion, it's better to try and evolve than to wait for the ultimate answer.

Does the number of outgoing links affect my rankings?
-----------------------------------------------------

**Duy:** Jemmy asked, does the number of outgoing links both internal and external, dilute PageRank, or is PageRank distributed differently for each type of link?

I think you might be overthinking several things. First of all, focusing too much on PageRank, through building unnatural links whether it violates a policy or not, takes time and effort away from other more important factors on your, such as helpful content and great user experience. Second of all, sites with internal links allowed us to discover not only new pages, but also understand your site better. Limiting them explicitly would likely do more harm than good.
