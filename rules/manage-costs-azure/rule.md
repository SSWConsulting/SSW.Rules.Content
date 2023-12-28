---
type: rule
title: Cost - Do you manage the cost of your Azure resources?
uri: manage-costs-azure
authors:
  - title: Kaique Biancatti
    url: https://ssw.com.au/people/kiki
  - title: Warwick Leahy
    url: https://ssw.com.au/people/warwick-leahy
related:
  - do-you-have-an-azure-spend-master
redirects:
  - do-you-manage-costs-azure
created: 2021-09-29T07:27:48.269Z
guid: fc2201ed-c7cd-4be0-98b9-e2f5957788a7
archivedreason: Duplicate of [https://www.ssw.com.au/rules/azure-budgets](/rules/azure-budgets)

---

Managing the monthly spend on cloud resources (e.g. Azure) is hard. It gets harder for the [Spend Master (e.g. SysAdmins)](/do-you-have-an-azure-spend-master) when developers add services without sending an email to aid in reconciliation.

<!--endintro-->

Azure has a nice tool for managing its own costs, called the [Cost Analysis](https://docs.microsoft.com/en-us/azure/cost-management-billing/costs/quick-acm-cost-analysis). You can break down costs per resource group, resource type and many other aspects in Azure.

::: info

**Note:** If your subscription is a Microsoft Sponsored account, you can't use the Cost Analysis tool to break down your costs, unfortunately. Microsoft
has this planned for the future, but it's not here yet.

:::

Even with Cost Analysis, Developers with enough permissions (e.g. Contributor permissions to a Resource Group) are able to create resources without the Spend Master knowing, and this will lead to budget and spending problems at the end of the billing cycle.

For everyone to be on the same page, the process a developer should follow is:

1. Use the [Azure calculator](https://azure.microsoft.com/en-au/pricing/calculator) - work out the monthly resource $ price

2. Email the Spend Master with $ and a request to create resources in Azure, like the below:

::: email-template
|          |     |
| -------- | --- |
| To:      | Spend Master |
| Subject: | Purchase Please - Azure Resource Request for {{product/service}} |
::: email-content  

### Hi Spend Master aka SysAdmins

I would like you to provision a new Azure Resource for xx

* Azure Resource needed: I would like to create a new App Service Plan
* Azure Calculator link: {{add link}}
* Environment: {{add Dev/Staging/Prod}}

Project details:

* Project Name: A new project called {{add project name}}
* Project Description (The SysAdmin will copy this info to the Azure Tag): {{add description}}
* Project URL (e.g. Azure DevOps / Github): {{add URL}}

Total: {{AUD$}} per month

![Figure: I generated the price from https://azure.microsoft.com/en-au/pricing/calculator](azurecalcexample.jpg)

1. Please approve

David

<As per SSW Rule: [https://www.ssw.com.au/rules/manage-costs-azure>](/manage-costs-azure>)

:::
:::

3. Add a tag of cost-category to each of your resources. This will allow you to see the daily costs of your Azure resources based on whether they are Core, Value adding or Dev/Test. Then you can quickly turn off resources to save money if you require. It also helps you to see where money is disappearing.

![Figure: Daily costs by category](azurecostsbycategory.png)
