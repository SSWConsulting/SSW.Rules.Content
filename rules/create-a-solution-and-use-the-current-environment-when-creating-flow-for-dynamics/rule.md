---
type: rule
archivedreason: 
title: Do you create a Solution and use the "Current Environment" when creating Flow for Dynamics?
guid: 1161e28b-130b-4401-947d-0037f61b877a
uri: create-a-solution-and-use-the-current-environment-when-creating-flow-for-dynamics
created: 2020-06-25T22:11:47.0000000Z
authors:
- title: Mehmet Ozdemir
  url: https://ssw.com.au/people/mehmet-ozdemir
related: []
redirects:
- do-you-create-a-solution-and-use-the-current-environment-when-creating-flow-for-dynamics

---

When creating workflows in Dynamics developers take for granted when a solution file is moved across environments, things just work. To achieve the same with Flows we need to make sure that when connecting to Dynamics using the Comm Data Service connector, we in fact connect with Common Data Service (Current Environment) connector. This connector is environmentally aware and will immediately work when the parent solution is deployed to another environment, it doesn't require any post-deployment steps.

<!--endintro-->

**Tip:** When searching for Common Data Services (Current Environment) it’s very easy to pick the wrong one:

![](common-data-services.png)  

### Related Rule

* [Do you bundle all your customizations in a Solution (Model-Driven)?](/bundle-all-your-customizations-in-a-solution)
