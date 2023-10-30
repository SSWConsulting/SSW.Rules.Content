---
type: rule
title: Do you know how to run an Event Storming workshop?
uri: event-storming-workshop
authors:
  - title: William Liebenberg
    url: https://www.ssw.com.au/people/william-liebenberg
related:
  - event-storming
created: 2022-08-03T05:42:33.397Z
guid: 6cd97f44-7b65-4718-bf57-0db7f92d5c75
---
[Event storming](/event-storming) is fun! Running a successful workshop requires preparation and understanding of the Event Storming process. 

Every workshop has an Event Storming Master (aka Facilitator or Moderator) to guide participants through the workshop.

<!--endintro-->

## What are the responsibilities of the Event Storming Master?

The person taking on the role of Event Storming Master does not need to be the project Scrum Master or Technical Lead - as long as they know and understand the Event Storming concepts and discovery steps then they can run the workshop.

### Before a workshop

Before a workshop, the Event Storming Master is responsible for: preparing the Event Storming workshop session which will include:

* finding the right participants
* allowing the right amount of time
* finding the right space (physical or virtual)

### During a workshop

During a workshop, the Event Storming Master is responsible for helping participants to:

* follow the Event Storming rules
* focus on the learning the modelling of the business domain 
* ask the right questions when getting stuck
* timeboxing the discovery steps

## Invite the right people

It is important to invite the right people to the workshop. Missing key participants or having too many participants

- Developers or Engineers usually ask the right questions
- Domain experts are the people who will answer the questions
- Dedicated Event Storming Master that will help guide the participants through the workshop

## Schedule the right amount of time

Depending on the size and complexity of the project you would typically need between 2 to 4 hours for a good Event Storming workshop session.

During a [Specification Review](/conduct-a-spec-review) you can schedule this workshop on the first day. Typically on the second day you can use the Event Storming visuals to help design your system and software architecture and produce better estimates.

## Preparation - In person workshop  

* Different colored sticky notes
* Marker pens
* Long roll of paper or 
* Wide white-board or 
* Office glass walls or windows

It is important to make sure that the common terms are recorded and clearly visible during the workshop.

Finally, make sure that the legend (explaining all the key concepts of Event Storming) is clearly visible. 
 
## Preparation - Choosing the right visualization tool

Real-time collaboration (remote or in-person) has become the default choice for many teams. Instead of sticky notes and white-boards we can use tools such as:

* [Miro](https://miro.com/)
* [Lucidcharts](https://www.lucidchart.com)
* [Diagrams.net](https://www.diagrams.net/). 

These tools will eliminate the worry of low-quality sticky notes falling off the white-board and your markers drying up!

For remote sessions, collaboration might not be as smooth as the in person events. However, it is also easier to arrange the attendees to join a remote session when the team is not all in a single location.

## Discovery Steps

You can break the workshop down into a number of distinct discovery steps. Each step adds more detail to the business domain or process you are trying to understand.

1. <svg width="1.4em" height="1em" style="display: inline-block;"><rect width="1em" height="1em" rx="0.15em" ry="0.15em" x="0.2rem" y="0em" style="fill:rgb(255,102,0);"/></svg> Domain events
2. <svg width="1.4em" height="1em" style="display: inline-block;"><rect width="1em" height="1em" rx="0.15em" ry="0.15em" x="0.2rem" y="0em" style="fill:rgb(255,0,0);"/></svg> Concerns and questions
3. <svg width="1.4em" height="1em" style="display: inline-block;"><rect width="1em" height="1em" rx="0.15em" ry="0.15em" x="0.2rem" y="0em" style="fill:rgb(0,51,255);"/></svg> Domain Commands and <svg width="1.4em" height="1em" style="display: inline-block;"><rect width="1em" height="1em" rx="0.15em" ry="0.15em" x="0.2rem" y="0em" style="fill:rgb(255,255,153);"/></svg> Personas
4. <svg width="1.4em" height="1em" style="display: inline-block;"><rect width="1em" height="1em" rx="0.15em" ry="0.15em" x="0.2rem" y="0em" style="fill:rgb(0,153,0);"/></svg> Read Models and <svg width="1.4em" height="1em" style="display: inline-block;"><rect width="1em" height="1em" rx="0.15em" ry="0.15em" x="0.2rem" y="0em" style="fill:rgb(255,204,0);"/></svg> Aggregates
5. <svg width="1.4em" height="1em" style="display: inline-block;"><rect width="1em" height="1em" rx="0.15em" ry="0.15em" x="0.2rem" y="0em" style="fill:rgb(102,0,153);"/></svg> External Systems
6. <svg width="1.4em" height="1em"><rect width="1em" height="1em" rx="0.15em" ry="0.15em" x="0.2rem" y="0em" style="fill:rgb(255,0,148);"/></svg> Policies

### Step 1: Discovering Domain Events

Use the orange <svg width="1.4em" height="1em" style="display: inline-block;"><rect width="1em" height="1em" rx="0.15em" ry="0.15em" x="0.2rem" y="0em" style="fill:rgb(255,102,0);"/></svg> sticky notes for Domain Events.

The domain experts and stakeholders can simply start recording the events that occur in a business domain or process. The events don't necessarily need to be in a precise timeline order (yet).

Domain events are always rooted in the **past tense** to represent a fact. Facts cannot be changed because they actually happened. 

For example, we can have domain events such as `Invoice Created` `Email sent` `Timesheet Updated`.

It can be expected that not all the participants will be aligned with the business domain or process at the start, but as the workshop progresses everyone will start to "get into the zone" and ideas will be put onto the board quickly and smoothly.

When there are concerns or contention, the participants can discuss and rearrange the events until it is resolved and everyone is aligned in their thinking. Sometimes the contention is due to a different terminology, so it is important to record the common terms and make sure that they are clearly visible to all participants.

The Event Storming Master should check the stickies to ensure that the basic rules are being followed (such as ensuring events are in the past tense), but instead of just correcting the stickies directly, they can be marked or rotated to be corrected at the end of the step. The Event Storming Master should not interrupt the participants while they are putting events on the board.

### Step 2: Discovering Concerns and Questions

Use the red <svg width="1.4em" height="1em" style="display: inline-block;"><rect width="1em" height="1em" rx="0.15em" ry="0.15em" x="0.2rem" y="0em" style="fill:rgb(255,0,0);"/></svg> sticky notes on corresponding domain events when a concern or question is raised.

This will make it clear to participants that not everyone is aligned and will prompt further discussions until everyone is aligned.

### Step 3: Discover Domain Commands

Use the blue <svg width="1.4em" height="1em" style="display: inline-block;"><rect width="1em" height="1em" rx="0.15em" ry="0.15em" x="0.2rem" y="0em" style="fill:rgb(0,51,255);"/></svg> sticky notes for Commands (also known as Actions).


Use the light yellow <svg width="1.4em" height="1em" style="display: inline-block;"><rect width="1em" height="1em" rx="0.15em" ry="0.15em" x="0.2rem" y="0em" style="fill:rgb(255,255,153);"/></svg> sticky notes for Users / Actors / Personas.


**Commands** are the result of a **User** making a decisions and executing an operation.

In this step we dive into the Mechanics and Core components of the domain. The discussions about commands and actions will prompt us to ask questions such as "Why does user X need to perform a particular command?"

Once the events ordered chronologically we can start seeing a flow emerge.


### Step 4: Discover Read Model and Aggregates

Use green <svg width="1.4em" height="1em" style="display: inline-block;"><rect width="1em" height="1em" rx="0.15em" ry="0.15em" x="0.2rem" y="0em" style="fill:rgb(0,153,0);"/></svg> sticky notes for the Read Model data sources / projections.

Read Model shows the data that a User needs data to make a decision.

At this point you should be able to start building up the Aggregates (entities).

### Step 5: Discover External Systems

Use purple <svg width="1.4em" height="1em" style="display: inline-block;"><rect width="1em" height="1em" rx="0.15em" ry="0.15em" x="0.2rem" y="0em" style="fill:rgb(102,0,153);"/></svg> sticky notes for External Systems or Dependencies.


External Systems represents parts of the business domain or process outside of our control such as:

* API Services
* Departments
* Other organizations

We expect external systems to respond to our Commands and/or Queries.

### Step 6: Discover Policies


<svg width="1.4em" height="1em"><rect width="1em" height="1em" rx="0.15em" ry="0.15em" x="0.3rem" y="0em" style="fill:rgb(255,0,148);"/></svg> Pink for Policies (aka Reactions)


Policies are the glue between the <svg width="1.4em" height="1em" style="display: inline-block;"><rect width="1em" height="1em" rx="0.15em" ry="0.15em" x="0.2rem" y="0em" style="fill:rgb(0,51,255);"/></svg> Commands and <svg width="1.4em" height="1em" style="display: inline-block;"><rect width="1em" height="1em" rx="0.15em" ry="0.15em" x="0.2rem" y="0em" style="fill:rgb(255,102,0);"/></svg> Events.

Policies are considered the reactive logic that represents the rules of a business domain or process. This reactive logic allows or denies the target event to be triggered.

Always spoken in terms of 'When-X Then-Y' or 'Whenever'.

For example:
- **When** a user logs > 8 hours work, **then** send a warning email and add to overtime
- **Whenever** an invoice is updated with < 8 hours, **then** send a warning email


### End Result

Lots of sticky notes arranged chronologically that shows:
- <svg width="1.4em" height="1em" style="display: inline-block;"><rect width="1em" height="1em" rx="0.15em" ry="0.15em" x="0.2rem" y="0em" style="fill:rgb(0,51,255);"/></svg>Commands & <svg width="1.4em" height="1em" style="display: inline-block;"><rect width="1em" height="1em" rx="0.15em" ry="0.15em" x="0.2rem" y="0em" style="fill:rgb(255,102,0);"/></svg>Events grouped with <svg width="1.4em" height="1em" style="display: inline-block;"><rect width="1em" height="1em" rx="0.15em" ry="0.15em" x="0.2rem" y="0em" style="fill:rgb(255,204,0);"/></svg>Aggregates
- Defined <svg width="1.4em" height="1em" style="display: inline-block;"><rect width="1em" height="1em" rx="0.15em" ry="0.15em" x="0.2rem" y="0em" style="fill:rgb(0,153,0);"/></svg>Read Models with data that <svg width="1.4em" height="1em" style="display: inline-block;"><rect width="1em" height="1em" rx="0.15em" ry="0.15em" x="0.2rem" y="0em" style="fill:rgb(255,255,153);"/></svg> Users need to make decisions
- Identified <svg width="1.4em" height="1em" style="display: inline-block;"><rect width="1em" height="1em" rx="0.15em" ry="0.15em" x="0.2rem" y="0em" style="fill:rgb(102,0,153);"/></svg>External Systems / Dependencies
- Identified <svg width="1.4em" height="1em"><rect width="1em" height="1em" rx="0.15em" ry="0.15em" x="0.2rem" y="0em" style="fill:rgb(255,0,148);"/></svg>Policies (reactive logic) that apply to the process

If you ran an in-person workshop using sticky notes and a white-board you should capture the end-to-end flow by taking a photograph or by digitizing it with one of the diagraming tool listed in [Preparation - Choosing the right visualization tool](#preparation-choosing-the-right-visualization-tool). 

Make sure that he flow is stored in a central repository where everyone can access it. 

Having access to this visual flow:

* can help new team members onboard
* clear up confusion when parts of the system is not understood
* accelerate the software design and development of the system or new features
