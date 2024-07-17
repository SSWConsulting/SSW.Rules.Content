---
type: rule
tips: ""
title: Do you know you should only Roll Forward?
seoDescription: Learn that you should only Roll Forward and not Roll Backward.
uri: when-to-roll-forward-or-roll-backward
authors:
  - title: Ozair Ashfaque
    url: https://www.ssw.com.au/people/ozair-ashfaque
  - title: Tino Liu
    url: https://ssw.com.au/people/tino-liu
  - title: Charles Vionnet
    url: https://www.ssw.com.au/people/charles-vionnet
  - title: Matt Wicks
    url: https://www.ssw.com.au/people/matt-wicks
  - title: Matt Goldman
    url: https://www.ssw.com.au/people/matt-goldman
created: 2024-07-10T05:56:48.707Z
guid: dc944a7a-f2dd-4410-8629-5eb8d320ff51
---
You found out there's a bug in your application. As a Developer, what are you going to do?

![New Bug](https://imgs.xkcd.com/comics/new_bug.png)

### Rolling Forward Makes the Dream Work

Rolling Forward involves moving ahead with a new deployment or update, even if issues arise. The aim is to apply a fix or additional update to resolve any problems caused by the initial deployment. By doing so, it continuously moves the project towards its goals.

#### Scenarios

- **Minor Issues:** Quick fixes for minor issues ensure continuous progress without reverting.
  - **Scenario:** A new feature is released with a minor UI bug that does not affect core functionality. The development team deploys a quick patch within hours, maintaining forward momentum.

- **Emergency Fixes:** Critical features or fixes are implemented promptly, prioritizing rolling forward over reverting.
  - **Scenario:** A security vulnerability is discovered, and an immediate patch is deployed to fix the issue. Although it introduces a few minor bugs, these are swiftly addressed with subsequent updates.

- **Improvement Over Existing State:** New deployments, even with minor issues, represent an overall improvement, justifying rolling forward.
  - **Scenario:** A feature update, while introducing minor bugs, significantly enhances system performance and security. The team quickly patches the minor issues, ensuring the system remains improved.

- **Cost of Rollback:** When the cost and impact of rolling back are higher than rolling forward with additional fixes.
  - **Scenario:** Rolling back would require significant downtime, severely impacting business operations. Instead, the team rolls forward, fixing the issues in the current deployment with minimal disruption.

- **Minimal Impact on User Data:** The changes do not significantly alter user data or the existing data schema.
  - **Scenario:** A minor update to the user interface does not affect the underlying data, allowing for quick fixes without risking data integrity.

- **Backward-Compatible Database Changes:** Database schema changes are implemented in a way that supports continuous forward compatibility.
  - **Scenario:** Adding a new table or column that does not interfere with existing database structures or application functionality.
 
#### Hold up! What if the issue is HUGE and CATASTROPHIC?

Generally speaking, catastrophic issues should be cought early in the delivery pipelines so that there's no need to Rolling Backward. Here are a few examples developers can do to prevent catastrophic issues from sneaking into prodcution ([Rules to Better Testing](https://www.ssw.com.au/rules/rules-to-better-testing/#3-integration-testing)):

- Write Unit Tests ([Rules to Better Unit Tests](https://www.ssw.com.au/rules/rules-to-better-unit-tests/))
- Understand the different types of testing ([Rules for Different Types of Testing](https://www.ssw.com.au/rules/different-types-of-testing/))
- Set up a production-like environment, such as a Staging environment, for testing ([Rules for Setting up Environments](https://www.ssw.com.au/rules/do-you-know-which-environments-you-need-to-provision-when-starting-a-new-project/))
- Developers can implement new features using feature flags. If an issue arises in production, the feature can be disabled, allowing developers to fix the problem without rolling back the entire release ([Manage Feature Flags in Azure App Configuration](https://learn.microsoft.com/en-us/azure/azure-app-configuration/manage-feature-flags?tabs=azure-portal))

Rolling Backwards should only be considered when abosolutely necessary if an error is threatening system stability and integrity.
Here are a few examples:

- Critical Production Outages
- Security Vulnerabilities
- Data Corruption
- Compliance Violation

### Summary
Software Engineers should prioritize Rolling Forward through practices that ensures continuous improvement, risk mitigation, and incremental process. Upwards and onwards!
