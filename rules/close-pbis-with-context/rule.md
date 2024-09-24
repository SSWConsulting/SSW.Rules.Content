---
seoDescription: When closing PBIs, tasks, and goals, provide valuable context to help teams understand the outcome and changes made.
type: rule
title: Do you close PBIs, tasks and goals with context?
uri: close-pbis-with-context
authors:
  - title: Gordon Beeming
    url: https://ssw.com.au/people/gordon-beeming
  - title: Piers Sinclair
    url: https://ssw.com.au/people/gordon-beeming
  - title: Brady Stroud
    url: https://ssw.com.au/people/brady-stroud
related:
  - write-a-good-pull-request
  - reply-done-and-delete-the-email
  - when-to-send-a-done-email-in-scrum
redirects: []
created: 2023-07-06T23:11:00.000Z
archivedreason: null
guid: 7cc338e9-0090-45c2-af82-936aa15ddb58
---

PBIs, tasks, and goals are the backbone of work regardless of whether they are stored in Azure DevOps, GitHub, Jira, Trello, or some other platform. When you finish a task, marking it as done is satisfying, but remember to add a closing comment for future context. By adding a closing comment, it allows others to understand why the PBI was closed and what the outcome was. This comment is critical when closing a PBI as "Won't Fix" or "Duplicate" but is valuable in all scenarios and should be the default approach.

For example, if you have UI changes, a couple of screenshots can go a long way to help the team understand what was done. Similarly, if there are changes to architecture documents or the readme, providing a link to those artifacts helps others get across the change.

<!--endintro-->

When you look at a PBI, you can navigate through the commits or pull requests that were linked to the PBI. This is great for understanding the code changes, but that doesn't easily show you what the outcome was.

::: bad  
![Figure: Bad example - This PBI is closed with no context around changes made](closing-pbis-without-context.jpg)
:::

::: good  
![Figure: Good example - This PBI informs the team that the work is complete and contains some examples of what the changes look like](closing-pbis-with-context.jpg)  
:::

Screenshots are just one of the things that you could add for more context, some other things you could have are:

* [Done Videos](/send-done-videos)
* Mention if there is relevant documentation that was updated
* Mention any additional context in the pull request that you didn't want to duplicate
* If you had a conversation with someone to change the outcome of the PBI, mention ["as per my conversation with..."](/as-per-our-conversation-emails/)
* If you are closing a PBI as "Duplicate", add a link to the PBI that is a duplicate
* If you are closing a PBI as "Won't Fix", mention the reason why it is not being fixed

::: info
**Note:** If you are using GitHub projects you will want to make sure you've checked the workflows for the your project to make sure the team understands the behavior of the work when it's state changes in the project.

You can open the **Hamburger menu | Workflows** to view all the workflows

![Figure: For issues specifically it's recommended you have these workflows configured and enabled](project-workflows.jpg)
:::

::: info
**Note:** In GitHub, there is a feature that allows PBIs to be automatically closed when a pull request (PR) is merged. Ideally, the PR contains all the context that would normally be included in a 'Done' reply to the PBI, streamlining the process. This feature is particularly useful as it ensures the issue is linked to the PR and eliminates the common 'I forgot to close the PBI' oversight. This feature is good for some teams.

Be aware, this auto-closes the issue and assumes merging the PR is the only work required. This is not always true depending on your [Definition of Done](/definition-of-done) and deployment process.

See [Avoid auto-closing issues](/avoid-auto-closing-issues).
:::
