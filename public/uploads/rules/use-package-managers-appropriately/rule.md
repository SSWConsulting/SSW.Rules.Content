---
seoDescription: Use a single package manager and be cautious of versioning issues to simplify your development workflow.
type: rule
archivedreason:
title: Do you use package managers appropriately?
guid: d32858ed-12ed-4d69-9aa4-92a01c16665d
uri: use-package-managers-appropriately
created: 2016-04-28T21:33:33.0000000Z
authors:
  - title: Steve Leigh
    url: https://ssw.com.au/people/steve-leigh
related: []
redirects:
  - do-you-use-package-managers-appropriately
---

Advice like this can be a minefield, and is constantly in flux, but there are some rules-of-thumb that can make life simpler.

<!--endintro-->

![Figure: Default ASP.NET Core project is package management done wrong](package1.jpg)

![Figure: Project using good package management](package2.jpg)

### Bower is dead

![Figure: Bower is dead](package3.jpg)

File-New Project in Visual Studio comes with bower packages, and there are a lot of old blog posts that recommend bower for client side libraries, but bower is dead. Angular2 is discouraging its use, and npm has all the same packages, and more. Prefer npm over bower, even for client-side dependencies.

### Use a single package manager

For client side libraries, avoid mixing npm, jspm and manually copy/pasted files. Life will be simpler if you stick with just 1.

Right now, this is npm, but watch out for jspm, which shows a lot of promise if you can get past the steep learning curve.

### Be careful with versioning

Theoretically, everything in npm is using semantic versioning. In practice, people aren’t that diligent, so it pays to be careful with your version numbers. It’s not rare for versions to disappear from npm, or for a build-servers internet connection to be flaky. If these issues are happening, consider using [npm-shrinkwrap](https://docs.npmjs.com/cli/shrinkwrap) to lockdown dependency versions.

### Track your dev dependencies and dependencies separately

All package managers distinguish between those used for development, and those used for the application. Use this feature – it will save you time.
