---
title: "January 2023 Google SEO office hours"
source_url: "https://developers.google.com/search/help/office-hours/2023/january?hl=en"
product: "Google Search Central"
section: "Help & FAQ"
language: en
scraped_date: 2026-06-08
doc_id: "search-central/help/office-hours/2023/january.md"
---
January 2023 Google SEO office hours
====================================

This is the transcript for the January 2023 edition of the [Google SEO Office Hours](/search/help/office-hours). For site-specific help,
we recommend posting your question in the [Google Search Central Help Community](https://support.google.com/webmasters/community).

Do meta keywords matter?
------------------------

**Lizzi:** Do meta keywords still help with SEO?

Nope. It doesn't help. If you're curious about why there's a [blog post from 2009](/search/blog/2009/09/google-does-not-use-keywords-meta-tag) that goes into more detail about why Google doesn't use meta keywords.

Why is my brand name not shown as-is?
-------------------------------------

**Gary:** Kajal is asking, my brand name is Quoality. That is, Quebec Uniform Oscar Alpha Lima India Tango Yankee, and when someone searches for our brand name, Google is showing the results for quality. That is the correct spelling. Why is Google doing this?

Great question. When you search for something that we often see as a misspelling of a common word, our algorithms learn that and will attempt to suggest a correct spelling or even just do a search for the correct spelling altogether As your brand grows, eventually our algorithms learn your brand name and perhaps stop showing results for what our algorithms initially detected as the correct spelling. It will take time though.

Which date should I use as `lastmod` in sitemaps?
-------------------------------------------------

**John:** Michael asks, the `lastmod` in a sitemap XML file for a news article. Should that be the date of the last article update or the last comment?

Well since the [sitemap file](/search/docs/crawling-indexing/sitemaps/build-sitemap) is all about finding the right moment to crawl a page based on its changes, the `lastmod` date should reflect the date when the content has significantly changed enough to merit being re-crawled. If comments are a critical part of your page, then using that date is fine. Ultimately, this is a decision that you can make. For the date of the article itself, I'd recommend looking at our guidelines on using dates on a page. In particular, make sure that you use the dates on a page consistently and that you include structured data, including the time zone, within the markup.

Can I have both a news and a general sitemap?
---------------------------------------------

**Gary:** Helen is asking, do you recommend to have news sitemap and general sitemap in the same website? Any issue if news sitemap and general sitemap contain the same URL?

You can have just one sitemap, a traditional web sitemap as defined by [sitemaps.org](https://sitemaps.org), and then add the [news extensions](/search/docs/crawling-indexing/sitemaps/news-sitemap#news-specific-tag-definitions) to the URLs that need it. Just keep in mind that, you'll need to remove the news extension from URLs that are older than 30 days. For this reason it's usually simpler to have separate sitemaps for news and for web. Just remove the URLs altogether from the news sitemap when they become too old for news. Including the URLs in both sitemaps, while not very nice, but it will not cause any issues for you.

What can I do about irrelevant search entries?
----------------------------------------------

**John:** Jessica asks In the suggest search, in Google, at the bottom of the page, there's one suggestion that is not related to our website. And after looking at the results, our website is not to be found for that topic.

Kind of hard for me to determine exactly what you mean, but it sounds like you feel that something showing up in search isn't quite the way that you'd expect it, something perhaps in one of the elements of the search results page. For these situations, we have a feedback link on the bottom, for the whole search results page, as well as for many of the individual features. If you submit your feedback there, it'll be sent through your appropriate teams. They tend to look for ways to improve these systems for the long run for everyone. This is more about feedback for a feature overall and less that someone will explicitly look at your site and try to figure out why this one page is not showing up there.

Why is my site's description not shown?
---------------------------------------

**Lizzi:** Claire is asking, I have a site description in my Squarespace website, but the Google description is different. I have reindexed it. How do I change it?

Something to keep in mind here is that it's not guaranteed that Google will use a particular meta description that you write for a given page. Snippets are actually auto-generated and can vary based off of what the user was searching for. Sometimes different parts of the page are more relevant for a particular search query. We're more likely to use the description that you write, if it more accurately describes the page than what Google can pull from the page itself. We have some [best practices about how to write meta descriptions](/search/docs/appearance/snippet) in our documentation, so I recommend checking that out.

How can I fix the spam score for a used domain?
-----------------------------------------------

**John:** Mohamed asks, I bought this domain and I found out it got banned or has a spam score, so what do I need to do? .

Well, like many things, if you want to invest in a domain name, it's critical that you do your due diligence ahead of time or that you get help from an expert. While for many things, a domain name can be reused, sometimes it comes with a little bit of extra balast that you have to first clean up. This is not something that Google can do for you. That said, I can't load your website at all when I tried it here. So perhaps the primary issue might be a technical one instead.

Are spammy links from porn sites bad for ranking?
-------------------------------------------------

**Lizzi:** Anonymous is asking, I've seen a lot of spammy back links from porn websites linking to our site over the past month using the Google Search Console link tool. We do not want these. Is this bad for ranking and what can I do about it?

This is not something that you need to prioritize too much since Google Systems are getting better at figuring out if a link is spammy. But if you're concerned or you've received a manual action, you can use the [disavow tool in Search Console](https://support.google.com/webmasters/answer/2648487). You'll need to create a list of the spammy links and then upload it to the tool. Do a search for disavow in Search Console for more steps on how to do this.

Does Google use keyword density?
--------------------------------

**John:** The next question I have here is, does Google consider keyword density for the content?

Well, no, Google does not have a notion of optimal keyword density. Over the years, our systems have gotten quite well at recognizing what a page is about, even if the keywords are not mentioned at all. That said, it is definitely best to be explicit. Don't rely on search engines guessing what your page is about and for which queries it should be shown. If your home page only mentions that you "add pizazz to places" and shows some beautiful houses, both users and search engines won't know what you're trying to offer. If your business paints houses, then just say that. If your business sells paints, then say that. Think about what users might be searching for and use the same terminology. It makes it easier to find your pages, and it makes it easier for users to recognize that they have found what they want. Keyword density does not matter, but being explicit does matter and contrary to the old SEO myth, story, joke, commentary, you don't need to mention all possible variations either.

Why is our title mixed up with the meta description?
----------------------------------------------------

**Lizzi:** Michael is asking, what should we do if we are seeing that certain pages have meta descriptions in SERPs displaying the exact same text as the title tag, not our custom descriptions or snippets from the page.

Hey, Michael. Well, first I'd check that the HTML is valid and that there's not any issue with how it's being rendered with the [URL inspection tool](https://support.google.com/webmasters/answer/9012289). It's hard to give any more advice without seeing more context, so I'd head to the [Search Central forums](https://goo.gle/sc-forum) where you can post some examples of the page and the search result you're seeing for it. The folks there can take a look and give some more specific advice on how to debug the issue further.

How can I remove my staging subdomain?
--------------------------------------

**Gary:** Anonymous is asking, I have a staging site which is on a subdomain, and unfortunately it got indexed. How can I remove it from search results?

Well, these things happen and it's not a reason to be worried. First, ensure that your staging site is actually returning a `404` or `410` status code, so Googlebot can update our records about that site. And then if it's a bother that the staging site appears in Search, submit a [site removal request](https://support.google.com/webmasters/answer/9689846) in Search Console. Just mind that you are going to need to verify the staging site in Search Console first.

Will disavowing links make my site rank better?
-----------------------------------------------

**John:** Jimmy asks, will disavowing spammy links linking to my website help recover from an algorithmic penalty?

So first off, I'd try to evaluate whether your site really created those spammy links. It's common for sites to have random, weird links, and Google has a lot of practice ignoring those. On the other hand, if you actively built significant spammy links yourself, then yes, cleaning those up would make sense. The [disavow tool](https://support.google.com/webmasters/answer/2648487) can help if you can't remove the links at the source. That said, this will not position your site as it was before, but it can help our algorithms to recognize that they can trust your site again, giving you a chance to work up from there. There's no low effort, magic trick that makes a site pop up back afterwards. You really have to put in the work, just as if you did it from the start.

How can I best move my site?
----------------------------

**Gary:** Clara Diepenhorst is asking, I want to implement a new name for my company, while the product and site stays mostly the same. This new name changes my URLs. How do I keep my credits of the old name?

Great question. And this is again, a site move question. Site moves are always fun and scary. The most important thing you need to do is to ensure that the old URLs are redirecting to the new URLs. This is the most important thing. Once you have your new domain, make sure that you [verify in Search Console](https://support.google.com/webmasters/answer/9008080). See if you get any red flags in the [security section](https://support.google.com/webmasters/answer/9044101) and other reports. And once you are already with the redirections, you can submit a site move request in Search Console also. Since it's a really big undertaking to do a site move, we have very [detailed documentation about site moves](/search/docs/crawling-indexing/site-move-with-url-changes). Try searching for something like "Google site move" on your favorite search engine and really just have a read, prepare yourself.

Why doesn't my site show up in Google?
--------------------------------------

**John:** Rob asks, my site does not show up on Google searches. I can't get it indexed.

So Rob mentioned the URL and I took a quick look and it turns out that the home page returns a `404` status code to us. Essentially for Google, the page does not exist at all. Trying it out a bit more, it looks like it returns a `404` status code to all Googlebot user agents and users can see it normally. You can test that using a [user agent switcher in Chrome](https://developer.chrome.com/docs/devtools/device-mode/override-user-agent) in the developer tools there. This seems to be more of a misconfiguration of your server, so you might need help from your hosting provider to resolve it. Google will keep retrying the page and once it's resolved, it should be visible in the search results again without, maybe a week or so.

How can I get my mobile version into Google?
--------------------------------------------

**Lizzi:** Matheus is asking Google Search Console looks at the desktop version of some, but not all articles on my website, even though it has a mobile version. How can I tell Google to look at the mobile version?

Well, we've got a list of things that you can check in our [documentation on mobile first indexing](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing), so I'd recommend going through that checklist and the troubleshooting section. Most of it boils down to this: make sure that you're providing the same content on both versions of your site and that both your users and Google can access both versions. If you're still having issues, we recommend posting in the forum so folks there can take a look at those specific pages that are not showing up as mobile friendly.

Why does a competitor's social account with the same name show up?
------------------------------------------------------------------

**John:** Anthony asks, my company's social media account is no longer appearing in the search results. Only my competitors are appearing now, and we have the same name.

It looks like it's more than just two sites using the particular name that you mentioned, and in this kind of situation it will always be hard to find your site, and it won't be clear to us or to users, which one is the so-called right one. They're all called the same, they're all essentially legitimate results. If you want people to find your site by name, then you should make sure that the name is a clear identifier and not a term that many others also use.

What could be a reason for a URL removal to not work?
-----------------------------------------------------

**Gary:** Lou is asking, why is my link still showing up on Google after I used the content removal tool and it got approved? Please help me understand this phenomenon.

Using the URL removal tool is very fast. Usually it removes the specified URL from search results within a few hours. If it didn't remove a URL that was approved for removal by the tool, that usually means that you specified the wrong URL. Try to click the actual result and see where you land. Is it the same URL that's shown in Search? If not, submit another [removal request](https://support.google.com/webmasters/answer/9689846) for that particular URL.

Which structured data should I use on a service-website?
--------------------------------------------------------

**John:** The next question I have here is our website is a service, not a product. The price will vary on the estimate. How do I fix the invalid item for a service like ours when I use product structured data?

For local business, like the one that you mentioned, I'd recommend looking at the [local business structured data](/search/docs/appearance/structured-data/local-business). This also lets you specify a price range for your services. We have more information about this markup in the search developer documentation.

Why might my content not be indexed?
------------------------------------

**Gary:** Anonymous is asking what could be the reason for our relatively healthy and content-rich country site to repeatedly be de-indexed and our old `404` subdomains and subfolders to be reindexed instead?

Well without the site URL, it's fairly impossible to give an exact answer, but it sounds like we just haven't visited all the URLs on those old subdomains and in subfolders, and that's why those URLs are still surfacing in search. If you are certain that the country site keeps falling out of Google's index and not just, for example, not appearing for the keywords you'd like, that could be a sign of both technical and quality issues. I suggest you drop by the [Google Search Central Forums](https://goo.gle/sc-forum) and see if the community can identify what's up with your site.

Can I get old, moved URLs ignored by Search?
--------------------------------------------

**John:** Alex asks, if you move a ton of content with `301` redirects, do you need to request removal of the old URLs from the index? Because even a decade later, Google still crawls the old URLs. What's up? Thank you.

No, you do not need to request re-indexing of moved URLs or request them to be removed. This happens automatically over time. The effect that you're seeing is that our systems are aware of your content having been on other URLs. So if a user explicitly looks for those old URLs, we'll try to show them , and this can happen for many years. It's not a sign of an issue. There is nothing that you need to fix in a case like this. If you check the URL's in Search Console, you'll generally see that the canonical URL has shifted when the redirect is being used. In short, don't worry about these old URLs showing up when you specifically search for those old URLs.

Does Search Console verification affect Search?
-----------------------------------------------

**Gary:** Avani is asking, changing Search Console ownership or verification code - does it affect website indexing?

Having your site verified in Search Console or changing the verification code and method has no effect on indexing or ranking whatsoever. You can use the data that Search Console gives you to improve your site and thus potentially do better in Search with your site, but otherwise has no effect on search whatsoever.

Why might my translated content not appear in Google?
-----------------------------------------------------

**John:** Now a question from Allan, about two months ago, I added another language to my website. I can't find the translated version through Google Search. What could be the reason for that?

When adding another language to a website, there are things that you need to do and things you could additionally do. In particular, you need to have separate URLs for each language version. This can be as little as adding a parameter to the URL, like question mark language equals German, but you must have separate URLs that specifically lead to that language version. Some systems automatically swap out the content on the same URL. This does not work for search engines. You must have separate URLs. The other important thing is that you should have links to the language versions. Ideally, you'd link from one language version to all versions of that page. This makes it easy for users and search engines to find that language version. Without internal links to those pages, Google might not know that they exist. And finally, using the hreflang annotations is a great way to tell us about connections between pages. I'd see this more as an extra, it's not required. You can find out more about sites that use [multiple language versions in our developer's documentation](/search/docs/specialty/international).

Does URL depth of an image affect ranking?
------------------------------------------

**Lizzi:** Sally is asking does the URL depth of an image affect image ranking and will adding the srcset and size code of an image in the HTML be good for image ranking?

Whether an image is three levels deep or five levels deep isn't really going to matter. What's more important is using a structure that makes sense for your site, and it makes it easy for you to organize your images in some kind of logical pattern, while still making sure that the file names are descriptive. For example, it might make sense to have a directory called `/photos/dog/havanese/Molly.png`, but if you don't have a ton of Havanese photos, then maybe just `/photos/Molly-Havanese-dog.png` might make sense. As far as `srcset` and size code goes, add those if it makes sense for your image. We recommend these for [responsive images](https://web.dev/learn/design/responsive-images) in particular so we can understand more about the different versions of a given image. Hope that helps.

What happens when a part of an `hreflang` cluster is bad?
---------------------------------------------------------

**Gary:** Anonymous is asking, is there a difference in how `hreflang` clusters are treated, depending on if the `hreflang` tag is broken or includes a `noindex` or a different canonical in the clusters.

Complicated topic. `Hreflang` clusters are formed with the `hreflang` links that we could validate. Validate in this context, meaning the back links between the `hreflang` tags. If an `hreflang` link couldn't be validated, that link will simply not appear in the cluster. The cluster will be created regardless with the other valid links. If one of the links is `noindex`, then that won't be eligible for getting into the cluster.

Are sitewide footer links bad?
------------------------------

**Lizzi:** Nazim is asking, are sitewide footer links that refer to the designer companies or the CMS harmful for SEO?

in general, if the links are boiler plate stuff like "made by Squarespace" that come with the website theme, this is not something that you need to worry about. If you have control over the link, we recommend that you add `nofollow` to these types of links. Also, check to make sure that the anchor text is something reasonable. For example, make sure that the link isn't gratuitously keyword rich, for example, "made by the best Florida SEO."

How can I speed up a site move?
-------------------------------

**Gary:** Mohamed is asking, I made a transfer request because I changed the domain name of our website in Search Console. What can I do to speed up this process? This is very, very important for me.

This is a good question. The most important thing you need to do is to ensure that your old URLs are redirecting to your new site. This will have the largest positive impact on your site move. The [site move request](https://support.google.com/webmasters/answer/9370220) in Search Console is a nice thing to submit, but even without it, site moves should do just fine, if you redirect the old URLs to the new ones and they are working properly. Search for something like "Google Site move" on your favorite search engine and check out our [documentation about site moves](/search/docs/crawling-indexing/site-move-with-url-changes), if you want to learn more.

How do I link desktop and mobile versions for m-dot sites?
----------------------------------------------------------

**Lizzi:** Nilton is asking, at the moment, my site is not responsive. It has a desktop version and an m-dot site. In the documentation it says the treatment we need to do is something in relation to canonical and alternate. My question is, do I need to put the canonical in the desktop version? The documentation doesn't make it very clear.

Thank you for your feedback, I will definitely try to make this clearer in the docs. The desktop URL is always the canonical URL, and the m-dot is the alternate version of that URL. So on the desktop version, you'll need a `rel=canonical` that points to itself and a `rel=alternate` that points to the m-dot version. And then on your m-dot page, you'll have only a `rel=canonical` that points to the desktop version of that page. Hope that helps.

How important is EXIF data?
---------------------------

**Gary:** Sagar is asking, how important is EXIF data from an SEO perspective for an e-commerce site or sites where images play key roles?

Well, this is an easy question. I really like easy questions. The answer is that Google doesn't use EXIF data for anything at the moment. The only image data, or metadata, that we currently use is [IPTC](/search/docs/appearance/structured-data/image-license-metadata#add-metadata).
