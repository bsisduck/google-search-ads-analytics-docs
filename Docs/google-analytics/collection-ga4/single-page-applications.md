---
title: "Measure single-page applications"
source_url: "https://developers.google.com/analytics/devguides/collection/ga4/single-page-applications?hl=en&client_type=gtag"
product: "Google Analytics 4"
section: "Collection (gtag)"
language: en
scraped_date: 2026-06-08
doc_id: "google-analytics/collection-ga4/single-page-applications.md"
---
> This document is for developers who want to measure page views on their
> single-page application using Google Analytics.

[Single-page applications](//developer.mozilla.org/en-US/docs/Glossary/SPA)
(SPA) are websites that load an HTML document once and fetch any additional
content using JavaScript APIs.

> Example: Suppose you have a form to acquire some leads. The form has three
> screens:
>
> * First screen to capture the customer information.
> * Second screen where customers indicate interest in certain services.
> * Third screen page to sign up for webinars related to the customer's
>   interests.

The key to measuring page views from SPAs correctly is to count page views for
each screen a user interacts with and get the page
[referrer](//developer.mozilla.org/en-US/docs/Web/API/Document/referrer) right,
so you can correctly trace the user journey.

Before you begin
----------------

This page assumes that you already have:

* A Google Analytics account and property for your website. Learn how to
  [Set up Google Analytics](//support.google.com/analytics/answer/9304153).
* A Google tag implemented on your website that fires when the page initially
  loads. Learn how to
  [Set up the Google tag](/analytics/devguides/collection/ga4/tag-options).

Implement single-page application measurement
---------------------------------------------

To implement accurate SPA measurement, use one of these methods to trigger a new
virtual page view:

* Browser history changes (recommended): If your SPA uses the [History
  API](//developer.mozilla.org/en-US/docs/Web/API/History), specifically
  the `pushState()` and `replaceState()` method to update screens, use this
  option.
* Custom events: If your website uses the
  [`DocumentFragment`](//developer.mozilla.org/en-US/docs/Web/API/DocumentFragment)
  object to render different screens, use this option.

Browser history implementation
Custom event implementation

### Browser history change implementation

If your SPA uses the History API, you can enable enhanced measurement in Google Analytics
to automatically track page views based on browser history events.

#### Enable enhanced measurement in GA4

To measure `page_views` automatically based on browser history:

1. Open [Google Analytics](//analytics.google.com/analytics/)
2. In **[Admin](//support.google.com/analytics/answer/6132368)**, under
   *Data collection and modification*, **click Data Streams > Web**.
3. Under *Enhanced measurement*, slide the switch **On** to enable all options.
4. Click to edit individual options. Under **Page Views**, click **Show
   advanced settings**. Make sure to enable both **Page loads** and **Page
   changes based on browser history events**.

   ![An image showing page views setting](/static/tag-platform/devguides/images/page-views.png)
5. **Save** the changes.

**Note:** When Enhanced Measurement is enabled for "Page changes based on
browser history events", Google Analytics automatically listens for history
events (like those used in SPAs) and sends `page_view` events. You don't need
to configure specific history variables or triggers in Google Tag Manager
*for the purpose of sending page views to GA4*.

Use Google Tag Manager triggers for history events
--------------------------------------------------

If you need to fire other types of tags in Google Tag Manager based on browser
history changes such as to send data to other marketing platforms, you can use
the "History Change" trigger type.

When configuring tags or variables to work with the History Change trigger, make
sure you use the correct **Built-In Variables** provided by Google Tag Manager:

* `History New URL Fragment`: The fragment of the URL after the history event.
* `History Old URL Fragment`: The fragment of the URL before the history event.
* `History New State`: The new history state object.
* `History Old State`: The old history state object.
* `History Source`: The source of the history event (such as `popstate`,
  `pushState`, `replaceState`).

These Built-In Variables may need to be enabled in Google Tag Manager first
under **Variables** > **Configure**.

**Important:** Avoid using undefined variable names. For example,
`New History URL` is not a standard GTM variable and will cause errors when
publishing. Always select from the available Built-In Variables or your own
defined variables.

For more details on this trigger, see
[History change trigger](//support.google.com/tagmanager/answer/7679322).

Verify your measurement setup
-----------------------------

To verify your single-page application measures page views correctly:

1. Enable debug mode for every tag in your SPA measurement setup. Learn how to
   [Monitor events in
   DebugView](//support.google.com/analytics/answer/7201382).
2. Click through your single-page application. When you click to a new virtual
   screen, you should see a new `page_view` event in DebugView. Compare the
   `page_view` event parameters with the preceding `page_view` event to check
   if the page referrer and page location have been updated correctly.

Additional considerations for SPAs
----------------------------------

Besides sending `page_view` events, consider these additional aspects for a
robust SPA integration with Google Analytics and better user experience:

### Manage scroll position

When users navigate between views in an SPA, the browser typically retains the
current scroll position. This can mean users don't see the top of the new
virtual page, and it can affect scroll depth tracking.

**Recommendation:** Programmatically reset the scroll position to the top of the
page or the main content container after each virtual page transition.

```
// Example: Reset window scroll position on a route change in your SPA
window.scrollTo(0, 0);

// Or, if your content is within a specific element:
// document.getElementById('main-content').scrollTo(0, 0);
```

With this change, users will start at the top of the new content, which allows
Google Analytics scroll tracking to measure engagement on the new virtual page
accurately.

### Ensure content accessibility for browser features

If users report issues with browser features like on-page search (Ctrl+F) not
working after a virtual page load, it might indicate how your SPA updates the
DOM.

**Recommendation:** Ensure that your SPA framework and routing logic completely
and synchronously update the relevant parts of the DOM with the new page's
content. Delayed rendering or content hidden from the main DOM tree might not be
immediately indexable by the browser's search function. Test on-page search
after virtual navigations to confirm content accessibility.

Impact on automatic events
--------------------------

If you correctly implement virtual page view measurement in your SPA, then
Google Analytics will handle other automatic events appropriately. If virtual page views
are not recorded for screen changes, Google Analytics treats the SPA as a single page,
leading to skewed metrics.

For example, the `user_engagement` event measures the time a user actively
spends on a page. Without virtual page views, all engagement time is
attributed to the initial page load, making it impossible to analyze time
spent on individual screens.

When virtual page view measurement is correctly implemented:

* The `user_engagement` event is sent when the user navigates from one
  virtual page to another.
* The engagement time for the *previous* virtual page is calculated and
  sent along with the `user_engagement` event, typically just before
  the `page_view` event for the *new* virtual page is processed.
* Other events, such as clicks or scrolls, are associated with the
  `page_location` of the virtual page the user is currently viewing.

This lets you analyze user engagement and other metrics for individual
screens or sections within your SPA, providing a more accurate understanding of
the user journey.
