---
seoDescription: Know when to multiply your estimates, based on the 3 main risk factors
type: rule
title: Do you know the 3 Risk Multipliers in Software Estimates?
uri: risk-multipliers
authors:
  - title: Andrew Harris
    url: https://www.ssw.com.au/people/andrew-harris
  - title: Luke Cook
    url: https://www.ssw.com.au/people/luke-cook
related:
  - underpromise-overdeliver
created: 2025-06-03T23:36:34.812Z
guid: b2b5a30c-7023-47a8-ac07-f8059e7f303d

---

Estimating time and complexity in software is hard. By its nature, almost all software development is attempting to solve problems no one else has done before. Industry veterans broadly agree that up to 60% of time and effort in software development is consumed by resolving unanticipated issues. Developers call these unanticipated issues "unknowns". Businesses call them "risks".

When you're scoping out a piece of work, it's important to help the business understand and manage those risks, and help shine a light on areas where risk can quickly snowball.

## The risk multipliers

Whenever you're estimating a piece of work, keep in mind the following risk multipliers and adjust your estimates accordingly:

### How well do you know the codebase?

If you've been working on a project for a suitable length of time, you should know your way around its architecture and code flows. This will provide significant context when gauging the required effort to build out the feature you're estimating. On the flipside, if you're a contractor, consultant, or simply new to a project, the existing codebase is a massive unknown and holds a great deal of potential risk. The feature you're estimating may seem simple at the surface, but when you discover a mess of spaghetti code and zero documentation, you will find yourself burning huge amounts of time just trying to grok what's currently happening before you can write a single line of code.

### How often have you done this work?

If you're a back-end web developer, and the feature you're estimating is some simple CRUD endpoints, you've probably done this type of work hundreds of times before. You know what's required, and you know can confidently gauge how long it will take. Alternatively, if you're being asked to build something exotic, or even just outside your wheelhouse, confidence can drop quickly. Maybe what's being asked is simply not possible, or requires significant infrastructure or iteration before meeting requirements. Know your strengths, and more importantly, know your blindspots.

### How big/complex is the change?

While this is probably the most obvious area of risk, it is still risk and therefore worth remembering. Perhaps the feature or change you're being asked to do is merely changing the colour of a button (hey, it happens!). Maybe the feature is adding a shopping cart to a website. Don't take things at face value: ask questions, describe the flow. More often than not, you'll start teasing out additional requirements that you didn't know about. A *very common* conversation around something like "add a shopping cart" might play out like this:

* I want a shopping cart on my website
* Oh, and it needs to process payments
* We already have a payment gateway! Talk to Alice about it.
* Oh, that payment gateway is throttled - it won't be able to handle the expected transaction increase...
* We need a new payment gateway!
* ...etc.

One of the best ways to identify these complexities is to **[run an Event Storming session.](/event-storming)** SSW highly recommends this for all medium to large projects, and we've found it incredibly effective at both identifying complexity, as well as *demonstrating that complexity* to non-technical stakeholders.

## Managing risk

Okay, so you've done your best to identify as many risk factors as possible. Great - so how do you *manage* that risk?

### Option 1: Overestimate everything

The old "think of a number and double it" approach has been a common estimation strategy for decades. While this definitely has its place, your doubled estimate is still at risk of [being wildly incorrect](https://en.wikipedia.org/wiki/Hofstadter%27s_law). Humans are [terrible at estimating](https://en.wikipedia.org/wiki/Planning_fallacy). If you're leaning on this approach, you still leave yourself open to risk when your doubled value should have been tripled, or quadrupled.

This can be acceptable when the work you're estimating is building on previous features, or when you already have a lot of the context front of mind and can already "see" the solution in your head. Just be conscious of the fallout if your estimate is off by a factor of 4 (or more). How does that affect the delivery of this PBI? A 2-hour estimate ballooning into a day is far less devastating than a 1-day estimate ballooning out to a week.

Use this approach when:

* The scope is known
* The codebase is known
* The complexity is low/moderate

### Option 2: Spike or PoC

One of the most reliable ways of reducing risk is to invest some R&D time into the task before committing to an approach and estimating the effort. There may be more than one **potential** way to solve a given problem, but you aren't sure which method will work best for the current project. Having time to investigate these options can save you hundreds of hours of pain further down the development cycle. The more variables there are in a given problem, the stronger the case for a Spike and/or PoC.

Use this approach when:

* The scope is known
* The codebase is known/unknown
* The complexity is moderate/high

### Option 3: Narrow the scope

Sometimes, a piece of work is simply too large to adequately identify and manage its risk. In these cases, the best thing to do is break the work down into smaller chuncks, and repeat the process outlined above for each subsequent chunk. This may need to be an iterative process (maybe the resultant chunks *still* have too many unknowns), but breaking down herculean tasks into smaller, more manageable pieces, is a tried and true way of making the impossible possible.

Use this approach when:

* The scope is unknown
* The codebase is known/unknown
* The complexity is moderate/high

## Guidance for large or complex projects

If you're in the enterprise space, or working on projects that have many moving parts, SSW recommends the following high-level plan:

1. Select a single business goal/process
2. Run one or more [Event Storming workshops](/event-storming-workshop) to map out the business flow
3. Create epics for each Key Event
4. Perform a [Specification Review](/what-is-a-spec-review) for each epic
5. Decomposing the epics into PBIs
6. Use the strategies above to identify high risk areas
