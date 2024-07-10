---
type: rule
tips: ""
title: Do you understand the risks of deploying on Fridays?
seoDescription: Avoid deploying on Fridays due to higher risks and potential
  weekend issues; if necessary, ensure comprehensive monitoring, follow a
  pre-deployment checklist, and have a robust communication and contingency plan
  in place
uri: risks-of-deploying-on-fridays
authors:
  - title: Charles Vionnet
    url: https://www.ssw.com.au/people/charles-vionnet/
created: 2024-07-05T02:41:49.271Z
guid: 530a2540-9b59-4272-8c86-f79d0bfa6aef
---
Deploying on a Friday has traditionally been risky due to limited post-deployment support over the weekend, potentially leaving issues unaddressed. Thanks to DevOps best practices, these concerns are largely mitigated by automated deployments, continuous integration, and real-time monitoring, making the deployment process smoother and more reliable.

Nonetheless, we should be aware of situations where caution is advised.

<!--endintro-->

::: img-large  
![Figure: Avoid deploying on Friday... unless you have a plan](risks-of-deploying-on-fridays.png)
:::

While it is best to avoid deployments on days with limited support availability, sometimes urgent updates like security patches cannot wait.

### How to be prepared?
- Pre-Deployment Communication:

  - Inform the team about the deployment and ensure that support staff or relevant team members are available if needed
  - Notify all relevant stakeholders, acknowledging that you and the team are prepared to fix issues over the weekend if they occur

- Deployment Checklist and Best Practices - Draft a document to cover each step of the deployment:
  - Pre-Deployment: Ensure that all project components are up-to-date and tested before deployment
  - [Staging Deployment](https://www.ssw.com.au/rules/do-you-have-separate-development-testing-and-production-environments/): Test the application and check for any errors before moving to production
  - Production Deployment: Proceed to production only after confirming no issues in staging
  - Post-Deployment: Monitor for any new issues
  - Troubleshooting: Outline key contacts for support and provide step-by-step actions to address issues

### How to Mitigate the Risk of a Deployment?

- [Use Feature Flags](https://www.ssw.com.au/rules/a-b-testing/): Implement feature flags to control the rollout of new features. This allows for quick disabling of problematic features without a full rollback

- Ensure Comprehensive Monitoring: Make sure all necessary monitoring tools are in place to quickly identify any issues. For instance, you can use [Application Insights](https://www.ssw.com.au/rules/how-to-set-up-application-insights/)
