---
type: rule
archivedreason: 
title: Do you conduct an architecture review every few Sprints?
guid: f1401eba-50d4-4c6e-bb16-3959b9c2920c
uri: do-you-conduct-an-architecture-review-after-every-sprint
created: 2009-02-26T02:02:17.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ulysses Maclaren
  url: https://ssw.com.au/people/ulysses-maclaren
- title: Cameron Shaw
  url: https://ssw.com.au/people/cameron-shaw
- title: Justin King
  url: https://ssw.com.au/people/justin-king
related: []
redirects:
- do-you-conduct-an-architecture-review-every-few-sprints

---

There are 2 main parts to any application. The UI which is what the customer can see and provide feedback on, and the underlying code which they really can't know if it is healthy or not.

Therefore it is important to conduct a '[test please](/conduct-a-test-please-internally-and-then-with-the-client)' on the internal code and architecture of the application.

Ideally conduct a small 'Code + Architecture Review' for every sprint. Assuming a 2 week sprint, schedule a 4 hour (2 architects x 2 hours) review.

<!--endintro-->

The following are items that are addressed in an architecture/code review:

**Background information/overview of the project**

* Current system
* Objectives of the system
* Number of users (internal, external, edit, read only)
* Current technologies
* Current environment (SOA, SOE)

**Points for discussion**

* Rich client
* Web client
* Smart client (any disconnected users?)
* Technology choices
    * Persistence layer (e.g. Database)
    * Business layer
    * UI
    * Communications
    * Workflow
    * Integration - external systems
* Requirements for 'package' software
    * PerformancePoint
    * Reporting Services
    * Accounting packages
    * SharePoint
* Usage Telemetry
* Performance Monitoring
* Data migrations
* Data reporting
* User experience
* Network
* Responsibilities/players
* Infrastructure
    * Network
    * Hardware
* Deployment
    * Staged implementation
    * In parallel
    * Development/Test/Staging/Production
* Disaster recovery
* Change control/source control
* Build Server
* Performance
* Scalability
* Extensibility
* Design patterns
* Maintainability
* Reliability (failover servers?)
* 'Sellability' i.e. is the solution appropriate for the client?


::: info
**Note:** If you are using Enterprise Architect, be aware of [technical debt](/technical-debt):

* Add a datetime of the last time the diagram was modified so we have an indication of when it is out of date
* On your diagrams, be aware that some parts are done and some are not.
:::
