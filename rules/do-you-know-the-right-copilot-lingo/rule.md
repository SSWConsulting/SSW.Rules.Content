---
type: rule
tips: ""
title: Do you know the right Copilot Lingo?
seoDescription: " Learn the correct terminology for Microsoft Copilot and its
  agents so your team chooses the right AI for every task and communicates
  without confusion. "
uri: do-you-know-the-right-copilot-lingo
authors:
  - title: Jean Thirion
    url: https://www.ssw.com.au/people/jean-thirion/
related:
  - rules-to-better-ai
created: 2025-07-04T16:20:00.000Z
guid: 37247f15-6904-450d-b784-f9e4d7856720
---

*“I asked Copilot to pull the sales deck, but nothing happened.”*  

Sounds familiar? Chances you were using the **personal** Copilot, while the deck lives in your Office 365 tenant. In the Microsoft world, not all Copilots are equal. Add Agents and Connectors to the mix and you can easily get lost.

<!--endintro-->

## Know your Copilots

| Flavor | Where to find it | What it can reach | Typical ask |
|---|---|---|---|
| **Personal Copilot** | Windows taskbar <br> copilot.microsoft.com <br> bing.com | ✅ Public web <br>  ✅ Your Microsoft (consumer) account | "What's the best way to do XYZ" |
| **Microsoft 365 Copilot** | O365 Waffle Menu <br> m365.cloud.microsoft <br> Google "M365 Copilot" | ✅ Public web <br> ✅ Your entire tenant - i.e. Teams, Outlook, SharePoint, etc. <br> ✅ Microsoft Agents | "What happened on Project XYZ while I was on leave?" |
| **Product Copilots** | Next to the search bar in each app (e.g., Azure, Power Apps, Excel) | ✅ Only that product’s docs <br> ✅ Current context (e.g. current spreadsheet) | "How do I snapshot a VM?" |

### Agents ≠ Copilots

Agents are not the same as Copilots. In fact, Office 365 Copilot can **invoke** Agents. There are task-specific AIs with their own memory.

There are 3 main types of Agents within the Microsoft world:

* **Built-in Agents** – research, image creation, and more.  
* **SharePoint Agents** – pointed at sites or libraries for focused intelligence.  
* **Custom Agents** – fully customized Agents with custom prompts, behaviours and knowledge (O365 Data or External)

### Copilot Connectors

Copilot Connectors (aka Graph Connectors) are gateways to access data from custom Agents. By default your tenant is configured for SharePoint Copilot Connectors (that's how SharePoint Agents access your data) but you can also roll your own connectors to access external Enterprise Data (SQL, Jira, Zendesk, etc...)


## Use precise language

::: greybox
“Just get **Copilot** to pull the latest bug list.”
:::
::: bad  
Figure: Bad Example – unclear which Copilot and where the bugs live  
:::

::: greybox
“Ask **Microsoft 365 Copilot** to summarise the *Bugs* list in **SharePoint→Northwind→Dev**.”  
:::
::: good  
Figure: Good Example – specifies the flavor and the data source  
:::

