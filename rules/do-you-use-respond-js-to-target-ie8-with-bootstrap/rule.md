---
type: rule
title: Do you use Respond JS to target IE8 with Bootstrap?
uri: do-you-use-respond-js-to-target-ie8-with-bootstrap
authors:
  - title: Ben Cull
    url: https://ssw.com.au/people/ben-cull
  - title: Drew Robson
    url: https://ssw.com.au/people/drew-robson
related: []
redirects: []
created: 2014-06-18T04:58:49.000Z
archivedreason: "The library Respond JS has not been updated since 2017 as per
  the GitHub repo: https://github.com/scottjehl/Respond and has very low usage
  on NPM: https://www.npmjs.com/package/respond.js . Supporting Internet
  Explorer versions under IE8 is also no longer relevant for most projects, used
  by 0.03% of devices: https://caniuse.com/usage-table ."
guid: a3a46cdc-7315-410d-8d6a-de40da64350a
---

By default, we do not accommodate IE8 or lower, but should it arise as a specific requirement, then you can include Respond JS in your application, after Bootstrap. Respond JS enables responsive web designs in browsers that don't support CSS3 Media Queries.

<!--endintro-->

![Figure: Include respond.js in your bootstrap bundle](18-06-2014 2-04-12 PM.png)  

**Note:** Respond JS will be included in a new MVC5 Web Application. If you are working on an existing application, you can get it from NuGet or https://github.com/scottjehl/Respond.

![Figure: A new MVC5 Web Application running in IE8 with Bootstrap and Respond JS](18-06-2014 2-15-09 PM.png)
