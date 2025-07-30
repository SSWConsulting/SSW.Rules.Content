---
seoDescription: Anchor tags should run at server only when needed to change target at runtime, avoiding unnecessary overhead.
type: rule
archivedreason:
title: Do you know when anchor should "run at server"?
guid: 721eda39-8237-40ca-8f6b-f3eb9ba8f0b6
uri: when-anchor-should-run-at-server
created: 2016-08-24T22:33:39.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-know-when-anchor-should-run-at-server
---

**&lt;a&gt;** tag should **runat=“server"** \*ONLY\* if you need to change the target at runtime.

If you include **runat=“server"** for an HTML element that you do not need access to in code behind, you are introducing a whole lot of overhead you do not need.

<!--endintro-->

We have a program called [SSW Code Auditor](https://www.ssw.com.au/ssw/CodeAuditor/) to check for this rule.
