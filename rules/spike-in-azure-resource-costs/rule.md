---
type: rule
title: Do you proactively notify about expected spikes in Azure Resource costs?
uri: spike-in-azure-resource-costs
authors:
  - title: Warwick Leahy
    url: https://ssw.com.au/rules/warwick-leahy
related:
  - azure-budgets
created: 2023-11-14T04:02:45.191Z
guid: 0f608bf3-d8b6-410f-8c9a-c4498f4eadad

---

Always inform stakeholders in advance if you anticipate a significant increase in Azure resource costs. This proactive communication is crucial for budget planning and avoiding unexpected expenses.

<!--endintro-->

## Why This Matters

1. **Budget Management:** Sudden spikes in costs can disrupt budget allocations and financial planning.
2. **Transparency:** Keeping stakeholders informed fosters trust and transparency in operations.
3. **Planning:** Advance notice allows for better resource allocation and potential cost optimization strategies.

## How to Implement

* **Communicate Early:** As soon as a potential cost increase is identified, communicate this to relevant stakeholders.
* **Provide Details:** Include information about the cause of the spike, expected duration, and any steps being taken to mitigate costs.

### Scenarios

::: greybox
A team needs to perform a bulk update on millions of records in an Azure Cosmos DB instance, a task that requires scaling up the throughput units substantially. They proceed without notifying anyone, assuming the cost would be minimal as usual. However, the intensive usage for a week leads to an unexpectedly high bill, causing budgetary concerns and dissatisfaction among stakeholders.
:::

::: bad
Figure: Bad example - Nobody likes a surprise bill
:::

::: greybox
Before running a large-scale data migration on Azure SQL Database, which is expected to significantly increase DTU (Database Transaction Unit) consumption for a week, the team calculates the expected cost increase. They inform the finance and management teams, providing a detailed report on the reasons for the spike, the benefits of the migration, and potential cost-saving measures.

Then send an email (as per the template below)
:::

::: good
Figure: Informing and emailing stakeholders before a spike makes everyone happy
:::

#### Email template

::: email-template  
|          |     |
| -------- | --- |
| To:      | {{ SpendMaster (aka SysAdmins) }} |
| Subject: | {{ PROJECT NAME }} - Cost spike due to data migration  |  
::: email-content  

### Hi {{ SpendMaster aka SysAdmins }}  

I need to perform {{ TASK }} on {{ PROJECT NAME }}. I know that this will cost more than our usual amount for Azure. I expect the process to run for {{ X }} days.

I have calculated this cost to be {{ $$ }}.

1. Please approve
:::  
:::

---

Remember, effective communication about cost management is key to maintaining a healthy and transparent relationship with all stakeholders involved in your Azure projects.
