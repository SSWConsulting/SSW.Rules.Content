---
seoDescription: When planning to use Workflow, consider using it with SharePoint List instead of BCS, as Workflow doesn't support external lists and requires data storage in SharePoint.
type: rule
archivedreason:
title: Do you avoid using BCS when you need Workflow?
guid: 3ded0c3f-ba49-4b56-9b40-4e85c8f1472c
uri: do-you-avoid-using-bcs-when-you-need-workflow
created: 2010-06-04T06:39:12.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []
---

If you are planning to use Workflow, use Workflow with SharePoint List instead of BCS. Because Workflow cannot be associated directly with external lists. The reason is data is not stored in SharePoint, so the Workflow cannot be notified when items change.

<!--endintro-->

![](BCSDoesNotSupportWF.jpg)

::: bad
BCS doesn't have WorkFlow support

:::

![](WFSupportList.jpg)

::: good
Use WorkFlow with SharePoint List  
:::
