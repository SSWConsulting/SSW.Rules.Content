---
type: rule
archivedreason: 
title: Spec - Do you know how to give the customer a ballpark?
guid: 1ac29d3d-fc89-462a-b0c5-d17c6889e66c
uri: spec-do-you-know-how-to-give-the-customer-a-ballpark
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
redirects: []

---

### How to create an Estimate For a Spec Review (Summary)

This process can take up to a few days, so if you're just after a ballpark, use epics instead of PBIs (Product Backlog Items).

Here are the 8 steps:

<!--endintro-->

1. List all of the PBIs into a Backlog in TFS (or visualstudio.com), sizing them with story points.
2. Open Excel and connect to the above Backlog
3. In Excel, add a column called "Hours"
Note: Once we move to estimating in time, this is no longer Scrum.
4. In Excel, copy this list and paste into another spreadsheet called the [Estimates Calculator](https://github.com/SSWConsulting/SSW.Rules.Content/raw/main/rules/spec-do-you-know-how-to-give-the-customer-a-ballpark/4.%20Estimates%20Calculator.xlsx), in order to add all of the extra items (testing, DevOps, Project management, etc.).  **See below for how to use this.** 
Note: It would be great if TFS (or visualstudio.com) had functionality to add [standard items to a Sprint](http://www.ssw.com.au/ssw/Standards/BetterSoftwareSuggestions/TeamFoundationServer.aspx#StandardItems)
5. Run a [Test Please](/conduct-a-test-please-internally-and-then-with-the-client) on the numbers
6. Add this spreadsheet to your specification review document
7. Present to the client
8. Much later, when the estimate is approved by the client, start work following these rules: [Rules to Better Project Management with TFS](http://www.ssw.com.au/ssw/Standards/Rules/RulesToBetterProjectManagementWithTFS.aspx).

### More Info - How to use the Estimates Calculator

Open the [Estimates Calculator](https://github.com/SSWConsulting/SSW.Rules.Content/raw/main/rules/spec-do-you-know-how-to-give-the-customer-a-ballpark/4.%20Estimates%20Calculator.xlsx) and do the following:

![Figure: Set the types and numbers of resources who will be working on the project](Resource tab.png)

![Figure: Enter your PBIs and estimates](Estimates tab.png)

### Why Microsoft Project isn't recommended

Microsoft Project is sophisticated waterfall planning software that has powerful features for auto-scheduling and dependency allocation (Note: Project allows you to add 2 people to a task, and then the calculations and dependencies are all worked out). However:

* In MS Project, tasks are auto scheduled based on dependency and resource allocation (who is assigned to it). This generates an estimated completion date which is never accurate, due to annual leave, public holidays and general shuffling of people in the team
* It gets the summing wrong (the totals don't seem to update and no way to trigger it)
* It's hard to synchronize with timesheets (as it doesn't connect to 3rd party timesheet systems out of the box – however, it does have its own time sheeting system... that is missing billing information!)
