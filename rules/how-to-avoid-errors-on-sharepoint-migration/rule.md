---
seoDescription: SharePoint migration experts remove customizations and unsupported columns to ensure error-free reports with Sharegate.
type: rule
archivedreason:
title: Do you know how to avoid errors?
guid: 94ef1ccc-e1a5-409d-a29d-258231e43ce4
uri: how-to-avoid-errors-on-sharepoint-migration
created: 2018-01-17T22:59:30.0000000Z
authors:
  - title: Jean Thirion
    url: https://ssw.com.au/people/jean-thirion
related: []
redirects:
  - do-you-know-how-to-avoid-errors
---

There are certain features in SharePoint on-premises that are no longer supported with SharePoint Online.

If you migrate using the Sharegate migration tool, you want to have zero errors in their reports. To do so, here are what you should do before considering migration:

<!--endintro-->

- Get rid of SharePoint Designer customizations on List form

::: bad  
![Bad example: Page customized using SharePoint Designer](avoid-errors-sp-migration1.png)  
:::

::: good  
![Good example: Out of the box list view page](avoid-errors-sp-migration2.png)  
:::

Remove unsupported columns such as:

- Publishing HTML
- Publishing Hyperlinks
- Calculated Columns with volatile functions ('Me', 'Today'…)
- Managed Metadata columns on folders
- Get rid of MicroFeed

::: bad  
![Bad example: Sharegate migration report shows error if MicroFeed(s) have not been removed](avoid-errors-sp-migration3.png)  
:::
