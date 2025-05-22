---
type: rule
title: Do you Health Check your Infrastructure?
seoDescription: Website dependency and infrastructure health checks
uri: infrastructure-health-checks
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Lewis Toh
    url: https://ssw.com.au/people/lewis-toh
  - title: Luke Cook
    url: https://ssw.com.au/people/luke-cook
related:
  - have-a-healthcheck-page-to-make-sure-your-website-is-healthy
redirects:
  - do-you-have-a-healthcheck-was-zsvalidate-page-to-test-your-website-dependencies
  - do-you-have-a-healthcheck-(was-zsvalidate)
  - page-to-test-your-website-dependencies
  - have-a-healthcheck-page-to-test-your-website-dependencies
created: 2020-03-12T20:57:37.000Z
archivedreason: null
guid: 015fcac3-c2c2-4d25-a6cd-1317eed69fc6
---
Most developers include [health checks for their own applications](/have-a-healthcheck-page-to-make-sure-your-website-is-healthy/), but modern solutions are often highly dependent on external cloud infrastructure. When critical services go down, your app could become unresponsive or fail entirely. Ensuring your infrastructure is healthy is just as important as your app.

<!--endintro-->

## Your app is only as healthy as its infrastructure

Enterprise applications typically leverage a large number of cloud services; databases, caches, message queues, and more recently LLMs and other cloud-only AI services. These pieces of infrastructure are crucial to the health of your own application, and as such should be given the same care and attention to monitoring as your own code. If any component of your infrastructure fails, your app may not function as expected, potentially leading to outages, performance issues, or degraded user experience. Monitoring the health of infrastructure services is not just a technical task; it ensures the continuity of business operations and user satisfaction.

`youtube: https://www.youtube.com/watch?v=ldj9YKz6FiA`
**Figure: Health Check Infrastructure | Toby Churches | Rules (3 min)**

## Setting Up Health Checks for App & Infrastructure in .NET

To set up health checks in a .NET application, start by configuring the built-in health checks middleware in your Program.cs (or Startup.cs for older versions). Use AddHealthChecks() to monitor core application behavior, and extend it with specific checks for infrastructure services such as databases, Redis, or external APIs using packages like AspNetCore.HealthChecks.SqlServer or AspNetCore.HealthChecks.Redis. This approach ensures your health endpoint reflects the status of both your app and its critical dependencies.

👉 See detailed implementation steps in the **video above**, and refer to the official [Microsoft documentation](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/health-checks?view=aspnetcore-9.0) for further configuration examples and advanced usage

## Alerts and responses

Adding comprehensive health checks is great, but if no-one is told about it - what's the point? There are awesome tools available to notify Site Reliability Engineers (SREs) or SysAdmins when something is offline, so make sure your app is set up to use them! For instance, Azure's [Azure Monitor Alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview) and AWS' [CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) provide a suite of configurable options for who, what, when, and how alerts should be fired.

## Health check UIs

Depending on your needs, you may want to bake in a health check UI directly into your app. Packages like [AspNetCore.HealthChecks.UI](https://www.nuget.org/packages/AspNetCore.HealthChecks.UI/) make this a breeze, and can often act as your canary in the coalmine. Cloud providers' native status/health pages can take a while to update, so having your own can be a huge timesaver.

![Figure: AspNetCore.HealthChecks.UI gives you a healthcheck dashboard OOTB](https://raw.githubusercontent.com/Xabaril/AspNetCore.Diagnostics.HealthChecks/refs/heads/master/doc/images/ui-home.png)

## Tips for Securing Your Health check Endpoints

Keep health check endpoints internal by default to avoid exposing sensitive system data.

## Health Checks in Azure

When deploying apps in Azure it's good practice to enable health checks within the Azure portal. The Azure portal allows you to perform health checks on specific paths for your app service. Azure pings these paths at 1 minute intervals ensuring the response code is between **200** and **299**. If 10 consecutive responses with error codes accumulate the app service will be deemed unhealthy and will be replaced with a new instance.

::: good
![Figure: Good example - Performing a health check on an azure app service](image-3-.png)
:::

### Private Health Check – Best Practices

✅ Require authentication (API key, bearer token, etc.)

✅ (Optional) Restrict access by IP range, VNET, or internal DNS

✅ Include detailed diagnostics (e.g., database, Redis, third-party services)

✅ Integrate with internal observability tools like Azure Monitor

✅ Keep health checks lightweight and fast. Avoid overly complex checks that could increase response times or strain system resources.

✅ Use caching and timeout strategies. To avoid excessive load, health checks can timeout gracefully and cache results to prevent redundant checks under high traffic. See more details on official [Microsoft's documentation](https://learn.microsoft.com/en-us/samples/dotnet/aspire-samples/aspire-health-checks-ui/).

## Handle offline infrastructure gracefully

| Category         | Example Services                                                      |
| ---------------- | --------------------------------------------------------------------- |
| **Critical**     | Database, Redis cache, authentication service (e.g., Auth0, Azure AD) |
| **Non-Critical** | OpenAI API, email/SMS providers, analytics tools                      |

**Table: Example of Critical and Non Critical Services in an application**

When using non-critical infrastructure like an LLM-powered chatbot, make sure to implement graceful degradation strategies. Instead of failing completely, this allows your app to respond intelligently to infrastructure outages, whether through fallback logic, informative user messages, or retry mechanisms when the service is back online.

::: bad
![Figure: Bad example – The user is given the chance to interact with a feature that is currently unavailable.](infra-bad-example.png)
:::

::: good
![Figure: Good example – The user is pre-emptively shown a message that shows this feature is currently unavailable.](infra-good-example.png)
:::
