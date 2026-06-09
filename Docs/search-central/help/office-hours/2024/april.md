---
title: "April 2024 Google SEO office hours"
source_url: "https://developers.google.com/search/help/office-hours/2024/april?hl=en"
product: "Google Search Central"
section: "Help & FAQ"
language: en
scraped_date: 2026-06-08
doc_id: "search-central/help/office-hours/2024/april.md"
---
April 2024 Google SEO office hours
==================================

This is the transcript for the April 2024 edition of the [Google SEO Office Hours](/search/help/office-hours). For site-specific help,
we recommend posting your question in the [Google Search Central Help Community](https://support.google.com/webmasters/community).

Is it likely my rankings have dropped because Google found out I have two websites?
-----------------------------------------------------------------------------------

**John:** A question from Faith: My rankings have dropped due to Google finding out I have two
websites. Is this correct?

No. That's not likely. Many people have several websites. Separate websites are not a problem. The
issue is often more indirect: if you work on a lot of websites, you're not going to have a lot of
time to make truly awesome websites everywhere. And, if you're making websites that aren't awesome,
then that can be something which our algorithms pick up on when it comes to recommending your site
to others.

Does it matter if one uses underscores or hyphens to separate keywords in the URL?
----------------------------------------------------------------------------------

**Gary:** Javier is asking: Does it really matter using underscore or hyphens to separate
keywords in the URL?

Well, keywords in URLs have barely any contribution to the rankings of your pages in Google's
search results, but yeah, it does matter what you use as separators, and hyphens are better in
some sense because it's clearer that they're separating words. I would really check our docs, we
have tons of ... well, [words about this](/search/docs/crawling-indexing/url-structure).

How do I tell Google not to crawl and index only paginated search results on my site? Should I
use "follow, noindex"?
---------------------------------------------------------------------------------------------------------------------

**John:** Another question: On my site, I want Google to crawl and index pages but not paginated
search results. If I use "follow, noindex" on my pagination pages, will Google not crawl through the
results and index my pages?

First of all, keep in mind that indexing is not guaranteed, even with a technically valid website.
Before you look too deeply into this, make sure that your website is truly fantastic and worthwhile
for the web's users. Going back to your question, theoretically, there are two outcomes here. Either
Google is able to see the page and the links, and follows them before dropping the page out of its
index. Or alternatively, the page is dropped out of the index and nothing from it is used. The
outcome is not defined, and will change over the site's lifetime. Practically speaking, if you're
only linking to the detail pages from unstable pages like this, it's not guaranteed that Google or
any other search engine will discover them. Maybe that's fine, and if you want more certainty, then
make sure search engines don't have to guess.

Should I continue counting impressions and clicks from an old domain after a new address relaunch?
--------------------------------------------------------------------------------------------------

**John:** Andi asks: Does it make sense to continue counting impressions and clicks from an
old domain in reports after a relaunch on a new address?

Hi Andi. Ultimately, this is your decision and it's not something that affects SEO.

Should I use `#color` or `?color` in the URL for a T-shirt product with
different colors in a drop-down?
--------------------------------------------------------------------------------------------------------

**Gary:** Javier is asking: I've got a t-shirt product with different colors in a drop-down.
Each variant has to be shareable. Should I use `#color` or `?color` on the
URL? Using `#` I make sure there is just one single indexable URL.

If you can use fragments in the URL to change the content, that's probably a nifty way to deal
with faceted results, but you can also just disallow crawling of URLs with certain parameters.
This is, I think, covered in our
[documentation for ecommerce sites](/search/docs/specialty/ecommerce/designing-a-url-structure-for-ecommerce-sites#how-google-understands-urls-for-product-variants).
In fact, check it out.

How do I remove my website from Google Search?
----------------------------------------------

**John:** How do I remove my website from Google searches?

Oh my! This is something I recently had a bit of practice with. So, SEO is often about getting
found, but not everyone wants that. When it comes to your website, there are a few ways to prevent
being found in search. Assuming you want your website to work for people, you could choose to either
use the [robots.txt file](/search/docs/crawling-indexing/robots/intro) or a
[`noindex` robots `meta` tag](/search/docs/crawling-indexing/block-indexing). I'll add
links for the details.

If you want to make sure that your site is not found at all, use the `noindex` robots `meta` tag.
This is because with robots.txt your website might still be findable if you search for it by name.
Many content management systems, like Wix or WordPress, make it easy to choose a `noindex`.

Additionally, if you urgently need to remove your website from Search, there's a
[removal tool in Search Console](https://support.google.com/webmasters/answer/9689846)
which you can use. You need to [verify ownership of your website](https://support.google.com/webmasters/answer/9008080)
for that first, and it's limited to a temporary removal. In short, try to use the `noindex`.

When linking to a URL with a highlighted text feature, does the PageRank flow to the page in
the same way?
----------------------------------------------------------------------------------------------------------

**John:** Sean asks: When linking to a URL with the link to a highlighted text feature, does
the PageRank flow to the page in the same way?

So this refers to the browser functionality where you can select a piece of text on a page and
ask for a link to that part of the page. Chrome calls this "link to text fragment". The way that
it's done is that the linked URL has a hash-symbol, followed by an identifier, something with
the word text, and then something that uniquely identifies the part of the page. This is pretty
cool, and helpful if you want to link to a specific part of a long document. From a search point
of view, any hash symbol and what follows there is ignored, so this has no special effect at all.
It's just a normal link!

If my site is down (`503` status code) 4 times a week, for 10-15 mins, is that a concern for SEO?
-------------------------------------------------------------------------------------------------

**Gary:** Robert is asking: Web releases, `503` server errors, and influence on
web rankings... We would like to increase the speed of web releases. The site will be down
(`503` temp. unavailable) four times a week, for about 10-15 mins. Is that a concern
for SEO? Either crawling, or for ranking.

Serving a [`503` status code](/crawling/docs/troubleshooting/http-status-codes#5xx-server-errors)
for an extended period of time will cause a decrease in crawl rate. This is documented extensively
on Search Central. Fortunately for you, 10-15 minutes every now and then is not "extended" by any
means, so you should be fine.

I changed the Facebook page URL to a new one. What do I need to do next?
------------------------------------------------------------------------

**John:** Pailin asks: I changed the Facebook page URL to a new one. What do I need to do next?

Hi Pailin. The ideal way to change the address shown in search results is to use a redirect.
I don't know if Facebook pages can do this for you. You can check for a redirect roughly by just
opening the old URL in a browser - if it redirects, it should move to the new URL. If you can't
redirect, ideally you'd remove the old page, so that it no longer appears. In any case, without
redirects, it usually takes a bit more time for search engines to understand that the new URL is
more relevant to users.

My site disappeared from search results after it was transferred from WordPress to self-publishing.
---------------------------------------------------------------------------------------------------

**John:** Eugene asks: After the site was transferred from WordPress to self-publishing,
almost all publications disappeared from the index. The search results are "0".

If your website dropped out of the search results and is no longer being indexed at all, right
about the time when you did a migration, then my guess is that your new website is somehow
blocking search engines, or at least, blocking Google. I'd start by analyzing the data in the
Search Console, and working forward from there.

If we switch to another website hosting provider, will this have a negative and lasting effect
on our SEO rankings?
-------------------------------------------------------------------------------------------------------------------

**Gary:** Someone is asking: My company is considering switching hosts for our website. Would
switching have a negative and lasting effect on our SEO rankings?

If you do things by the book, meaning the website keeps being resolvable and the actual downtime
is minimal, changing hosts should not have negative effects on your pages' rankings in Google's
search results.

Google is indexing URLs from my website which seem to have been created by a bot in Chinese.
--------------------------------------------------------------------------------------------

**John:** Kostas asks: Google is indexing search URLs that were created by bots in Chinese,
will this affect SEO?

Hi there. Well, bad news! Your website is probably hacked if you see pages like these in the
search results. It sounds a lot like a common kind of hack that's called the Japanese Keyword
Hack. You really need to resolve this if you want to use your website for users or for search.
We have documentation on how to work on a [variation of this hack in our documentation](https://web.dev/articles/fix-the-japanese-keyword-hack),
which I'll link to. And, of course, don't be afraid to get help for something like this — it
can be quite technical and complex to resolve.

We have blocked some IPs from App Engine and when we submit sitemaps, we get the HTTP `403` error.
--------------------------------------------------------------------------------------------------

**Gary:** Someone is asking: We have blocked some IPs from App Engine and when submitting
sitemaps we get `403` general HTTP error.

We publish our full range of IP addresses that we use for crawling, including crawling sitemaps.
I don't know how you do the blocking, but I'd allow-list those IPs. Check our docs for more info
about [Google's crawlers' IP ranges](/search/docs/crawling-indexing/verifying-googlebot).

How do I remove the old cached version of my site from Google Search results?
-----------------------------------------------------------------------------

**John:** Cedrick asks: How do I clear the historical search results on Google as it has cached
the old information?

Well, good news! We've started to remove the link to the cached version of a page in search, so
at least there's that. However, the page might still be indexed and visible with a snippet. These
are refreshed automatically over time, so they'll reflect the current status of your web page given
time, and might disappear if your page has been removed completely from your website. For urgent
situations, there's a [removal tool](https://support.google.com/webmasters/answer/9689846)
which you can use; I'll link to it for you.

Can I use Indexing API for a real estate ad?
--------------------------------------------

**Gary:** Reda is asking: I would like to know if I can use Indexing API for a real estate
website (as a real estate ad).

I strongly recommend checking the [docs for Indexing API](/search/apis/indexing-api/v3/quickstart).
As far as I remember, it's limited to just job postings and broadcast events, and not for anything
else. It might still work, but since it's intended for those two things, I wouldn't be surprised
if suddenly it stopped working for unsupported verticals overnight.

Is it OK to integrate headlines in images as HTML text (e.g. as an H1 tag)?
---------------------------------------------------------------------------

**John:** Nataliya asks: Is it okay to integrate headlines in images as HTML text? For example as H1?

There are various ways to integrate text into HTML elements and images. For the most part, they
just work. The only variation I'd avoid is putting text into the image file, since this makes it
hard for search engines and for some users to recognize.

Is there any sanction if a website has a hidden burger menu with the same links as the desktop menu?
----------------------------------------------------------------------------------------------------

**Gary:** Someone's asking: Is there any sanction if a website got a hidden burger menu with the
same links as the desktop menu? Duplicate link in DOM?

Well, the answer is "No".

Can you use multiple hreflang tags to indicate preferred locations if a domain is using a
regional subdomain?
-------------------------------------------------------------------------------------------------------------

**John:** Darren asks: Can you still use multiple hreflang tags to indicate preferred locations
if a domain is using a regional subdomain like me.domain (for the Middle East)?

Yes, you can use multiple hreflang values for the same page. For example, you might have one
German-language page for both Germany and Austria. Keep in mind that this is specifically for
hreflang, where we swap out the URLs shown to users in search results based on their language and
location. Check out our [internationalization documentation](/search/docs/specialty/international)
for more details!

Should I create a new Search Console property when moving my website from HTTP to HTTPS?
----------------------------------------------------------------------------------------

**John:** Ivan asks: Should I create a new Search Console property when moving my website from HTTP to HTTPS?

In short: yes. Or alternatively, verify at the domain level, and you'll have both covered
automatically.

How can I fix fake 404s hitting my site from an external source? Is it related to a ranking drop?
-------------------------------------------------------------------------------------------------

**Gary:** Klaudia is asking: False 404 URLs hitting my website from external source, could this
be related to ranking drop? What can I do to fix it?

Fake 404s that Googlebot might've crawled cannot be reasonably attributed to a ranking drop.
It's normal to have any number of 404s on a site and you don't *have to* fix them, though
if you see in your analytics software that a larger number of actual users are also coming through
those 404 URLs, I would personally try to convert them somehow by, for example, showing them some
relevant content instead.

Does the Google Account used to verify a domain in Search Console have to match the owner of the
new website?
-------------------------------------------------------------------------------------------------------------

**John:** Does the Google Account used to verify a domain on Google Search Console have to
match the owner of a new Google site?

Search Console verification is so that you have access to the data and settings that are
relevant for your website. For Google, it doesn't matter who has verified ownership of the website.
That said, from an organizational point of view, it seems like a bad practice to rely on employees'
personal accounts to manage the company web presence. But again, for Search Console and Google
Search, that doesn't matter. That's up to you.

Does a sitemap filename have to be `sitemap.xml` or `sitemap_index.xml`?
And is it mandatory to have a sitemap?
---------------------------------------------------------------------------------------------------------------

**Gary:** Ranjeet is asking: Can a sitemap filename be anything other than `sitemap.xml` or
`sitemap_index.xml`? Additionally, is it mandatory to have a sitemap?

You really don't have to have a sitemap, but if you choose to have one (or more!), you can name
it anything you like. Mines are named `johnmu_loves_cheese.xml` for example.

Should I redirect my mobile site URL to my desktop URL instead of responsive web design or
dynamic serving?
-----------------------------------------------------------------------------------------------------------

**John:** Prem asks: Redirecting the mobile site URL to the common desktop URL instead of using
a responsive or dynamic serving approach, is this right?

Taking a step back, the approach of using separate URLs for mobile and desktop versions is
certainly an option, but you make things so much harder than they need to be, not just for SEO
but also for analytics, maintenance, and testing. I'd recommend that you move to a clean
responsive setup when you can.
