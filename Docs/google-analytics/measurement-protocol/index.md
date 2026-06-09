---
title: "Measurement Protocol"
source_url: "https://developers.google.com/analytics/devguides/collection/protocol/ga4?hl=en&client_type=gtag"
product: "Google Analytics 4"
section: "Measurement Protocol"
language: en
scraped_date: 2026-06-08
doc_id: "google-analytics/measurement-protocol/index.md"
---
**Note:** The Measurement protocol is now in maintenance mode. No future
enhancements are planned. [Upgrade to the Data Manager
API](/data-manager/api/devguides/events/analytics/measurement-protocol/upgrade)
to future-proof your integration.

The Google Analytics Measurement Protocol enhances measurement for web and app
streams by [sending events](/analytics/devguides/collection/protocol/ga4/sending-events) directly to Google Analytics servers in
HTTP requests. You can record server-to-server and offline interactions, and
send them as Measurement Protocol events to Google Analytics, where they can be
viewed in [reports](/analytics/devguides/reporting/data/v1/basics).

**Key Point:** The intent of the Measurement Protocol is to augment automatic
collection through gtag, Tag Manager, and Google Analytics for Firebase, not to
replace it.

You must use tagging (gTag, Tag Manager, or Google Analytics for Firebase) to
use this protocol. See [key features](#key_features) for important information
on how this Measurement Protocol works with Google Analytics.

Use cases
---------

Here are some ways to use the Measurement Protocol:

* Tie online to offline behavior.
* Measure client-side and server-side interactions.
* Send events that happen outside standard user-interaction, like offline
  conversions.
* Send events from devices and apps where automatic collection isn't
  available, like kiosks and watches.

Read more about how to implement common use cases in the [use cases guide](/analytics/devguides/collection/protocol/ga4/use-cases).

Get started
-----------

See [send events](/analytics/devguides/collection/protocol/ga4/sending-events) to learn how to send events to Google Analytics using the
Measurement Protocol.

If you're implementing the Measurement Protocol for an app stream, you can start
with the [Send app events to Google Analytics using Measurement Protocol](//firebase.google.com/codelabs/firebase_mp)
codelab.

Architecture
------------

Here is an overview of the Measurement Protocol.

![sequence diagram of measurement protocol](/static/analytics/devguides/collection/protocol/ga4/img/mp_sequence_diagram.png)

Key features
------------

This section explains important information for using the Measurement Protocol.
You must use gTag, Tag Manager, or Google Analytics for Firebase for tagging to
use most of the Measurement Protocol features with Google Analytics.

### Remarketing

Same device remarketing is supported when [Google signals](//support.google.com/analytics/answer/9445345) is turned on. For
cross-device remarketing, a User ID is required.

### Advertising identifiers

Advertising identifiers such as GBRAID/WBRAID collected during online
interactions are automatically joined with Measurement Protocol events using `client_id`
or `app_instance_id`.

### Privacy settings

Measurement Protocol events are joined with online interactions using
`client_id` or `app_instance_id` to functionally adopt user privacy settings
such as "non personalized ads" and "limit ad tracking".

### Geographic and device information

Google Analytics automatically joins the most recent geographic and device
information from tagging with Measurement Protocol events using `client_id` or
`app_instance_id`. This ensures that your Measurement Protocol events are reflected in
reports that include geographic and device dimensions.

If you want a Measurement Protocol event to reflect geographic and device information
from a *specific* session instead of the latest information for the `client_id`
or `app_instance_id`, then include `session_id` in the event and send it to
Measurement Protocol within 24 hours of the start of the session.

You can provide [geographic information](/analytics/devguides/collection/protocol/ga4/reference#payload_geo_info) and [device information](/analytics/devguides/collection/protocol/ga4/reference#payload_device_info) for events
using the Measurement Protocol.

If device information isn't collected by your tag, it defaults to
`desktop` for Web streams, and `mobile` for App streams.

### Full server-to-server

While it's possible to send events to Google Analytics solely with the
Measurement Protocol, only partial reporting may be available. The purpose of the
Measurement Protocol is to augment existing events collected using gtag, GTM, or
Firebase. Some event and parameter names are [reserved](/analytics/devguides/collection/protocol/ga4/reference?#reserved_names) for use through
automatic collection and cannot be sent through the Measurement Protocol.

### Generate or rename events

Rules for [generating or renaming
events](//support.google.com/analytics/answer/10085872) aren't triggered by
events sent with the Measurement Protocol. Your application should implement the logic
to send custom events through the Measurement Protocol, similar to the rules configured
in the Google Analytics UI.

Next steps
----------

* Learn how to [send events](/analytics/devguides/collection/protocol/ga4/sending-events) using the Measurement Protocol.
* Validate your event payloads using the [Measurement Protocol validation
  server](/analytics/devguides/collection/protocol/ga4/validating-events).
* Check out the [protocol](/analytics/devguides/collection/protocol/ga4/reference) and [event](/analytics/devguides/collection/protocol/ga4/reference/events) reference.

**Note:** All applications that use the Measurement Protocol must follow the
[protocol policy](/analytics/devguides/collection/protocol/ga4/policy)
