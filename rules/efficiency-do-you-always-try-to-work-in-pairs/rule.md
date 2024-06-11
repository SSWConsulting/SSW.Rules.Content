---
seoDescription: Efficiency Tip - Do You Always Try to Work in Pairs? Work smarter, not harder! Pair programming boosts productivity and code quality. Two heads are better than one, especially when working on complex projects. Reduce problem-solving time, stay motivated, and learn from each other's expertise.
type: rule
title: Efficiency - Do you always try to work in pairs?
uri: efficiency-do-you-always-try-to-work-in-pairs
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - efficiency-do-you-always-try-to-work-in-pairs-1
created: 2009-03-17T07:35:05.000Z
archivedreason: null
guid: e1ce40a6-7c15-4974-9e57-506b1bc7c337
---

There are many good reasons why it's better to work in pairs.

<!--endintro-->

![Figure: Do you always try to work in pairs?](ProjectManagement_PairProgramming_Luge.jpg)

For everyone:

* Less time stuck on a problem - you have someone familiar with the project to help you work through the problem
* You can keep each other motivated and you absorb knowledge from each other
* Experience shows that two people working on a problem together are often more productive than one person working alone for twice as long

Extra for developers:

* Code will have less strange workarounds - because if something doesn't add up to a developer, they've got someone to ask
* Cleaner code - because you know someone else is going to be looking at your code
* Support - when you need changes down the track, you have two people to call on

> _"I have found developers work better in pairs. I am not a fan of the classical pair programming - which is 2 developers working on the 1 PC. There are times for that especially during brainstorming activities, however on a day-to-day basis, I advise that developers work in pairs, but they each have their own PC."_
>
> **\- Adam Cogan**
> SSW Chief Architect + Microsoft Regional Director

---

If you are not sitting next to a person working on the same project, then fix it. If you cannot then at least mention it to your manager.

### Working Alone and Getting Stuck

If you find yourself working alone, which we don't recommend, you should speak up as soon as possible. You should make it clear that working alone is not best practice and that developers working together are worth more than the sum of their parts.

1 dev plus 1 dev doesn't equal 2 devs worth of work. It equals 3! 🎉

::: bad
![Figure: Bad example - This is normal ‘pair programming’, two people working at one PC](PairProgramming01.jpg)
:::

::: good
![Figure: Good example - This is ‘working in pairs’, two devs working on the same project, with their own laptops, but sitting very close to each other](PairProgramming02_Small.jpg)
:::

### Is there an overhead?

Some projects are done quicker with two people - especially when they are complex. But on most projects there is an overhead, because of the extra communication between the developers - you now have to please someone else - not just yourself.

Estimates vary for the overhead, but say it is 20% extra, this is more than offset by the cleaner code and better solutions that come from two brains working together.

### What if you are working remotely from each other?

If you are working with someone remote, you will be using an application like [Teams, TeamViewer, or another support tool](/do-you-know-the-best-way-to-give-the-best-customer-support) to view one another's desktops so you can help each other out when necessary. You should have [a 2nd monitor](/efficiency-do-you-use-two-monitors).

### What is the best code collaboration tool?

[Visual Studio Live Share](https://visualstudio.microsoft.com/services/live-share/) - See Video (3 minutes):

`youtube: https://www.youtube.com/watch?v=A2ceblXTBBc`

* VS Code - [Install extension](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare)
* Visual Studio 2022! It's built in!

[Code With me](https://www.jetbrains.com/code-with-me/) - A great tool for JetBrains IDE users who want to pair program. Though it isn't supported in Rider right now.

### Alternative Approach when there’s not enough Budget or Work: Weekly Senior Involvement

In situations where there isn't enough work for two people, or budget constraints limit resources, an alternative can be adopted. This approach involves a single developer handling the majority of development tasks, with a more senior developer contributing primarily on Sprint Review day. See below for an example:

::: greybox

If a client only has 1 developer working with them for 1 day a week, they must still keep regular Scrum cadence. In this case they would break the work down into 5-week (5 working days) Sprints. Every 5th booking, a senior developer or Solution Architect must be booked with them to ensure the project is running smoothly and to help them plan the next Sprint.
:::

The primary developer progresses the project mostly autonomously, while the senior developer's weekly involvement primarily ensures strategic oversight and quality control, particularly during Sprint Reviews. While the primary developer has greater autonomy, the availability of the senior developer for occasional guidance is crucial. This ensures the project remains on track and the primary developer does not feel isolated.

In a situation where we can’t even do the above, get cross-approval from another Account Manager to make sure the exception makes sense.
