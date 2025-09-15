---
seoDescription: Microsoft Teams usage reports help identify popular and unused teams, track adoption, and monitor meeting and chat activity.
type: rule
title: Do you review Microsoft Teams usage reports?
uri: teams-usage
authors:
  - title: Jean Thirion
    url: https://www.ssw.com.au/people/jean-thirion
related:
  - rules-to-better-google-analytics-reports
  - sharepoint-usage
created: 2021-11-17T06:17:05.753Z
guid: afceb7ff-03e5-4260-87b8-71d581c73ffd
---

Usage analytics is quite important - it allows you to identify popular and unused teams, and helps figuring out Microsoft Teams adoption across your business (i.e. How many meetings? How many chats? etc...)

There are 2 places to check for usage reports in Teams:

<!--endintro-->

### Team Usage

![Figure: Access team usage from "Team Settings" | "Manage Team" | "Analytics"](teams-team-usage.jpg)

### Tenant Usage

This is by far the most interesting and import report. You need special (tenant-level) permissions to access those [usage reports](https://admin.microsoft.com/?source=applauncher#/reportsUsage/TeamsUserActivityV1).

![Figure: Access tenant level usage via "Office 365 Admin Center" | "Reports" | "Usage" | "View More" (under Microsoft Teams activity section)](teams-tenant-usage.jpg)

Now enjoy the full power of Teams usage analytics!

![Figure: Click on column names to sort data (e.g. "Chat Messages")](teams-tenant-usage-home.jpg)

::: info
**Important:** If you can't see users logins such but GUIDs instead, you will need some SysAdmin magic to make it happen. Simply follow these steps: [Show user details in the reports](https://docs.microsoft.com/en-AU/microsoft-365/admin/activity-reports/activity-reports?view=o365-worldwide#show-user-details-in-the-reports&WT.mc_id=M365-MVP-33518)

...and unlock the power of full O365 reporting!
:::
