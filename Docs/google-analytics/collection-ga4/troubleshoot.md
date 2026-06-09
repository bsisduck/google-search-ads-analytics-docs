---
title: "Verify and troubleshoot your Google Analytics setup"
source_url: "https://developers.google.com/analytics/devguides/collection/ga4/troubleshoot?hl=en&client_type=gtag"
product: "Google Analytics 4"
section: "Collection (gtag)"
language: en
scraped_date: 2026-06-08
doc_id: "google-analytics/collection-ga4/troubleshoot.md"
---
This guide helps you confirm that your Google Analytics tag is correctly
installed and sending data, and provides steps to diagnose common issues if
you're not seeing the data you expect.

Immediate verification methods
------------------------------

These tools help you check if your tag is firing as soon as you set it up:

* **Google Analytics DebugView:** Enable DebugView to see events in real-time
  as you interact with your website or app. This is the best way to confirm
  events and parameters are being sent correctly. See [Monitor events in
  DebugView](//support.google.com/analytics/answer/7201382).
* **Google Tag Assistant Companion:** This browser extension helps validate
  your Google tag (gtag.js) implementation on websites. It shows you which
  tags are firing and the data being passed. See [About Tag
  Assistant](//support.google.com/tagmanager/answer/15212503).
  + **Browser developer tools:**
  + **Network tab:** Open your browser's developer tools (e.g., Chrome
    DevTools) and look for network requests to
    `google-analytics.com/g/collect` as you navigate your site. You should
    see these requests firing on each page load and for events. A `200 OK`
    status code indicates a successful transmission.
  + **Console tab:** Check for any JavaScript errors related to `gtag.js` or
    your site's code that might prevent the tag from running.

Check Google Analytics reports
------------------------------

* **Realtime report:** Data should start appearing in the [Realtime report](//support.google.com/analytics/answer/9271392)
  within minutes of the tag being correctly fired. You should see page views,
  events, and active users.
* **Standard reports:** Most data in standard reports takes **24-48 hours** to
  be fully processed and available. Don't be alarmed if you don't see complete
  data immediately outside of the Realtime and DebugView.

Common setup issues and how to fix them
---------------------------------------

* **Incorrect measurement ID:** Ensure the Measurement ID in your
  `gtag('config', 'G-XXXXXX')` call exactly matches the ID from your Google
  Analytics web data stream settings. Typos in the Measurement ID are one of
  the most common and easy-to-make setup mistakes, so double-check it
  carefully.
* **Tag not on all pages:** The Google tag snippet must be present within the
  `<head>` section of *every page* you want to track.
* **Incorrect tag placement:** The global site tag (gtag.js) should be placed
  as high as possible in the `<head>` of your HTML.
* **Consent mode issues:** If you've implemented Consent Mode, ensure that
  tags are not being blocked unduly. Tags will only fire after the user has
  granted the required consent. Use Tag Assistant to debug consent states. See
  [Troubleshoot Consent
  Mode](//developers.google.com/tag-platform/security/guides/consent-debugging).
  + **Ad blockers and privacy extensions:** Some browser extensions can
    block Google Analytics scripts from running. Test in an incognito window
    or different browser with extensions disabled.
* **Google Analytics filters:** Check if any [data filters](//support.google.com/analytics/answer/13296761)
  are active in your Google Analytics property settings (Admin > Data settings
  > Data filters) that might be excluding the data you're looking for.
* **Caching:** Browser or server-side caching might serve older page versions
  without the tag. Clear caches after adding the tag.

What to expect: Initial data
----------------------------

Once data starts flowing, you should see:

* **Automatically collected events:** `page_view`, `session_start`,
  `first_visit`, and `user_engagement` are collected by default.
* **Basic dimensions:** In reports, you'll start seeing data for dimensions
  like *Page path*, *Source/Medium*, *Device category*, *Country*, etc.

How long does data take to appear?
----------------------------------

* **DebugView:** Events appear within seconds.
* **Realtime reports:** Data appears within minutes.
* **Standard reports:** Allow 24-48 hours for full data processing and
  reporting.

If you've gone through these steps and still don't see data, double-check the
tag implementation and consult the [Google Analytics Help
Center](//support.google.com/analytics).
