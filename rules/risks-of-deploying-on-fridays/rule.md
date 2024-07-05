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
  - title: ""
  - title: Charles Vionnet
    url: https://www.ssw.com.au/people/charles-vionnet/
created: 2024-07-05T02:41:49.271Z
guid: 530a2540-9b59-4272-8c86-f79d0bfa6aef
---
A well-known Golden Rule says: 
> Never deploy on Friday.

Deploying on Fridays is inherently risky. If something goes wrong, it could lead to unresolved issues over the weekend, negatively impacting users and the business.

<!--endintro-->

::: img-large  
![Figure: When the Golden Rule is not followed](risks-of-deploying-on-fridays.png)
:::

While it is best to avoid Friday deployments, sometimes it’s unavoidable, such as for a security update. In that case, you must weigh up the pros and cons, acknowledge the risks involved and have a plan ready.

### How to be prepared?

- Ensure Comprehensive Monitoring: Make sure all necessary monitoring tools are in place to quickly identify any issues. For instance, use [Application Insights](https://www.ssw.com.au/rules/how-to-set-up-application-insights/)

- Follow a Pre-Deployment Checklist: Verify the deployment process, including tests, backups, and a rollback plan in case something goes wrong.
- Pre-Deployment Communication:

  - Inform the team about the deployment and ensure that support staff or relevant team members are available if needed.
  - Depending on company or country regulations, get approval from your manager to work over the weekend.
  - Notify all relevant stakeholders, acknowledging that you and the team are prepared to fix issues over the weekend if they occur.
- Post-Deployment Communication: Inform stakeholders whether the deployment was successful or if there were any failures.
- Document Everything: Record any issues, what was done to resolve them, and how to improve in the future.

### How to Mitigate the Risk of a Friday Deployment?
- [Set Up Staging Environments](https://www.ssw.com.au/rules/do-you-have-separate-development-testing-and-production-environments/): Always deploy to a staging environment first to test the deployment before pushing to production.

- [Use Feature Flags](https://www.ssw.com.au/rules/a-b-testing/): Implement feature flags to control the rollout of new features. This allows for quick disabling of problematic features without a full rollback.

Now, the Golden Rule can be updated to:
> Never deploy on Friday… but be prepared if you must.
