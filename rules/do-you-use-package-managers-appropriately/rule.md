---
type: rule
title: Do you use package managers appropriately?
uri: do-you-use-package-managers-appropriately
created: 2016-04-28T21:33:33.0000000Z
authors:
- id: 55
  title: Steve Leigh

---



<span class='intro'> <p>Advice like this can be a minefield, and is constantly in flux, but there are some rules-of-thumb that can make life simpler.</p> </span>

<dl class="image"><dt>​<img src="/PublishingImages/package1.jpg" alt="package1.jpg" /></dt><dd>Figure&#58; Default ASP.NET Core project is package management done wrong</dd></dl><dl class="image"><dt>​<img src="/PublishingImages/package2.jpg" alt="package2.jpg" /></dt><dd>Figure&#58; Project using good package management</dd></dl><h3>Bower is dead</h3><dl class="image"><dt>​<img src="/PublishingImages/package3.jpg" alt="package3.jpg" /></dt><dd>Figure&#58; Bower is dead </dd></dl><p>File-New Project in Visual Studio comes with bower packages, and there are a lot of old blog posts that&#160; recommend bower for client side libraries, but bower is dead. Angular2 is discouraging its use, and npm has all the same packages, and more. Prefer npm over bower, even for client-side​ dependencies.</p><h3>Use a single package manager</h3><p>For client side libraries, avoid mixing npm, jspm and manually copy/pasted files. Life will be simpler if you stick with just 1.&#160;</p><p>Right now, this is npm, but watch out for jspm, which shows a lot of promise if you can get past the steep learning curve.</p><h3>Be careful with versioning</h3><p>Theoretically, everything in npm is using semantic versioning.&#160; In practice, people aren’t that diligent, so it pays to be careful with your version numbers. It’s not rare for versions to disappear from npm, or for a build-servers internet connection to be flaky.&#160; If these issues are happening, consider using 
      <a href="https&#58;//docs.npmjs.com/cli/shrinkwrap" target="_blank">npm-shrinkwrap </a>&#160;to lockdown dependency versions.</p><h3>Track your dev dependencies and dependencies separately​</h3>
<p>All package managers distinguish between those used for development, and those used for the application.&#160; Use this feature – it will save you time. </p>


