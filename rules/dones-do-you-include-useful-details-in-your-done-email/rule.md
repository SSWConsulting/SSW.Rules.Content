---
type: rule
title: Dones - Do you include useful details in your 'Done' email?
uri: dones-do-you-include-useful-details-in-your-done-email
authors:
  - title: Adam Cogan
    url: /people/adam-cogan
  - title: Ulysses Maclaren
    url: /people/ulysses-maclaren
  - title: Cameron Shaw
    url: /people/cameron-shaw
  - title: Justin King
    url: /people/justin-king
related:
  - definition-of-done
  - comments-do-you-enforce-comments-with-check-ins
  - do-you-add-context-reasoning-to-your-emails
redirects: []
created: 2011-05-29T16:10:16.000Z
archivedreason: null
guid: d5b7a283-6bad-4b12-a49d-9a88e30a552b
---
An email with just the word "done" can often be enhanced with a screen capture or code snippet. Obviously this is also valid for tasks/requests.

In any email you send, **include relevant information**, such as [URLs](/dones-do-your-dones-include-a-url), screenshots, and pieces of code/text that will allow others to understand what was done or needs to be done straight away.

<!--endintro-->

### Benefits

* Improved visibility and transparency - The recipients can see the work actually being done
* Reduced cost of fixing a bug - the cost of a bug goes up based of the length of time taken for the client to ask for a change. If you tell a developer to change something they did today, it is many times cheaper for them to fix than if they got the same request 2 months later (when they have forgotten what it was about)
* The client can raise questions based on what they see in the code
* Finally, in the very unlikely case that the code repository and backup goes corrupt, your emails are a backup!

### Examples

::: email-template
|          |     |
| -------- | --- |
| To:      | Dave |
| Subject: | RE: Northwind - Include one more field to the form |
::: email-content  

### Hi Dave,

Done on the contact page

:::
:::
::: bad
Figure: Bad example - "Done" email lacks details
:::

::: email-template
|          |     |
| -------- | --- |
| To:      | Dave |
| Subject: | RE: Northwind - Include one more field to the form |
::: email-content  

### Hi Dave,

Done - added "State" field to the contact form - northwind&#46;com/contact

  ![Figure: New "State" field added](good-done-example-form.png)  

\[Insert code changes\]

:::
:::
::: good
Figure: Good example - "Done" email has a link, a screenshot, and code changes
:::

### Tips

* [Use balloons instead of a 'Wall of Text'](/screenshots-do-you-use-balloons-instead-of-a-wall-of-text)
* On browser screenshots, make sure you include the top-left area - so others can see the URL and what browser is being used. E.g. Chrome or Edge 
* If you are using Azure DevOps or GitHub, you should also include a URL to the work item
* Include a [.diff file](https://www.diffchecker.com/) for greater code/text changes
