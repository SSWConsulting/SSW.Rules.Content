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

## Power Automate
Power Automate lets any random user automate away things they find painful. They can go from zero to hero in under a day!

Power Automate is the perfect tool for non-developers who want to spin-up a bit of automation to address tasks that cause daily pain for them personally. 

Power Automate is also pretty simple to deploy, you can package it up in a Power Platform solution and then deploy it to dev, test and production at the click of the button. That way you can skip building DevOps pipelines!

However, once the logic gets complex or you need to integrate with custom systems, it's time to look at another solution.

## Azure Logic Apps
Azure Logic Apps are a really awesome way to integrate different systems and transfer data.

The best thing about Logic Apps is that it provides heaps of out-of-the-box integrations that mean you don't need to code in authentication, security and custom integrations with APIs. So long as your logic is just moving data from one place to another it can be done really fast with Azure Logic Apps.

Some of the awesome things Azure Logic Apps move data between include
* CRM systems
* Emails
* Microsoft Dataverse
* Microsoft Office365
* Microsoft SharePoint
* Custom APIs
* and more...

However, once you start to get complex loops, lots of variables or mathematical manipulation that is where it starts to fall over and you might be better off looking at something like Azure Functions.

## Azure Functions
Azure functions help make complex automation quick, easy and pain free. While they still need a developer, it is much easier to get things spun up and you can hook them into all sorts of built-in triggers.

For large, scalable solutions Azure Functions provide the best automation capability.

## The best of all worlds
In reality, automation solutions often combine these tools to make the best possible architecture.

Perhaps you have an Azure Logic App that gets triggered by input in Dynamics, hits an Azure Function to do some calculations and then returns the data in an email to the user. That way Azure Logic Apps handles the integration aspects while Azure functions takes care of the complex logic. You end up with the best aspects of both!

Always keep in mind that you don't need to limit yourself to one tool.

## Benefits Breakdown
By now, your head might be spinning wondering what are the advantages and disadvantages of all the automation tools. Here's a quick overview to give you an idea:

| | PowerAutomate | Azure Logic Apps | Azure Functions | Traditional API
| ----------- | ----------- | ----------- | ----------- | ----------- |
| Pricing | Per User | Per Run or Hosted | Per Run or Hosted | Customisable |
| Built-In packaging for easy deployment | ✅ | ❌ | ❌ | ❌ |
| Quick To Spin-up | ✅ | ✅ | ❌ | ❌ |
| Heaps of built-in Connectors | ✅ | ✅ | ❌ | ❌ |
| No Coding Required | ✅ | 🟠** | ❌ | ❌ |
| Built-in Triggers | ✅ | ✅ | ✅ | ❌ |
| Vendor Agnostic | ❌ | ❌ | 🟠* | ✅ |
| Fully Customisable DevOps | ❌ | ✅ | ✅ | ✅ | 
| Robust Source Control | ❌ | 🟠*** | ✅ | ✅ |
| Smooth Debugging Experience | ❌ | ❌ | ✅ | ✅ |
| Easy Mathematical Manipulation | ❌ | ❌ | ✅ | ✅ |
| Easy Modularization and Refactoring | ❌ | ❌ | ✅ | ✅ |
| Easy Logic Flows and Looping | ❌ | ❌ | ✅ | ✅ |
 
\* Azure Functions can be ported to other platforms with some minor modifications

\** Doesn't require coding, but does need some technical know how to implement

\*** Has source control, but it isn't as smooth as traditional code



