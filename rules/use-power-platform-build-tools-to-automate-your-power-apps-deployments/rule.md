---
seoDescription: Automate Power Apps deployments using Microsoft Power Platform Build Tools to streamline your application lifecycle and reduce manual errors.
type: rule
archivedreason:
title: Do you use Power Platform Build Tools to automate your Power Apps deployments?
guid: 426541a0-eb23-4224-a230-891420ec08f0
uri: use-power-platform-build-tools-to-automate-your-power-apps-deployments
created: 2020-10-28T18:48:50.0000000Z
authors:
  - title: Mehmet Ozdemir
    url: https://ssw.com.au/people/mehmet-ozdemir
related: []
redirects:
  - do-you-use-power-platform-build-tools-to-automate-your-power-apps-deployments
---

You’ve built your Power App using all the best practices, have multiple solutions that are split into a logical component, you’re using environment variables to handle your configuration data everything is going great! Now it comes time to deploy these changes to the Test environment. Do not deploy these manually. It is a repetitive step and if you have multiple solutions, there will be installation order dependencies that need to be handled, etc. Then the whole process will need to be repeated when you promote the changes to production, rinse, and repeat for the next round of changes for test and production. Highly repetitive, error-prone, and a prime example of automation.

<!--endintro-->

The solution, Power Platform Build Tools:

![Figure: ALM for your Power Platform projects](almpowered.png)

### What do I get with the Microsoft Power Platform Build Tools?

The Power Platform Build Tools are a collection of Power Platform-specific Azure DevOps build tasks. They automate the manual steps and scripts needed to manage the application lifecycle. There four types of tasks:

- Helper
- Quality check
- Solution
- Environment management

What Power Platform Projects are supported?

- Canvas and Model-Driven Apps
- Power Virtual Agents
- UI Flows and Traditional Flows
- AI Builder
- Custom Connectors and Dataflows

If it can be included in a solution, then it's supported.

More Information here: https://docs.microsoft.com/en-us/power-platform/alm/devops-build-tools
