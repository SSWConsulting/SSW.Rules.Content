---
type: rule
title: Do you know where to host your Frontend application?
guid: 4481526b-a691-4570-87d3-a9d474ae0dfd
uri: do-you-know-where-to-host-your-frontend-application
redirects:
  - do-you-know-where-to-host-frontend
created: 2024-05-29T00:54:42.810Z
authors:
  - title: Chris Clement
    url: https://www.ssw.com.au/people/chris-clement/
related: 
  - migrating-frontend-to-net8

---

When building a frontend application for your API, there's a point where the team needs to choose where and how to host the frontend application.
Choosing the right hosting option is critical to scalability, available features, and flexibility of the application.

<!--endintro-->

There are two primary ways to serve your frontend (e.g. Angular) application depending on where the frontend is hosted:

* **Option 1: Integrated with backend**

    The frontend is served by the backend API. Both frontend and backend are hosted on the same server.
    This is usually the easiest way and what the ASP.NET 8 Web Application starter Angular template has.

    Pros & Cons:
  * 🟢 Simple deployment story; backend and frontend will always be in the same version
  * 🟢 Ability to put business logic before serving the frontend
  * 🟢 Ability to serve server-side frontend
  * 🟢 No cross-origin requests
  * ❌ Difficult to scale
  * ❌ Complicated development workflow for multi-team projects
  * ❌ Backend deployment is tied to frontend deployment

* **Option 2: Externally hosted**

    The frontend is served standalone on its own separate host. The backend is hosted on a different server.

    Pros & Cons:
  * 🟢 Highly scalable
  * 🟢 Access to CDN
  * 🟢 Reduced backend load
  * 🟢 Flexible technology options - e.g. swapping technology is easier
  * ❌ More complicated deployment
  * ❌ Higher cost

Based on the pros and cons of each option above, the recommended options are:

* **For small to medium-sized projects** with less complicated requirements: **Option 1: Integrated with backend** is the recommended option since it allows faster development without having to worry too much about infrastructure.
* **For larger projects** or projects with complicated requirements: **Option 2: Externally hosted** is the recommended option since it is more scalable and more flexible with infrastructure or technology changes.
