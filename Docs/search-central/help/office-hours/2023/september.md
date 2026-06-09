---
title: "September 2023 Google SEO office hours"
source_url: "https://developers.google.com/search/help/office-hours/2023/september?hl=en"
product: "Google Search Central"
section: "Help & FAQ"
language: en
scraped_date: 2026-06-08
doc_id: "search-central/help/office-hours/2023/september.md"
---
September 2023 Google SEO office hours
======================================

This is the transcript for the September 2023 edition of the [Google SEO Office Hours](/search/help/office-hours). For site-specific help,
we recommend posting your question in the [Google Search Central Help Community](https://support.google.com/webmasters/community).

Is Google wrongly indexing the www version of my website?
---------------------------------------------------------

**John:** Wan asks: Google wrongly indexes the www version of my website. The correct page is supposed to be HTTP and then their domain name .my without the www.

Hi Wan! I took a look at your pages, and it looks like your server is automatically redirecting from the non-www to the www version, and setting the link rel canonical element appropriately. At first glance, if you're using Chrome, it might look like it doesn't have a www in front, but if you click twice into the URL on top in the browser, it expands to the full URL, with www. In practice, this is fine - both the www and the non-www versions of a site are totally ok with Google Search. Wow, that's a lot of wwws!

Why is filtered data higher than the overall data on Search Console?
--------------------------------------------------------------------

**Gary:** Ornella is asking: Why is filtered data higher than overall data on Search Console, it doesn't make any sense.

First of all, I love this question, but probably for the wrong reason. The short answer is that we make heavy use of something called [Bloom filters](https://www.google.com/search?q=bloom+filters&tbm=vid&source=lnms) because we need to handle a lot of data, and Bloom filters can [save us lots of time and storage](https://en.wikipedia.org/wiki/Bloom_filter#Space_and_time_advantages). The long answer is still that we make heavy use of Bloom filters because we need to handle a lot of data, but I also want to say a few words about Bloom filters: when you handle large number of items in a set, and I mean billions of items, if not trillions, looking up things fast becomes super hard. This is where Bloom filters come in handy: they allow you to consult a different set that contains a [hash](https://en.wikipedia.org/wiki/Hash_function) of possible items in the main set, and you look up the data there. Since you're looking up hashes first, it's pretty fast, but hashing sometimes comes with data loss, either purposeful or not, and this missing data is what you're experiencing: less data to go through means more accurate predictions about whether something exists in the main set or not. Basically Bloom filters speed up lookups by predicting if something exists in a data set, but at the expense of accuracy, and the smaller the data set is the more accurate the predictions are.

Why are the pages of my Google Sites website not being indexed properly?
------------------------------------------------------------------------

**John:** There was a question submitted in French, which basically asks why the pages of my [Google Sites](https://sites.google.com/) website aren't being indexed properly.

It's great to get questions in other languages. Taking a step back, websites created on Google Sites can and do get indexed in Google Search. However, the URLs used in Google Sites are a bit hard to track since the public version can be different from the URL you see when logged in. To be blunt, while it's technically indexable, it's not ideal for SEO purposes, and can be complex for tracking in Search Console. If SEO is your primary consideration, it might be worthwhile to explore other options and check the pros and cons before committing. For performance tracking in Search Console, you could also use your own domain name for the Google Sites content. Using your own domain name makes it easier to migrate, should you choose to do so, and allows you to [verify ownership of the whole domain for Search Console](https://support.google.com/webmasters/answer/9008080#zippy=%2Cdomain-name-provider).

Our site has many buttons, when clicking on them they fetch links to other pages. Can Google crawl these links?
---------------------------------------------------------------------------------------------------------------

**Gary:** Sarabjit is asking: Our website has multiple buttons, on clicking them we are fetching links to other pages. Will Google be able to crawl these links?

Generally speaking Googlebot doesn't click on buttons.

Is a "guest post" (to gain a backlink) against Google's guidelines if I'm writing valuable content?
---------------------------------------------------------------------------------------------------

**John:** Brooke asks: Most websites only offer the option to purchase a "guest post" (to gain a backlink) from them nowadays. Is this against Google's guidelines if I'm writing valuable content?.

Hi Brooke, thanks for posting your question. It sounds like you're already on the right track. Yes, using guest posts for links is against our [spam policies](/search/docs/essentials/spam-policies#link-spam). In particular, it's important that these [links are qualified](/search/docs/crawling-indexing/qualify-outbound-links) in a way that signal that they don't affect search results. You can do this with the `rel=nofollow` or `rel=sponsored` attributes on links. It's fine to use advertising to promote your site, but the links should be blocked as mentioned.

Is content on an e-commerce category page valuable to improving overall rankings?
---------------------------------------------------------------------------------

**Gary:** Brooke is asking: Is content on an e-commerce category page valuable to improving overall rankings?

You can add whatever content you like to your pages, they are your pages after all. But please don't do those auto-generated low-quality repeated, blurbs of text over and over again on all your category pages. It just looks silly, even for the average person. If you need content on your pages add content that people will actually find useful, don't add content because search might require it or so you think. Also check out our [e-commerce recommendations](/search/docs/specialty/ecommerce).

Do incorrect semantic tags cause Google to have a poorer understanding of the website content?
----------------------------------------------------------------------------------------------

**John:** Do incorrect semantic tags cause Google to have a poorer overall understanding of the website content, and thus a poorer ability to assign it to a branch? In particular `<hr>` tags signal a change of topic, but I might only use them for design purposes.

That's an interesting question. In general, using semantic HTML correctly can help search engines to better understand the content of a page, and its context. For example, if you mark up [headings on a page](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements), that's a clear sign that you believe your content fits to that heading. It's not a secret path to number one rankings, but if we have trouble understanding what you mean in the text, then providing a clear summary in the form of headings does help. Because it's a subtle thing that depends on how well we otherwise understand the page, I'd see it as a good practice to make sure you have everything covered. Reversing that, going from semantically correct to semantically incorrect HTML, is also subtle. Can search engines still understand your page? Then probably you wouldn't see a difference in how they understand it. Is the meaning suddenly blurry? Then, well, maybe make it less blurry, perhaps with some semantic structure. To your specific example of `<hr>` tags, I can't think of a situation where there would be a difference in understanding of a page due to them being used incorrectly. There are infinite ways to use something incorrectly, but the ones which I think a web designer might accidentally run into with `<hr>` tags seem pretty safe. I guess that's a long way to say 'it depends', you're welcome.

In Google Search Console, the report for `404` pages has many URLs that appear to be from JSON or JavaScript. Should we ignore?
-------------------------------------------------------------------------------------------------------------------------------

**Gary:** Reza is asking: In Google Search Console the report for `404` pages is filled with URLs that appear to be somehow picked up by mistake from within some JSON or JavaScript code. Should we ignore this?

You can ignore those or just add a [`noindex` HTTP header](/search/docs/crawling-indexing/block-indexing) for them.

Can sitemap index files have links to sitemap files on other domains?
---------------------------------------------------------------------

**John:** Dhruv askes: Can [sitemap index file](/search/docs/crawling-indexing/sitemaps/large-sitemaps) have links to sitemap files on other domains?

Hi Dhruv, interesting question. The answer from Google's side is a definite maybe, and because of that, my suggestion is not to use a setup like that. You can [submit sitemaps for URLs that aren't on the same domain](/search/docs/crawling-indexing/sitemaps/build-sitemap#cross-submit) in two situations, either you submit the sitemap via robots.txt, or you have verified ownership of all domains in Search Console. Especially Search Console ownership can be subtle and not immediately visible when you analyze the website, so it's easy to forget about that connection. If you're working on sitemap files and decide that you do want to use a setup like this, my tip would be to add an [XML comment](https://www.google.com/search?q=comments+in+xml) to the sitemap file so that you remember these requirements, and don't accidentally break them in the future. Since Search Console is Google-specific, you'd also want to check the requirements that other search engines might have about this.

How does one reduce the likelihood of Google choosing their own meta-descriptions for websites?
-----------------------------------------------------------------------------------------------

**Gary:** Sam Bowers is asking: How does one reduce the likelihood of Google choosing their own meta-descriptions for websites?

Good question: not always, but usually our algorithms will use your meta description when there's not much content on the page, or when the meta description is more relevant to a user's query than the actual content of the page. Learn more about [descriptions and snippets](/search/docs/appearance/snippet).

Is there a way to specify search engine bots not to crawl certain sections on a page?
-------------------------------------------------------------------------------------

**John:** Is there a way to specify Search Engine bots not to crawl certain sections on a page (the page is allowed for crawling and indexing otherwise). They go on to mention that they have a lot of duplication in "mega-menus" and would like to block them.

Yes, there are things you can do to prevent the indexing of parts of a page, but especially for common page elements like headers, menus, sidebars, footers, it's not necessary to block them from indexing. Search engines deal with the web as it is, and sometimes there are giant mega-menus or over-footers, that's fine. For other pieces of content on a page, you could either use an iframe with a source [disallowed by robots.txt](/search/docs/crawling-indexing/robots/intro) or pull in content with JavaScript that's similarly blocked by robots.txt. If you just want to avoid something being shown in a snippet, using the [`data-nosnippet` attribute](/search/docs/crawling-indexing/robots-meta-tag#data-nosnippet-attr) is a good way to do that. But again, there's no need to add this much complexity just to hide a menu. Unnecessary complexity brings a risk of things breaking unexpectedly, so it's good to limit that to cases where it's really needed.

Do you recommend infinite scrolling on web pages? Are there any implications to the organic traffic or Googlebot?
-----------------------------------------------------------------------------------------------------------------

**Gary:** Jeethu is asking: Do you recommend infinite scrolling on web pages? Are there any implications to the organic traffic or GoogleBot if I add that feature?

It depends how you implement infinite scrolling. if each piece or virtual page is also accessible and findable through a unique URL, generally it should be fine to have infinite scroll

I have links shown on the mobile web version, but hidden on the desktop. Will Google de-value them?
---------------------------------------------------------------------------------------------------

**John:** Ryan asks: If a homepage has links that are shown on the mobile web, but hidden behind a JavaScript toggle on desktop and not included in the HTML unless clicked, will Google de-value them?

Hey Ryan. With [mobile first indexing](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing), we use the mobile version of a page as the basis for indexing and for discovering links. If the mobile version has the full content, you're all set. It feels surprising to me that you'd have less content on desktop, but I guess you have reasons for that.

Does Google index PDF files that are saved to Google Drive that are not hosted on a website?
--------------------------------------------------------------------------------------------

**Gary:** Anonymous is asking: Does Google index PDF files that are saved to Google Drive that are not hosted on a website? If so, how long does it take?

Yes, Google can index public PDF files hosted on Google Drive, it's just another URL on a site. As with any URL it can take anywhere between a few seconds to never to get these PDFs indexed.

How does Google crawl Scrolljacking content and will this approach to UX impact rankings?
-----------------------------------------------------------------------------------------

**John:** Matt submitted a question saying: "Scrolljacking" is increasing in popularity across the web. Generally it is seen as a poor user experience, how does Google crawl this content and will this approach to UX impact rankings? They also added a link to an article about scrolljacking, which I'll link to in the transcript.

Hi Matt, that's an interesting question. I didn't realize it was called "[Scrolljacking](https://www.nngroup.com/articles/scrolljacking-101/)", thanks for the link. I don't think we'd see this setup as abusive, so there's not going to be a direct effect. However, there might be technical second order effects that you might see. For example, [Google renders pages](/search/docs/crawling-indexing/javascript/javascript-seo-basics) by loading them in a theoretically really-large mobile device. If the page doesn't display the content there due to shenanigans with scroll events, then our systems might assume that the content isn't properly visible. So in short, I'd see this more as a potential rendering issue, than a quality one.

Why is the URL indexed, though blocked by robots.txt on my Google Search Console?
---------------------------------------------------------------------------------

**Gary:** Deniz Can Aral is asking: Why indexed, though blocked by robots.txt on my Google Search Console?

This is a relatively common question: Google can index the URL, and only the URL not the content, even if that [URL is blocked for crawling through robots.txt](/search/docs/crawling-indexing/robots/intro). The number of such URLs in our index is tiny though, because this happens only if the blocked URL is highly sought after on the internet. If this is problematic for you, allow crawling the URL and use a [`noindex` rule in the HTTP headers or a `<meta>` tag](/search/docs/crawling-indexing/block-indexing).

We have unwanted AI content! How can I fix or remove it from my website?
------------------------------------------------------------------------

**John:** Sonia asks: We hired some content writers but they gave us AI content, how can I fix it? Do I just delete AI content? Replace with new content? Scrap and create a new website with a new URL? Please advise!

I don't know what to say, Sonia. It sounds like you just blindly published content from external authors without review? That seems like a bad idea, even without [the AI content aspect](/search/blog/2023/02/google-search-and-ai-content). Well, regardless of the reasons and source, if you published low-quality content on your website, and don't want to be associated with it anymore, you can either remove the content or fix it. I'd suggest looking at the bigger picture: is content like this missing on the web, and your site could add significant value for users overall? Or is it just rehashed content that already exists on the rest of the web? Or think of it this way, if your content is essentially the same as what others already have, why should search engines even index it, much less show it highly in the search results? And of course, making a great website takes more than just good articles, it takes a clear strategy, and processes that ensure that everyone is on board with your goals.

We got a spike in indexed URLs from one day to another. What are the reasons?
-----------------------------------------------------------------------------

**Gary:** Lorenzo is asking: We got a spike in indexed URLs from one day to another: what are the reasons?

Maybe we got more hard drives, maybe we freed up some space, maybe we just discovered those new URLs. It's hard to tell. Open the bubbly nonetheless! Celebrate!

Can Google use multiple file sizes in one favicon file?
-------------------------------------------------------

**John:** Dave asks: Can Google use multiple file sizes in one favicon file? Does it understand multiple icons marked up with the sizes attribute and pick an appropriate one?

Hi Dave. Technically, the [.ico file format](https://en.wikipedia.org/wiki/ICO_(file_format)) allows you to provide files in multiple resolutions. However, with the rise in the number of sizes that are used for various purposes, I suspect it's generally better to specify the sizes and files individually. Google does [support multiple favicon sizes](/search/docs/appearance/favicon-in-search) in HTML, so if there are specific sizes you want to provide, I'd go with that.

Does Google judge parts of a website differently when a different CMS lies behind them?
---------------------------------------------------------------------------------------

**Gary:** Vivienne is asking: Does Google judge parts of a website differently when a different CMS lies behind them?

No.

In Google Search, our website displays a PDF download as the main page. Can the search result be changed?
---------------------------------------------------------------------------------------------------------

**John:** Anna asks: The Google search result from our foundations website needs to be re-crawled, it displays a PDF download as the main page. Our website is a Dutch human rights foundation. Can the search result be changed?

Hi Anna, I took a look at your website and the reason why other pages are being shown instead of your homepage is that the homepage has a `noindex` robots `<meta>` tag on it. This `<meta>` tag will [prevent indexing of that page](/search/docs/crawling-indexing/block-indexing). Once you remove it, things should settle down quickly.

When I search for my website on Google Search, the first result is a product page and not my welcome page. Why?
---------------------------------------------------------------------------------------------------------------

**John:** Julien asks: When I search for my website on Google search, the first result is a product page and not my welcome page? Why is that? The product page is not even prepared with the SEO but my welcome page is.

Hi Julien. Google uses a number of factors to try to figure out which pages might be the most relevant to users for specific queries. In [information retrieval](https://en.wikipedia.org/wiki/Information_retrieval), one of the concepts is based on the perceived user intent. In short: what were they trying to do when they searched for this? Are they looking for more information about a product or company? Or are they looking to buy that product right now? This can change over time for the same query too. In short though, this means that even when a page is not prepared for SEO, it can still be that it shows up in search, if the systems think it's relevant at the time. In practice, my recommendation is to understand the different ways users might come to your site, and to try to cover their needs appropriately, so that regardless of where they end up, they have a good experience.

I received a Search Console alert for improving INP issues. How do you calculate this and what's the easiest fix?
-----------------------------------------------------------------------------------------------------------------

**John:** Alejandro submitted a question: Hi John and Google team, today I received a Search Console alert regarding improving INP issues. How do you calculate this data and what is the easiest way to correct it?

I don't have a full answer here, but there's quite a bit of [documentation on Interaction to Next Paint, or INP for short, on the web.dev site](https://web.dev/articles/inp). I'd recommend checking that out, if you're interested in improving your site's scores there. Keep in mind that INP is not yet a part of [Core Web Vitals](/search/docs/appearance/core-web-vitals), and that Core Web Vitals is just one of many things that play a role in our [page experience](/search/docs/appearance/page-experience) and [helpful content systems](/search/updates/helpful-content-update). While improving INP can definitely help user experience, I wouldn't expect it to visibly change search ranking.

How do I remove 30K URLs from Google Search Console from a Japanese keyword hack?
---------------------------------------------------------------------------------

**John:** Heather asks: How to remove 30K URLs from GSC from Japanese Keyword Hack?

Hi Heather, sorry to hear about getting hacked. I hope you were able to resolve it in the meantime, but we have a bit of [content on this kind of hack over on web.dev](https://web.dev/articles/fix-the-japanese-keyword-hack), I'll link to it from [the transcript](/search/help/office-hours/2023/september). Keep in mind that this hack tends to cloak the hacked content to Google, so you may need some help to double-check that it's fully removed. And with regards to search results, given the number of pages involved, I'd recommend focusing on the more visible pages and getting those manually resolved by either [removing](https://support.google.com/webmasters/answer/9689846) or [reindexing](/search/docs/crawling-indexing/ask-google-to-recrawl) them, and then let the rest drop out on its own. If you're explicitly looking for the hacked content, you will still be able to find it for quite some time, but the average user would be looking for your site, and the goal should be to make those search results ok.

Why are my pages getting de-indexed after submitting them for indexing in Search Console? I've done this multiple times now.
----------------------------------------------------------------------------------------------------------------------------

**John:** Grace asks: Why are pages getting de-indexed after submitting them for indexing in Search Console? I've done this multiple times now.

Hi Grace. I can't really say without knowing the pages involved, however, to me this hints at our systems not being convinced about the value of your site and its content. We almost never index all pages from a website, so some of that is also to be expected. You may be able to push for indexing once, but our systems will re-evaluate the content and the website over time, and may drop those pages again. The best course of action is not to keep trying to push these pages in, but rather to make it so that our systems are convinced about the overall quality of your website, the unique value that it's adding to the web, and the match for what users are actually looking for. Then we'll go off and index it on our own.
