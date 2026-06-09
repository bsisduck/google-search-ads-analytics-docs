---
title: "Google Analytics for websites"
source_url: "https://developers.google.com/analytics/devguides/collection/ga4/web?hl=en&client_type=gtag"
product: "Google Analytics 4"
section: "Collection (gtag)"
language: en
scraped_date: 2026-06-08
doc_id: "google-analytics/collection-ga4/web.md"
---
This page explains Google Analytics for websites, and what you need to do to get
started.

Google Analytics measures events to help you learn about your performance. For
example, you can use Google Analytics to measure web traffic, insights about
your audience, and how they interact with your website.

**Tip:** Before you begin, read about the [tagging options for
developers](/analytics/devguides/collection/ga4/tag-options).

Here's a high-level overview of the process:

![Google Analytics web setup flow](https://developers.google.com/analytics/devguides/collection/ga4/img/web-setup-flow.png)

Set up your account
-------------------

Here's an overview of the steps to set up your Google Analytics account for data
collection:

1. If you don't already have one, [create a Google Analytics
   account](//support.google.com/analytics/answer/9304153#account).
2. After creating an account, [create a new
   property](//support.google.com/analytics/answer/9304153#property&zippy=%2Cweb).
   Properties are like containers that hold the data you collect.
3. Once you've created a new property, [add a web data stream](//support.google.com/analytics/answer/9304153#stream&zippy=%2Cweb)
   that sends the data from your website to the property.

Tag your website
----------------

Once you have a Google Analytics account with a web data stream, you're ready to
tag your site and start collecting data.

We recommend that you [use Google Tag
Manager](//support.google.com/tagmanager/answer/14842164). With
Tag Manager, you can make changes to your tagging configuration and push them to
your site automatically, without needing to change your code every time.

For information on other tagging options, see [tagging
for Google Analytics](/analytics/devguides/collection/ga4/tag-options).
