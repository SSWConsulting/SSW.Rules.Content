---
type: rule
archivedreason:
title: Do you use SharePoint Integration Reporting Mode over Normal(Native) Reporting Mode?
guid: c5baeed9-b836-40f7-9039-75be9612fbc9
uri: use-sharepoint-integration-reporting-mode
created: 2024-09-16T09:12:00.0000000Z
authors: 
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
related:
- when-to-use-reporting-services
redirects: []

---

With the use of SharePoint 2010 Integration mode of Reporting, users can have the following advantages:

<!--endintro-->

The users can easily deploy data sources, reports to sharePoint document libraries instead of Report Manager.
The users can be much more self-sufficient with SharePoint.
Very easy one step configuration of the add-in
37 languages supported including bi-directional languages.
Accessing Reporting in local mode when Access Services is enabled.
Improved Report Preview experience with Report Builder 3.0 and edit sessions and deploy their reports to SharePoint document libraries, leveraging SharePoint for security.
The users can take advantage of the new version of Report Builder that came with SQL Server 2008 R2 and deploy their reports to SharePoint document libraries, leveraging SharePoint for security.

::: bad  
![Figure: Bad example - SQL Report Manager (which requires Visual Studio and TFS if you want source control)](NativeMode.jpg)  
:::

::: good  
![Figure: Good example - SharePoint Integration (you get nice source control via SharePoint and you can use the nice Report Builder 3)](SharePointIntegratedMode.jpg)
:::
