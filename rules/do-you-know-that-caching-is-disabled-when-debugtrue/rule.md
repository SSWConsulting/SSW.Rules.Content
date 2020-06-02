---
uri: do-you-know-that-caching-is-disabled-when-debugtrue
title: Do you know that caching is disabled when debug="true"
created: 2014-07-04 02:27:16
authors:
  - id: 38
    title: Drew Robson
---




<span class='intro'> ​​Sitefinity uses caching heavily so ensure debug=&quot;false&quot; when deploying to non-development environments. </span>

<p>​</p><p>When developing with Sitefinity in a local development environment, the compilation element in your web.config file will be set to false. While this is common practice when developing ASP.NET applications, Sitefinity disables caching in this scenario. This will make development slower (but easier as changes will be immediate) but will severly impact performance in test and production environments.</p><p><img src="/PublishingImages/4-07-2014-2-07-31-PM-compressor.png" alt="4-07-2014-2-07-31-PM-compressor.png" style="margin&#58;5px;" /><br></p><p><strong>Figure&#58; Default compilation settings in Sitefinity</strong></p>


