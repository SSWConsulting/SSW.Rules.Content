---
type: rule
tips: ""
title: Do you know the right Copilot Lingo?
seoDescription: Learn the correct terminology for Microsoft Copilot and its agents so your team chooses the right AI for every task and communicates without confusion.
uri: copilot-lingo
authors:
  - title: Jean Thirion
    url: https://www.ssw.com.au/people/jean-thirion
related:
  - best-ai-tools
created: 2025-07-04T16:20:00.000Z
guid: 37247f15-6904-450d-b784-f9e4d7856720
redirects:
  - do-you-know-the-right-copilot-lingo
---

> *“I asked Copilot to pull the sales deck, but nothing happened.”*  

Sounds familiar? Chances you were using the **personal** Copilot, while the deck lives in your Office 365 tenant. In the Microsoft world, not all Copilots are equal. Add Agents and Connectors to the mix and you can easily get lost.

<!--endintro-->

## Know your Copilots

<table>
  <thead>
    <tr>
      <th>Type</th>
      <th>Where to find it</th>
      <th>✅ What it can reach</th>
      <th>Typical ask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Personal Copilot</strong></td>
      <td>
        <ul>
          <li>Windows taskbar</li>
          <li><a href="https://copilot.microsoft.com">copilot.microsoft.com</a></li>
          <li><a href="https://bing.com">bing.com</a></li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Public web</li>
          <li>Your Microsoft (consumer) account</li>
        </ul>
      </td>
      <td>“What’s the best way to do XYZ?”</td>
    </tr>
    <tr>
      <td><strong>Microsoft 365 Copilot</strong></td>
      <td>
        <ul>
          <li>O365 Waffle Menu</li>
          <li>m365.cloud.microsoft</li>
          <li>Google “M365 Copilot”</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Public web</li>
          <li>Your entire tenant (Teams, Outlook, SharePoint, etc.)</li>
          <li>Microsoft Agents</li>
        </ul>
      </td>
      <td>“What happened on Project XYZ while I was on leave?”</td>
    </tr>
    <tr>
      <td><strong>Product Copilots</strong></td>
      <td>
        <ul>
          <li>Next to the search bar in each app (e.g., Azure, Power Apps, Excel)</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Only that product’s docs</li>
          <li>Current context (e.g., current spreadsheet)</li>
        </ul>
      </td>
      <td>“How do I snapshot a VM?”</td>
    </tr>
  </tbody>
</table>

### Agents ≠ Copilots

Agents are not the same as Copilots. In fact, Office 365 Copilot can **invoke** Agents. There are task-specific AIs with their own memory.

There are 3 main types of Agents within the Microsoft world:

* **Built-in Agents** – Research, image creation, and more
* **SharePoint Agents** – Pointed at sites or libraries for focused intelligence
* **Custom Agents** – Fully customized Agents with custom prompts, behaviours and knowledge (O365 Data or External)

### Copilot Connectors

Copilot Connectors (aka Graph Connectors) are gateways to access data from custom Agents. By default your tenant is configured for SharePoint Copilot Connectors (that's how SharePoint Agents access your data) but you can also roll your own connectors to access external Enterprise Data (SQL, Jira, Zendesk, etc.).

## Use precise language

::: greybox
“Just get **Copilot** to pull the latest bug list.”
:::
::: bad  
Figure: Bad example – Unclear which Copilot and where the bugs live  
:::

::: greybox
“Ask **Microsoft 365 Copilot** to summarize the *Bugs* list in **SharePoint→Northwind→Dev**.”  
:::
::: good  
Figure: Good example – Specifies the flavor and the data source  
:::
