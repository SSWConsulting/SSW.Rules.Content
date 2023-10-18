---
type: rule
title: Do you use prefixes to improve code review communication?
uri: use-prefixes-to-improve-code-review-communication
authors:
  - title: Tom Iwainski
created: 2023-10-15T22:50:55.343Z
guid: 0e1a4c32-1bd2-49a8-8421-53157195738c
related:
  - prefixes
---

In the world of code reviews, ambiguity can lead to confusion, misunderstandings, and wasted time. Failing to utilize prefixes for code review comments feels like navigating a complex terrain without a map, leaving everyone involved in the review process susceptible to a myriad of problems.
Neglecting the use of prefixes in code review communication can create a cascade of challenges that hinder efficient collaboration, clarity, and code quality. By adhering to this SSW rule, you can mitigate these pain points and significantly enhance the code review process.

<!--endintro-->

When conducting code reviews in a collaborative environment, it is essential to maintain effective communication. Utilizing prefixes in your comments, as suggested at [https://conventionalcomments.org](https://conventionalcomments.org/), can significantly enhance the code review process. Prefixes help convey the intent and impact of a comment, making it easier for the author and other team members to understand how to address it.

```plain
@developer
This code could be better optimized.
```

::: bad  
Figure: Without a prefix, this comment's intent is vague. It's not evident whether it's a suggestion, a question, or an issue.
:::

```plain
@developer
**suggestion**: Consider refactoring this function for improved performance.

This change could lead to a significant speed improvement in our app and
follows our best practices.
```

::: good  
Figure: The prefix "suggestion" indicates that the comment is a suggestion for improvement
:::

Adding a prefix like "suggestion" clarifies the intent of the comment, making it actionable. The context provided helps the author see the potential impact of the suggested change.

```plain
@developer
**issue**: We must address this security vulnerability before merging.

There is a potential for SQL Injection and this vulnerability could lead to a critical security breach if not fixed.
```

::: good
Figure: The prefix "issue" and following context clearly define the comment's importance and category.
:::

In this example, the prefix "issue" convey the urgency of the matter, helping the team prioritize and act accordingly.

Using prefixes also helps categorize comments for tracking and reporting purposes, providing valuable insights into the development process.

By adhering to a consistent format such as:

```plain
<prefix>: <subject>

[discussion]
```

You can create a standardized system that makes comments more parseable by machines, which can lead to valuable metrics and reports in the future.

### Prefixes

The following list is what we suggest and use at SSW. This is based on [https://conventionalcomments.org](https://conventionalcomments.org/)

| Prefix         | non-/blocking | Description                                                                                                                                                                                                |
| -------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **praise**     | non-blocking  | Praises highlight something positive. Try to leave at least one of these comments per review. Do not leave false praise (which can actually be damaging). Do look for something to sincerely praise.       |
| **nitpick**    | non-blocking  | Nitpicks are trivial preference-based requests.                                                                                                                                                            |
| **suggestion** | non-blocking  | Suggestions propose improvements to the current subject. It's important to be explicit and clear on what is being suggested and why it is an improvement.                                                  |
| **todo**       | blocking      | TODO's are necessary changes. If they are too big and complicated to action then a new PBI item needs to be created and linked.                                                                            |
| **issue**      | blocking      | Issues highlight specific problems with the subject under review. These problems can be user-facing or behind the scenes.                                                                                  |
| **question**   | blocking      | Questions are appropriate if you have a potential concern but are not quite sure if it's relevant or not. Asking the author for clarification or investigation can lead to a quick resolution.             |
| **thought**    | non-blocking  | Thoughts represent an idea that popped up from reviewing. These comments are non-blocking by nature, but they are extremely valuable and can lead to more focused initiatives and mentoring opportunities. |

By incorporating prefixes like these, you can enhance the clarity and effectiveness of your code review comments.

Remember, effective code review communication can save hours of undercommunication and misunderstandings, leading to better code quality and a more efficient development process.
