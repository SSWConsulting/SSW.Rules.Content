---
type: rule
archivedreason: 
title: Do you swarm to fix the build?
guid: f51b4c00-7b7d-4b6a-a35e-096cdf1c9e39
uri: do-you-swarm-to-fix-the-build
created: 2015-11-03T08:46:16.0000000Z
authors:
- title: Ben Cull
  url: https://ssw.com.au/people/ben-cull
related: []
redirects: []

---

If you or someone on your team has broken the build, the whole team should swarm to fix the problem immediately. 
<!--endintro-->





It is PERFECTLY ok to have the CI build go red, that is what is there for, but when the build goes red the team should go immediately into corrective action mode and make sure the build goes green again.

Two things should be done:

1. Get it Green
2. Find out WHY it went green locally but red on build server. This may indicate something is brittle in the application structure, and that is the underlying cause – and should of course also be fixed.





![](broken builds.png)



::: bad
Bad Example: Too many broken builds in a row.  
:::



![](good builds.png)


::: good
Good Example: Broken build was fixed immediately.  
:::
