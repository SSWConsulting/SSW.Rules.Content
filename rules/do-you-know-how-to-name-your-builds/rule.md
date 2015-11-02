---
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
<br><excerpt class='endintro'></excerpt><br>
<p>​</p><p>The build name should have the following suffixes, depending on their purpose&#58;</p><ul><li><span style="line-height&#58;20.8px;"><strong>.CI</strong> - For continouos integration builds. These are triggered automatically and do not deploy anywhere.<br></span></li><li><span style="line-height&#58;20.8px;"><strong>.CD.[Environment]</strong> - For continouos delivery builds. These are triggered automatically and deploy to an environment. You should specify which environment it deploys to as well.</span></li></ul><div><span style="line-height&#58;20.8px;"><br></span></div>


