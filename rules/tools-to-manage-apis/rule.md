---
type: rule
archivedreason: 
title: Do you know the best tools to manage APIs?
guid: 66ea1ecd-0fb8-4aa0-a0b4-423d87577fa8
uri: tools-to-manage-apis
created: 2021-05-11T22:00:01.0000000Z
authors:
- title: William Liebenberg
  url: https://ssw.com.au/people/william-liebenberg
- title: Bryden Oliver
  url: https://ssw.com.au/people/bryden-oliver
related:
- brand-your-api-portal
- mockup-your-apis
redirects:
- comments-do-you-know-the-best-tools-to-manage-apis
- do-you-know-the-best-tools-to-manage-apis

---

When building APIs one of the challenges is in how to document the API for other developers to consume.

<!--endintro-->

Using a tool that automates this is extremely valuable as it helps avoid the biggest bugbear of developers, stale documentation. This resulted in a number of standards being developed for specifying APIs. [Swagger](https://swagger.io/) and [OpenAPI](https://www.openapis.org/) being being the most common, but there are a few others.

## Azure API Management

The best tool for use in medium to large organizations is **Azure API Management** (APIm for short). It has all the features other API Management tools and wraps everything up in a very nice UI.

By supporting Code First APIs, APIm can generate the Swagger documentation from your API code. For the developers consuming your API this is really fantastic!

APIm allows you to centralize all your APIs and provide a consistent front-end interface for developers. You also get to securely provide all your APIs behind a single static IP address.

You can use APIm to secure your APIs, improve API discoverablility, transform existing services and even mock services for testing.

**Pros:**
* Very nice UI compared to many alternatives
* Import API definitions from Swagger, OpenAPI, WSDL, etc
* Centralized API management
* API policy management (aka request processing pipeline)
  * mutate incoming and outgoing requests
  * XML to JSON and vice verca
  * Add/Remove/Modify request headers
  * Redirects
* Caching
* Rate limiting
* API Versioning
* Response Mocking
* Security features
* Developer Portal
  * API Documentation
  * Branded APIs
* Product customization
  * expose parts of any API as individual products
* Monetization (sell your API)
* Custom Identity Provider
* Free Developer Tier
* Comprehensive SLAs

**Cons:**
* Pricing is complex - Standard to Premium scales exponentially
* Lots of advanced features, requires a lot of learning

Watch Adam Cogan and William Liebenberg explain more about Azure API Management.

`youtube: https://youtu.be/fWe8ZOOhcyA`

::: good
Figure: Good Example (more comprehensive)
:::

::: greybox
For smaller organizations one of the [http://swagger.io](http://swagger.io) products may suit better. They are free to start with until you start looking for more advanced features. The feature set even on the paid tiers is still significantly more limited than Azure API Management, however the cost is also much lower.
:::

::: good
Figure: Good Example (for small teams or projects)
:::
