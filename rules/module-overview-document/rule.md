---
seoDescription: Ensure every modular monolith has a clear, up-to-date module overview document to help teams understand, maintain, and extend the system.
type: rule
title: Do you have a module overview document for your Modular Monolith?
uri: module-overview-document
authors:
  - title: Brady Stroud
    url: https://www.ssw.com.au/people/brady-stroud
created: 2025-05-30T00:00:00.000Z
guid: b9ad75d5-0cc7-48fb-9a18-2e0d35c74e78
related:
  - modular-monoliths
  - modular-monolith-testing
---

A common pain in large modular monoliths (MoMo's) is new devs trying to work out what each module does, leading to confusion, slow onboarding and sometimes even accidentally duplicated code. Without an understanding of the module structure, teams waste time discovering module responsibilities.

<!--endintro-->

> "A well-maintained module overview is the map that keeps your monolith navigable as it grows."

## Why you need a module overview document

* **Faster onboarding:** New developers can quickly understand the system's structure and purpose of each module
* **Reduced duplication:** Teams avoid building the same functionality twice by knowing what's already there
* **Reduced Tech Debt** Avoid things going in the wrong module and creating [tech debt](/technical-debt)
* **Better communication:** A shared reference for discussions about architecture and future changes

## What does a good module overview look like?

A good overview document (e.g., `MODULES.md` or `docs/modules-overview.md`) should:

* List every module, its purpose, and key dependencies
* Be updated whenever modules are added, removed, or changed
* Be easy to find at the root or in the documentation folder
* Use a table to clearly show module names, types, and links to their documentation

Some modular monolith solutions have two types of modules:

* **Web API** modules (external, exposed to the internet via rest APIs)
* **Service** modules (internal, available via CQRS Mediatr queries and commands)

### Example - Northwind 365 Module Overview

::: greybox

**Northwind 365** is a Modular Monolith Application.  
Each Module is either a **Service** or **Web Module**.  
Read more about [Modules](https://github.com/northwind365/Northwind365/blob/main/docs/modular-architecture/modular-architecture.md)

#### Modules

| Module Name           | Type    | Link to Module README                                                          |
|-----------------------|---------|--------------------------------------------------------------------------------|
| IdentityAccess        | Web API | [IdentityAccess Module README](./IdentityAccess/README.md)                     |
| AuditTrail            | Web API | [AuditTrail Module README](./AuditTrail/README.md)                             |
| TaskRunner            | Service | [TaskRunner Module README](./TaskRunner/README.md)                             |
| IntegrationBridge     | Service | [IntegrationBridge Module README](./IntegrationBridge/README.md)               |
| Clients               | Web API | [Clients Module README](./Clients/README.md)                                   |
| DataSync              | Service | [DataSync Module README](./DataSync/README.md)                                 |
| Deployments           | Web API | [Deployments Module README](../Deployments/README.md)                          |
| Diagnostics           | Web API | [Diagnostics Module README](../Diagnostics/README.md)                          |
| Docs                  | Service | [Docs Module README](./Docs/README.md)                                         |
| Notifications         | Service | [Notifications Module README](./Notifications/README.md)                       |
| Storage               | Service | [Storage Module README](./Storage/README.md)                                   |
| Reviews               | Web API | [Reviews Module README](./Reviews/README.md)                                   |
| HealthStatus          | Service | [HealthStatus Module README](./HealthStatus/README.md)                         |
| ReferenceData         | Service | [ReferenceData Module README](./ReferenceData/README.md)                       |
| Surveys               | Web API | [Surveys Module README](./Surveys/README.md)                                   |
| LiveUpdates           | Web API | [LiveUpdates Module README](./LiveUpdates/README.md)                           |
| BusinessProcesses     | Web API | [BusinessProcesses Module README](./BusinessProcesses/README.md)               |

:::

::: info
**Tip:** Keep the overview up to date as your application evolves. Assign responsibility for maintaining it.
:::
