---
title: "Validate events"
source_url: "https://developers.google.com/analytics/devguides/collection/protocol/ga4/validating-events?hl=en&client_type=gtag"
product: "Google Analytics 4"
section: "Measurement Protocol"
language: en
scraped_date: 2026-06-08
doc_id: "google-analytics/measurement-protocol/validating-events.md"
---
Choose your platform:

Firebase
gtag.js

The Google Analytics Measurement Protocol does not return
`HTTP` error codes, even if an event is malformed or missing required
parameters. To verify your events are valid, you should test them against the
Measurement Protocol validation server before deploying them to production.
After you have validated that your events are structured properly, you should
[verify your implementation](/analytics/devguides/collection/protocol/ga4/verify-implementation) to make sure you're using the correct keys.

**Caution:** The validation server does *not* validate the `api_secret` or
`measurement_id`.
Carefully review those values to
make sure they are correct.

You can either call the validation server directly, or use the [Google Analytics
Event Builder](https://ga-dev-tools.web.app/ga4/event-builder/). The Google Analytics Event Builder lets you interactively
construct events, and uses the Measurement Protocol validation server to
validate them.

This guide describes how to send events to the Measurement Protocol for Google
Analytics validation server and interpret the response.

**Important:** Events sent to the validation server don't show up in reports.

Send events for validation
--------------------------

The only difference in the request for events sent to the Measurement Protocol
and the Measurement Protocol validation server is the URL.

| Server | URL |
| --- | --- |
| Measurement Protocol | `/mp/collect` |
| Measurement Protocol validation server | `/debug/mp/collect` |

All other [request fields](/analytics/devguides/collection/protocol/ga4/reference) are the same.

We recommend the following approach to validation:

* Use strict validation checks during development using either of the following
  options:
  + Validate requests with the [Event Builder](//ga-dev-tools.google/ga4/event-builder/).
  + Send requests to the validation server with `validation_behavior` set to
    `ENFORCE_RECOMMENDATIONS`.
* In production, send requests without `validation_behavior` set to minimize the
  data rejected by the Measurement Protocol.

### Example of an invalid event

The following code shows an invalid event being sent to the Measurement Protocol
validation server:

```
const measurementId = "MEASUREMENT_ID";
const apiSecret = "API_SECRET";

fetch(`https://www.google-analytics.com/debug/mp/collect?measurement_id=${measurementId}&api_secret=${apiSecret}`, {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    client_id: "CLIENT_ID",
    validation_behavior: "ENFORCE_RECOMMENDATIONS",
    events: [{
      // Event names must start with an alphabetic character.
      name: "_badEventName",
      params: {},
    }]
  })
});
```

### Example of a valid event

The following code shows a valid event being sent to the Measurement Protocol
validation server. This request would yield an empty `validationMessages` array
in the response, as shown in the [Validation response](#validation-response)
section.

```
const measurementId = "MEASUREMENT_ID";
const apiSecret = "API_SECRET";

fetch(`https://www.google-analytics.com/debug/mp/collect?measurement_id=${measurementId}&api_secret=${apiSecret}`, {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    client_id: "CLIENT_ID",
    validation_behavior: "ENFORCE_RECOMMENDATIONS",
    events: [{
      name: "level_up",
      params: {
        level: 2,
        character: "MyHero"
      },
    }]
  })
});
```

**Tip:** If you want your data to be collected in the EU, change the URL passed to
the `fetch` method to begin with `https://region1.google-analytics.com` instead
of `https://www.google-analytics.com`.

Validation response
-------------------

Here's the validation server's response to the invalid event example.

```
{
  "validationMessages": [
    {
      "fieldPath": "events",
      "description": "Event at index: [0] has invalid name [_badEventName]. Names must start with an alphabetic character.",
      "validationCode": "NAME_INVALID"
    }
  ]
}
```

Here's the validation server's response to a request with no validation issues:

```
{
  "validationMessages": []
}
```

### Response

| Key | Type | Description |
| --- | --- | --- |
| `validationMessages` | Array<[ValidationMessage](#validation_message)> | An array of validation messages. |

### ValidationMessage

| Key | Type | Description |
| --- | --- | --- |
| `fieldPath` | string | The path to the field that was invalid. |
| `description` | string | A description of the error. |
| `validationCode` | [ValidationCode](#validation_code) | A validation code that corresponds to the error. |

### ValidationCode

| Value | Description |
| --- | --- |
| `VALUE_INVALID` | The value provided for a `fieldPath` was invalid. See [limitations](/analytics/devguides/collection/protocol/ga4/sending-events#limitations). |
| `VALUE_REQUIRED` | A required value for a `fieldPath` was not provided. |
| `NAME_INVALID` | The name provided was invalid. See [limitations](/analytics/devguides/collection/protocol/ga4/sending-events#limitations). |
| `NAME_RESERVED` | The name provided was one of the reserved names. See [reserved names](/analytics/devguides/collection/protocol/ga4/reference#reserved_names). |
| `VALUE_OUT_OF_BOUNDS` | The value provided was too large. See [limitations](/analytics/devguides/collection/protocol/ga4/sending-events#limitations). |
| `EXCEEDED_MAX_ENTITIES` | There were too many parameters in the request. See [limitations](/analytics/devguides/collection/protocol/ga4/sending-events#limitations). |
| `NAME_DUPLICATED` | The same name was provided more than once in the request. |
