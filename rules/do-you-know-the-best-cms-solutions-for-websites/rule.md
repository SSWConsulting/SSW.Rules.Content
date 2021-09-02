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

### Top 6 CMS vendors of 2021 by Market Share (including eCommerce and websites)

<br>

* WordPress
* Joomla
* Drupal
* Shopify
* Squarespace
* Wix

Source: https://www.isitwp.com/popular-cms-market-share/

### Top 5 CMS vendors for Enterprise websites (.NET based)

<br>

* DotNetNuke - DNN (Open source) (pricing non-transparent)
* Umbraco (Open source) ($ - https://umbraco.com/umbraco-cms-pricing/)
* Kentico Xperience (Formerly Kentico EMS) ($$ - https://xperience.io/pricing)
* Sitefinity (pricing non-transparent)
* SiteCore ($$$ - pricing non-transparent)

Source: https://theonetechnologies.com/blog/post/top-5-dot-net-based-cms-platforms
\
\
![Figure: .NET CMS Google Trends](googletrendsnet.png ".NET CMS Google Trends")

See google trends information for these products: https://trends.google.com/trends/explore?q=dotnetnuke,sitefinity,sitecore,kentico,Umbraco

### Popular Headless CMS of 2021

<br>

* Contentful ($$ - https://www.contentful.com/pricing/)
* Magnolia (pricing non-transparent)
* Strapi (open source) (free / $ enterprise plan - https://strapi.io/pricing-self-hosted)
* Directus (open source) ($ - https://directus.io/pricing/)
* Kontent (Kentico) ($$ - https://kontent.ai/pricing)

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

For example, you can use a Headless CMS with a super fast Static Site Generator (SSG). See our rule on the [best static site tech](https://www.ssw.com.au/rules/do-you-use-the-best-static-site-tech-stack).

**The bottom line:** if you value your content over the general look and feel of the content, then you should use a Headless CMS. A Headless CMS allows you to display your data as you like, without restrictively coupling the backend content and frontend UI.

### Pros of a Traditional CMS

<br>

* **Simple and fast** - for setup and maintenance 
* **No developers needed** - for larger websites or a complicated CMS (e.g. SiteCore), this may become necessary
* **Simple to control look and feel** - using available themes and templates
* **Large community support**
* **Out of the box integrations** - payments, social media, etc.

### Cons of a Traditional CMS

<br>

* **Performance is not amazing** - the frontend is coupled with the backend.
* **Does not scale very well** - all pages render server side, so you will need more servers if you have lots of traffic.
* **Locked-in** - content is only available on browsers and not on native mobile apps.
* **Limited flexibility** - you are limited to themes and templates, e.g. if you want to build a multi-step form.
* **You need developers with particular CMS skills** - If you have a big website or are using complicated CMS features, you will need CMS developers - e.g. for SiteCore or Sitefinity.
* **It is not an API first solution**

### Pros of a Headless CMS

<br>

* **Super fast** - fast initial load time when using Static Site Generator (SSG).
* **Scales very well** - when using Static Site Generator, and the frontend can be cached via CDN.
* **Ultimate flexibility with how to use content** - can use SPA, Static Site Generator or even native mobile apps. Not restricted by themes, templates or vendor, and you can have multiple frontends with 1 headless CMS backend.
* **Many options to build frontend** - NextJs, HUGO. Gatsby, React, Angular, etc. This makes it easier and cheaper to find developers.
* **Easy publishing** - The same content can be published to different platforms at the same time (website, web app, native mobile app).

### Cons of a Headless CMS

<br>

* **You need frontend developers** - the CMS only handles the backend content.
* **Greater overhead** - to maintain the code base, DevOps, etc.
* **Limited preview functionality** - Content creator can’t preview exact content (Netlify CMS helps).

## Headless CMS Comparison: Kontent vs Contentful

<br>

Let's compare two popular CMSs:

<br>

| **Name**                     | [Kontent](https://kontent.ai/) (Recommended)                                                                                                               | [Contentful](https://www.contentful.com/)                                       |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **Video**                    | [Kontent](https://www.youtube.com/watch?v=wZLw3UKNQk8)                                                                                                     | [Contentful](https://www.youtube.com/watch?v=TNE9OAXP4R0)                       |
| **Content Modelling**        | Yes                                                                                                                                                        | Yes                                                                             |
| **Unlimited Content Types**  | Yes                                                                                                                                                        | No                                                                              |
| **SSO and MFA**              | Yes                                                                                                                                                        | Yes                                                                             |
| **GraphQL Support**          | Soon: [October 2021](https://portal.productboard.com/kontent/2-kontent-public-roadmap/c/119-allow-developers-to-query-data-more-efficiently-using-graphql) | Yes                                                                             |
| **Collections**              | [Yes](https://kontent.ai/specials/collections)                                                                                                             | No                                                                              |
| **Content Collaboration**    | Yes + [Simultaneous Editing](https://kontent.ai/blog/better-real-time-collaboration-with-simultaneous-editing)                                             | No                                                                              |
| **Task Management**          | Yes ([with more functionality](https://kontent.ai/blog/better-content-operations-for-enterprises-and-developers))                                          | [Yes](https://www.contentful.com/help/tasks/)                                   |
| **In-Context Editing**       | [Yes](https://kontent.ai/blog/in-context-editing-the-best-way-to-update-website-content)                                                                   | No                                                                              |
| **Localization**             | Yes                                                                                                                                                        | Yes                                                                             |
| **Workflows**                | Yes                                                                                                                                                        | Yes                                                                             |
| **Website Optimisation**     | Yes                                                                                                                                                        | No                                                                              |
| **Personalized Experiences** | Yes: [Uniform](https://uniform.dev/uniform-for-kontent/)                                                                                                   | Yes: [Frosmo](https://frosmo.com/frosmo-with-contentful/)                       |
| **Transparency**             | Good + [feature release roadmap](https://portal.productboard.com/kontent/2-kontent-public-roadmap/tabs/7-upcoming-public-releases)                         | [Good](https://www.contentful.com/whats-new/)                                   |
| **Pricing**                  | [Premium](https://kontent.ai/pricing): $30,000 pa (cheaper with scaling)                                                                                   | [Team](https://www.contentful.com/pricing/): $24,000 pa (with Compose + Launch) |

<br>

**The bottom line:** we recommend Kontent as the Headless CMS of choice because it has better UI editing features, better [Content Modelling](https://docs.kontent.ai/tutorials/set-up-kontent/content-modeling/what-is-content-modeling) features, is more future-proofed with its Content Modelling, and has more scalable pricing.

Source: https://kontent.ai/compare/contentful

## Dead CMSs

<br>

* Microsoft SharePoint for public sites
* CommunityServer.org