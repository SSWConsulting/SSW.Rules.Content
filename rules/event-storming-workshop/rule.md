---
type: rule
title: Do you know how to facilitate an Event Storming workshop?
uri: event-storming-workshop
authors:
  - title: William Liebenberg
    url: https://www.ssw.com.au/people/william-liebenberg
related:
  - event-storming
created: 2022-08-03T05:42:33.397Z
guid: 6cd97f44-7b65-4718-bf57-0db7f92d5c75
---
Event storming is fun, but you have to be prepared for it.

<!--endintro-->

## Schedule an appropriate time

Depending on the size and complexity of the process you would typically need between 40 minutes up to 2 hours for a good Event Storming workshop session.

During a specification review you can schedule this workshop on the first day.

## Invite the right people

- Developers or Engineers usually ask the right questions
- Domain experts are the people who will answer the questions
- Dedicated facilitator or moderator that will help guide the participants through the workshop

## Preparation - In person workshop  

- Different coloured sticky notes
- Marker pens
- Long roll of paper or 
  - a wide white-board or 
  - the glass walls/windows
- Make sure that the common terms are clearly visible
- Make sure that the legend is clearly visible
 
## Preparation - Remote session

Use tools such as Miro, Lucidcharts or even Diagrams.net. This will eliminate the worry of low-quality sticky notes falling off the wall!

For remote sessions, collaboration might not be as smooth as the in person events. However, it is also easier to arrange the attendees to join a remote session when the team is not all in a single location.

## Discovery Steps

You can break the workshop down into a number of distinct discovery steps. Each step adds more detail to the process you are trying to understand.

1. 🟧 Domain events
2. 🟥 Concerns and questions
3. 🟦 Domain Commands and 🟨 Personas
4. 🟩 Read Models and 🟨 Aggregates
5. 🟪 External Systems
6. ⬜ Policies

### Discovering Domain Events

Use the orange 🟧 sticky notes.

The domain experts and stakeholders can simply start recording the events that occur in a process. The events don't necessarillyh need to be in a precise timeline order (yet).

Domain events are always rooted in the **past tense** to represent a fact. Facts cannot be changed because they actually happened. 

For example, we can have domain events such as `Invoice Created` `Email sent` `Timesheet Updated`.

It can be expected that not all the participants will be aligned with the process at the start, but as the workshop progresses everyone will start to get into "the zone" and ideas will be put onto the board quickly and smoothly.

When there are concerns or contention, the participants can discuss and rearrange the events until it is resolved and everyone is aligned in their thinking. Sometimes the contention is due to a different terminology, so it is important to record the common terms and make sure that they are clearly visible to all participants.

The moderator should check the stickies to ensure that the basic rules are being followed (such as ensuring events are in the past tense), but instead of just correcting the stickies directly, they can be marked or rotated to be corrected at the end of the step. The moderator should not interrupt the participants while they are putting events on the board.

### Discovering Concerns and Questions

Use the red 🟥 sticky notes.

Place the red 🟥sticky on corresponding domain events when a concern or question is raised.

This will make it clear to participants that not everyone is aligned and will prompt further discussions until everyone is aligned.

### Discover Domain Commands

Use the blue 🟦 sticky notes for Commands (also known as Actions).


Use the yellow 🟨 Yellow for Users / Actors / Personas.


Commands are the result of a User making a decisions and executing

In this step we dive into the Mechanics and Core components of the domain. The discussions about commands and actions will prompt us to ask questions such as "Why does user X need to perform a particular command?"

Once visualized and ordered chronologically, 


### Discover Read Model and Aggregates

User needs data to make a decision
Green sticky for Data sources / projections
Start building up Aggregates (entities)

### Discover External Systems
🟪 Purple sticky
- Parts of the flow outside of our control
- API Services / Departments / Organizations
- Respond to Commands / Queries

### Discover Policies

🟦 Pink for Policies (aka Reactions)
Between 🟦 Command and 🟧 Event
Represents the rules of a process
Allow / Deny an event to be triggered
“When Then” or “Whenever”
Whenever an invoice is updated with < 8 hours, send a warning email
When a user logs > 8 hours work, then send a warning email and add to overtime

### End Result

Lots of sticky notes defining the process:
- 🟦Commands & 🟧Events grouped with 🟨Aggregates
- Define 🟩Read Model with data 🟨 Users need to make decisions
- Identified 🟪External Systems / Dependencies
- Identified ⬜Policies that apply to Business Processes


