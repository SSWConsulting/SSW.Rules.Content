---
type: rule
archivedreason: 
title: Do you avoid publishing from Visual Studio?
guid: a67b023d-b40f-4619-9d3d-2490f98e153b
uri: do-you-avoid-publishing-from-visual-studio
created: 2013-02-06T18:47:32.0000000Z
authors:
- id: 24
  title: Adam Stephensen
related: []

---


<p>​Publishing from Visual Studio is a convenient way to deploy a web application, but it relies on a single developer’s machine which can lead to problems. Deploying to production should be easily repeatable, and able to be performed from different machines.</p>
<br><excerpt class='endintro'></excerpt><br>
<p>A better way to deploy is by using a defined Build in TFS.</p><dl class="badImage"><dt>
      <img src="/PublishingImages/test-publish.jpg" alt="" />
   </dt><dd>Figure&#58; Bad Example – Using Publish to deploy </dd></dl><dl class="goodImage"><dt>
      <img src="/PublishingImages/queuing-new-build.jpg" alt="" />
   </dt><dd>Figure&#58; Good Example – Queuing a new build to deploy your application</dd></dl><dl class="goodImage"><dt>
      <img src="/PublishingImages/continuous-integration.jpg" alt="" />
   </dt><dd>Figure&#58; Best example – Use continuous integration to trigger your Continuous Deployment build</dd></dl>


