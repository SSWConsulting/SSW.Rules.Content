---
type: rule
title: Cost - Do you manage the cost of your Azure resources?
uri: manage-costs-azure
authors:
  - title: Kiki Biancatti
    url: https://www.ssw.com.au/people/kiki
created: 2021-09-29T07:27:48.269Z
guid: fc2201ed-c7cd-4be0-98b9-e2f5957788a7
---
Managing the monthly spend on cloud resources eg. Azure is hard. It gets harder for SysAdmins when developers add services without sending an email to aid in reconciliation.

<!--endintro-->

Azure has a nice tool for managing its own costs, called the Cost Analysis - https://docs.microsoft.com/en-us/azure/cost-management-billing/costs/quick-acm-cost-analysis \
You can break down costs per resource group, resource type and many other aspects in Azure.

Note: If your subscription is a Microsoft Sponsored account, you can't use the Cost Analysis tool to break down your costs, unfortunately. Microsoft has this planned for the future, but it's not here yet.

Even with Cost Analysis, Developers with enough permissions (e.g. Contributor permissions to a Resource Group) are able to create resources without the spend master (generally the SysAdmins) knowing, and this will lead to budget and spending problems at the end of the billing cycle.

For everyone to be on the same page, the process a developer should follow is:

1. Use the Azure calculator - work out the montly resource $ price   https://azure.microsoft.com/en-au/pricing/calculator
2. Email SysAdmins with $
   and a request to create in Azure