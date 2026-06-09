---
title: "Set up event parameters"
source_url: "https://developers.google.com/analytics/devguides/collection/ga4/event-parameters?hl=en&client_type=gtag"
product: "Google Analytics 4"
section: "Collection (gtag)"
language: en
scraped_date: 2026-06-08
doc_id: "google-analytics/collection-ga4/event-parameters.md"
---
This guide shows you how to set up parameters for [recommended events](//support.google.com/analytics/answer/9267735) and
[custom events](//support.google.com/analytics/answer/12229021) on your website so you can collect more information from your
events. For information about how to add item-scoped parameters, see
[Measure ecommerce](/analytics/devguides/collection/ga4/ecommerce#implementation).

Audience
--------

You want to collect more information about your users' activity through the
events you've already set up.

You use either the Google tag (gtag.js) or Google Tag Manager on your website.
If you want to set up event parameters for a mobile app, see [Log events](//firebase.google.com/docs/analytics/events).

gtag.js
Tag Manager

Before you begin
----------------

This guide assumes that you've done the following:

* [Create a Google Analytics account and property](//support.google.com/analytics/answer/9304153#account)
* [Create a web data stream for your website](//support.google.com/analytics/answer/9304153#stream&zippy=%2Cweb)
* [Place the Google tag snippet on your website](//support.google.com/analytics/answer/9304153#add-tag&zippy=%2Cadd-the-google-tag-directly-to-your-web-pages)

It also assumes that you have the following:

* Access to your website source code
* The Editor (or above) role to the Google Analytics account

You should also read [Set up events](/analytics/devguides/collection/ga4/events) before reading this guide.

Understand event parameters
---------------------------

Parameters provide additional information about the ways users interact with
your website. For example, when someone views a product you sell, you can
include parameters that describe the product they viewed, such as the name,
category, and price.

The automatically collected and enhanced measurement events include parameters
by default. Google also provides a set of required and optional parameters to
include with each recommended event. Additionally, you can add more event
parameters when you need them.

Set up event parameters
-----------------------

Events have the following structure, where `<event_parameters>` are your event
parameters, written as key-value pairs:

```
gtag('event', '<event_name>', {
  <event_parameters>
});
```

Consider the following example:

```
gtag('event', 'screen_view', {
  'app_name': 'myAppName',
  'screen_name': 'Home'
});
```

In this example:

* `app_name` and `screen_name` are event parameter names
* `myAppName` and `Home` are event parameter values

> **Important: Register custom parameters**
>
> Sending custom parameters in your code is only the first step. For Google
> Analytics to display and allow you to analyze data from any **custom
> parameters** in standard reports and explorations, you **must register them as
> custom dimensions or metrics** within the Google Analytics interface.
> Without this registration, the parameter data is collected but isn't
> available for reporting.
>
> [Learn more about custom dimensions and metrics](//support.google.com/analytics/answer/14240153).

Set up parameters for every event
---------------------------------

The examples in the previous section use the `event` command in a [`gtag()`](/tag-platform/gtagjs/reference)
function to send parameters for one event. You can also update the [`config`](/tag-platform/gtagjs/reference#config)
command in the Google tag snippet (in your `<head>` HTML tag) to send parameters
with every event on the page.

The following sets the page title and then sends the parameter with every event
on the page:

```
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());

gtag('config', 'G-XXXXXXXXXX', {
  'page_title': 'Contact Us',
  'currency': 'EUR'
});
</script>
```

If you add more than one tag ID to your page, use the `set` command for
**documented global parameters** (such as `user_id`, `page_title`, `currency`)
so all IDs inherit the values. Place the `set` command **above** the `config`
command.

**Note:** For custom event parameters, we recommend using `config` or `event`
commands. The `set` command may not reliably propagate custom parameters to all
Google Analytics measurement streams.

```
gtag('set', {
  'page_title': 'Travel Destinations',
  'currency': 'USD'
});
// Place your config commands after the set command like follows
gtag('config', 'G-XXXXXXXXXX-1');
gtag('config', 'G-XXXXXXXXXX-2');
gtag('config', 'G-XXXXXXXXXX-3');
```

See your events in Analytics
----------------------------

You can verify that your events and parameters are being sent correctly by using
the [*Realtime*](//support.google.com/analytics/answer/9271392) and [*DebugView*](//support.google.com/analytics/answer/7201382) reports. These reports show data as it
arrives. Note that the *DebugView* report requires some
[additional configuration](//support.google.com/analytics/answer/7201382#enable) before you can use it.

However, to see and analyze the values of any **custom parameters** you send
within the broader Google Analytics reporting interface (such as in Explorations
or standard reports), you **must first register them as custom dimensions or
metrics**. After you register a custom dimension or metric, it can take up to 48
hours for the data to become available in your reports.

[Learn about custom dimensions and metrics](//support.google.com/analytics/answer/14240153).

### Verify in DebugView

When using the [*DebugView*](//support.google.com/analytics/answer/7201382) report, parameters defined with `gtag('set')` are
applied to all subsequent `gtag('event')` invocations on the page. To verify,
make sure the `gtag('set')` command is executed **before** the event fires.
Then, select an event in DebugView and examine its **Parameters** tab to see the
merged list of parameters, including those globally set.

Some parameters automatically populate prebuilt [dimensions and metrics](//support.google.com/analytics/answer/9143382) in
Google Analytics. For example, the parameters on the automatically collected
and enhanced measurement events, as well as the required and optional parameters
you send with the recommended events, populate prebuilt dimensions and metrics.

Other parameters require you to create [custom dimensions and metrics](//support.google.com/analytics/answer/10075209) to
see the parameter values in Google Analytics.

**Important:** To analyze custom parameters in Google Analytics reports, you must
first register them as custom dimensions or metrics. This step is required
regardless of whether the parameters are sent using `gtag('event')`,
`gtag('config')`, or `gtag('set')`.

Next steps
----------

[Create custom dimensions and metrics](//support.google.com/analytics/answer/10075209) for your custom event parameters.
