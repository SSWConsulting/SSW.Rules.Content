---
type: rule
title: Do you use GitHub Discussions to suggest new ideas?
guid: 5ed09331-e71d-433e-90b7-4ae509ea0099
uri: use-github-discussions
created: 2023-01-25T06:20:09+0000
authors:
- title: Matt Wicks
  url: https://ssw.com.au/people/matt-wicks
- title: Brady Stroud
  url: https://ssw.com.au/people/brady-stroud
- title: Sam Wagner
  url: https://ssw.com.au/people/sam-wagner
related: []
redirects: []
---

Sometimes when working on a product, you need a way to communicate with the team and users of the software that isn't limited to known issues with the product. GitHub Discussions are a great way to provide an open forum for communication. 

GitHub Discussions can be used for:
- Product announcements e.g. New feature - users can now have a profile picture
- Potential feature ideas and bugs e.g. Feature idea - Let users upload their work hours
- Customer support e.g. Login help - I forgot my password and am not sure how to reset it
- Technical discussions e.g. Trouble running migration - has anyone seen this before?
- Gauging community sentiment e.g. Poll - Is the user screen's new design a better UX?
- and much more... 

<!--endintro-->

Here's a [great video](https://www.youtube.com/watch?v=bErGYN3Ljz8) by the GitHub team that explains Discussions in full!

`youtube: https://www.youtube.com/embed/bErGYN3Ljz8`

**Video: What is GitHub Discussions? (40sec)**

## Product announcements
GitHub Discussions are accessible to the entire user base, so when there is a new release it is a great place to announce new products or share release notes.

## Potential improvements - 3 stages

New improvements can be simple or complex. Before implementing an improvement, think about how to communicate it to the team. Generally, an improvement will go through 3 stages:

* Stage 1 - GitHub Discussions
* Stage 2 - GitHub Issues
* Stage 3 - Pull Request 

However, sometimes a stage can be skipped depending on the certainty and difficulty of implementation.

### Stage 1 - GitHub Discussions

GitHub Discussions is the right place to start when **certainty** is low. Raising it in this setting let's the whole team discuss the proposal and reach a consensus about what to do. Make sure to @mention any important stakeholders (E.g. @BobNorthwind)

![Figure: SSW Rules | GitHub | Discussions](https://user-images.githubusercontent.com/66365977/214453285-b074f967-a637-4968-bd0d-ce79198f8bc3.png)

### Stage 2 - GitHub Issues

Once the team has made a decision on a GitHub Discussion or if you are certain the issue doesn't need a discussion, then you need to evaluate the difficulty of implementation. If it is difficult to implement then GitHub Issues is the right place to put it, since it provides a place to manage work as the improvement is developed.

GitHub Discussions can be converted to GitHub Issues with a single click! 

![Figure: SSW Rules | GitHub | Discussions - Convert a Discussion to an issue](https://user-images.githubusercontent.com/66365977/214461325-7bd47032-3b8f-4e1c-96f4-63b7ee02a64d.png)

![Figure: SSW Rules Content Discussion Converted To Issue](https://user-images.githubusercontent.com/66365977/214463615-2b27e427-93a9-4d49-ab2b-bdb06859c816.png)

### Stage 3 - Pull Request
Once the work is complete, it can be turned into a Pull Request 
Now that it's an issue, you can of course associate Pull Requests with that issue and otherwise associate work with that rather than the whole project.

Of these three stages: Discussion, Issue and Pull Request, you can always jump in at any point. For example, if all it is that you're doing is updating a spelling error, It might be worth just opening a Pull Request.
