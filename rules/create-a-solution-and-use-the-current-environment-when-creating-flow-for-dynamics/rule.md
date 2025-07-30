---
seoDescription: Create workflows in Dynamics by using the Common Data Service (Current Environment) connector, ensuring seamless connections and deployments across environments.
type: rule
archivedreason:
title: Do you create a Solution and use "Current Environment" when creating Flow for Dynamics?
guid: 1161e28b-130b-4401-947d-0037f61b877a
uri: create-a-solution-and-use-the-current-environment-when-creating-flow-for-dynamics
created: 2020-06-25T22:11:47.0000000Z
authors:
  - title: Mehmet Ozdemir
    url: https://ssw.com.au/people/mehmet-ozdemir
related:
  - bundle-all-your-customizations-in-a-solution
redirects:
  - do-you-create-a-solution-and-use-the-current-environment-when-creating-flow-for-dynamics
---

When creating workflows in Dynamics developers take for granted when a solution file is moved across environments, things just work. To achieve the same with Flows we need to make sure that when connecting to Dynamics using the Common Data Service connector, we in fact connect with Common Data Service (Current Environment) connector. This connector is environmentally aware and will immediately work when the parent solution is deployed to another environment, it doesn't require any post-deployment steps.

<!--endintro-->

**Tip:** When searching for Common Data Services (Current Environment) it’s very easy to pick the wrong one...

![Figure: Use 'Common Data Services (Current Environment)' instead of 'Common Data Services'](common-data-services.png)
