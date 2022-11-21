---
type: rule
title: Do you use Co-Creation Patterns?
uri: do-you-use-co-creation-patterns
authors:
  - title: Daniel Mackay
    url: https://ssw.com.au/people/daniel-mackay
related: []
created: 2022-11-21T00:28:43.256Z
guid: 4ff555fd-3f4c-416b-9fc3-1bf9409cc0ab
---
These days pull requests are the de facto standard for getting code reviewed.  Once a developer has finished their change, they will typically submit a pull request and move on to their next task.  This allows for an asynchronous process to take place which may seem like a good idea, but this can also lead to inefficiencies.

## Inefficient Code Reviews

### Providing Feedback Too Late

Reviewing at the end of a change (especially a large change) makes the review less effective.  Any major feedback will result in substantial rework which causes waste.

### Providing Feedback Too Slow

The longer a developer needs to wait to continue with a change, the more they are tempted to start something else.  This also negatively affects the 'Lead Time for Change' (see below).

<!--StartFragment-->
![](https://imgopt.infoq.com/fit-in/700x1400/filters:quality(80)/filters:no_upscale()/articles/co-creation-patterns-software-development/en/resources/38-1667592466401.jpeg)
<!--EndFragment-->

### Creating Huge Pull Requests

Big pull requests hinder the ability to build-in quality. Developers can get emotionally attached to their code which makes substantial changes hard and the [sunk cost fallacy](https://www.grammarly.com/blog/sunk-cost-fallacy/) kicks in.

Give a reviewer 10 lines of code and they'll find 10 bugs.  Give them 1000 lines of code to review and they'll approve without comment. 😲

### Excessive Context Switching

When a developer submits a change for review, they will often move onto a new task and context switch.  After their change has been reviewed, they need to switch from the current task back to the old task, address feedback, then switch from the old task to the current task.  The more pull requests a developer has open the more context switching needs to take place.  This division of focus can lead to lower quality code.

### Too Much Work in Progress

One of the DORA Metrics used to measure high-performing teams is called [Lead Time for Change](https://www.leanix.net/en/wiki/vsm/dora-metrics#lead-time-for-changes).  High-performing teams can get changes into production faster.  

The more work in progress a developer has, the more context switching is required and the longer it will take to get these changes 'done'.  This also has a flow on effect of the more work in progress a developer has, the longer it will take them to review another developers code,

The more WIP we have in the system, the less responsive it becomes, and the longer the wait times and delays, which in turn incentivizes even higher WIP because people pull in more stuff as they need to wait.

### Unclear Feedback

Asynchronous feedback can sometimes not be clear.  This can result in back-and-forth discussing the feedback which results in more waste and more context switching.

<!--StartFragment-->
![](https://imgopt.infoq.com/fit-in/1200x2400/filters:quality(80)/filters:no_upscale()/articles/co-creation-patterns-software-development/en/resources/61-1667592466401.jpeg)
<!--EndFragment-->

## Efficient Code Reviews

There are several improvements we can make to address some of the issues above.

### Avoid Pull Request Churn

When suggesting a change, be explicit and suggest the exact code changes where possible.  This avoids ambiguity and increases the chances the developer will get the change right the first time.

GitHub has this feature baked in and allows the developer to approve the suggestion with a single click.

Where the suggestion is more complicated, reach out directly to the developer and walk them through the change.

### Limit Work in Progress

The fewer items a developer is concurrently working on the less context-switching they need to do. Avoiding context switching allows both the developer and reviewer to make quality contributions.

You can limit WIP by:

1. Chasing up your outstanding pull requests before starting something new
2. Reviewing other developer's pull requests before starting something new

### Create Small PRs

Advantages of small pull requests:

1. Require a smaller block of time to review - this makes it easier for the reviewer to find the time
2. Get feedback earlier - makes change easier to adopt
3. Less risk - reduces the chance of an incorrect approach being taken
4. Get quality feedback - small blocks of code are easier to digest

## Co-Creation Patterns

Small pull requests have many benefits as outlined above.  However, each pull request comes with an overhead and making pull requests too small can introduce unnecessary waste and negatively affect the throughput of code.  In order to not lose throughput with small PRs, reviewers need to react faster
That leads us to synchronous, continuous code reviews and co-creation patterns

 So, with the async way of working, we’re forced to make a trade-off between losing quality (big PRs) and losing throughput (small PRs).

We can avoid this by using co-creation patterns.

> As a general rule pull requests with less that 20 lines of code and larger changes with a degree of complexity or risk make good candidates for co-creation

### Techniques

Co-creation patterns can take several forms:

1. **Pair-programming**: starting, reviewing and finishing a change together
2. **Mob-programming**: working in a small group, that collectively has all skills required

### Advantages

Co-creation allows us to have both quality and throughput by providing the following advantages:

1. More context when reviewing
2. Higher quality
3. Faster communication
4. Faster course correction
5. Less delay - no waiting
6. Eliminates context switching - working on a change together reduces WIP which further increases throughput
7. Emotions are removed - instead of having an 'author' and 'critic', the code is created together.