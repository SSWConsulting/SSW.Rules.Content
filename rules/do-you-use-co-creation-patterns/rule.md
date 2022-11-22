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

## Problem - Inefficient Code Reviews

Inefficient code reviews can be caused by:

- Providing Feedback Too Late
- Providing Feedback Too Slow
- Creating Huge Pull Requests
- Excessive Context Switching
- Too Much Work in Progress
- Unclear Feedback

::: bad
![Figure: Vicious cycle of being blocked and picking up yet another task](https://imgopt.infoq.com/fit-in/700x1400/filters:quality(80)/filters:no_upscale()/articles/co-creation-patterns-software-development/en/resources/38-1667592466401.jpeg)
:::

::: bad
![Figure: Inefficiencies caused by asynchronous code reviews](https://imgopt.infoq.com/fit-in/1200x2400/filters:quality(80)/filters:no_upscale()/articles/co-creation-patterns-software-development/en/resources/61-1667592466401.jpeg)


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