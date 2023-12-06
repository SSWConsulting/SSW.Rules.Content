---
type: rule
title: Backlog - Do you keep your PBIs smaller than 2 days' effort?
uri: create-pbis-under-2-days
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
  - create-PBIs-under-2-days
created: 2009-09-15T09:20:55.000Z
archivedreason: null
guid: 06f5e085-3d2f-466d-91e9-6d0efe2b9d16
---

Very often you can come to the end of the Sprint and have incomplete features that either can’t be shipped or can be shipped but don't add any value to the end user or Product Owner. If you are given a feature that is going to take weeks, then split it following this rule.

<!--endintro-->

Your project could be a very small project spanning just a few weeks/few Sprints or it could be a big project spread across months with multiple Sprint reviews and multiple teams involved. The massive PBI problem finds its way in all projects. Inspite of all devs being available to work, no blockers, no last minute issues hijacking the Sprint, you could still end up either not pushing things to production or pushing some half done feature that can't be used.

### How to avoid this

There are a few steps to take that help avoid this problem:

1. [Check the PBI is well-defined](/defining-pbis)
2. [Review the PBI estimate](/estimating-do-you-know-how-to-size-user-stories-effectively)
3. [Check if you need a spike](/planning-meeting-do-you-encourage-spikes-aka-investigation-tasks-when-a-story-is-inestimable)
4. Check the PBI fits in with the Sprint Goal.
5. Avoid monolithic Product Backlog Items (PBIs). If the estimate is 2 days or more, it can probably be broken down further to make it more manageable.
6. Consider turning it into a parent PBI with many child PBIs using Epics (Azure DevOps) or Tasks/Sub-tasks (GitHub)

### How to break up PBIs

When you break a monolithic PBI down, try to see if you can break this into shippable features that the customer can use. From a user perspective, it might be better to have a new UI page with only 2 textboxes that actually save data to the DB than have a page with all UI elements but the save button doesn’t work.

If shippable features isn't going to work then another good way of splitting up a PBI is to think about what little pieces of functionality can be demoed to the Product Owner in the Sprint Review

Let's take a look at some examples:

Say you are doing the Sprint Planning and you see a PBI that says “Sync data with Xero” but not much else. It's been estimated as an 8 day task, which will almost certainly take multiple Sprints. Here are some ways to approach it:

#### Example 1 - Sync Data with Xero - UI First

* Start by having a PBI that shows the sync status of invoices. Then, during the Sprint Review you might not have any backend working, but at least you can show off a nice little UI addition.
* Next, you might have the logic for syncing the invoice to Xero when you save it. Now in the Sprint Review, you can show that little UI piece changing as it syncs.
* After that, you might do the reverse, and implement the web hooks to sync from Xero to the app. Then, in the Sprint Review you will be able to show the sync status changing the other way.
* Finally, the last part might be to implement a manual sync fallback in case the automatic sync fails.

#### Example 2 - Sync Data with Xero - Backend First

* Start by having a PBI that just calls the Xero API with the required data. During the Sprint review, you can then use Postman to demo this API call and Xero getting updated.
* Similarly, the next PBI could be the web hooks from Xero calling your APIs to send data back which again you can demo via Postman or the Xero developer portal
* The next PBI can be the API getting triggered via the UI or as required by the app. This part will lend to the demo quite easily.

If for some reason you do end up with incomplete PBIs at the end of the Sprint, check out [Ending a Sprint - Do you know what to do with partially completed PBI?](/ending-a-sprint-do-you-know-what-to-do-with-partially-completed-stories)

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
