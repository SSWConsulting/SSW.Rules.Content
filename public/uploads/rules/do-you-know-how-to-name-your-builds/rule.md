---
seoDescription: Mastering build naming conventions ensures easy identification of their purpose.
type: rule
archivedreason:
title: Do you know how to name your builds?
guid: c97f2177-c0d7-445e-bda7-fb4909db7710
uri: do-you-know-how-to-name-your-builds
created: 2015-11-02T10:44:59.0000000Z
authors:
  - title: Ben Cull
    url: https://ssw.com.au/people/ben-cull
related: []
redirects: []
---

You should always follow a naming standard when naming your builds. This helps you identify their purpose at a glance.

<!--endintro-->

The build name should have the following suffixes, depending on their purpose:

- **.CI** - For continuous integration builds. These are triggered automatically and do not deploy anywhere.
- **.CD.[Environment]** - For continuous delivery builds. These are triggered automatically and deploy to an environment. You should specify which environment it deploys to as well.

![](buildnames.png)

::: good
Good Example: We have two continuous delivery builds to our staging environment.  
:::
