---
type: rule
archivedreason: 
title: Spec - Do you keep your PBIs smaller than 2 days' effort?
guid: 06f5e085-3d2f-466d-91e9-6d0efe2b9d16
uri: spec-do-you-create-tasks-under-4-hours
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

---

Avoid monolithic Product Backlog Items (PBIs). Ideally, all PBIs should be less than 2 days. If you are given a feature that is going to take weeks, then split it following this rule. 

<!--endintro-->


::: greybox
Subject: Create an .NET 5 prototype with web services 

:::
Figure: Bad example – This is a monolithic 4-day task

::: greybox
Email #1 Subject:  .NET 5 prototype - Create a web page with firstname and lastname textboxes, a save button (and remmed out code to later call a web service)

Email #2 Subject:  .NET 5 prototype - Create a table for customer with firstname and lastname and any other fields required for this table

Email #3 Subject:  .NET 5 prototype - Create a web service with the customer CRUD methods
Angular prototype - with firstname and lastname textboxes, a save button (and remmed out code web service) 

Email #4 Subject:  .NET 5 prototype - Create methods on webservice exposed to client
.NET 5 prototype - with firstname and lastname textboxes, a save  
:::
Figure: Good example – The same monolithic task, broken down into 4 smaller tasks
