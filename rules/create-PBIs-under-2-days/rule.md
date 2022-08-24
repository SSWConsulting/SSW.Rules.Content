---
type: rule
archivedreason: 
title: Backlog - Do you keep your PBIs smaller than 2 days' effort
guid: 06f5e085-3d2f-466d-91e9-6d0efe2b9d16
uri: create-PBIs-under-2-days
created: 2009-09-15T09:20:55.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ulysses Maclaren
  url: https://ssw.com.au/people/ulysses-maclaren
- title: Cameron Shaw
  url: https://ssw.com.au/people/cameron-shaw
related: []
redirects:
- spec-do-you-keep-your-pbis-smaller-than-2-days-effort
- spec-do-you-create-tasks-under-4-hours
- keep-PBIs-smaller-than-2-days/

---

Avoid monolithic Product Backlog Items (PBIs). Ideally, all PBIs should be less than 2 days. If you are given a feature that is going to take weeks, then split it following this rule. 

<!--endintro-->

::: email-template  
|          |     |
| -------- | --- |
| Subject: | Create an .NET 5 prototype with web services |   
:::
::: bad
Figure: Bad example - This is a monolithic 4-day task
:::

::: email-template  
|          |     |
| -------- | --- |
| Subject: | .NET 5 prototype #1 - Create a web page with firstname and lastname textboxes, a save button |   
:::
::: email-template  
|          |     |
| -------- | --- |
| Subject: | .NET 5 prototype #2 - Create a table for customer with any other fields required for this table |   
:::
::: email-template  
|          |     |
| -------- | --- |
| Subject: | .NET 5 prototype #3 - Create a web service with the customer CRUD methods |   
:::
::: email-template  
|          |     |
| -------- | --- |
| Subject: | .NET 5 prototype #4 - Create methods on webservice exposed to client |   
:::
::: good
Figure: Good example - The same monolithic task, broken down into 4 smaller tasks
:::
