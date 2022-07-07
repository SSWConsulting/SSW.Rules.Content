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
created: 2022-07-04T07:46:30.373Z
guid: 9d76ab58-ad71-4cb1-af08-68330f7e3a8e
---
Often when building systems it isn't super clear what all the nuts and bolts should be. There might be several major stakeholders or domain experts each with slightly different ideas understanding that causes contention in how the system functions. 

[Event Storming](https://www.eventstorming.com/) is a fun collaborative modeling technique invented by [Alberto Brandolini](https://twitter.com/ziobrando) that enables members from different teams and disciplines to participate in workshops to learn and breaking down complex business domains and processes. 
            
<!--endintro-->

Simple Intro:
`youtube: https://youtu.be/Y7NzXl-ahtU`

Detailed Intro:
`youtube: https://youtu.be/a0lWpjlSRA0`

Alternative Intro:
`youtube: https://youtu.be/-RjsdYwsAac`

### Event Storming can be done at different levels

* Big Picture (aka 30,000 foot view)
  
  -  Explore the whole business across multiple boundaries by gathering people who each own/understands one part of the truth

* Process Modeling (aka 10,000 foot view)

  -  model a single business process from beginning to end and ensure no ambiguity or contention exists by clarifying all the business rules

* Software Design (aka As high as the swing goes)

  - start the software design using methods from Domain-Driven Design (DDD), [Clean Architecture](https://www.ssw.com.au/rules/rules-to-better-clean-architecture) and [CQRS](https://www.ssw.com.au/rules/use-the-mediator-pattern-with-cqrs). Each sticky note can potentially turn into a Product Backlog Item during the software development phase.

![](https://www.agilepartner.net/wp-content/uploads/Levels.png)
Figure: Levels of Event Storming (original source: https://www.agilepartner.net)

Notice as you traverse the levels from top to bottom that new concepts are introduced that help describe the domain or process which gets us closer to being able to build a concrete software solution.  

### How to start an Event Storming workshop

To start an Event Storming workshop, get all the stakeholders, domain experts and developers into a room and hand out sticky notes and pens. 

From here everyone starts to write out all the events they think are necessary on the sticky notes and put the sticky notes on the wall. 

Alternatively, an online platform like [Miro](https://miro.com/) could be used to do it virtually.

Different colored sticky notes should be used to denote different concepts:

🟧 Domain Events - Orange

🟨 Actors (aka Personas) - Yellow

⬜ Business Process (aka Policies) - White

🟦 Commands - Blue

🟨 Aggregate - Light Yellow

🟪 External System - Pink/Purple

🟩 Read Model - Green

You can use whatever colors you can find, as long as a legend is always visible to the team.

TODO: INSERT THE COOL IMAGE I MADE IN POWERPOINT

### The phases of Event Storming

There are multiple phases to facilitating an Event Storming workshop. Each phase continues to refine and enrich the domains with new concepts until a full end-to-end flow of the system is realized. In the end this end-to-end flow is valuable to the business itself but also help accelerate the software design and development phase.

#### 1. Discover Domain Events
- Be relevant for the domain experts in the room
- All Domain events are described in Past Tense

  - InvoiceCreated
  - InvoiceReceived
  - EmailSent
  - ReportUpdated

#### 2. Enforce Timeline
- By enforcing a timeline you can move events into the right order, and eventually see a process or flow emerging

#### 3. Walkthrough
- Understanding and discussing the big picture
  - capture hotspots or points of contention in a domain
  - what an action should be from a user perspective
  - enable business and tech to avoid miscommunication 
  - avoid building expensive misaligned software

#### 4. Complete the picture
- Including actors, motivations, dependencies
- people and purpose of events
- mapping the relationships between domain and external dependencies

#### 5. Observe the outcome
- Now we have an End-to-end model of the system
- All relevant concepts are captured and documented
- For different scenarios this enables anyone to gain understanding of the end-to-end flow of the system (e.g. onboarding)

### Scenario - Invoicing

Phase 1 - Bob, Linda and Sam all get together to storm out their new invoicing system. Some of the events they might all come up with include:

* InvoiceCreated
* InvoiceUpdated
* InvoicePaid
* InvoicePrinted
* and many more...

Phase 2 - The events are then arranged on a timeline to visualize the flow of the invoicing system.

Phase 3 - Discovering what issues could arise with the current system. For example:
- "What if Adam does not pay an invoice by the due date?"
- "What is we over charged the client and need to issue a refund?"

Phase 4 - Add actors or personas to each event. Discover the commands and dependencies of each event by asking:
- "What does the Sales Manager need to do update invoices?"
- "Does the read model contain all the necessary information?"
- "Which external systems are required for this event to occur?"
- ...

Phase 5 - Bob, Linda and Sam now have a nicely visualized process for their invoicing system which is also fully documented. As far as they are concerned, nothing has been left ambiguous and everyone agrees on how the system works. 
