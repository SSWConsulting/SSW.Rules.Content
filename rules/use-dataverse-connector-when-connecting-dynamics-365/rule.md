---
seoDescription: Do you need a Dynamics 365 connection? Use the Dataverse connector to unlock faster and more customizable reporting.
type: rule
archivedreason:
title: Do you use the Dataverse connector when connecting the Dynamics 365?
guid: 05bebc24-ba23-469d-9930-1cdc8ee9d253
uri: use-dataverse-connector-when-connecting-dynamics-365
created: 2021-02-08T20:35:17.0000000Z
authors:
  - title: Mehmet Ozdemir
    url: https://ssw.com.au/people/mehmet-ozdemir
related: []
redirects:
  - do-you-use-the-dataverse-connector-when-connecting-the-dynamics-365
---

When creating a Power BI connection to Dynamics 365, the first thing that comes to mind when searching for a connector is to search for Dynamics 365, seems logical enough right?

<!--endintro-->

Wrong.

::: bad  
![Figure: Bad example - Searching for Dynamics 365 connector](dynamics-connector-1.png)  
:::

When connecting to Dynamics 365 data [always use the Dataverse connector](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-powerbi-connector?tabs=Dataverse) (if it is available). Your system admin will need to tinker with some settings to enable this support, but it's simple and easy enough to do.

Once enabled instead of using Dynamics 365 (online) connector use the Dataverse connector.

::: good  
![Figure: Good example - Use the Dataverse connector instead](dynamics-connector-2.png)  
:::

✅ Advantages of using the Dataverse connector:

* Supports both Import and Direct Query (Direct Query means live reporting 🙂)
* Dataverse is built on top of TDS (Tabular Data Stream), meaning it should be much faster than the WebAPI connector
* Potential to write custom SQL queries for data sources

There are **no** disadvantages of using the Dataverse connector.
