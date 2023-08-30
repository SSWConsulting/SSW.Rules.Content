---
type: rule
title: Power Automate Flows - Do you use service accounts?
uri: power-automate-flows-service-accounts
authors:
  - title: Adam Cogan
    url: https://www.ssw.com.au/people/adam-cogan
  - title: Ash Anil
    url: https://www.ssw.com.au/people/ash/
  - url: https://www.ssw.com.au/people/kiki/
    title: Kaique Biancatti
related:
  - disable-leaving-employee-accounts
created: 2022-05-26T17:50:48.698Z
guid: 3203bffa-26ab-4325-a866-ec2abcaec377
---
Using a service account is a common best practice. If a flow is not shared with a group, it will be lost when an owner leaves the company. 

<!--endintro-->

::: bad
![Figure: Bad example – The red arrow shows the user as an owner. It is not shared to a group](2023-07-17_17-16-51.jpg)
:::

::: good
![Figure: Good example – see arrows the names are service accounts that will still work after an employee leaves the company](power-platform-services-accounts.png)
:::

### Do you have issues with connections in Power Automate flows?

If a Flow is exclusively shared with a single user, it will be deleted shortly after that user is deleted. We aim to avoid having any deleted flows.

For the above to not happen, share your flow with a group, so it is never deleted when the owner leaves the company or gets deleted. 

For e.g. Share with the SysAdmin group. Even when a connection string is lost or invalid, SysAdmins will get a notification to fix the problem
