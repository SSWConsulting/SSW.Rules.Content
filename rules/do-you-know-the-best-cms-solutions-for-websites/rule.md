---
type: rule
title: Do you know the best CMS solutions for websites?
uri: do-you-know-the-best-cms-solutions-for-websites
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Anthony Nguyen
    url: https://www.ssw.com.au/people/anthony-nguyen
related: []
redirects: []
created: 2009-03-10T08:44:37.000Z
archivedreason: null
guid: af85d3bd-de7f-488e-8a21-6393d8907ab8
---
You don’t want to build solutions from scratch, so take what business value you can from a CMS: don't reinvent the wheel.

> A CMS allows business users to build and manage websites without having to write any code.

### Top 6 CMS vendors of 2021, by Market Share (including eCommerce and websites)

* WordPress
* Joomla
* Drupal
* Shopify
* Squarespace
* Wix

Source: https://www.isitwp.com/popular-cms-market-share/

### Top 5 CMS vendors for Enterprise websites (.NET based)

* DotNetNuke - DNN (Open source) (pricing non-transparent)
* Umbraco (Open source) ($ - https://umbraco.com/umbraco-cms-pricing/)
* Kentico Xperience (Formerly Kentico EMS) ($$ - https://xperience.io/pricing)
* Sitefinity ($ - pricing non-transparent)
* SiteCore ($$$ - pricing non-transparent)

Source: https://theonetechnologies.com/blog/post/top-5-dot-net-based-cms-platforms
\
\
![Figure: .NET CMS Google Trends](googletrendsnet.png ".NET CMS Google Trends")

See google trends information for these products: https://trends.google.com/trends/explore?q=dotnetnuke,sitefinity,sitecore,kentico,Umbraco

### Popular Headless CMS of 2021

* Contentful ($ - https://www.contentful.com/pricing/)
* Magnolia (pricing non-transparent)
* Strapi (open source) (free / $ enterprise plan - https://strapi.io/pricing-self-hosted)
* Directus (open source) ($ - https://directus.io/pricing/)
* Kontent (Kentico) ($ - https://kontent.ai/pricing)

Source: <https://www.izooto.com/blog/best-headless-cms-2021>
\
\
![Figure: Headless CMS Google Trends](googletrendsheadless.png "Headless CMS Google Trends")

See google trends info formation these products: https://trends.google.com/trends/explore?q=contentful,magnolia%20cms,strapi,directus,kontent

## Headless CMS vs Traditional CMS

\
**Source**: <https://www.udig.com/digging-in/traditional-cms-vs-headless-cms/>

A Traditional CMS is a monolith, which means it has both a front-end and back-end. It uses server side technology like PHP (Wordpress,  Joomla, Magento) or ASP.Net (DNN, Umbraco, Sitefinity) and a single database. All pages are served by one or many backend servers.

A Headless CMS deals strictly with the content. Created content is accessed via Application Programming Interfaces (APIs), which gives you full flexibility on how you build the front-end for your website.

### Pros of a Traditional CMS

* **Simple and fast** - for setup and maintenance 
* **No developers needed** - although for larger websites, or complicated CMS (e.g. SiteCore) this may become necessary
* **Simple to control look and feel** - using available themes and templates
* **Large community support**
* **Out of the box integrations** - payments, social media, etc.

### Cons of a Traditional CMS

* **Performance is not amazing** - the frontend is coupled with backend.
* **Does not scale very well** - all pages render server side, so you will need more servers if you have lots of traffic.
* **Locked-in** - content is only available on browsers and not on native mobile apps.
* **Limited flexibility** - you are limited to themes and templates, e.g. if you want to build a multi-step form.
* **You need developers with particular CMS skills** - If you have a big website or are using complicated CMS features, you will need CMS developers - e.g. for SiteCore or Sitefinity.
* **It is not an API first solution**

### Pros of a Headless CMS

* **Super fast** - fast initial load time when using Static Site Generator (SSG)
* **Scales very well** - when using Static Site Generator, and the frontend can be cached via CDN
* **Ultimate flexibility** - can use SPA, Static Site Generator or even native mobile apps. Not restricted by themes, templates or vendor, and you can have multiple frontends with 1 headless CMS backend
* **Many options to build frontend** - NextJs, HUGO. Gatsby, React, Angular, etc. This makes it easier and cheaper to find developers 
* **Easy publishing** - The same content can be published to different platforms at the same time (website, web app, native mobile app)

### Cons of a Headless CMS

* **You need frontend developers** - the CMS only handles the backend content
* **Greater overhead** - to maintain the code base, DevOps, etc.
* **Limited preview functionality** - Content creator can’t preview exact content (Netlify CMS helps)

### Dead CMSs

* Microsoft SharePoint for public sites
* CommunityServer.org