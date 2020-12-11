---
type: rule
archivedreason: 
title: Do you standardize AD group names?
guid: 6681c17d-fa8f-4187-8bed-a0df63f0e90c
uri: do-you-standardize-ad-group-names
created: 2015-02-16T00:13:41.0000000Z
authors:
- id: 45
  title: Chris Briggs
- id: 47
  title: Stanley Sidik
related: []

---

The use of standardized AD Group names is a simple yet crucial step towards building more manageable software. Raining in on the number of AD Groups used by an application will make it simpler to manage and allow new developers to pick up an existing project faster.

<!--endintro-->

**You can save yourself countless confused conversations by standardizing AD Group Names.**

For example: This is a list of AD groups associated with products.


::: greybox
SSWSugarLearningEvents
 SSWCodeAuditorAlerts
 SSWLinkAuditorDevs
:::



::: bad
Figure: Bad Example – It is difficult to know the correct name for an AD group
:::



::: greybox
SSWSugarLearning
 SSWSugarLearningEvents
 SSWCodeAuditor
 SSWCodeAuditorEvents
 SSWLinkAuditor
 SSWLinkAuditorEvents
:::



::: good
Figure: Good Example – By standardizing the names of AD groups it saves confusion

:::


**
Note: ** For large organizations, a better way is  to use a type of group (eg. Local or Global)… then the entity it is associated to… then the resource (or service).

**E** **xample** **#1:**

L-LocalGroupName-
   SYD-EntityName-
   SP-Sharepoint-

That becomes “L-SYD-SP-SSW-Users"

**E** **xample** **#2:**

G-GlobalGroupName-
   SYD-EntityName-
   SP-Sharepoint-

That becomes “G-SYD-SP-SSW-Users"

**Note:** You would not use this naming convention for distribution groups – as they would display to users.

It is recommended by default to have two AD groups per product. The following table should be used as a guide for naming them:


| Name | Type | Purpose |
| --- | --- | --- |
| SSW&lt;ProductName&gt; | Distribution group | This email is used to send emails to the development team for a product. |
| SSW &lt;ProductName&gt;Events | Mailbox | Acts as the collection point for all automatic notifications. For example notifications from Elmah and/or application insights. <br> |
