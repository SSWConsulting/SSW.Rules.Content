---
seoDescription: Server-side commenting in ASP.NET allows efficient comment usage while preserving page performance and reducing kilobytes.
type: rule
archivedreason:
title: Do you use server side comments?
guid: 6fb14641-f2ca-4634-8c14-8efa742d16c1
uri: use-server-side-comments
created: 2016-08-24T22:29:47.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-use-server-side-comments
---

Use server side comments:

- Use **&lt;%-- Comment Here --%&gt;** instead of **&lt;!-- Comment Here --&gt;** (Does not get rendered to the client, saves us a few precious kilobytes)
- Use **CTRL + K, C** to comment and **CTRL + K, U** to uncomment

<!--endintro-->
