---
seoDescription: Upgrade your website seamlessly with efficient redirects using Cloudflare Workers or Azure Front Door to preserve SEO and traffic during the migration
type: rule
archivedreason:
title: Do you know you to handle redirects?
guid: 746cfdd5-68d6-4080-b4c8-af73daa2769e
uri: handle-redirects
created: 2024-06-14T06:32:40.0000000Z
authors:
  - title: Aman Kumar
    url: https://ssw.com.au/people/aman-kumar
related:
  - do-you-use-cdn-for-js-files
---

When migrating your old website to a new technology stack, maintaining SEO and avoiding potential 404 errors is crucial. Implementing redirects ensures smooth traffic transition and preserves your SEO rankings.

<!--endintro-->

### Choosing the Right Redirect Method

#### 1. Application Level

Client-Side Redirects: Easy but poor for SEO and maintenance. Migrating pages in the future would make this approach cumbersome.

Server-Side Application: A dedicated web app can handle redirects, but maintenance and scalability become challenging over time.

#### 2. CDN Level (Global)

Edge Level Redirects: Ideal for global distribution and ease of management. Solutions like Azure Front Door or Cloudflare can be effective.

### ❌ Azure Front Door

- [Limit of 800 deployments per resource group](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits).
- Maximum of 100 redirects per route.
- Deployment via Bicep can be lengthy.
- Generally expensive.

### ✅ Cloudflare Workers

- Offers customizable redirects through scripts hosted within Cloudflare CDN.
- Cost-effective and straightforward to deploy using Wrangler CLI.
- Efficiently manage hundreds of redirects without delays.

For a seamless migration and efficient redirect management, leveraging a CDN-level solution like [Cloudflare Workers](https://developers.cloudflare.com/workers/) is recommended.
