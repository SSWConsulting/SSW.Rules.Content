---
type: rule
title: Do you use labels to improve code review communication?
uri: use-labels-to-improve-code-review-communication
authors:
  - title: Tom Iwainski
created: 2023-10-15T22:50:55.343Z
guid: 0e1a4c32-1bd2-49a8-8421-53157195738c
---
Ensure clear communication during code reviews by using labels to categorize comments, making it easier to understand their intent and impact on the code.
            
<!--endintro-->

When conducting code reviews in a collaborative environment, it is essential to maintain effective communication. Utilizing labels in your comments can significantly enhance the code review process. Labels help convey the intent and impact of a comment, making it easier for the author and other team members to understand how to address it.

```
@developer
This code could be better optimized. 
```
::: bad  
Figure: Without a label, this comment's intent is vague.
:::
In this case, the comment's intent is unclear, making it less effective for collaboration. It's not evident whether it's a suggestion, a question, or an issue.

```
@developer
**suggestion**: Consider refactoring this function for improved performance.

This change could lead to a significant speed improvement in our app.
```
::: ok  
Figure: The label "suggestion" indicates that the comment is a suggestion for improvement
:::
Adding a label like "suggestion" clarifies the intent of the comment, making it actionable. The context provided helps the author see the potential impact of the suggested change.
```
@developer
**issue (security,blocking)**: We must address this security vulnerability before merging.

This vulnerability could lead to a critical security breach if not fixed promptly.
```
::: ok
Figure: The labels "issue" and "security" clearly define the comment's importance and category.
:::

In this example, the labels "issue" and "security" convey the urgency of the matter, helping the team prioritize and act accordingly.

Using labels also helps categorize comments for tracking and reporting purposes, providing valuable insights into the development process. By adhering to a consistent format such as:


```
<label> [decorations]: <subject>

[discussion]
```

You can create a standardized system that makes comments more parseable by machines, which can lead to valuable metrics and reports in the future.



### Labels

| Label      | Description                                                                                                 |
|------------|-------------------------------------------------------------------------------------------------------------|
| **praise**  | Praises highlight something positive. Try to leave at least one of these comments per review. Do not leave false praise (which can actually be damaging). Do look for something to sincerely praise.                                      |
| **nitpick** | Nitpicks are trivial preference-based requests. These should be non-blocking by nature.                     |
| **suggestion** | Suggestions propose improvements to the current subject. It's important to be explicit and clear on what is being suggested and why it is an improvement. Consider using patches and the blocking or non-blocking decorations to further communicate your intent.                     |
| **issue**   | Issues highlight specific problems with the subject under review. These problems can be user-facing or behind the scenes. It is strongly recommended to pair this comment with a suggestion. If you are not sure if a problem exists or not, consider leaving a question.                      |
| **todo**    | TODO's are small, trivial, but necessary changes. Distinguishing todo comments from issues: or suggestions: helps direct the reader's attention to comments requiring more involvement.                       |
| **question** | Questions are appropriate if you have a potential concern but are not quite sure if it's relevant or not. Asking the author for clarification or investigation can lead to a quick resolution.                       |
| **thought** | Thoughts represent an idea that popped up from reviewing. These comments are non-blocking by nature, but they are extremely valuable and can lead to more focused initiatives and mentoring opportunities.                  |
| **chore**   | Chores are simple tasks that must be done before the subject can be “officially” accepted. Usually, these comments reference some common process. Try to leave a link to the process description so that the reader knows how to resolve the chore.       |
| **note**    | Notes are always non-blocking and simply highlight something the reader should take note of.                  |


By incorporating labels like these, you can enhance the clarity and effectiveness of your code review comments.


### Key Points
* Use labels to categorize comments during code reviews.
* Clearly indicate the intent of the comment using labels, such as "suggestion," "issue," or "nitpick."
* Encourage team members to provide actionable comments for improved collaboration.
* Follow a consistent format to ensure comments are easily parseable by machines for future reporting.

Remember, effective code review communication can save hours of undercommunication and misunderstandings, leading to better code quality and a more efficient development process.