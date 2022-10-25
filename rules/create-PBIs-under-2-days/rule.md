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

Your project could be a very small project spanning just a few weeks/few sprints or it could be a big project spread across months with multiple sprint reviews and multiple teams involved. The massive PBI problem finds its way in all projects. Inspite of all devs being available to work, no blockers, no last minute issues hijacking the sprint, you could still end up either not pushing things to production or pushing some half done feature that can't be used. 

### How can we avoid this?

1. The first step when you start planning for a Sprint is to make sure that there is enough detail in the PBI. Read [Do you know how to define a PBI](https://www.ssw.com.au/rules/defining-pbis) for more information on this. 
2. Once you have enough detail in the PBI, you should reassess the estimate and effort required for this PBI. Read [Do you know how to size your PBIs effectively?](https://www.ssw.com.au/rules/estimating-do-you-know-how-to-size-user-stories-effectively) for more information on this. 
3. If there are unknowns in the PBI or you need to investigate something, try and do a spike so you can estimate more accurately. [Do you encourage Spikes in your sprint?](https://www.ssw.com.au/rules/planning-meeting-do-you-encourage-spikes-aka-investigation-tasks-when-a-story-is-inestimable)
4. Once you have done this, you should have a good estimate of what is the effort required for this feature to be shipped. So take a look at this again from a Sprint Goal perspective. 
5. Avoid monolithic Product Backlog Items (PBIs). Ideally, all PBIs should be less than 2 days. Anything over means there is an opportunity to break this down further or you run the risk of not being able to complete it in time for the Sprint.
6. For multiple PBIs that are part of a larger feature, you may also want to consider creating Epic (Azure DevOps) or Tasks/Sub-tasks (GitHub).

### How to break up PBIs 

When you break a monolithic PBI into a single one, try to see if you can break this into shippable features that the customer can use. From a user perspective, it might be better to have a new UI page with only 2 textboxes that actually save data to the DB than have a page with all UI elements but the save button doesn’t work.

Let's take a look at another example. Say you are doing the Sprint planning and you see a PBI that says “Sync data with Xero” but not much else. So first step we speak to the Product Owner and try to get a lot more detail. And once we have more info, we realise that this is not a 2-day task. This will be more likely a 8-day task which could very well go across multiple sprints. We know we need to split this up into multiple PBIs but how do we break this into manageable chunks? 

A good benchmark is to think in terms of “How can the user start using at least a part of this feature by the end of the sprint?” or What can I demo in my Sprint Review? In the above example, you could start off by having a PBI that shows the sync status of invoices. So even if nothing else goes into Production you have still shipped a feature that is telling the user whether the data they are looking at has been synced with Xero even though in this case none of the data is synced. Not a lot of effort for this one but a far more powerful than someone working on the entire API features in the backend but nothing tangible for the user at the end of the sprint. If you are working on integration back-end features, then split your PBIs based on what can be demo-ed in your Sprint Review. Maybe use Postman to show your APIs returning partial data if not everything. 

If for some reason you do end up with incomplete PBIs at the end of the sprint, check out [Ending a sprint - Do you know what to do with partially completed PBI?](https://www.ssw.com.au/rules/ending-a-sprint-do-you-know-what-to-do-with-partially-completed-stories)


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

 
