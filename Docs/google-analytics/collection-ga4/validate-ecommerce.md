---
title: "Validate your ecommerce setup (gtag.js)"
source_url: "https://developers.google.com/analytics/devguides/collection/ga4/validate-ecommerce?hl=en&client_type=gtag"
product: "Google Analytics 4"
section: "Collection (gtag)"
language: en
scraped_date: 2026-06-08
doc_id: "google-analytics/collection-ga4/validate-ecommerce.md"
---
This document provides an overview on how to validate that Analytics is
collecting ecommerce events from your website when you use gtag.js. The document
assumes that you've read [Measure ecommerce](/analytics/devguides/collection/ga4/ecommerce?client_type=gtag).

**Got 3 mins?** Help us improve the Google Analytics ecommerce documentation
by taking [a quick online survey](https://forms.gle/ab1ADpfw6xZEkFAC6).

See ecommerce events in real time
---------------------------------

Once you add ecommerce events to your website and begin to trigger the events,
use [the DebugView report](https://support.google.com/analytics/answer/7201382) to validate that Analytics has received the ecommerce
events and event parameters. The DebugView report lets you see each event-level
and item-level parameter that Analytics collects from your website.

The DebugView report continuously streams events and displays the event name
each time an event is collected. To see the parameters associated with an event,
click the name of the event. If you've included an `items` array, you will see
an additional tab for the items sent with the event.

Troubleshoot missing ecommerce events
-------------------------------------

The following describes possible reasons why you don't see an ecommerce event in
Analytics.

### Check the commas

You must include a comma after every parameter value. Analytics ignores
ecommerce events that have a parameter with a missing comma, as well as any
other events that come after the ignored event. For example, the following event
isn't collected:

```
gtag("event", "refund", {
  currency: "USD",
  transaction_id: "T_12345" // Missing a trailing comma
  value: 30.03,
  coupon: "SUMMER_FUN",
  shipping: 3.33,
  tax: 1.11
});
```

### Check the placement

You must place ecommerce events in JavaScript rather than HTML, and your events
must go after the Google tag rather than before the Google tag.

**Good:**

```
<body>
  <p>Hello, World!</p>
  <script>
    gtag("event", "<event-name>");
  </script>
</body>
```

**Good:**

```
<body>
  <p>Hello, World!</p>
  <script src="my_events.js"></script>
</body>
```

**Bad:**

```
<body>
  <p>Hello, World!</p>
  gtag("event", "<event-name>");
</body>
```

**Bad:**

```
<head>
  <script>
    gtag("event", "<event-name>");
  </script>
  <!-- the Google tag -->
</head>
```

### Check the event syntax

The following `purchase` event uses the correct syntax:

```
gtag('event', 'purchase', {
    transaction_id: "T_12345",
    value: 72.05,
    currency: "USD",
    items: [
     {
      item_id: "SKU_12345",
      item_name: "Stan and Friends Tee",
     },
     {
      item_id: "SKU_12346",
      item_name: "Google Grey Women's Tee",
     }]
});
```

Check that the separators in your event are correctly placed:

* Parentheses after `gtag` and before the closing semicolon
* Curly brackets before and after event parameters
* Square brackets before and after item-scoped event parameters

Additionally, make sure you include all of the [required event parameters](/analytics/devguides/collection/ga4/reference/events). If
you don't include a required parameter, you will still see the event and
parameters in Google Analytics, but Analytics will treat the event as a custom
event rather than an ecommerce event.

**Note:** The order of the parameters does not matter. You can send them in any
order.

### Check the event name

When setting up ecommerce events, make sure you use the correct recommended
event name. For example, use the event name "add\_to\_cart" rather than
"add\_to\_basket" to ensure that Analytics registers the event as one of the
recommended ecommerce events. Additionally, make sure you spell the event names
correctly and don't have any typos.

### Check the transaction ID

If the same ecommerce event is triggered twice with the same [transaction ID](https://support.google.com/analytics/answer/12313109),
Google Analytics will only collect the first event and ignore the second event,
even if you changed some of the values in the new event.

If you don't see an ecommerce event while testing, try changing the transaction
ID or removing the transaction ID during testing so you see each version of the
event.

Troubleshoot duplicate ecommerce events
---------------------------------------

The following describes a possible reason why you see duplicate ecommerce events
in Analytics.

### Use one tag on every page

Make sure you add the Google tag snippet to every page of your website.
Additionally, make sure you use the Google tag (gtag.js) or Google Tag Manager,
but not both. Using both options will double count certain events and have other
unintended consequences.
