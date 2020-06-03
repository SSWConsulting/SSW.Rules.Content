---
type: rule
title: Do you know how to name your builds?
uri: do-you-know-how-to-name-your-builds
created: 2015-11-02T10:44:59.0000000Z
authors:
- id: 37
  title: Ben Cull

---



<span class='intro'> You should always follow a naming standard when naming your builds. This helps you identify their purpose at a glance. </span>

<p>​</p><p>The build name should have the following suffixes, depending on their purpose&#58;</p><ul><li><span style="line-height&#58;20.8px;"><strong>.CI</strong> - For continuous integration builds. These are triggered automatically and do not deploy anywhere.<br></span></li><li><span style="line-height&#58;20.8px;"><strong>.CD.[Environment]</strong> - For continuous delivery builds. These are triggered automatically and deploy to an environment. You should specify which environment it deploys to as well.</span></li></ul><div><span style="line-height&#58;20.8px;"><img src="/PublishingImages/buildnames.png" alt="buildnames.png" style="margin&#58;5px;" /><br></span></div><dd class="ssw15-rteElement-FigureGood">Good Example&#58;&#160;We have two continuous delivery​&#160;builds to our staging environment.</dd><div><span style="line-height&#58;20.8px;"><br></span></div>


