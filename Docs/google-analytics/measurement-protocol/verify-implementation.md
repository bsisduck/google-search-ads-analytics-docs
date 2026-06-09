---
title: "Verify implementation"
source_url: "https://developers.google.com/analytics/devguides/collection/protocol/ga4/verify-implementation?hl=en&client_type=gtag"
product: "Google Analytics 4"
section: "Measurement Protocol"
language: en
scraped_date: 2026-06-08
doc_id: "google-analytics/measurement-protocol/verify-implementation.md"
---
After going through [validating events](/analytics/devguides/collection/protocol/ga4/validating-events), you'll want to verify your
implementation. The validation server validates that your events have the
correct structure, but to verify that they are being sent correctly to your
property, you'll need to do the following:

* [Send an event from a client](#client_send)
* [Send an event to your property](#send)
* [Check the Realtime view](#realtime)
* [Check DebugView](#debugview)

If you're not seeing your events after going through these steps, check
[troubleshooting](/analytics/devguides/collection/protocol/ga4/troubleshooting) for common implementation errors.

Send an event from a client
---------------------------

Choose your client:

Firebase
gtag.js

In order for an event to be valid, it must have a `client_id` that has already
been used to send an event from `gtag.js`. Capture this ID
client-side, and include it in your call to the Measurement Protocol. In
[send an event to your property](#send), we use `"client_id"` as the
`client_id`. You must replace `"client_id"` with a real `client_id`
from `gtag.js`.

Send an event to your property
------------------------------

After you have sent an event from a client and captured a valid `client_id`,
you'll be ready to send an event using the Measurement Protocol. When verifying
your implementation, you should send the exact event that you're trying to
measure using the Measurement Protocol.

For example, the following sends a [refund](/analytics/devguides/collection/protocol/ga4/reference/events#refund) event:

```
const measurementId = "MEASUREMENT_ID";
const apiSecret = "API_SECRET";

fetch(`https://www.google-analytics.com/mp/collect?measurement_id=${measurementId}&api_secret=${apiSecret}`, {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    "client_id": "CLIENT_ID",
    "events": [{
      "name": "refund",
      "params": {
        "currency": "USD",
        "value": "9.99",
        "transaction_id": "ABC-123"
      }
    }]
  })
});
```

Check the Realtime view
-----------------------

After sending an event using the Measurement Protocol, check the Realtime view
for your property. Events typically show up within a few seconds.

Go to the Realtime view by opening [Google Analytics](https://analytics.google.com), then going to
**Reports** > **Realtime** in the left navigation. You'll want to focus on the
bottom charts, such as "Event count by Event name" and "Key Events by Event
name."

![Realtime view showing an event](/static/analytics/devguides/collection/protocol/ga4/img/refund-realtime.png)

Check DebugView
---------------

If the Realtime view doesn't provide enough detail for you to verify your
implementation, enable debug mode in some test events by including the following
parameters in the `params` collection so you can monitor and review the events
in **DebugView**:

1. `"debug_mode": true` or `"debug_mode": 1`
2. `"engagement_time_msec"` set to a positive number

For example, the following sends a [refund](/analytics/devguides/collection/protocol/ga4/reference/events#refund) with debug mode enabled:

```
const measurementId = "MEASUREMENT_ID";
const apiSecret = "API_SECRET";

fetch(`https://www.google-analytics.com/mp/collect?measurement_id=${measurementId}&api_secret=${apiSecret}`, {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    "client_id": "CLIENT_ID",
    "events": [{
      "name": "refund",
      "params": {
        "currency": "USD",
        "value": "9.99",
        "transaction_id": "ABC-123",
        "engagement_time_msec": 1200,
        "debug_mode": true
      }
    }]
  })
});
```

After you send events with debug mode enabled, follow the instructions for
[monitoring events using **DebugView**](//support.google.com/analytics/answer/7201382) to verify your implementation.
