---
type: rule
title: Do you know the value of Event Storming?
uri: event-storming
authors:
  - title: William Liebenberg
    url: https://www.ssw.com.au/people/william-liebenberg
  - title: Matt Wicks
    url: https://www.ssw.com.au/people/matt-wicks
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
related:
  - user-journey-mapping
  - event-storming-workshop
created: 2022-07-04T07:46:30.373Z
guid: 9d76ab58-ad71-4cb1-af08-68330f7e3a8e
---

Often when building systems it isn't super clear what all the nuts and bolts should be. The complexity of projects can vary quite a lot - and getting customers to tell us what they need is not easy. There might be several major stakeholders or domain experts each with slightly different ideas understanding that causes contention in how the system functions. Being a good consultant requires good listening and then good analytical skills to determine the customer's technical needs.

[Event Storming](https://www.eventstorming.com) is a fun collaborative modeling technique invented by [Alberto Brandolini](https://twitter.com/ziobrando) that enables members from different teams and disciplines to participate in workshops to learn how to break down complex business domains and processes.  

<!--endintro-->

`youtube: https://youtu.be/YeRfugbKuHk`

**Video: Do you know the value of Event Storming? with William Liebenberg (6 min)**

### The benefits of Event Storming

Having the client just talking to our consultants for a couple of days can be intense and it's difficult to stay engaged (on both sides), this is where Event Storming shines. Event Storming is fun and helps us to break down the complex requirements with hands-on client participation. We also get an awesome deliverable that we can use to develop a backlog and "better" estimates.

Another benefit of Event Storming is helping you determine the correct System Architecture. For instance choosing between a Monolith or Microservice architecture by looking at the groupings of domain events, commands and policies (aka Bounded Contexts if you are talking in pure Domain Driven Design DDD terms).

### Event Storming can be done at different levels

There are multiple levels that Event Storming workshops can be run at. Each level continues to refine and enrich the domains with new concepts until a full end-to-end flow of the system is visualized. This end-to-end flow is valuable to the business itself but also helps accelerate software design and development.

#### Big Picture (aka 30,000 foot view)

* Explore the whole business across multiple boundaries by gathering people who each own/understands one part of the truth
* All Domain events are described in past tense (past tense because it's an event that happened, its a fact that cannot be changed)
* Capture hotspots or points of contention in a domain (this is usually when the experts don't all agree on a concept)
* Map the relationships between the domain and external dependencies

**Example events:**

🟧 InvoiceCreated

🟧 InvoiceReceived

🟧 EmailSent

🟧 ReportUpdated


#### Process Modeling (aka 10,000 foot view)

* Model a single business process from beginning to end and ensure no ambiguity or contention exists by clarifying all the business rules
* Enforce a timeline so that you can move events into the right order, and eventually see a process or flow emerging.
* Attach the actors, their motivations, and any dependencies required for executing actions (aka Commands)
* Enable stakeholders, domain experts and developers to communicate via **ubiquitous language** (all participants are able to communicate using the same terminology)

#### Software Design

* Now we have an end-to-end model of the system
* All relevant concepts are captured and documented
* The software design phase can proceed using methods from Domain-Driven Design (DDD), [Clean Architecture](/rules-to-better-clean-architecture) and [CQRS](/use-the-mediator-pattern-with-cqrs). Each sticky note can potentially turn into a Product Backlog Item during the software development phase.

![Figure: Levels of Event Storming](event-storming-levels.png)

Notice as you traverse the levels from top to bottom that new concepts are introduced that help describe the domain or process which gets us closer to being able to build a concrete software solution.  

### How to start an Event Storming workshop

To start an Event Storming workshop, get all the stakeholders, domain experts and developers into a room or virtual call. 

From here everyone starts to write out all the events they think are necessary on the sticky notes and put the sticky notes on the *real* or *virtual* wall. 
 
Check out [how to run an Event Storming workshop](/event-storming-workshop) for detailed steps and more information on how to prepare and run an Event Storming workshop.

### Key concepts in Event Storming

Different colored sticky notes should be used to denote different concepts:

<svg width="1.4em" height="1em" style="display: inline-block;"><rect width="1em" height="1em" rx="0.15em" ry="0.15em" x="0.2rem" y="0em" style="fill:rgb(255,102,0);"/></svg> **Domain Events** - Orange  

<svg width="1.4em" height="1em" style="display: inline-block;"><rect width="1em" height="1em" rx="0.15em" ry="0.15em" x="0.2rem" y="0em" style="fill:rgb(255,255,153);"/></svg> **Actors (aka Personas)** - Light Yellow  

<svg width="1.4em" height="1em" style="display: inline-block;"><rect width="1em" height="1em" rx="0.15em" ry="0.15em" x="0.2rem" y="0em" style="fill:rgb(255,0,148);"/></svg> **Policies (aka Business Process)** - Pink  

<svg width="1.4em" height="1em" style="display: inline-block;"><rect width="1em" height="1em" rx="0.15em" ry="0.15em" x="0.2rem" y="0em" style="fill:rgb(0,51,255);"/></svg> **Commands** - Blue  

<svg width="1.4em" height="1em" style="display: inline-block;"><rect width="1em" height="1em" rx="0.15em" ry="0.15em" x="0.2rem" y="0em" style="fill:rgb(255,204,0);"/></svg> **Aggregate** - Yellow  

<svg width="1.4em" height="1em" style="display: inline-block;"><rect width="1em" height="1em" rx="0.15em" ry="0.15em" x="0.2rem" y="0em" style="fill:rgb(102,0,153);"/></svg> **External System** - Purple 

<svg width="1.4em" height="1em" style="display: inline-block;"><rect width="1em" height="1em" rx="0.15em" ry="0.15em" x="0.2rem" y="0em" style="fill:rgb(0,153,0);"/></svg> **Read Model** - Green

You can use whatever colors you can find, as long as a legend is always visible to the team.

![Figure: Example of Domain Events, Commands, Actors, etc. arranged underneath the Aggregate](event-storming-example-stickies.png)

![Figure: Example events and timeline of a booking system](event-storming-03.jpeg)
