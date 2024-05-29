---
type: rule
title: Migrating frontend to .NET 8
uri: migrating-frontend-to-net8
authors:
  - title: Chris Clement
    url: https://www.ssw.com.au/people/chris-clement/
related:
  - migration-plans
  - modernize-your-app
  - do-you-know-where-to-host-your-frontend-application
created: 2024-05-29T00:54:42.810Z
authors:
  - title: Chris Clement
    url: https://www.ssw.com.au/people/chris-clement/
guid: d38c1c55-8f32-403c-86c5-c97760fd7d0a
---

In the case where the legacy .NET Framework application is hosting the frontend, it is recommended to also think about the hosting method of the frontend in .NET 8.

This issue is best to be considered when before or during the migration so the team will not spend time on implementing something that will be removed shortly in the future.


<!--endintro-->

Depending on the scenario and the situation of the projects, there are many options available to host the frontend with .NET 8. Here are couple of the many options available.

### Option 1: Keep hosting frontend integrated with .NET 8 

No changes to the flow, keep hosting the frontend the same way as before (e.g. bundling the frontend build artifacts as a static resource in .NET 8).

- **Pros:**
  - 🟢 Simple setup with no need for additional infrastructure
  - 🟢 Familiar workflow if migrating from .NET Framework

- **Cons:**
  - ❌ Frontend and backend must be built and deployed together
  - ❌ Less flexibility for future scalability and updates



#### Option 2: Host frontend on its own

This option fully separate the frontend from the backend. This requires serving the frontend on a separate hostname or using a gateway service to redirect API with frontend routes.
e.g. Hosting frontend in Azure Static WebApp and use Azure Frontdoor to route requests to frontend on frontend routes and backend routes to the .NET 8 application.

- **Pros:**
  - 🟢 Future-proof hosting that allows for independent frontend updates
  - 🟢 Supports preview environments for testing
  - 🟢 Faster build times due to separate frontend and backend builds
  - 🟢 Direct CDN integration (e.g. with Azure front door), improving performance

- **Cons:**
  - ❌ More complex deployment story
  - ❌ Higher infrastrucure cost
  - ❌ Requires extra configuration and management effort

 

#### Option 3: Host frontend externally, serve it together with .NET 8

Hosting your frontend application in a separate storage (e.g. in Azure Blob Storage) is the mixed transitionary approach where the frontend artifacts is hosted separately from the backend, and backend will pass these artifacts to the frontend without staticly embed the resource in the backend.
This option still allows a clean separation of concerns, allowing for independent scaling and deployment of the frontend and backend, while also sit in a transition where we have the option to host the frontend standalone, similar to Option 2 setup.

- **Pros:**
  - 🟢 Faster build times due to separate frontend and backend builds
  - 🟢 Similar serving setup as before

- **Cons:**
  - ❌ Slighly more complex deployment story
  - ❌ Requires extra configuration and management effort
  - ❌ Increased ingress network load to the backend



::: greybox

Option 2 is typically preferred for future proofing, but Option 3 can also be recommended for its balance of cost, build efficiency, and future flexibility. Remember to weigh these factors in the context of your project's specific needs and constraints.

:::


::: good 

Figure: Good Example - Deciding on frontend hosting, considering its scalability and cost benefits.

:::

 
### Best Practices


- **Cost-Effectiveness:** Evaluate the cost against benefits for each option. If budget is tight, Option 1 is less costly while Option 3 offers a good balance.

- **Development Workflow:** Consider the impact on your development workflow. Option 2 and Option 3 promote a more decoupled architecture, which could be beneficial for teams.

- **Performance:** Assess how each option affects the performance of your application. Decoupling the frontend can offer performance benefits through CDN caching.

- **Future Proofing:** Think long-term. Option B and C provide more flexibility for future changes and scalability.


By carefully assessing your needs and understanding the trade-offs of each option, you can make an informed decision on how to serve your Angular applications in a .NET 8 environment.


