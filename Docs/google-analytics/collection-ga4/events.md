---
title: "Set up events"
source_url: "https://developers.google.com/analytics/devguides/collection/ga4/events?hl=en&client_type=gtag"
product: "Google Analytics 4"
section: "Collection (gtag)"
language: en
scraped_date: 2026-06-08
doc_id: "google-analytics/collection-ga4/events.md"
---
Events let you measure user interactions on your website or app; for example,
you can measure when someone loads a page, clicks a link, and makes a purchase.
Google Analytics uses data from events to create reports with information about
your business. [Learn more](//support.google.com/analytics/answer/9322688)

Event types
-----------

Google Analytics events are grouped into four categories:

| Event Type | Link | Setup Needed? | Description & Use Case |
| --- | --- | --- | --- |
| **Automatically collected** | [Learn more](//support.google.com/analytics/answer/9234069) | **No** | Collected by default when you set up the Google Analytics tag on your site or app. Examples include `first_visit`, `session_start`, and `user_engagement`. |
| **Enhanced measurement** | [Learn more](//support.google.com/analytics/answer/9216061) | **No** (typically) | Collected automatically when enhanced measurement is enabled in the Google Analytics UI. Measures common web interactions like `scroll`, `click`, and `file_download`. |
| **Recommended** | [Recommended Events Reference](/analytics/devguides/collection/ga4/reference/recommended-events) | **Yes** | Standardized events for different business verticals (e.g., retail, travel, games) that unlock prebuilt reporting panels. Examples: `purchase`, `login`, `sign_up`. |
| **Custom** | [Learn more](//support.google.com/analytics/answer/12229021) | **Yes** | Events that you define yourself because no prepopulated automatic, enhanced, or recommended event fits your needs. Accessible using custom reports. |

This guide shows you how to set up [recommended events](//support.google.com/analytics/answer/9267735) and [custom events](//support.google.com/analytics/answer/12229021) on
your website using the Google tag (gtag.js) or Google Tag Manager. You don't
need to set up [automatically collected](//support.google.com/analytics/answer/9234069) and [enhanced measurement](//support.google.com/analytics/answer/9216061) events.

Audience
--------

You've set up Google Analytics and are starting to see data in your reports, but
you want to collect more information than what Analytics collects automatically,
or you want to unlock certain features and capabilities in Analytics.

**Note:** For information on events in 360, see [Google Analytics
360](//support.google.com/analytics/answer/11202874).

gtag.js
Tag Manager

Before you begin
----------------

This guide assumes that you've done the following:

* [Create a Google Analytics account and property](//support.google.com/analytics/answer/9304153#account)
* [Create a web data stream for your website](//support.google.com/analytics/answer/9304153#stream&zippy=%2Cweb)
* [Place the Google tag on your website](//support.google.com/analytics/answer/9304153#add-tag&zippy=%2Cadd-the-google-tag-directly-to-your-web-pages)

It also assumes that you have the following:

* Access to your website source code
* The [Editor](//support.google.com/analytics/answer/9305587), or higher, role to the Google Analytics account

Google tag (gtag.js) overview
-----------------------------

Use [the Google tag (gtag.js) API](/tag-platform/gtagjs/reference) to send
events to Google Analytics. The API has one function called `gtag()`, and
whenever you want to send an event to Google Analytics, you use the following
syntax:

```
gtag('event', '<event_name>', {
  <event_parameters>
});
```

In this example, the `gtag()` function includes the following:

* An `event` command that tells Google that you are sending an event
* The name of the recommended or custom event
* (Optional) A collection of [parameters](/analytics/devguides/collection/ga4/event-parameters) that provide additional information
  about the event

For example, the following is a recommended event called `screen_view` with two
parameters:

```
gtag('event', 'screen_view', {
  'app_name': 'myAppName',
  'screen_name': 'Home'
});
```

Add events to your JavaScript
-----------------------------

`gtag()` is a JavaScript function so you need to add the function to the
JavaScript on your web page. For example, you could add the function within your
`<script>` tags or in a separate JavaScript file that you import into your HTML
page.

You can add events to your JavaScript anywhere **below** the Google tag snippet.
Google won't process data from events that you place above the Google tag
snippet. For example, the following sample code includes a recommended event
called `screen_view` and a custom event called `signup_newsletter` within a
`<script>` tag:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'G-XXXXXXXXXX');
    </script>

    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Title of the page</title>
</head>
<body>
    <p>Welcome to my website!</p>
    
    <script>
      /**
      *   The following events are sent when the page loads. You send
      *   recommended and custom events the same way. You could wrap
      *   the events in JavaScript functions so they are sent when
      *   users perform specific actions.
      */
      gtag('event', 'screen_view', {
        'app_name': 'myAppName',
        'screen_name': 'Home'
      });
      gtag('event', 'signup_newsletter', {
        'method': 'web'
      });
    </script> 
</body>
</html>
```

If you want to send the event based on a button click (or some other user
action), you can add some additional JavaScript to your event.

See your events in Analytics
----------------------------

You can see your events and their parameters using the [*Realtime*](//support.google.com/analytics/answer/9271392) and
[*DebugView*](//support.google.com/analytics/answer/7201382) reports. Note that the *DebugView* report requires some additional
configuration before you can use the report. These two reports show you the
events users trigger on your website as the events are triggered.

Next steps
----------

* [Set up event parameters](/analytics/devguides/collection/ga4/event-parameters) to add more information to your events.
* [Mark events as key events](//support.google.com/analytics/answer/9267568#mark).
