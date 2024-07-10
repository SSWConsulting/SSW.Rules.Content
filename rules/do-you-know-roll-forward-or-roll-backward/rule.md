---
type: rule
tips: ""
title: Do You Know When to Roll Forward and When to Roll Backward?
seoDescription: Do You Know When to Roll Forward and When to Roll Backward?
uri: do-you-know-roll-forward-or-roll-backward
authors:
  - title: Ozair Ashfaque
    url: https://www.ssw.com.au/people/ozair-ashfaque
  - title: Charles Vionnet
    url: https://www.ssw.com.au/people/charles-vionnet
  - title: Matt Wicks
    url: https://www.ssw.com.au/people/matt-wicks
  - title: Matt Goldman
    url: https://www.ssw.com.au/people/matt-goldman
  - title: Christian Morford-Waite
    url: https://www.ssw.com.au/people/christian-morford-waite
created: 2024-07-10T05:26:23.421Z
guid: dc944a7a-f2dd-4410-8629-5eb8d320ff51
---
In software development, deciding whether to **roll forward** or **roll backward** during deployments is crucial for maintaining system stability. This rule provides detailed scenarios to help determine the best strategy for handling deployment issues.

#### Rolling Forward
Rolling forward involves moving ahead with a new deployment or update, even if issues arise. The aim is to quickly apply a fix or additional update to resolve any problems caused by the initial deployment.

##### Scenarios for Rolling Forward:
- **Minor Issues:** If the deployed update has minor issues that can be quickly fixed with subsequent patches.
  - **Scenario:** A new feature is released with a minor UI bug that does not affect core functionality. The development team can deploy a quick patch within hours.

- **Emergency Fixes:** When the new deployment includes critical features or fixes that are necessary for the business.
  - **Scenario:** A security vulnerability is discovered, and an immediate patch is deployed to fix the issue, even though it introduces a few minor bugs.

- **Improvement Over Existing State:** If the new deployment, despite issues, is an improvement over the existing state of the system.
  - **Scenario:** A security vulnerability is discovered, and an immediate patch is deployed to fix the issue, even though it introduces a few minor bugs.

- **Cost of Rollback:** When the cost and impact of rolling back are higher than rolling forward with additional fixes.
  - **Scenario:** Rolling back would require significant downtime, impacting business operations more than fixing the issues in the current deployment.

- **Minimal Impact on User Data:** The changes do not significantly alter user data or the existing data schema.
  - **Scenario:** A minor update to the user interface does not affect the underlying data, allowing for quick fixes without risking data integrity.

- **Backward-Compatible Database Changes:** If the deployed update has minor issues that can be quickly fixed with subsequent patches.
  - **Scenario:** A new feature is released with a minor UI bug that does not affect core functionality. The development team can deploy a quick patch within hours.
