---
title: "Measure pageviews"
source_url: "https://developers.google.com/analytics/devguides/collection/ga4/views?hl=en&client_type=gtag"
product: "Google Analytics 4"
section: "Collection (gtag)"
language: en
scraped_date: 2026-06-08
doc_id: "google-analytics/collection-ga4/views.md"
---
Whenever someone loads a page of your website or their browser history state is
changed by the active site, an [enhanced measurement
event](//support.google.com/analytics/answer/9216061#page_view) called
`page_view` is sent from your website to Google Analytics. Since the event is
sent automatically, you don't need to send pageview data to Analytics manually.

However, when you want to manually control how pageviews are sent (e.g.
single-page applications or infinite scrolling), you can disable pageviews and
then manually send them from your website. Learn how to [Measure single-page
applications](/analytics/devguides/collection/ga4/single-page-applications).

This document describes the default pageview behavior and then how to send your
own pageviews manually.

For information about how to measure screenviews on a mobile app, see [Measure
screenviews](//firebase.google.com/docs/analytics/screenviews) instead.

gtag.js
Tag Manager

Before you begin
----------------

This guide assumes that you've done the following:

* [Create a Google Analytics account and property](https://support.google.com/analytics/answer/9304153#account). This step automatically
  creates a Google tag for you.
* [Create a web data stream for your website](https://support.google.com/analytics/answer/9304153#stream&zippy=%2Cweb)
* [Place the Google tag snippet on your website](https://support.google.com/analytics/answer/9304153#add-tag&zippy=%2Cadd-the-google-tag-directly-to-your-web-pages)

It also assumes that you have the following:

* Access to your website source code
* The Editor (or above) role to the Google Analytics account

Default behavior
----------------

When you add the Google tag (gtag.js) to your site, the snippet includes a
`config` command that sends a pageview by default. You can include additional
`<parameters>` with information about the pageview in order to specify how
Google Analytics is initialized:

```
gtag('config', 'TAG_ID', <parameters>);
```

When customizing the pageview behavior, the following keys may be used:

| Name | Type | Required | Default value | Description |
| --- | --- | --- | --- | --- |
| `page_title` | `string` | No | [document.title](https://developer.mozilla.org/docs/Web/API/Document/title) | The title of the page. |
| `page_location` | `string` | No | [location.href](https://developer.mozilla.org/docs/Web/API/Location/href) | The URL of the page.  If you override `page_location`, the value must start with the protocol followed by the full URL; for example, https://www.example.com/contact-us-submitted. **Note:** The default value excludes the fragment portion of the URL. |
| `send_page_view` | `boolean` | No | `true` | Whether or not a pageview should be sent. |

For example, the following overrides the page\_title values:

```
gtag('config', 'TAG_ID', {
  'page_title' : 'homepage'
});
```

Manual pageviews
----------------

When you want to manually control how pageviews are sent (e.g. single-page
applications or infinite scrolling), do the following:

1. [Disable pageview measurement](#disable_pageview_measurement)
2. [Send the `page_view` event when appropriate](#page_view_event)

**Caution:** If you send manual pageviews without disabling pageview measurement,
you may end up with duplicate pageviews.

### Disable pageview measurement

To disable the default `page_view` event that is sent by the `config` command
when the Google tag loads, set the `send_page_view` parameter to `false` in the
Google tag snippet:

```
    gtag('config', 'TAG_ID', {
      send_page_view: false
    });
```

The `send_page_view` setting in the `config` command does not persist across
pages. This setting must be repeated on every page of your website where you
want to disable the automatic pageview on tag load.

### Disable page changes based on browser history events

If Enhanced Measurement is enabled, Google Analytics
will send `page_view` events based on browser history changes even if you set
`send_page_view: false`. By default, Enhanced Measurement listens for history
events, like those used in single-page applications, and sends `page_view`
events independently of the `send_page_view` parameter in the `config` command.

To prevent `page_view` events from being sent due to history changes, you must
also configure the Enhanced Measurement settings within your Google Analytics property.
You can disable the "Page changes based on browser history events" option under
Enhanced Measurement settings for your web data stream. Learn more about
[Enhanced measurement events](//support.google.com/analytics/answer/9216061).

### Manually send `page_view` events

Where appropriate, make the following `gtag` call, replacing placeholder values
as necessary:

```
gtag('event', 'page_view', {
  page_title: '<Page Title>',
  page_location: '<Page Location>'
});
```
