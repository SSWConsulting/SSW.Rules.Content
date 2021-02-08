---
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


<p class="ssw15-rteElement-P">​When creating a Power BI connection to Dynamics 365, the first thing that comes to mind when searching for a connector is to search for Dynamics 365, seems logical enough right?​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="badImage"><dt><img src="/PublishingImages/dynamics-connector-1.png" alt="dynamics-connector-1.png" /></dt><dd>Figure&#58; Bad example - Searching for Dynamics 365 connector</dd></dl><p>Wrong.</p><p>When connecting to Dynamics 365 data always use the Dataverse connector (if it is available). Your system admin will need to tinker with some settings to enable this support, but it's simple and easy enough to do, here's the link&#58;&#160;<a href="https&#58;//docs.microsoft.com/en-us/powerapps/maker/data-platform/view-entity-data-power-bi">https&#58;//docs.microsoft.com/en-us/powerapps/maker/data-platform/view-entity-data-power-bi</a>.</p><p>Once enabled instead of using Dynamics 365 (online) connector use the Dataverse connector.</p><dl class="goodImage"><dt><img src="/PublishingImages/dynamics-connector-2.png" alt="dynamics-connector-2.png" /></dt><dd>Figure&#58; Good example - Use the Dataverse connector instead</dd></dl><p>The advantages of using the Dataverse connector are&#58;<br></p><ul><li>Supports both Import and Direct Query (Direct Query means live reporting &#128578;)</li><li>Dataverse is built on top of TDS (Tabular Data Stream), meaning it should be much faster than the WebAPI connector</li><li>Potential to write custom SQL queries for data sources​<br></li></ul><p>The disadvantages of using the Dataverse connector are&#58;<br></p><ul><li>None</li></ul>


