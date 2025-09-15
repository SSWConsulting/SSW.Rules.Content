---
seoDescription: How to give customers a ballpark estimate of project costs using Scrum and Excel.
type: rule
archivedreason:
title: Do you know how to give the customer a ballpark?
guid: 1ac29d3d-fc89-462a-b0c5-d17c6889e66c
uri: spec-give-customers-a-ballpark
created: 2009-11-04T08:35:51.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Ulysses Maclaren
    url: https://ssw.com.au/people/ulysses-maclaren
  - title: Cameron Shaw
    url: https://ssw.com.au/people/cameron-shaw
  - title: Justin King
    url: https://ssw.com.au/people/justin-king
related: []
redirects:
  - spec-do-you-know-how-to-give-the-customer-a-ballpark
---

### How to create an estimate for a Spec Review (Summary)

This process can take up to a few days, so if you're just after a ballpark, use epics instead of PBIs (Product Backlog Items).

Here are the 8 steps:

<!--endintro-->

1. List all of the PBIs into a Backlog in Azure DevOps (or visualstudio.com), sizing them with story points
2. Open Excel and connect to the above Backlog
3. In Excel, add a column called "Hours"  
   **Note:** Once we move to estimating in time, this is no longer Scrum
4. In Excel, copy this list and paste into another spreadsheet called "Estimates Calculator" (see below for how to use this), in order to add all of the extra items (Testing, DevOps, Project management, etc.)  
   **Note:** It would be great if Azure DevOps had functionality to “Add Standard Items" to a Sprint
5. Run a [Test Please](/conduct-a-test-please-internally-and-then-with-the-client) on the numbers
6. Add a screenshot of this spreadsheet to your Specification Review document under Costing Summary
7. Present to the client
8. When the estimate is approved by the client, start work following [Rules to Better Scrum using Azure DevOps (Work Items)](/rules-to-better-scrum-using-azure-devops).

### Extra - How to use "Estimates Calculator"

Open the [Estimates Calculator](estimates-calculator.xlsx) and do the following:

![Figure: Set the types and numbers of resources who will be working on the project](resource-tab.png)

![Figure: Enter your PBIs and estimates](estimates-tab.png)

### Why Microsoft Project isn't recommended

Microsoft Project is sophisticated waterfall planning software that has powerful features for auto-scheduling and dependency allocation (Note: Project allows you to add 2 people to a task, and then the calculations and dependencies are all worked out). However:

- In MS Project, tasks are auto scheduled based on dependency and resource allocation (who is assigned to it). This generates an estimated completion date which is never accurate, due to annual leave, public holidays and general shuffling of people in the team
- It gets the summing wrong (the totals don't seem to update and no way to trigger it)
- It's hard to synchronize with timesheets (as it doesn't connect to 3rd party timesheet systems out of the box – however, it does have its own time sheeting system... that is missing billing information!)
