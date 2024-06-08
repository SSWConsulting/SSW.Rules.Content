---
type: rule
title: Do you know why it’s important to talk to clients on Teams? 
uri: connect-client-im
authors:
  - title: Asher Paris
    url: https://ssw.com.au/people/
related:
  - rules-to-better-microsoft-teams
created: 2023-10-31T16:50:21.000Z
guid: 4332723e-c780-4d0c-a759-5067404ed8fc
---

Effective communication with your clients on Microsoft Teams builds credibility, trust and ensures they receive the deserved attention.

![Figure: Keeping Teams at the centre of client communication](Teams-image.png)

<!--endintro-->

## Talking to clients on Teams

Microsoft Teams is an excellent channel for communicating with clients, especially at the early stage of client development, like after the initial meeting. It encourages the client to reach out and ask you anything about the business, like an upcoming Spec Review. It also gives you an easy way to be able to get hold of them to chase potential work. This impresses the client and can strengthen your relationship.

In other words, Microsoft Teams = buddies :-)

### Open vs closed tenants

An open Microsoft 365 (tenant) means any external email address can communicate with you via Teams. However, some organizations have a closed tenant, meaning you can only communicate via Teams with their organization’s consent.

### Getting started

Once you’ve arranged an Initial Meeting or before a Spec Review, follow these steps to begin communicating with your client on Teams.

1. Open Microsoft Teams
2. Open a ‘New Chat’ or press (Ctrl + N)
3. Enter the client’s email address
4. Create the chat

![Figure: Client with open tenant](https://github.com/SSWConsulting/SSW.Rules.Content/assets/147477898/202b36bf-f727-470b-ae25-4985aed1ff2c)

### If the client has an open tenant, you should send a welcome message in Teams

:::  greybox
Hey thanks for the meeting. Feel free to ping me on Teams or by email any time if you have any questions 😀
:::  

**Figure: Send an email to your client confirming you will contact them through Teams**

### If the client has a closed tenant, you should send a closed tenant request email

![Figure: Client with a closed tenant](https://github.com/SSWConsulting/SSW.Rules.Content/assets/147477898/c6cead28-1d2c-45e3-8e3f-d089447de683)

::: email-template  
|          |     |
| -------- | --- |
| To:      | {{ CLIENT }} |
| Subject: | Communication via Microsoft Teams |  
::: email-content  

### Dear {{ CLIENT }}

As discussed earlier, we should use Microsoft Teams to chat because it ensures quick responses to your queries.

No development question is too big or too small so don’t hesitate to reach out.

Because your Microsoft 365 tenant is ‘closed’, we’ll need your IT team to add my email address to your server. Read [this](https://support.microsoft.com/en-us/office/add-guests-to-a-team-in-microsoft-teams-fccb4fa6-f864-4508-bdde-256e7384a14f) Microsoft Support 'how to' for more information on the topic.

Please copy them your IT into this email chain so I can request access.

Thanks,
{{ YOUR NAME }}
:::  
:::  

**Figure: Send an email to your client requesting access to their organization's tenant**
