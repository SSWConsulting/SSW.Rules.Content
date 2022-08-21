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
[Event storming](https://www.ssw.com.au/rules/event-storming) is fun! Running a successful workshop will require preparation and understanding of the Event Storming process. 

At SSW we have dedicated Event Storming Masters. You may also call them Event Storming Facilitators or Event Storming Moderators.

Preparation will include finding the right participants, the right amount of time and the right space (physically or virtually).

<!--endintro-->

## Schedule the right amount of time

Depending on the size and complexity of the project you would typically need between 2 to 4 hours for a good Event Storming workshop session.

During a [Specification Review](https://www.ssw.com.au/rules/spec-do-you-conduct-a-specification-review-ask-for-a-coffee-not-a-marriage) you can schedule this workshop on the first day. Typically on the second day you can use the Event Storming visuals to help design your system and software architecture and produce better estimates.

## Invite the right people

- Developers or Engineers usually ask the right questions
- Domain experts are the people who will answer the questions
- Dedicated Event Storming Master that will help guide the participants through the workshop

## Preparation - In person workshop  

- Different coloured sticky notes
- Marker pens
- Long roll of paper or 
  - a wide white-board or 
  - the glass walls/windows
- Make sure that the common terms are clearly visible
- Make sure that the legend is clearly visible
 
## Preparation - Choosing the right visualization tool

Real-time collaboration (remote or in-person) has become the default choice for many teams. Instead of sticky notes and white-boards we can use tools such as:

* [Miro](https://miro.com/)
* [Lucidcharts](https://www.lucidchart.com)
* [Diagrams.net](https://www.diagrams.net/). 

These tools will eliminate the worry of low-quality sticky notes falling off the white-board and your markers drying up!

For remote sessions, collaboration might not be as smooth as the in person events. However, it is also easier to arrange the attendees to join a remote session when the team is not all in a single location.

## Discovery Steps

You can break the workshop down into a number of distinct discovery steps. Each step adds more detail to the business domain or process you are trying to understand.

1. 🟧 Domain events
2. 🟥 Concerns and questions
3. 🟦 Domain Commands and 🟨 Personas
4. 🟩 Read Models and 🟨 Aggregates
5. 🟪 External Systems
6. <svg width="1.4em" height="1em"><rect width="1em" height="1em" rx="0.15em" ry="0.15em" x=0.2rem y=0em style="fill:rgb(255,0,148);"/></svg> Policies

### Step 1: Discovering Domain Events

Use the orange 🟧 sticky notes.

The domain experts and stakeholders can simply start recording the events that occur in a business domain or process. The events don't necessarily need to be in a precise timeline order (yet).

Domain events are always rooted in the **past tense** to represent a fact. Facts cannot be changed because they actually happened. 

For example, we can have domain events such as `Invoice Created` `Email sent` `Timesheet Updated`.

It can be expected that not all the participants will be aligned with the business domain or process at the start, but as the workshop progresses everyone will start to "get into the zone" and ideas will be put onto the board quickly and smoothly.

When there are concerns or contention, the participants can discuss and rearrange the events until it is resolved and everyone is aligned in their thinking. Sometimes the contention is due to a different terminology, so it is important to record the common terms and make sure that they are clearly visible to all participants.

The Event Storming Master should check the stickies to ensure that the basic rules are being followed (such as ensuring events are in the past tense), but instead of just correcting the stickies directly, they can be marked or rotated to be corrected at the end of the step. The Event Storming Master should not interrupt the participants while they are putting events on the board.

### Step 2: Discovering Concerns and Questions

Use the red 🟥 sticky notes.

Place the red 🟥sticky on corresponding domain events when a concern or question is raised.

This will make it clear to participants that not everyone is aligned and will prompt further discussions until everyone is aligned.

### Step 3: Discover Domain Commands

Use the blue 🟦 sticky notes for Commands (also known as Actions).


Use the yellow 🟨 sticky notes for Users / Actors / Personas.


Commands are the result of a User making a decisions and executing an operation.

In this step we dive into the Mechanics and Core components of the domain. The discussions about commands and actions will prompt us to ask questions such as "Why does user X need to perform a particular command?"

Once the events ordered chronologically we can start seeing a flow emerge.


### Step 4: Discover Read Model and Aggregates

Green sticky 🟩 for Data sources / projections.

Read Model shows the data that a User needs data to make a decision.

At this point you should be able to start building up Aggregates (entities).

### Step 5: Discover External Systems

🟪 Purple sticky for External Systems or Dependencies.


External Systems represents parts of the business domain or process outside of our control such as:

- API Services
- Departments
- Other organizations

We expect external systems to respond to our Commands and/or Queries.

### Step 6: Discover Policies


<svg width="1.4em" height="1em"><rect width="1em" height="1em" rx="0.15em" ry="0.15em" x=0.3rem y=0em style="fill:rgb(255,0,148);"/></svg> Pink for Policies (aka Reactions)


Policies are the glue between the 🟦 Commands and 🟧 Events.

Policies are considered the reactive logic that represents the rules of a business domain or process. This reactive logic allows or denies the target event to be triggered.

Always spoken in terms of 'When-X Then-Y' or 'Whenever'.

For example:
- **When** a user logs > 8 hours work, **then** send a warning email and add to overtime
- **Whenever** an invoice is updated with < 8 hours, **then** send a warning email


### End Result

Lots of sticky notes defining the business domain or process:
- 🟦Commands & 🟧Events grouped with 🟨Aggregates
- Defined 🟩Read Models with data that 🟨 Users need to make decisions
- Identified 🟪External Systems / Dependencies
- Identified <svg width="1.4em" height="1em"><rect width="1em" height="1em" rx="0.15em" ry="0.15em" x=0.2rem y=0em style="fill:rgb(255,0,148);"/></svg>Policies (reactive logic) that apply to the process

If you ran an in-person workshop using sticky notes and a white-board you should capture the end-to-end flow by taking a photograph or by digitizing it with one of the diagraming tool listed in [Preparation - Choosing the right visualization tool](#preparation-choosing-the-right-visualization-tool). 

Make sure that he flow is stored in a central repository where everyone can access it. 

Having access to this visual flow:

* can help new team members onboard
* clear up confusion when parts of the system is not understood
* accelerate the software design and development of the system or new features
