---
type: rule
title: Do you use prefixes to improve code review communication?
uri: use-prefixes-to-improve-code-review-communication
authors:
  - title: Thomas Iwainski
    url: https://www.ssw.com.au/people/thomas-iwainski/
created: 2023-10-15T22:50:55.343Z
guid: 0e1a4c32-1bd2-49a8-8421-53157195738c
related:
  - prefixes
---

In the world of code reviews, ambiguity can lead to confusion, misunderstandings, and wasted time. Utilizing prefixes for code review comments is like providing a map for navigating complex terrain, ensuring that everyone involved in the review process remains on the same page. Incorporating prefixes in code review communication can prevent potential challenges, enhancing collaboration, clarity, and code quality. With these small changes, you can streamline and improve the overall code review process and complete reviews quickly and efficiently.

<!--endintro-->

When conducting code reviews in a collaborative environment, it is essential to maintain effective communication. Utilizing prefixes in your comments, as suggested at [https://conventionalcomments.org](https://conventionalcomments.org/), can significantly enhance the code review process. Prefixes help convey the intent and impact of a comment, making it easier for the author and other team members to understand how to address it.

Let's have a look at the following example from Bob Northwind:

:::greybox
@bob-northwind

This code could be better optimized
:::

::: bad  
Figure: Without a prefix, this comment's intent is vague. It's not evident whether it's a suggestion, a question, or an issue.
:::

:::greybox
@bob-northwind

**suggestion**: This code could be better optimized.

It is not critical but there are a few minor improvements that can be applied
to increase performance.
:::

::: good  
Figure: The prefix "suggestion" indicates that the comment is a suggestion for improvement
:::

Adding a prefix like "suggestion" clarifies the intent of the comment, making it actionable. The context provided helps the author see the potential impact of the suggested change.

:::greybox
@bob-northwind

**issue**: We must address this security vulnerability before merging.

There is a potential for SQL Injection and this vulnerability could lead to a critical security breach if not fixed.
:::

::: good
Figure: The prefix "issue" and following context clearly define the comment's importance and category.
:::

In this example, the prefix "issue" conveys the urgency of the matter, helping the team prioritize and act accordingly.

Using prefixes also helps categorize comments for tracking and reporting purposes, providing valuable insights into the development process.

By adhering to a consistent format such as:

:::greybox
**\<prefix>**: \<subject>

[discussion]
:::

You can create a standardized system that makes comments more parseable by machines, which can lead to valuable metrics and reports in the future.

### Prefixes

The following list is what we suggest and use at SSW. It is based on [https://conventionalcomments.org](https://conventionalcomments.org/).

| Prefix         | non-/blocking | Description                                                                                                                                                                 |
| -------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **issue**      | blocking      | Issues point out specific problems with the code. These can affect users or happen behind the scenes.                                                                       |
| **todo**       | blocking      | TODOs are essential changes. If they're complex, create a new task or PBI for them.                                                                                         |
| **question**   | blocking      | Questions are suitable when you're uncertain about something's relevance. Ask for clarification or investigation for a quick resolution.                                    |
| **praise**     | non-blocking  | Praises highlight something positive. It's good to include at least one in each review. Avoid false praise as it can be harmful. Look for something genuinely praiseworthy. |
| **suggestion** | non-blocking  | Suggestions offer ways to make the code better. Be clear about what you're suggesting and why it's an improvement.                                                          |
| **thought**    | non-blocking  | Thoughts are ideas that came up during the review. They don't block progress, but they can lead to more focused initiatives and learning opportunities.                     |
| **nitpick**    | non-blocking  | Nitpicks are minor, preference-based suggestions.                                                                                                                           |

By incorporating prefixes like these, you can enhance the clarity and effectiveness of your code review comments.

Remember, effective code review communication can save hours of undercommunication and misunderstandings, leading to better code quality and a more efficient development process.
