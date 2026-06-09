---
title: "Using the Google Search Status Dashboard"
source_url: "https://developers.google.com/search/help/status-dashboard?hl=en"
product: "Google Search Central"
section: "Help & FAQ"
language: en
scraped_date: 2026-06-08
doc_id: "search-central/help/status-dashboard.md"
---
Using the Google Search Status Dashboard
========================================

The [Google Search Status Dashboard](https://status.search.google.com) provides
status information on the systems that power Google Search. The dashboard shows issues that
affect many sites or users, so if you see an annotation in the dashboard, it may be related to
the change in your site's performance.

The dashboard also shows the latest ranking updates made to Google Search that are relevant to
website owners. To learn more about how Google makes improvements to Search and why we share
updates, check out our blog post on
[How Google updates Search](https://blog.google/products/search/how-we-update-search-improve-results/).
You can also find more updates about Google Search on [our blog](/search/blog).

To get notified about issues and updates, you can subscribe to
[our RSS feed](https://status.search.google.com/en/feed.atom).

[View the Dashboard](https://status.search.google.com)

Lifecycle of an issue
---------------------

When an issue with Google Search is detected, the Search Relations team and Search engineering
team work together to resolve the issue and communicate it to you:

1. [Detection and initial response](#detection)
2. [Investigation](#investigation)
3. [Follow up](#follow-up)
4. [Mitigation or fix](#fix)

Detection and initial response
------------------------------

The Search Relations team monitors the status of Google Search systems by looking at many
different types of signals (including [internal monitoring](https://sre.google/sre-book/monitoring-distributed-systems/)
and feedback from the community). In the event of a widespread issue, the Search Relations team
updates the dashboard. A widespread issue means there's something affecting a large number of
sites or users.

The status dashboard may use the following statuses:

| Status definitions | |
| --- | --- |
| Available | The system is generally working and available. |
| System information | There's been an update or change to a system (for example, a ranking update started rolling out, or Googlebot started crawling over HTTP/2). |
| System disruption | Websites may experience degraded system performance due to a common third-party (for example, DNS servers). |
| System outage | The system isn't functioning to a large extent, and the issue is affecting a large number of sites or users. |

Investigation
-------------

Search engineering teams are responsible for investigating the root cause of issues. For more
information, see [Chapter 12 of the Site Reliability Engineering Book](https://sre.google/sre-book/effective-troubleshooting/).

Follow up
---------

While an issue is ongoing, the Search Relations team provides regular updates. Updates may
include:

* Information about the issue, such as the scale of the issue or regions affected.
* Timeline for when you can expect the next update.
* Progress towards fixing the issue, such as when the root cause has been found, or if there
  are workarounds.

Mitigation or fix
-----------------

An issue is considered *fixed* only when changes have been made that Google is confident
will end the impact in the system. Sites may still experience effects until Google can reprocess
sites again.

While an issue is in progress, the Site Reliability Engineering team attempts to mitigate the
issue. *Mitigation* is when the impact or scope of an issue can be reduced, for
example, by providing additional internal resources to affected Search systems or by providing
workarounds for website owners.

When possible, the Search Relations team finds and communicates workarounds. *Workarounds*
are steps that you can take to solve the underlying need despite the issue. For example, a
workaround might be to use a different DNS server.

FAQs
----

### What happens if an issue is noted?

When an issue with Google Search is detected, the Search Relations team and Search engineering
team work together to resolve the issue and communicate it to you.

### What happens if an update is noted?

When a ranking system update is noted, follow the link (when provided) to learn more about the
update and any guidance to consider. Often, there's no action needed.

### What ranking updates are listed?

The dashboard lists the latest ranking updates made to Google Search that are relevant to
website owners. To learn more about how Google makes improvements to Search and why we share
updates, check out our blog post on
[How Google updates Search](https://blog.google/products/search/how-we-update-search-improve-results/).
You can also find more updates about Google Search on [our blog](/search/blog).

### I'm experiencing an issue, but it's not listed in the dashboard.

The issue may be isolated to your web pages, or it may be impacting a limited number of searchers
or websites. If you're a website owner, you can
[contact us in the Google Search Central help community](https://support.google.com/webmasters/community)
about any issues you are experiencing that are not listed on the dashboard. If you're experiencing
issues with your searches on Google, visit the [Google Search help forum](https://support.google.com/websearch/community).

### Where can I find information about past system statuses?

Issues and updates reported on the dashboard are available on the
[Summary and History page](https://status.search.google.com/summary)
for 5 years. Click a summary row to review the posts about the annotation.
