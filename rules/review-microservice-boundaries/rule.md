---
seoDescription: Microservice boundaries are hard. Keep your product healthy, scalable, and successful by reviewing your boundaries regularly.
type: rule
title: Do you regularly review your Microservice boundaries?
uri: review-microservice-boundaries
authors:
  - title: Luke Cook
    url: https://www.ssw.com.au/people/luke-cook
  - title: Daniel Mackay
    url: https://www.ssw.com.au/people/daniel-mackay
related:

created: 2024-10-25T01:09:23.840Z
guid: f10dba3f-e56a-4289-9127-9cb48e40a7f6
archivedreason: null
---
Microservice architecture poses some unique challenges that can often trip up even the most experienced development teams. One of the hairiest problems is creating well-defined boundaries between your services, and the ideal Microservice architecture often differs from what was originally drawn on the whiteboard. So how do you tell if you got it right?
<!-- endintro -->

## Map your Microservice architecture

* Draw your Microservices on a whiteboard
* Whenever one Microservice needs to communicate with another, draw a line between them. If there are several distinct integration points between the same 2 Microservices, add a "+1" or "+2" or "+N" to the line, indicating how many distinct calls those services share. For every paired Microservice, list all the integration points, with particular focus on *why* this integration exists, and the *frequency* in which it occurs (ie rarely, frequently, every time). For example: `OrdersService.Create(...)->Customers.GetCustomer(...). Frequency: every request.`.

![Microservice maps can get intense](bad-example-microservice-boundaries.png)
**Figure: Incorrect boundaries result in spaghetti services**

### Identify hotspots

* Flag "chatty" services - ie, those services that have the most number of integration points
* Flag *blocking calls* - ie, if a particular Microservice must wait on downstream/dependent service call before completing
* Flag *local caches* - ie, if Microservice A keeps a local cache of Microservice B's data

Hotspots are often a **code smell** that could point to Microservices being tightly coupled. These are telltale signs that the boundaries between those services may be in need of adjusting.

## Compare and contrast with BAU

In order to measure your Microservice boundary health, you should see what path a "typical" use case takes through your Microservice.
A great way of performing this exercise is using your [event storming](https://ssw.com.au/rules/event-storming) artefacts (if you haven't previously gone through an event storming exercise, it's highly recommended you do so).

Another great DDD method is [context mapping](https://www.infoq.com/articles/ddd-contextmapping/), which helps make context boundaries more explicit.

Pick the most common or business-critical use case for your business (if there are several, repeat this exercise per use case). Map out your user's journey through your current Microservice ecosystem.

## Reflect and adjust

You will often find obvious groupings of Microservices divided by "pivotal moments" in your user journey, with a sprinkling of "shared" or cross-boundary services (like an email notification service). These grouped services may better serve your application by being merged into a singular Microservice (or [Modular Monolith](https://ssw.com.au/rules/rules-to-better-modular-monoliths)).

### Don't ignore the problem

It can be daunting to consider architectural changes to a Microservices application, and difficult to justify such changes to business stakeholders. However, it's an accepted fact in Microservice design that bounded contexts are an incredibly difficult thing to get right, and wrong boundaries can accrue **technical debt** quickly due to the snowball effect that "hacks" can have on a distributed system. When ignored, this technical debt can rapidly (and covertly) alter your entire system from Microservice architecture to a [distributed monolith](https://medium.com/simpplr-technology/microservices-architecture-the-hard-parts-trap-of-distributed-monolith-7d707858aa32). At that point, you're in a world of hurt.

### Put the next session in your calendar now

Microservices require a significantly more architectural discipline than traditional monolithic systems, for the reasons mentioned above. As such, this exercise should be repeated regularly to prevent your microservice ecosystem getting the better of you.

Even when you *do* get your boundaries right, they will inevitably change over time as the domain model is changed to reflect new features and insights into the business.
