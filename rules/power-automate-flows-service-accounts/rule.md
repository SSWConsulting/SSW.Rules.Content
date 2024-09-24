---
seoDescription: Power Automate flows management best practices - Share flows with groups and use service accounts to ensure continuity and security.
type: rule
title: Power Automate Flows - Do you use groups and service accounts?
uri: power-automate-flows-service-accounts
authors:
  - title: Adam Cogan
    url: https://www.ssw.com.au/people/adam-cogan
  - title: Ash Anil
    url: https://www.ssw.com.au/people/ash-anil
  - title: Kaique Biancatti
    url: https://www.ssw.com.au/people/kaique-biancatti
related:
  - disable-leaving-employee-accounts
created: 2022-05-26T17:50:48.698Z
guid: 3203bffa-26ab-4325-a866-ec2abcaec377
---

Using groups and service accounts is a common best practice in the Power Platform world.

<!--endintro-->

### Groups

In Power Automate, if a flow is owned by an individual and not shared with a group, there's a risk of losing it if the owner leaves the company. In such cases, no notifications are sent out, and even Microsoft support cannot retrieve the lost data or flow.

Always share your flows with a relevant group. This ensures that the flow is not lost and that the group members receive notifications and can manage the flow.

::: bad
![Figure: Bad example – The red arrow shows the user as an owner. It is not shared to a group](2023-07-17_17-16-51.jpg)
:::

### Service Accounts

Using personal employee accounts for connectors in Power Automate can lead to disruptions. For instance, if an employee leaves or changes their password, the connector linked to their account breaks.

Utilize service accounts (e.g., `info@northwind.com` instead of `BobNorthwind@northwind.com`) for connectors. This ensures continuity and security, as service accounts are not subject to frequent changes like employee accounts.

::: good
![Figure: Good example – Groups and Service Accounts cleverly used to not lose any flows](powerautomateowner.png)
:::
