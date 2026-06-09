---
title: "Send user IDs"
source_url: "https://developers.google.com/analytics/devguides/collection/ga4/user-id?hl=en&client_type=gtag"
product: "Google Analytics 4"
section: "Collection (gtag)"
language: en
scraped_date: 2026-06-08
doc_id: "google-analytics/collection-ga4/user-id.md"
---
User IDs are your own unique identifiers that you assign to individual users.
This guide explains how to send user IDs to Google Analytics, so you can connect
user behavior across different sessions, devices, and platforms.

To learn more about the User-ID feature, see [Measure
activity across platforms](//support.google.com/analytics/answer/9213390). To learn how to set a user ID for an app, see [Set a
user ID](//firebase.google.com/docs/analytics/userid).

**Warning:** Don't set custom dimensions based on user IDs. Setting custom
dimensions based on user IDs leads to dimensions with too many unique values.
Having too many unique values causes issues with Google Analytics data and
reporting accuracy. [Learn more about best practices for setting custom
dimensions](//support.google.com/analytics/answer/14240153#best-practices).

The `user_id` parameter is a configuration parameter, not a custom user property
or standard event parameter. Instead, `user_id` is a reserved system parameter
used specifically to identify authenticated users across devices and sessions.
Don't set it as a custom user property (for example, in the `user_properties`
object for `gtag.js` or in the **User Properties** section of Google Tag Manager
tags), and don't register it as a custom dimension in the Analytics UI.
Likewise, don't pass it as an event-level parameter on individual events.
Instead, set `user_id` only as a configuration parameter using the following
methods.

gtag.js
Tag Manager

Before you begin
----------------

Before you can send user IDs, make sure you've completed the following:

* [Create a Google Analytics account and property](//support.google.com/analytics/answer/9304153#account).
* [Create a web data stream for your website](//support.google.com/analytics/answer/9304153#stream&zippy=%2Cweb).
* [Place the Google tag on your website](//support.google.com/analytics/answer/9304153#add-tag&zippy=%2Cadd-the-google-tag-directly-to-your-web-pages%2Cadd-your-tag-using-google-tag-manager).
* Have access to your website's source code.
* Have the [Editor](//support.google.com/analytics/answer/9305587) role (or above) to the Google Analytics account.

Send user IDs
-------------

The value you send for `user_id` depends on the state of
the user:

* **User has never signed in**: Don't send the `user_id` parameter.
* **User is signed-in**: Send their user ID.
* **User was signed-in, then signed out**: Send `null`.

To send a user ID to Analytics, add the `user_id` parameter to the `config`
command on each page of your website:

```
if (/* your logic for determining if the user is signed in */) {
  gtag('config', 'TAG_ID', {
    'user_id': 'USER_ID'
  });
} else if (/* your logic for determining if the user signed out */) {
  gtag('config', 'TAG_ID', {
    'user_id': null
  });
} else {
  // Do nothing if the user never signed in.
}
```

1. Replace TAG\_ID with your [tag ID](//support.google.com/analytics/answer/9539598#find-G-ID).
2. Replace the comments with your checks for if the user is signed-in, and
   if the user was signed-in but then signed out.
3. If a user is signed-in, replace USER\_ID with their user ID.
4. When a user signs out, set `user_id` to `null`. Don't send an
   empty string (`""`), a blank string (`" "`), or the quoted words `"null"` or
   `"NULL"`.

### Set user ID after initialization

In many cases, the `user_id` is not known when the Google tag is first
initialized. For example, a user may visit your site and only log in later.

To set or update the `user_id` after the initial page load, use the
`gtag('set')` command. This command sets the `user_id` for all subsequent events
on the page and is the recommended approach instead of `gtag('config')` in this
scenario.

#### Set the user ID upon login

When a user successfully logs in, call `gtag('set')` to associate their ID with
future events:

```
// Example function called after successful login
function handleUserLogin(userId) {
  if (userId) {
    gtag('set', {'user_id': userId});
    console.log('User ID set for GA:', userId);

    // You can also send a login event
    gtag('event', 'login', { method: 'your_login_method' });
  }
}

// Example usage:
// handleUserLogin('12345_user');
```

#### Clear the user ID upon logout

When a user logs out, you should clear the `user_id` by setting its value to
`null`:

```
// Example function called after logout
function handleUserLogout() {
  gtag('set', {'user_id': null});
  console.log('User ID cleared for GA.');

  // You can also send a logout event
  gtag('event', 'logout');
}

// Example usage:
// handleUserLogout();
```

By using `gtag('set')`, you make sure that the `user_id` is correctly managed
throughout the user session, reflecting the user's current login state even if
it changes after the page has loaded.

How User-ID is used in Google Analytics
---------------------------------------

Once you send `user_id` values to Google Analytics, they are used to:

* **Unify user journeys:** Connect user activity across different sessions,
  devices, and platforms for signed-in users.
* **Improve user counts:** Provide more accurate, de-duplicated user metrics.
* **Enable analysis:**
  + Analyze activity based on signed-in status: Use dimensions like
    "Signed in with user ID" to create comparisons in standard reports
    or segments in Explorations.
  + Power the [User Explorer](//support.google.com/analytics/answer/9283607) exploration technique, allowing you to drill
    down into the timeline of activities for individual users.

### Important considerations

* **Do NOT create custom dimensions for User ID:** You should **not**
  register the `user_id` as a user-scoped custom dimension. This is a key
  best practice. Doing so creates an unnecessary high-cardinality dimension,
  which can severely impact report performance, cause data to be grouped into
  the "(other)" row, and consume your custom dimension quota. The built-in
  User-ID feature handles the user stitching. Learn more in
  [Best practices for User-ID](//support.google.com/analytics/answer/12675187).
* **Set `user_id` as a configuration setting, not a user property or event
  parameter:**
  Because `user_id` is a reserved system parameter, it must only be applied as
  a configuration or a setting parameter (using the `gtag()` `config` or `set`
  commands, or Google Tag Manager's Google tag configuration settings). Don't
  configure it as a custom user property, pass it inside the `user_properties`
  settings object, or send it as an event-level parameter on individual
  events.
* **Direct ID visibility in standard reports vs. explorations:** Raw `user_id`
  values are not available as a standard dimension in standard reports or most
  explorations (such as Free Form) to maintain privacy and manage cardinality.
  However, you can view the raw `user_id` in the [User Explorer](//support.google.com/analytics/answer/9283607) exploration
  template under the column labeled **Effective user ID** for logged-in users.
* **Accessing raw user IDs:** If you need to perform analysis using the
  raw `user_id` values, the recommended approach is to use the
  [GA4 BigQuery Export](//support.google.com/analytics/answer/9823238). The `user_id` field is available in
  the exported data.

To ensure User-ID data is being used and visible in the [User Explorer](//support.google.com/analytics/answer/9283607), make
sure your property's [Reporting Identity](//support.google.com/analytics/answer/10976610) is set to **Blended** or **Observed**.
