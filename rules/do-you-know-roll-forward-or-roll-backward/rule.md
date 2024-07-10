---
type: rule
tips: ""
title: Do you know when to Roll Forward and when to Roll Backward?
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
created: 2024-07-10T05:56:48.707Z
guid: dc944a7a-f2dd-4410-8629-5eb8d320ff51
---
In software development, deciding whether to **Roll Forward** or **Roll Backward** during deployments is crucial for maintaining system stability. This rule provides detailed scenarios to help determine the best strategy for handling deployment issues.

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

- **Backward-Compatible Database Changes:** Database schema changes do not break the previous version's functionality.
  - **Scenario:** Adding a new table or column that does not interfere with existing database structures or application functionality.

#### Rolling Forward
Rolling backward involves reverting to a previous stable version of the software after encountering issues with the new deployment. This strategy aims to restore the system to a known good state. 

##### Scenarios for Rolling Backward: 
- **Major Issues:** When the new deployment has significant bugs or performance issues that severely impact functionality.
  - **Scenario:** A new release causes the application to crash frequently, making it unusable for users.

- **No Immediate Fix:** If there are no immediate fixes available for the issues introduced by the new deployment.
  - **Scenario:** A critical bug is discovered, and the development team estimates that it will take several days to fix.

- **Data Integrity Risks:** When the new deployment risks compromising data integrity or security.
  - **Scenario:** A deployment causes data corruption, putting user data at risk and requiring an immediate rollback to protect integrity.

- **Regulatory Compliance:** When the issues violate regulatory compliance or legal requirements.
  - **Scenario:** A deployment unintentionally causes the system to be non-compliant with **GDPR** regulations, necessitating a rollback to avoid legal consequences.

- **Non-Backward-Compatible Database Changes:** The new release involves database schema changes that are not compatible with the previous version.
  - **Scenario:** A new deployment alters the data schema in a way that breaks existing reports and data integrations, requiring a rollback.

- **High Downtime:** When the new deployment leads to high system downtime, affecting availability.
  - **Scenario:** The new version causes the system to be down frequently, impacting business operations and leading to a decision to revert to the stable version. 

#### Summary
- **Rolling Forward** is used when issues are minor, fixes are known and quick to apply, or the new deployment is crucial for business operations. Scenarios include minor bugs, emergency fixes, and improvements over the existing state. 

- **Rolling Backward** is used when issues are major, no immediate fixes are available, or the impact on users and business operations is severe. Scenarios include significant bugs, data integrity risks, and regulatory compliance issues. 
