---
seoDescription: Sitefinity disables caching when debug="true", impacting performance in test and production environments.
type: rule
archivedreason:
title: Do you know that caching is disabled when debug="true"
guid: 511991ee-5a08-4119-9ca0-10ceb82c2a9f
uri: do-you-know-that-caching-is-disabled-when-debug-true
created: 2014-07-04T02:27:16.0000000Z
authors:
  - title: Drew Robson
    url: https://ssw.com.au/people/drew-robson
related: []
redirects:
  - do-you-know-that-caching-is-disabled-when-debug-＂true＂
---

Sitefinity uses caching heavily so ensure debug="false" when deploying to non-development environments.

<!--endintro-->

When developing with Sitefinity in a local development environment, the compilation element in your web.config file will be set to false. While this is common practice when developing ASP.NET applications, Sitefinity disables caching in this scenario. This will make development slower (but easier as changes will be immediate) but will severly impact performance in test and production environments.

![](4-07-2014-2-07-31-PM-compressor.png)

**Figure: Default compilation settings in Sitefinity**
