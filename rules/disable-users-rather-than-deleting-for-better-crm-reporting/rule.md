---
type: rule
title: Do you Disable AD Users rather than Deleting for better CRM Reporting?
uri: disable-users-rather-than-deleting-for-better-crm-reporting
authors:
  - title: Steven Andrews
    url: https://ssw.com.au/people/steven-andrews
  - title: Chris Schultz
    url: https://www.ssw.com.au/people/chris-schultz
related: []
redirects:
  - do-you-disable-ad-users-rather-than-deleting-for-better-crm-reporting
created: 2019-07-10T22:47:08.000Z
archivedreason: null
guid: e3a7e485-04bc-43d8-82c4-e8a788ea06cc
---
When a user is created in Active Directory (AD), a Global Unique Identifier (GUID) is also created. As the name suggests this is unique for each user and is never duplicated in a domain.

<!--endintro-->

![Figure: GUID for User Steven Andrews](guid.png)

When adding a user to CRM, they are assigned with an Employee ID that is linked to the AD account’s GUID.

![Figure: AD User StevenAndrews is tied to STA Employee ID through AD GUID](aduser.png)

When a user leaves, many companies go through the process of disabling the CRM account and then deleting the AD User.


This creates problems if the employee comes back to the company and a new AD account is created for them - they are no longer able to be associated with the previously created CRM account. Instead, they will need a new CRM user with a different Employee ID.

This makes reporting on a user that has returned more difficult. To get around this problem, it is better to disable and move the user to a "Disable Users" OU in AD, so that if they return, the AD and CRM user can just be re-enabled.