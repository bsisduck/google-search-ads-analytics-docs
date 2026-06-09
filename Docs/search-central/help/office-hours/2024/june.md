---
title: "June 2024 Google SEO office hours"
source_url: "https://developers.google.com/search/help/office-hours/2024/june?hl=en"
product: "Google Search Central"
section: "Help & FAQ"
language: en
scraped_date: 2026-06-08
doc_id: "search-central/help/office-hours/2024/june.md"
---
June 2024 Google SEO office hours
=================================

This is the transcript for the June 2024 edition of the [Google SEO Office Hours](/search/help/office-hours). For site-specific help,
we recommend posting your question in the [Google Search Central Help Community](https://support.google.com/webmasters/community).

How can one be transparent in the use of AI translations without being punished for AI heavy
content?
-----------------------------------------------------------------------------------------------------

**John:** Viktor asks, how can one be transparent in the use of AI translations without being
punished for AI heavy content?

Hi Viktor, well, there's no special markup that you can add to your pages to label them as
automatic translations. Instead, I would consider whether you consider these translated pages to
align with the quality bar that you set for yourself. If the pages are well-translated, if it uses
the right wording for your audience, in short, if you think they're good for your users, then
making them indexable is fine. If you're not happy with them, you could just include the `noindex`
robots `meta` tag on them, to let search engines know not to index them. Ultimately,
a good localization is much more than just a translation of words and sentences, so I would
definitely encourage you to go beyond the minimal bar, if you want users in other regions to
cherish your site.

Does Search Console include `site:` search results?
---------------------------------------------------

**Gary:** Hi, this is Gary. Leslie Leal is asking, does Search Console include `site:`
search results?

And the answer is: yes.

PageSpeed Insights vary from time to time when I check my website. Why is it not stable? Can you
give me the performance score?
-------------------------------------------------------------------------------------------------------------------------------

**John:** PageSpeed Insights vary from time to time when I check my website. Why is it not
stable? Can you give me the performance score?

Hi there! PageSpeed Insights uses so-called lab tests to evaluate the performance of your pages.
These are more like simulations, and depending on how your server is configured, you will see more
or less variance in their measurements. This is fine and expected. Instead of focusing on those
individual measurements, I'd recommend focusing on so-called field data, which is a compilation
based on what some of your site's users have actually seen. Keep in mind that while we do use Core
Web Vitals in our systems, they're an aspect of many. I wouldn't recommend over-focusing on minute
changes in these metrics, but rather use them to determine roughly where your site is, to find
low-hanging fruit in terms of performance, and to monitor for unexpected changes over time.

We've just bought a domain name, but the cache hasn't reset and it's not showing up in Google
results. How do we fix this?
--------------------------------------------------------------------------------------------------------------------------

**Gary:** FORMET Théo is asking, we've just bought a domain name, but the cache hasn't reset
and it's not showing up in Google results. How do we fix this?

Well, first and foremost, I would strongly advise you to [verify your new site in Search Console](https://support.google.com/webmasters/answer/9008080)
and then look at the data in there to make informed decisions about what should be your next step.
In general having the domain previously owned shouldn't be a problem and all you'd have to do is
to publish high quality, helpful content and wait for it to be indexed. If you see errors along
the way, fix them, and keep doing what you're doing.

Is it "against" webmaster guidelines if we use AI tools to generate initial content drafts
but have hired editors to humanize and review them, and to implement brand and SEO guidelines?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**John:** KG asks, is it "against" webmaster guidelines if we use AI tools to generate initial
content drafts but have hired editors to humanize and review them, and to implement brand and SEO
guidelines?

Well, what matters for us is the overall quality that you end up publishing on your website. If
you're using tools to get started, to help with spelling and formulations, that's not a problem on
its own — but it's also not a sign that what you've created will automatically be considered
high quality content. I'd recommend checking out our [guidance about AI-generated content](/search/blog/2023/02/google-search-and-ai-content)
and to go through the questions in our [helpful content page](/search/docs/fundamentals/creating-helpful-content).
I realize it's more work, but I find getting input from independent third-party folks on these
kinds of questions extremely insightful.

Does an auto translation of my website for other regions affect my ranking negatively?
--------------------------------------------------------------------------------------

**Gary:** Florian is asking, does an auto translation of my website for other regions affect
my ranking negatively?

Well, if the auto translation is of low quality, maybe. You should ensure that a human native
in those languages reviews (and perhaps fixes) the translations to ensure that the content is
actually helpful for users. Of course this is not a problem if you block crawling of such content.

Do many affiliate links hurt the ranking of a page?
---------------------------------------------------

**John:** Florian asks, do many affiliate links hurt the ranking of a page?

Hi Florian! We have a blog post from about 10 years ago about this, and it's just as relevant
now. The short version is that having affiliate links on a page does not automatically make your
pages unhelpful or bad, and also, it doesn't automatically make the pages helpful. You need to
make sure that your pages can stand on their own, that they're really useful and helpful in the
context of the web, and for your users.

Should I fix all broken backlinks to my site to improve overall SEO?
--------------------------------------------------------------------

**Gary:** Ryan Archer is asking, should I fix all broken backlinks to my site to improve
overall SEO?

You should fix the broken backlinks that you think would be helpful for your users. You can't
possibly fix all the links, especially once your site grew to the size of a mammoth. Or
brontosaurus.

Is a website using NextJS technology SEO friendly? Are there any issues I need to pay attention
to in order to configure my website to be SEO friendly?
-------------------------------------------------------------------------------------------------------------------------------------------------------

**John:** Is a website using NextJS technology SEO friendly? Are there any issues I need to
pay attention to in order to configure my website to be SEO friendly?

We see this question for many content management systems and platforms. For most platforms,
there are ways to make websites which work well for SEO, and ways that don't work so well. Often
there are blog posts and documentation available which will help you to make sure that a new site
is set up in a way which works well for Search. Most platforms work fairly well for SEO out of the
box. If you're using a framework like nextJS, and doing significant work with JavaScript, it's
worth reviewing our [JavaScript SEO best practices](/search/docs/crawling-indexing/javascript/javascript-seo-basics).
And regardless of platform, framework, or CMS, if it's a new website, make sure the SEO side is
properly set up before launching, get help for that if needed — adding SEO later is always
much harder.

I canonicalized part time course pages to full time course pages on a university website as the
content was 93% same. Is this a good strategy?
----------------------------------------------------------------------------------------------------------------------------------------------

**Gary:** Ammad's asking, I canonicalized part time course pages to full time course pages on
a university website as the content was 93% same. Is this a good strategy?

Well, from Google's perspective, it doesn't matter. You do you.

If most crawl requests are sent to a subdomain that's not used anymore, what should be the best
course of action? `noindex`? Redirection?
-----------------------------------------------------------------------------------------------------------------------------------------

**John:** Arthur asks, if most crawl requests are sent to a subdomain that's not used anymore,
what should be the best course of action? `noindex`? Redirection? Thanks.

With a question like this, one aspect that would help would be to know whether users also try to
access the old subdomain. This is unfortunately only possible if you enable hosting for the
subdomain. If you do that, I'd recommend setting up a redirect to the appropriate new pages. If
actual users also request the old subdomain, I'd figure out where they're coming from, and update
those links. If users are not going to the subdomain, if it's only crawlers, then just turning it
off is completely is fine. If you remove the DNS entry, then your server won't even see those
crawl requests. If you've had it disabled for longer, I'd just keep it turned off: users would
have told you if they regularly ran into problems. Hope that helps!

How to alert Google of sabotage via toxic links?
------------------------------------------------

**Gary:** Someone's asking, how to alert Google of sabotage via toxic links?

I know what I would do: I'd ignore those links. Generally Google is really, REALLY good at
ignoring links that are irrelevant to the site they're pointing at. If you feel like it, you can
always [disavow those "toxic" links](https://support.google.com/webmasters/answer/2648487),
or [file a spam report](https://search.google.com/search-console/report-spam).

On March 3rd 2024 we migrated our website from a bespoke ecommerce site to Shopify. Since then
our search traffic has fallen by over 60%. What could be the reason?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

**John:** Ken asks, on March 3rd 2024 we migrated our website from a bespoke ecommerce site
to Shopify. Since then our search traffic has fallen by over 60%. What could be the reason?

Hi Ken. Unfortunately, this is not something straightforward to diagnose, because there are two
relatively complex changes. On the one hand, during this time we launched a core update, which
affects how our systems look at relevance. On the other hand, you migrated your website to a new
infrastructure, with a new website structure, including new pages, text, headings, internal links,
and more. The redirects you mentioned are critical in forwarding signals across versions, but
quite a bit otherwise has also changed on the site.

My recommendation would be to focus more on the migration than the core update — since the
migration is something that's directly in your control. In particular, I'd use Search Console to
analyze the situation before the change including the more important URLs and queries, and to use
the Internet Archive at archive.org to view those old pages for a comparison. You don't need to
make things exactly as before and I would not recommend reverting the migration, but perhaps you
can find some changes that can be improved. Additionally, I would do similar checks for Google
Images since your products seem very image-heavy, and Merchant Center, for the products you
submit to the organic product listings. None of this is easy, and given the core update, you may
see differences even when doing things well, but working through the pieces individually can be
useful in the end.

Is it important for title tags to match the H1 tag?
---------------------------------------------------

**Gary:** Danielle is asking, is it important for title tags to match the H1 tag?

No, just do whatever makes sense from a user's perspective. We actually have [docs about this topic](/search/docs/appearance/title-link),
too, you should check it out.

Does Google penalize duplicate content for localized websites?
--------------------------------------------------------------

**John:** Jack asks, does Google penalize duplicate content for localized websites?

The answer here is: no. Localized content is not considered duplicate content.

I am using a third party tool to check indexation in Google Search results for an A/B Test. Is
this in violation of Google's machine generated traffic policy?
--------------------------------------------------------------------------------------------------------------------------------------------------------------

**Gary:** Someone is asking, hi, I am using a third party tool to check indexation in Google
Search results for an A/B Test. Is this in violation of Google's machine generated traffic policy?

Ignoring the question about whether the practice is in violation of our [machine generated traffic policies](/search/docs/essentials/spam-policies#machine-generated-traffic),
a site column query is a low reliability query, meaning that it may or may not return results
depending on, for example, what data center is serving the result. If I were you I'd use Search
Console for this, perhaps combined somehow with its API.

I have a High Search Volume, with a Top number 1 Keyword Ranking, and my CTR is just 0.8%. What
could be the reason for the low CTR? What's your suggestion?
------------------------------------------------------------------------------------------------------------------------------------------------------------

**John:** Rakesh asks, I have a High Search Volume, with a Top number 1 Keyword Ranking, and
my CTR is just 0.8%. What could be the reason for the low CTR? What's your suggestion?

Hey Rakesh, these are all interesting metrics to look at and to track, but to be quite honest,
they're not a great way of looking at the usefulness of a website. Instead of looking at these
numbers, I'd recommend looking at the actual search results, considering what users might be
seeing there, and how your site fits in, also taking into account everything else on those search
results pages. This is not something that just numbers will be able to tell you — instead you
have to look at the details, and the bigger picture. Often it also makes sense to get thoughts
from folks who are not associated with your website. Don't make decisions purely on metrics like
these.

Can broken HTML and errors in browser console cause a negative impact on a website?
-----------------------------------------------------------------------------------

**Gary:** Nikola Donev is asking, can broken HTML and errors in browser console cause a
negative impact on a website?

Well, it depends what and how it is broken. If it's just a paragraph or similarly benign
element, it's unlikely it will negatively affect the site. If the head element is broken, that
might be bad. See our [documentation about using valid HTML](/search/docs/crawling-indexing/valid-page-metadata).

On some of my ecommerce category pages, is it OK to list (and link to) all products pages with
all variants for Googlebot but not to list all for humans?
---------------------------------------------------------------------------------------------------------------------------------------------------------

**John:** Fred asks, on some of my ecommerce category pages, is it OK to list (and link to)
all products pages with all variants for Googlebot but not to list all for humans?

Hi Fred, technically this would be considered [cloaking](/search/docs/essentials/spam-policies#cloaking)
and would be considered in violation of the web spam policies. That said, one way that you can
achieve something similar is to use Merchant Center to submit your product variants. Content
submitted like that will be visible as a product in Search, even if any associated URL is not
indexed for web Search. You can [submit products](/search/docs/specialty/ecommerce/share-your-product-data-with-google)
through Merchant Center either with a feed, a spreadsheet, or even manually — if you just
want to try things out.

The SEO Starter Guide specifically makes the statement "If your website includes pages that are
primarily about individual videos..." Can we have clarification on the meaning of this?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Gary:** Steve Crandall is asking, the SEO Starter Guide specifically makes the statement "If
your website includes pages that are primarily about individual videos..." Can we have
clarification on the meaning of this?

That just means that you should have a dedicated page for each video, where the video is the
main focus of the page. Most video results require that type of video page, including features
like Key Moments, the Live Badge, and other rich result formats. See our [video guidelines](/search/docs/appearance/video)
for more info that should be helpful.

Why would Google consider LinkedIn Pulse articles as an original publisher even though it was
published on our website first?
-----------------------------------------------------------------------------------------------------------------------------

**John:** Asif asks, why would Google consider LinkedIn Pulse articles as an original
publisher even though it was published on our website first?

Hey Asif, thanks for asking. First off, the search results are not an indication of what
Google's systems consider to be the original source. In general, when you syndicate or
republish your content across platforms, you're trading the extra visibility within that platform
with the possibility that the other platform will appear in the search results above your website.
In some cases, this might be fine, for example, if you want to drive awareness of your website or
business in other locations. In other cases, you might prefer to have only your website appear in
Search. Ultimately, this is a business decision on your end.
