---
type: rule
title: Do you use Co-Creation Patterns?
uri: do-you-use-co-creation-patterns
authors:
  - title: Daniel Mackay
    url: https://ssw.com.au/people/daniel-mackay
related: 
  - over-the-shoulder
created: 2022-11-21T00:28:43.256Z
guid: 4ff555fd-3f4c-416b-9fc3-1bf9409cc0ab
---
These days Pull Requests are the de facto standard for getting code reviewed.  Once a developer has finished their change, they will typically submit a Pull Request and move on to their next task.  This allows for an asynchronous process to take place which may seem like a good idea, but often is not and can also lead to inefficiencies.

## ❌ Problem - Inefficient Code Reviews

Inefficient code reviews can be caused by:

* Requesting feedback too late
* Receiving feedback too slow
* Creating large Pull Requests
* Excessive context switching
* Too much work in progress
* Unclear feedback

::: bad
![Figure: Vicious cycle of being blocked and picking up yet another task (source: https://www.infoq.com/articles/co-creation-patterns-software-development)](co-creation-1.png)
:::

::: bad
![Figure: Inefficiencies caused by asynchronous code reviews (source: https://www.infoq.com/articles/co-creation-patterns-software-development)](co-creation-2.png)
:::

## ✅ How to Make Code Reviews More Efficient

* Author - [Do over the shoulder reviews](https://www.ssw.com.au/rules/over-the-shoulder/)
* Author - Ask for feedback early before the PR, if you are uncertain that you're on the correct path
* Limit work in progress
  * Author - Make sure your Pull Requests are merged, before starting a new task
  * Reviewer - Prioritize Pull Requests before starting a new task
* Author - Create small Pull Requests
  * This requires a smaller block of time to review which makes it easier for the reviewer to find the time
  * Less risk - reduces the chance of an incorrect approach being taken
  * Get quality feedback - small blocks of code are easier to digest
* Reviewer - When reviewing asynchronously
  * Be explicit and suggest the exact code changes where possible (GitHub has a feature for this, see https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/incorporating-feedback-in-your-pull-request)
  * Call the developer for more complicated changes

## The Ultimate Solution - Co-Creation Patterns

Small Pull Requests have many benefits as outlined above.  However, each Pull Request comes with an overhead and making Pull Requests too small can introduce unnecessary waste and negatively affect the throughput of code.  In order to not lose throughput with small PRs, reviewers need to react faster
That leads us to synchronous, continuous code reviews and co-creation patterns

 So, with the async way of working, we’re forced to make a trade-off between losing quality (big PRs) and losing throughput (small PRs).

We can avoid this by using co-creation patterns. As a general rule, Pull Requests with less than 20 lines of code, and larger changes with a degree of complexity/risk, make good candidates for co-creation

> The idea is that you do small PR's but also limit WIP. If you are do several small PR's quickly and are waiting for review, you become blocked very quickly. By co-creating, the small PR's get reviewed & merged instantly which avoids getting blocked and enables you to smash out loads of small PRs! 💪
> 
> Daniel Mackay

### Patterns

Co-creation patterns can take several forms:

1. **Pair-programming**: starting, reviewing and finishing a change together
2. **Mob-programming**: working in a small group, that collectively has all skills required

### Advantages of co-creation

Co-creation allows us to have both quality and throughput by providing the following advantages:

1. More context when reviewing
2. Higher quality
3. Faster communication
4. Faster course correction
5. Less delay - no waiting
6. Eliminates context switching - working on a change together reduces WIP which further increases throughput
7. Emotions are removed - instead of having an 'author' and 'critic', the code is created together.

<!-- 
TODO: Add a PR screenshot of pair programming, show the PR Dan M with Jack R for the big PR for Rules GPT
TODO: Add a PR screenshot of mob programming, we need to demonstrate what the PR would look like for this
 -->

