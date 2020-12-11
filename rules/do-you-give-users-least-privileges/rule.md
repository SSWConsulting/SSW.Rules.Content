---
type: rule
archivedreason: 
title: Do you give users least privileges?
guid: 84021197-733f-4203-b734-df845a2be063
uri: do-you-give-users-least-privileges
created: 2018-04-09T21:28:47.0000000Z
authors:
- id: 71
  title: Steven Andrews
related: []

---

Like other services, it is important that your company has a structured and secure approach to managing Azure Permissions.

First a little understanding of how Azure permissions work. For each subscription, there is an Access Control (IAM) section that will allow you to grant overall permissions to this Azure subscription. It is important to remember that any access that is given under Subscriptions | "Subscription Name" | Access Control (IAM), will apply to all Resource Groups within the Subscription.

<!--endintro-->
<dl class="badImage">&lt;dt&gt;<img src="azure-permissions-bad.jpg" alt="azure-permissions-bad.jpg">&lt;/dt&gt;<dd>Figure: Bad example - too many people have Owner permission on the subscription level</dd></dl><dl class="goodImage">&lt;dt&gt;<img src="azure-permissions-good.png" alt="azure-permissions-good.png">&lt;/dt&gt;<dd>Figure: Good Example - only Administrators that will be managing overall permissions and content have been given Owner/Co-administrator</dd></dl>
From the above image, only the main Administrators have been given Owner/Co-administrator access, all other users within the SSWDesigners and  **SSWDevelopers** Security Groups have been given Reader access. The  **SSWSysAdmins** Security group has also been included as an owner which will assist in case permissions are accidentally stripped from the current Owners.
