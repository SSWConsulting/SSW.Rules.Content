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

::: bad  
![Figure: Bad example - Searching for Dynamics 365 connector](dynamics-connector-1.png)  
:::

Wrong.

When connecting to Dynamics 365 data always use the Dataverse connector (if it is available). Your system admin will need to tinker with some settings to enable this support, but it's simple and easy enough to do, here's the link: <https://docs.microsoft.com/en-us/powerapps/maker/data-platform/view-entity-data-power-bi.?WT.mc_id=DX-MVP-33518>

Once enabled instead of using Dynamics 365 (online) connector use the Dataverse connector.

::: good  
![Figure: Good example - Use the Dataverse connector instead](dynamics-connector-2.png)  
:::

The advantages of using the Dataverse connector are:

* Supports both Import and Direct Query (Direct Query means live reporting 🙂)
* Dataverse is built on top of TDS (Tabular Data Stream), meaning it should be much faster than the WebAPI connector
* Potential to write custom SQL queries for data sources

The disadvantages of using the Dataverse connector are:

* None
