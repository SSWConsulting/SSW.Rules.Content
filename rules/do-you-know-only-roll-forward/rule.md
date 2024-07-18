---
type: rule
tips: ""
title: Do you know you should only Roll Forward?
seoDescription: Learn that you should only Roll Forward and not Roll Backward.
uri: software-engineers-should-only-roll-forward
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

### In the Face of Armageddon

When there's a major error during deployment or a catastrophic fault happens, what is your first instinct? Is it to hit that Roll Back button?

It feels like reverting back to the previous stable version is the safest and quickest way to restore functionality. 

![Fixing Problems](https://imgs.xkcd.com/comics/fixing_problems.png)

But SIKE! Rolling back not only negates new features and improvements but also risks reintroducting problems that were previously fixed. If rolling backwards become a habit, it can create a cycle of constant reversion, preventing your software from evolving and improving.

Additionally, rolling backwards can be resource-intensive and disruptive, often requiring significant downtime and manual intervention, which can negatively impact business operations.

### Never Compromise

Rolling Forward involves moving ahead with a new deployment or update, even if issues arise. The aim is to apply a fix or additional update to resolve any problems caused by the initial deployment. By doing so, it continuously moves the project towards its goals.

Here are the reasons why you should Roll Forward:

- **Continuous Improvement:** Rolling forward allows for incremental improvements, ensuring that any issues are promptly addressed without hindering overall progress.
- **Minimized Downtime:** By fixing issues on the go rather than reverting to previous versions, Rolling Forward reduces system downtime and minimizes disruptions to business operations.
- **Data Integrity:** Changes that minimally impact user data or schema allow for seamless updates without risking data integrity. Rolling Forward ensures that data remains intact and consistent.
- **Customer Confidence:** Demonstrating a commitment to Rolling Forward and resolving issues promptly can build customer confidence and trust in your ability to deliver reliable and up-to-date solutions.

By prioritizing rolling forward, you embrace a proactive approach that promotes resilience, agility, and continuous delivery.
 
### The Painkiller

Generally speaking, catastrophic issues should be caught early in the delivery pipeline, reducing the likelihood of deployment failures or major faults. Here are a few examples developers can do to prevent them from sneaking into prodcution ([Rules to Better Testing](https://www.ssw.com.au/rules/rules-to-better-testing/#3-integration-testing)):

- Write Unit Tests ([Rules to Better Unit Tests](https://www.ssw.com.au/rules/rules-to-better-unit-tests/))
- Understand the different types of testing ([Rules for Different Types of Testing](https://www.ssw.com.au/rules/different-types-of-testing/))
- Set up a production-like environment, such as a Staging environment, for testing ([Rules for Setting up Environments](https://www.ssw.com.au/rules/do-you-know-which-environments-you-need-to-provision-when-starting-a-new-project/))
- Developers can implement new features using feature flags. If an issue arises in production, the feature can be disabled, allowing developers to fix the problem without rolling back the entire release ([Manage Feature Flags in Azure App Configuration](https://learn.microsoft.com/en-us/azure/azure-app-configuration/manage-feature-flags?tabs=azure-portal))

### Summary
While rolling back during a deployment failure seems to be the easier route, it's essential to recognize the limitations and drawbacks of this approach. By adopting robust mitigation strategies and embracing the philosophy of rolling forward, software engineers can ensure continuous improvement, enhanced security, and a positive user experience. Upwards and onwards!
