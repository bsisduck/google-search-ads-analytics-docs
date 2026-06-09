---
title: "Measure exceptions"
source_url: "https://developers.google.com/analytics/devguides/collection/ga4/exceptions?hl=en&client_type=gtag"
product: "Google Analytics 4"
section: "Collection (gtag)"
language: en
scraped_date: 2026-06-08
doc_id: "google-analytics/collection-ga4/exceptions.md"
---
You can send exception events to measure the number and type of crashes or
errors that occur on a web page. This page describes how to use gtag.js to send
exceptions to Google Analytics.

Implementation
--------------

When an error occurs, send an exception event to Google Analytics:

```
gtag('event', 'exception', {<exception_parameters>});
```

where `<exception_parameters>` is one or more parameter-value pairs. Separate
each pair by a comma. For example, this command sends a nonfatal error
exception.

```
gtag('event', 'exception', {
  'description': 'error_description',
  'fatal': false   // set to true if the error is fatal
});
```

Exception parameters
--------------------

The following table lists the exception parameters:

| Parameter name | Data type | Required | Description |
| --- | --- | --- | --- |
| `description` | string | No | A description of the error. |
| `fatal` | boolean | No | `true` if the error was fatal. |

Example
-------

Given the following function:

```
function divide(x, y) {
  if (y === 0) {
    throw "Division by zero";
  }
  return x/y;
}
```

the following code will send an exception event to Google Analytics if the
divisor y is zero:

```
var x = document.getElementById('x').value;
var y = document.getElementById('y').value;

try {
  var r = divide(x, y);
} catch(err) {
  gtag('event', 'exception', {
    'description': err,
    'fatal': false
  });
}
```
