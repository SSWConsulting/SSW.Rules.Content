---
type: rule
title: Microservices - Do you break down your apps?
uri: microservices
authors:
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
  - title: Matt Wicks
    url: https://www.ssw.com.au/people/matt-wicks
created: 2021-11-11T05:54:22.790Z
guid: e4d0411a-6184-4f16-9caf-f522bb07c703
---
N-Tier applications have their place. They are easy to get going and often make a lot of sense when you are starting out. However, sometimes your app may grow in size and become difficult to maintain. Then you might want to consider Microservices...

<!--endintro-->

Microservices let you break down your app into little pieces to make them more manageable, replaceable and maintainable.

.NET 6 and Azure have heaps of great tools for developing simple APIs and worker services in a Microservices pattern.

## The tools of the trade

[Minimal APIs](https://devblogs.microsoft.com/dotnet/asp-net-core-updates-in-net-6-preview-4/#introducing-minimal-apis) give you a way to write APIs in just a few short lines of code

[.NET Worker Services](https://docs.microsoft.com/en-us/dotnet/core/extensions/workers) let you scale your services up and down on an as need basis

[Azure Container Apps](https://azure.microsoft.com/en-us/services/container-apps/#overview) give you a way to host different little subsections of the app


## What's the point?

* Cost - Provides separation of scalability, keep the hot parts of your app hot and the cold parts of your app cold to achieve maximum pricing efficiency
* Maintainability - Keep code more manageable by making it bite sized chunks
* Simplify code - Write minimal APIs
* Deployment - Standardize deployment with containers
* Testing - Easier to find problems since they are isolated to a specific part of the app

## What's the downside?
* Upfront Cost - More upfront work is required
* Communication Complexity - While individual apps are simpler, the communication between different parts of the app can become more complex