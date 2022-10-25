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
- title: Prem Radhakrishnan
  url: https://ssw.com.au/people/prem-radhakrishnan
related: 
- defining-pbis
- estimating-do-you-know-how-to-size-user-stories-effectively
- planning-meeting-do-you-encourage-spikes-aka-investigation-tasks-when-a-story-is-inestimable
redirects:
- spec-do-you-keep-your-pbis-smaller-than-2-days-effort
- spec-do-you-create-tasks-under-4-hours
- keep-PBIs-smaller-than-2-days/

---

Very often you can come to the end of the Sprint and have incomplete features that either can’t be shipped or can be shipped but don't add any value to the end user or Product Owner. If you are given a feature that is going to take weeks, then split it following this rule. 

<!--endintro-->

Your project could be a very small project spanning just a few weeks/few sprints or it could be a big project spread across months with multiple sprint reviews and multiple teams involved. The massive PBI problem finds its way in all projects. Inspite of all devs being available to work, no blockers, no last minute issues hijacking the sprint, you could still end up either not pushing things to production or pushing some half done feature that can't be used. How can we avoid this?

The first step when you start planning for a Sprint is to make sure that there is enough detail in the PBI. Read [Do you know how to define a PBI](https://www.ssw.com.au/rules/defining-pbis) for more information on this. Once you have enough detail in the PBI, you should reassess the estimate and effort required for this PBI. Read [Do you know how to size your PBIs effectively?](https://www.ssw.com.au/rules/estimating-do-you-know-how-to-size-user-stories-effectively) for more information on this. If there are unknowns in the PBI or you need to investigate something, try and do a spike so you can estimate more accurately. [Do you encourage Spikes in your sprint?](https://www.ssw.com.au/rules/planning-meeting-do-you-encourage-spikes-aka-investigation-tasks-when-a-story-is-inestimable)

Once you have done this, you should have a good estimate of what is the effort required for this feature to be shipped. So take a look at this again from a Sprint Goal perspective. Avoid monolithic Product Backlog Items (PBIs). Ideally, all PBIs should be less than 2 days. Anything over means there is an opportunity to break this down further.

When you break a monolithic PBI into a single one, try to see if you can break this into shippable features that the customer can use. From a user perspective, it might be better to have a new UI page with only 2 textboxes that actually save data to the DB than have a page with all UI elements but the save button doesn’t work.


::: email-template  
|          |     |
| -------- | --- |
| Subject: | Sync data to Xero |   
:::
::: bad
Figure: Bad example - This is a monolithic 8-day task
:::

::: email-template  
|          |     |
| -------- | --- |
| Subject: | Xero Sync #1 - Update UI to show sync status for invoices and receipts |   
:::
::: email-template  
|          |     |
| -------- | --- |
| Subject: | Xero Sync #2 - Update the "Save" option in "Invoice Details" page to push data to Xero |   
:::
::: email-template  
|          |     |
| -------- | --- |
| Subject: | Xero Sync #3 - Create endpoints for Xero web hooks to push data from Xero to client app  |   
:::
::: email-template  
|          |     |
| -------- | --- |
| Subject: | Xero Sync #4 - As a backup, add a manual option to re-sync data with Xero in case either system was down |   
:::
::: good
Figure: Good example - The same monolithic task, broken down into 4 smaller tasks which can all be shipped incrementally
:::

If for some reason you do end up with incomplete PBIs at the end of the sprint, check out [Ending a sprint - Do you know what to do with partially completed PBI?](https://www.ssw.com.au/rules/ending-a-sprint-do-you-know-what-to-do-with-partially-completed-stories)

For multiple PBIs that are part of a larger feature, you may also want to consider creating Epic (Azure DevOps) or Tasks/Sub-tasks (GitHub). 
