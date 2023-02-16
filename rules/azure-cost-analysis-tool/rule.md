---
type: rule
title: Do you Monitor Your Azure Costs Using The Azure Cost Analysis Tool?
uri: manage-azure-costs
authors:
  - title: Bryden Oliver
    img: https://www.ssw.com.au/people/static/Bryden-Oliver-Profile-7f1d63b91752134e13ca69002e619720.jpg
    url: https://www.ssw.com.au/people/bryden-oliver
  - title: Jonty Gardner
    img: https://www.ssw.com.au/people/static/Jonty-Gardner-Profile-f8b9960c1c5482051abe7255cbc2dfcd.jpg
    url: https://www.ssw.com.au/people/jonty-gardner
created: 2023-02-16T00:43:29.261Z
guid: 41299301-4290-4a07-a974-a065e28cff0b
---

Dealing with questions from Product Owners about expenses related to applications hosted on Azure can be a real headache 🥲

Get ready to empower your Product Owners! When it comes to expenses related to applications hosted on Azure, you want to have a solution that can not only help you understand where the spending is coming from but also find ways to optimize it. With Azure cost analysis, you can confidently provide your Product Owners with insights and recommendations that will save time and money, and make everyone's day a little brighter ✨

<!--endintro-->

`youtube: whXWijQCQTU`

Azure cost analysis gives you a detailed breakdown of where any Azure spending is coming from. It tells you costing by: 

* Scoped Area e.g. a subscription 
* Resource Group e.g. Northwind.Website
* Location e.g. Australia East
* Service type e.g. Azure App Service
Note: You can also 'filter by' any of these things to give you a narrowed down view

## Analysing the big dog spenders 

To optimize spending, analyze major costs in each category. Focus on top three contributors - optimizing beyond that may not be worth the effort. 

Key questions to ask:

* Can you scale down? 
* Did you need it in the first place? 
* Can you refactor your application to consume less? 
* Can you change the type of service or consumption model?

## Scoped Area

The acculmulative costs of a selected area over a given time period e.g. the cost of a subscription charted over the last year showing the trends and spikes during that time. 

Use this chart to identify spikes or lulls in costs. 

![Figure: Azure Portal | Cost Analysis | Scoped Area Chart](/area-chart.jpg) 

## Resource Group 

The cost of each resource group in the scoped area e.g the cost of the northwind website infrastructure

Look for the application costing the most and try to reduce it. Ignore the tiny ones.

![Figure: Azure Portal | Cost Analysis | Resource Group Breakdown](/resource-groups.jpg)

## Location 

The cost of each location e.g. Australia East

If you have your applications spread across multiple locations, this chart can help figure out if one of those locations is costing more than others. Consider scaling each location to the scale of usage in that location. ⚖️

![Figure: Azure Portal | Cost Analysis | Location breakdown ] (/locations.jpg)

## Service type 

The cost of each service used e.g. Azure App Service

If a specific service is costing alot of money, consider if there is a service that might be better suited, or if that service can have it's consumption model adapted to better fit the usage levels.

![Figure: Azure Portal | Cost Analysis | Service type breakdown] (/services.jpg)

## What if you suspect a specific resource is a problem?

The Azure cost analysis tool also allows for different views to be selected. If you think a specific resource is causing a problem, then select the "CostByResource" view and then you can view each aspect of a resource which is costing money. That way you can identify an area which can be improved.🎯

![Figure: Azure Portal | Cost Analysis | View | CostByResource | Individual component breakdown](/Service-Breakdown.jpg) 
