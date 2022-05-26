---
type: rule
title: Do you use the right tool to automate your processes
uri: automation-tools
authors:
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
created: 2022-05-26T02:02:31.620Z
guid: 27675645-003e-4199-aa57-cdcb2182af48
---
In the old days, if employees wanted something automated they would have to call up the development team and go through a long bureaucratic process to get a custom API built. These days, there are heaps of tools that make this easy, quick and simple.

<!--endintro-->

## PowerAutomate
PowerAutomate lets any random user automate away things they find painful. They can go from zero to hero in under a day!

PowerAutomate is the perfect tool for non-developers who want to spin-up a bit of automation to address tasks that cause daily pain for them personally. 

However, once the logic gets complex or you need to integrate with custom systems, it's time to look at another solution.

## Azure Logic Apps
Azure Logic Apps are a really awesome way to integrate different systems and transfer data.

The best thing about Logic Apps is that it provides heaps of out-of-the-box integrations that mean you don't need to code in authentication, security and custom integrations with APIs. So long as your logic is just moving data from one place to another it can be done really fast with Azure Logic Apps.

Some of the awesome things Azure Logic Apps move data between include
* CRM systems
* Emails
* Microsoft Dataverse
* Microsoft Office365
* Custom APIs

However, once you start to get complex loops, lots of variables or mathematical manipulation that is where it starts to fall over and you might be better off looking at something like Azure Functions.

## Azure Functions
Azure functions help make complex automation quick, easy and pain free. While they still need a developer, it is much easier to get things spun up and you can hook them into all sorts of built-in triggers.

For large, scalable solutions Azure Functions provide the best automation capability.

| | PowerAutomate | Azure Logic Apps | Azure Functions | Traditional API
| ----------- | ----------- | ----------- | ----------- | ----------- |
| Built-in Triggers | ✅ | ✅ | ✅ | ❌ |
| Built-in Connectors | ✅ | ✅ | ❌ | ❌ |
| Quick To Spin-up | ✅ | ✅ | ❌ | ❌ |
| Vendor Agnostic | ❌ | ❌ | 🟠* | ✅ |
| No Coding Required | ✅ | 🟠** | ❌ | ❌ |
| Fully Customisable DevOps | ❌ | ✅ | ✅ | ✅ | 
| Robust Source Control | ❌ | 🟠*** | ✅ | ✅ |
| Smooth Debugging Experience | ❌ | ❌ | ✅ | ✅ |
| Easy Mathematical Manipulation | ❌ | ❌ | ✅ | ✅ |
| Easy Modularization and Refactoring | ❌ | ❌ | ✅ | ✅ |
| Easy Logic Flows and Looping | ❌ | ❌ | ✅ | ✅ |
 
\* Azure Functions can be ported to other platforms with some minor modifications

\** Doesn't require coding, but does need some technical know how to implement

\*** Has source control, but it isn't as smooth as traditional code



