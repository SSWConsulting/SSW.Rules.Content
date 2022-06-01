---
type: rule
title: Do you use the right tool to automate your processes?
uri: automation-tools
authors:
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
  - title: Matt Wicks
    url: https://www.ssw.com.au/people/matt-wicks
  - title: Calum Simpson
    url: https://www.ssw.com.au/people/calum-simpson
  - title: Norman Russ
    url: https://www.ssw.com.au/people/norman-russ
  - title: Adam Cogan
    url: https://www.ssw.com.au/people/adam-cogan
created: 2022-05-26T02:02:31.620Z
guid: 27675645-003e-4199-aa57-cdcb2182af48
---
::: img-medium 
![Figure: The power of Power Automate](power-automate-logo.png)
:::

In the old days, if employees wanted something automated they would have to call up the development team and go through a long bureaucratic process to get a traditional API built. These days, there are heaps of tools that make this easy, quick and simple.

<!--endintro-->

## Power Automate

Power Automate lets power users automate away repeatable manual processes. They can go from zero to hero in under a day!

For example say you want to:

* Monitor an inbox
* Read emails with the subject “Invoice”
* Get the attached PDF
* Put the PDF in a SharePoint Document Library (there is a connector)
* Put a record in Xero (there is an API - no connector)

These are all easy in Power Automate, and a tonne of code in an Azure Function

### Connectors

Power Automate provides heaps of out-of-the-box integrations that mean you don't need to code in authentication, security and custom integrations with APIs. So long as your logic is just moving data from one place to another it can be done really fast.

Some of the awesome connectors that exist include

* CRM systems e.g. Dynamics 365
* Emails
* Microsoft Dataverse
* Microsoft Office 365
* Microsoft SharePoint
* Custom APIs
* and more...

### Custom Connectors

If the connector you want doesn't exist you can create custom connectors to access your favourite APIs and you can even [throw your own code into them](https://docs.microsoft.com/en-us/connectors/custom-connectors/write-code).

### Power Automate Beyond the Basics

DevOps with Power Automate is simple. You can you can package it up in a Power Platform solution and then deploy it to dev, test and production at the click of the button. That way you can skip building DevOps pipelines!

However, once the logic gets complex or you need to integrate with custom systems, it's time to look at another solution.

## Azure Logic Apps

Azure Logic Apps are a really awesome way to integrate different systems and transfer data. Azure Logic Apps take integration to another level, by providing all the same connectors as Power Automate + tonnes more. 

You can also configure RBAC for Azure Logic Apps providing extra security control.

However, once you start to get complex loops, lots of variables or mathematical manipulation that is where it starts to fall over and you might be better off looking at something like Azure Functions.

## Azure Functions

Azure functions help make complex automation quick, easy and pain free. While they still need a developer, it is much easier to get things spun up and you can hook them into all sorts of built-in triggers.

For large, scalable solutions Azure Functions provide the best automation capability.

## The best of all worlds

In reality, automation solutions often combine these tools to make the best possible architecture.

Perhaps you have an Azure Logic App (or Power Automate Flow) that gets triggered by input in Dynamics 365, hits an Azure Function to do some calculations which returns the data to the Azure Logic App and then sends an email to the user. That way the Azure Logic Apps handles the integration aspects while Azure functions takes care of the complex logic. You end up with the best aspects of both!

Always keep in mind that you don't need to limit yourself to one tool.

## Benefits Breakdown

By now, your head might be spinning wondering what are the advantages and disadvantages of all the automation tools. Here's a quick overview to give you an idea:

|                                        | Power Automate | Azure Logic Apps     | Azure Functions                    | Traditional API |
| -------------------------------------- | -------------- | -------------------- | ---------------------------------- | --------------- |
| Pricing                                | Per User       | Per Action or Hosted | Consumption (CPU/Memory) or Hosted | Customisable    |
| Target Users                           | End Users      | IT Pros              | Developers and IT Pros             | Developers      |
| Built-In packaging for easy deployment | ✅              | ❌                    | ❌                                  | ❌               |
| Quick To Spin-up                       | ✅              | ✅                    | ❌                                  | ❌               |
| Heaps of built-in Connectors           | ✅              | ✅                    | ❌                                  | ❌               |
| No Coding Required                     | ✅              | ✅                    | ❌                                  | ❌               |
| Built-in Triggers                      | ✅              | ✅                    | ✅                                  | ❌               |
| Vendor Agnostic                        | ❌              | ✅                    | ✅                                  | ✅               |
| Fully Customisable DevOps              | ❌              | ✅                    | ✅                                  | ✅               |
| Robust Source Control                  | ❌              | 🟠*                  | ✅                                  | ✅               |
| Smooth Debugging Experience            | ❌              | ❌                    | ✅                                  | ✅               |
| Easy Mathematical Manipulation         | ❌              | ❌                    | ✅                                  | ✅               |
| Easy Modularization and Refactoring    | ❌              | ❌                    | ✅                                  | ✅               |
| Easy Logic Flows and Looping           | ❌              | ❌                    | ✅                                  | ✅               |

\* Has source control, but it isn't as smooth as traditional code