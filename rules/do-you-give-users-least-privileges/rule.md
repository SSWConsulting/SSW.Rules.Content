---
type: rule
title: Do you give users least privileges?
uri: do-you-give-users-least-privileges
created: 2018-04-09T21:28:47.0000000Z
authors:
- id: 71
  title: Steven Andrews

---



<span class='intro'> <p class="ssw15-rteElement-P">Like other services, it is important that your company has a structured and secure approach to managing Azure Permissions.<br></p><div><p class="ssw15-rteElement-P">First a little understanding of how Azure permissions work. For each subscription, there is an Access Control (IAM) section that will allow you to grant overall permissions to this Azure subscription. It is important to remember that any access that is given under Subscriptions | &quot;Subscription Name&quot; | Access Control (IAM), will apply to all Resource Groups within the Subscription.<br></p></div> </span>

<dl class="badImage"><dt><img src="/PublishingImages/azure-permissions-bad.jpg" alt="azure-permissions-bad.jpg" /></dt><dd>Figure&#58;&#160;Bad example - too many people have Owner permission on the subscription level</dd></dl><dl class="goodImage"><dt><img src="/PublishingImages/azure-permissions-good.png" alt="azure-permissions-good.png" /></dt><dd>Figure&#58; Good Example - only Administrators that will be managing overall permissions and content have been given Owner/Co-administrator</dd></dl> ​
<p>From the above image, only the main Administrators have been given Owner/Co-administrator access, all other users within the SSWDesigners and <b> SSWDevelopers</b> Security Groups have been given Reader access. The <b>SSWSysAdmins</b> Security group has also been included as an owner which will assist in case permissions are accidentally stripped from the current Owners.<br>​​<br></p>


