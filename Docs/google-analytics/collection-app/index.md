---
title: "Google Analytics for apps"
source_url: "https://developers.google.com/analytics/devguides/collection/app?hl=en"
product: "Google Analytics 4"
section: "App (Firebase)"
language: en
scraped_date: 2026-06-08
doc_id: "google-analytics/collection-app/index.md"
---
This page explains Google Analytics for apps, and what you need to do to get
started.

Google Analytics measures events to help you learn about your performance. For
example, you can use Google Analytics to measure engagement, insights about your
audience, and how they interact with your app.

Set up your account
-------------------

Here's an overview of the steps to set up your Google Analytics account for data
collection:

1. If you don't already have one, [create a Google Analytics
   account](//support.google.com/analytics/answer/9304153#account).
2. After creating an account, [create a new
   property](//support.google.com/analytics/answer/9304153#property).
   Properties are like containers that hold the data you collect.
3. Once you've created a new property, [add an app data stream](//support.google.com/analytics/answer/9304153#stream&zippy=%2Cios-app-or-android-app)
   that sends the data from your app to the property.

Tag your app
------------

To add Google Analytics to your app and begin logging events, use
[Firebase](//firebase.google.com/docs/analytics/get-started).

Firebase is Google's integrated app-developer platform. The Firebase SDK
collects basic app-usage data for you automatically, without the need to write
any additional code. Here are some examples of what you can measure:

* How many times your app was opened.
* How often in-app purchases were made.
* How many users were active during a certain period of time.

Measure additional platforms
----------------------------

For measurement across multiple platforms, use the [Measurement
Protocol](/analytics/devguides/collection/protocol/ga4). To get started, try our
[Send app events to Google Analytics
codelab](//firebase.google.com/codelabs/firebase_mp#0).
