---
type: rule
title: Triaging - Do you correctly triage additional item requests?
uri: triaging-do-you-correctly-triage-additional-item-requests
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
  - turn-emails-into-pbis
redirects: []
created: 2009-08-18T04:45:08.000Z
archivedreason: null
guid: 368379e7-2a52-439c-973f-e58de293d65b
---

"Triage" is a term originally used to describe the assessment of injured persons into a priority order based on the severity and urgency of their injuries. While developers don't often deal with real life and death situations, the ability to prioritise and action issues that arise can keep the heartbeat of a project steady and strong.

<!--endintro-->

Managing additional work requests can reduce the adverse impact on estimates and deadlines.

![Figure: Only if it's life and death does it get added "in this Sprint"](SuccessfulProjects\_Triage.jpg)  

The first step is to analyse the priority of the additional item. Let's look at the rules to how to prioritize:

### By default, move new work into the next Sprint

Priority is dependent upon the severity of the request. Only if it is a 'critical bug', then it will be done "in this Sprint", most tasks however go "into the Backlog". They can include new feature requests, non-critical bug fixes, modifications and undiscovered work (i.e. work you didn't initially anticipate).   

::: info 
**Note:** On a fixed price contract, the rules change. Bugs should be fixed in the current Sprint if time allows, otherwise first thing in the next Sprint as they are stopping you from being paid.  
:::

### Exception #1 - Critical Bugs go into the current Sprint 

If you have a crash-to-code bug, most of the time it will go into the current Sprint. If it prevents one or more users accessing the system, it will also go into the current Sprint. High-priority bugs are fixed "in this Sprint".

Bugs are usually prioritised, so even non-critical bugs will likely end up in the next Sprint (via the Backlog).

### Exception #2 - A client can override

A request for a new screen with a new look-up table that doesn't prevent users from operating the system, should be allocated to "a later Sprint". 
If the client really *needs* it done now, they must specify "must be in this Sprint". This will become an 'additional item' in the current Sprint. 

If this request from the client will have a material impact on inflexible time and budget restraints, you need to speak and inform the client. 

For example: *"Hi Bill, this task you specified 'must be in this Sprint' will take an extra 4 days. Our critical deadline will be missed. Is that OK?"*

### Exception #3 - A Developer can override

A client may request a small feature (e.g. changing the sort order of a combo-box). This work can go in the current Sprint as long as the task is small (less than 1/2 hour) and the Sprint is not already slipping.  
  
If the work is over budget, then you need to obtain approval for any 'additional item', from both the project manager and the client, before adding the request into the Sprint. See more about how to [obtain approval for additional items that exceed estimates](/do-you-email-clients-as-soon-as-you-realise-you-will-overrun-your-original-estimate).

::: email-template  
|          |     |
| -------- | --- |
| To:      | Dave |
| Subject: | Northwind - Client List for Administrators  |  
::: email-content  

### Hi Dave,  

1. Please add a sort function (like the one in Office) next to the fields: Last Name, First Name, Advisers and Organization. 
2. Apply to other relevant pages which have these fields in a list i.e. adviser list for administrators, client list for advisers etc. 
3. Please use the text Ascending instead of "smallest to Largest" and Descending for "Largest to Smallest".

:::  
:::  
**Figure: The above email sample from a customer will, by default, go into a future Sprint, not the current**

