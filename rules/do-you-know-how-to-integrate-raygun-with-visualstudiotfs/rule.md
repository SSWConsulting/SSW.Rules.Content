---
type: rule
archivedreason: 
title: Do you know how to integrate RayGun with VisualStudio/TFS?
guid: cd59e270-70b7-4dd3-9a90-64d2dd5849ea
uri: do-you-know-how-to-integrate-raygun-with-visualstudiotfs
created: 2016-10-25T17:10:27.0000000Z
authors:
- id: 3
  title: Eric Phan
related: []

---

TFS/VisualStudio.com is the source of truth for product development, so how do you get issues in RayGun into TFS? Thankfully there’s a built in integration that lets you do that. 

<!--endintro-->

1. Under Integrations
2. Select Visual Studio Team Services
3. Connect to your TFS or VisualStudio.com instance

<dl class="image">&lt;dt&gt;
      <img src="raygun-integration-tfs-1.png" alt="raygun-integration-tfs-1.png">
   &lt;/dt&gt;<dd>Figure: Link RayGun with TFS/VisualStudio.com</dd></dl>
Now under the crash report, you have to option to create a PBI and link it to the crash report.
<dl class="image">&lt;dt&gt;
      <img src="raygun-integration-tfs-2.png" alt="raygun-integration-tfs-2.png">
   &lt;/dt&gt;<dd>Figure: Create a new PBI or link to an existing PBI</dd></dl>
Now you can see which RayGun create reports have already been added to the backlog.
<dl class="image">&lt;dt&gt;
      <img src="raygun-integration-tfs-3.png" alt="raygun-integration-tfs-3.png">
   &lt;/dt&gt;<dd>Figure: Link RayGun with TFS/VisualStudio.com<br></dd></dl>

::: greybox
  RayGun is a useful tool to use for your DevOps. Check out our rule “[Do you know how DevOps fits in with Scrum?](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=16b925f9-05fd-4758-a370-14e16e281f84)”

:::
