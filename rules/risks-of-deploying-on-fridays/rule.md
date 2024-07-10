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
Deploying on a Friday has traditionally been seen as risky due to limited post-deployment support over the weekend and potential issues not being addressed quickly. In the DevOps era, these concerns are largely mitigated by automated deployments, continuous integration, and real-time monitoring, making the deployment process smoother and more reliable.

Nonetheless, caution is still advised.

<!--endintro-->

::: img-large  
![Figure: Follow good practices help to avoid deployment stress](risks-of-deploying-on-fridays.png)
:::

While it is best to avoid Friday deployments, sometimes it’s unavoidable, such as for a security update. To ensure smooth operation and prevent any issues, make sure you have:
- Informed the team about the deployment and ensure that support staff or relevant team members are available if needed
- A document with a detailed checklist and best practices for all the main steps:

  - Pre-Deployment Checklist
  - Staging Deployment Verification
  - Production Deployment Verification
  - Post-Deployment Verification
  - Troubleshooting


### How to Mitigate the Risk of a Deployment?

- [Set Up Staging Environments](https://www.ssw.com.au/rules/do-you-have-separate-development-testing-and-production-environments/): Always deploy to a staging environment first to test the deployment before pushing to production.

- [Use Feature Flags](https://www.ssw.com.au/rules/a-b-testing/): Implement feature flags to control the rollout of new features. This allows for quick disabling of problematic features without a full rollback.

- Ensure Comprehensive Monitoring: Make sure all necessary monitoring tools are in place to quickly identify any issues. For instance, you can use [Application Insights](https://www.ssw.com.au/rules/how-to-set-up-application-insights/)
