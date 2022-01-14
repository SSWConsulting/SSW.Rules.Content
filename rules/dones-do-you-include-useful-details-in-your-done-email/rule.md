---
type: rule
archivedreason: 
title: Dones - Do you include useful details in your 'Done' email?
guid: d5b7a283-6bad-4b12-a49d-9a88e30a552b
uri: dones-do-you-include-useful-details-in-your-done-email
created: 2011-05-29T16:10:16.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ulysses Maclaren
  url: https://ssw.com.au/people/ulysses-maclaren
- title: Cameron Shaw
  url: https://ssw.com.au/people/cameron-shaw
- title: Justin King
  url: https://ssw.com.au/people/justin-king
related: 
- dones-do-you-reply-done-and-delete-the-original-email
- done-do-you-go-beyond-done-and-follow-a-definition-of-done
- comments-do-you-enforce-comments-with-check-ins
redirects: []

---

An email with just the word "done" can often be enhanced with a screen capture or code snippet.

In any reply, **include relevant information**, such as URLs, screenshots, and pieces of code/text that have been updated. This allows others to check what was done straight away.

<!--endintro-->

### Benefits 

This has several benefits:

* Improved visibility and transparency - The client can see the work actually being done
* Reduced cost of fixing a bug - the cost of a bug goes up based of the length of time taken for the client to ask for a change. If you tell a developer to change something he did today, it is many times cheaper for him to fix, than if he got the same request 2 months later (when he has forgotten was it was about)
* The client can raise questions based on what he sees in the code
* Finally, in the very unlikely case that the code repository and backup goes corrupt, your emails are a backup!

### Examples

::: email-template  
|          |     |
| -------- | --- |
| To:      | Jason |
| Subject: | RE: Northwind - Include one more field to the form |  
::: email-content  

### Hi Jason,  
Done on the contact page

:::  
:::  
::: bad  
Figure: Bad Example - "Done" email lacks details
:::

::: email-template  
|          |     |
| -------- | --- |
| To:      | Jason |
| Subject: | RE: Northwind - Include one more field to the form |  
::: email-content  

### Hi Jason,  
Done - added "State" field to the contact form - <u>northwind&#46;com/contact</u>

  ![Figure: New "State" field added](good-done-example-form.png)  

\[Insert code changes\]

:::  
:::  
::: good  
Figure: Good Example - "Done" email has a link, a screenshot, and code changes
:::

### Tips

- Read [Screenshots - Do you use balloons instead of a 'Wall of Text'?](/screenshots-do-you-use-balloons-instead-of-a-wall-of-text).
- On browser screenshots, make sure you include the top-left area - so you can see the URL and what browser it is. E.g. Chrome or Edge.  
- If you are using Azure DevOps or GitHub, you should also include a URL to the work item.
- Include a [.diff file](https://www.diffchecker.com/) for greater code/text changes.
