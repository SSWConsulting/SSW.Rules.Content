---
type: rule
archivedreason:
title: Do you keep Failed Requests clean?
guid: efa91cc5-943b-42f9-acc8-867ef943e4eb
uri: clean-failed-requests
created: 2023-09-22T06:44:51Z
authors:
  - title: Vlad Kireyev
    url: https://www.ssw.com.au/people/vlad-kireyev/
related:
---
Application Insights provide crucial insights into the health and performance of the application. Failed Requests allow the DevOps specialists to identify the specific errors and exceptions occurring in the application. However, keeping Failed Requests clean is crucial to troubleshoot and pinpoint the root causes of the problems efficiently. A cluttered failed requests list filled with irrelevant entries can make it difficult to identify the critical issues that require immediate attention.

<!--endintro-->

## Understand your Failed Requests

When cleaning up Failed Requests, it is important to identify the patterns between frequent offenders and categorize them into the following three categories:
1.	Irrelevant – Failed Requests that you expect but cannot do anything about.  
Examples: 404 responses to “/autodiscover.xml”, “/robots933456.txt”.

2.	Spam – Failed requests to the non-existent URLs for your application.  
Examples: 404 responses to “.php” or “wordpress” endpoints, which are not part of your application.

3.	Fixable – Failed Requests that you identify as bugs in your application.  
You can identify these requests by their URL belonging to the real endpoints or files in your application.  
Create Issues for these bugs, and if you cannot fix any of them yourself, pass them on to the people who can.  
Examples: 404 responses from missing images, 400 responses from API.

::: info
**Note:** Not everything you encounter can be matched to a pattern or fixed straight away.

If that is the case, continue to other requests. As the logs become cleaner, it will get easier to understand the problems with the left-over requests.
:::


## Clean your Failed Requests

While the Fixable Failed Requests can be nicely dealt with, by resolving their underlying causes, the other two will continue to clutter your Application Insights.

You can use **Application Dashboard** and **Azure Workbook** to filter out any unwanted failed requests and display only useful information.

**Application Dashboard** is a customizable interface that provides an overview of an application's performance and health. You can access it at the top of the Overview page of your Application Insights. If the Application Dashboard was not yet created, you must have a **Contributor Role** in that Resource Group. A new Application dashboard automatically displays various charts, metrics, and alerts to monitor application behavior.

**Azure Workbooks** is a tool that allows users to create customized dashboards for data visualization and reporting on Azure resources. You can use it to create charts and tables with custom queries in **Kusto Query Language (KQL)**, and then pin them to your **Application Dashboard**. By using the custom Kusto query, it is possible to filter out any unwanted Failed Requests for your custom chart!

::: info
**Tip:** You do not need to write your query from scratch! 

Go to Application Insights | Failures | View in Logs | Failed request count. 

This will provide you with the default query, that you can customize and test in Azure Logs, before sending it to Workbooks.
:::
