---
seoDescription: Learn how to effectively choose a multi-tenancy model that suits your system's needs. This rule covers various models, their advantages, and considerations for optimal implementation.
type: rule
title: Do you know how to choose the right multi tenancy model for your system?
uri: multi-tenancy-models
authors:
  - title: Rick Su
    url: https://www.ssw.com.au/people/rick-su
created: 2024-10-25T17:00:00.000Z
guid: 89CAA458-C142-47D2-A3B0-4F39CF18262C
---

Learn how to effectively choose a multi-tenancy model that suits your system's needs. This rule covers various models, their advantages, and considerations for optimal implementation.

<!--endintro-->

## Popular Models

* Single Application, Single Database
* Single Application, Multiple Databases
* Hybrid Models

Other models: <https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/considerations/tenancy-models>

## Decision Factors

### Cost Considerations

Analyze the total cost of ownership for each model, including initial setup costs, ongoing maintenance, and potential scaling expenses. Single database models tend to be more cost-effective initially but may incur higher operational costs as usage grows.

### Scalability Requirements

Consider how easily each model can scale with your user base. If you anticipate rapid growth, a model that allows for seamless scaling without significant re-architecture (like single application with multiple databases) may be preferable.

### Data Isolation and Security Needs

Evaluate the level of data isolation required by your tenants. Industries with strict compliance regulations may necessitate models that provide stronger data separation (like multiple applications with multiple databases) to ensure tenant data privacy.

### Customization Requirements

Determine if tenants need customized features or configurations within the application. Some models allow for greater customization at the database level but may complicate maintenance and upgrades.

### Performance Expectations

Assess how performance will be impacted by tenant activities in each model. Models that share resources can lead to performance degradation if not managed properly; hence understanding your workload patterns is essential.

### Management Complexity

Consider the complexity involved in managing each model over time. Simpler models may reduce operational overhead but could limit flexibility as business needs evolve.

By carefully weighing these factors against your organizational goals and tenant requirements, you can make a more informed decision regarding which multi-tenancy model best fits your system architecture.
