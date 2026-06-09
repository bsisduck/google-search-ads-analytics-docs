---
title: "Tagging for Google Analytics"
source_url: "https://developers.google.com/analytics/devguides/collection/ga4/tag-options?hl=en&client_type=gtag"
product: "Google Analytics 4"
section: "Collection (gtag)"
language: en
scraped_date: 2026-06-08
doc_id: "google-analytics/collection-ga4/tag-options.md"
---
This page provides an overview of the tagging options you can use to measure
activity on your site and send the data to Google Analytics. The Google tag is
designed for measurement across many Google products, including Google Ads. We
recommend [using Tag Manager to get
started](//support.google.com/tagmanager/answer/14842164).

For details on the Google tag, Tag Manager and gtag.js products, see the [Tag
platform documentation](/tag-platform/devguides).

The Google tag
--------------

The Google tag is a single tag you can add to your website to measure organic
and ad performance. You can configure a Google tag for Google Analytics, and
send the data from that tag to other products, like Google Ads, by adding
[destinations](//support.google.com/tagmanager/answer/12324388) to your tag.

To send data from a Google tag to your Google Analytics account, you need to
accept the Google Analytics Terms of Service (ToS).

To get started with the Google tag for Google Analytics, we recommend using
[Google Tag Manager](//support.google.com/tagmanager/answer/9442095).

**Note:** The **Google Analytics: GA4 Configuration tag** is now the Google tag. If
you were using Google Analytics configuration tags, they have been automatically
upgraded to the Google tag. Your measurement and capabilities haven't changed,
and you don't need to take any action. Your Google Analytics event tags stay the
same.

Google Tag Manager
------------------

[Google Tag Manager](//support.google.com/tagmanager/answer/6102821) is a
web-based tag management system, that lets you create Google tags and install
them on your website, without manually adding JavaScript snippets to your site.
You can also update the settings for tags that are already in use on your site
in Tag Manager, without needing to re-deploy your site each time.

Google Tag Manager supports the Google tag you need for Google Analytics, a wide
array of third-party tags, and even custom tags.

[Set up and install Tag Manager](//support.google.com/tagmanager/answer/14842164)

gtag.js
-------

If you use Google Tag Manager, you don't need to add gtag.js snippets to your
site.

gtag.js is a JavaScript framework you can use to add Google tags to web pages.
To use gtag.js effectively, you need to be proficient in HTML, CSS, and
JavaScript.

**Note:** gtag.js doesn't support third-party or custom tags, and can only send data
to Google services.

You can [migrate](/tag-platform/tag-manager/web/migrate) your tags to Google Tag
Manager from gtag.js if needed.

### gtag.js cookie usage

For the latest information on cookie usage in Google Analytics, see [Cookie
usage on websites](//support.google.com/analytics/answer/11397207).

The gtag.js JavaScript library uses
*first-party* cookies to do the following:

* Distinguish unique users.
* Distinguish sessions for a user.

When using the recommended JavaScript snippet, cookies are set at the highest
possible domain level. For example, if your website address is
`blog.example.co.uk`, gtag.js sets the cookie domain to `.example.co.uk`.
Setting cookies on the highest level domain possible lets measurement occur
across subdomains without extra configuration.

**Note:** gtag.js doesn't require setting cookies to transmit data to Google
Analytics.

gtag.js sets the following cookies:

| Cookie name | Default expiration time | Description |
| --- | --- | --- |
| `_ga` | 2 years | Used to distinguish users. |
| `_ga_<container-id>` | 2 years | Used to persist session state. |

### Customization

To learn how you can customize the default cookie settings using gtag.js, see
[Cookies and user identification
guide](/tag-platform/security/concepts/cookies).

Google Tag Manager versus gtag.js
---------------------------------

Here's an overview of the differences between gtag.js and Tag Manager for Google
Analytics.

The following table highlights the differences between gtag.js and Tag Manager
for Google Analytics.

| `gtag.js` (code deployment) | Google Tag Manager (Tag Management System) |
| --- | --- |
| You need to write code to deploy tags and customize your web collection | Deploy and modify both tags from Google and third-parties on the fly **without editing code**. [See all supported tags](//support.google.com/tagmanager/answer/6106924) |
| Can only send data for Google products. | Can send data for Google tags, third party tags, and custom tags. |
| You need to manage your tags from within your code, and may need to duplicate code for different outlets, for example, web and app. | Manage tags for your website and apps all from [tagmanager.google.com](https://tagmanager.google.com) |
| Version control depends on how you manage your code. | Collaborate with others using workspaces, and version control tags. |
| Server-side tagging is possible. You still need to use Google Tag Manager to deploy and interact with your server container. | Tag Manager helps you deploy tags on a server. If you are exploring this option, read [Client-side and server-side tagging](//support.google.com/tagmanager/answer/13387731). |
| Compatible with static-site generators, CMSs, website builders or manually authored HTML pages that support JavaScript. | Compatible with many CMSs and website builders. If your system doesn't support Tag Manager, use the Google tag (`gtag.js`) instead. |
| Cost: Free | Cost: Free |
