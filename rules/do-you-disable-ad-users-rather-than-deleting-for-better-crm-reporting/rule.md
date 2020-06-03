---
type: rule
title: Do you Disable AD Users rather than Deleting for better CRM Reporting?
uri: do-you-disable-ad-users-rather-than-deleting-for-better-crm-reporting
created: 2019-07-10T22:47:08.0000000Z
authors:
- id: 71
  title: Steven Andrews

---



<span class='intro'> <p class="ssw15-rteElement-P">When a user is created in Active Directory (AD) a Global Unique Identifier (GUID) is also created. As the name suggests this is Unique for each user and is never duplicated in a Domain.<br></p> </span>

<dl class="image"><dt>​<img src="/PublishingImages/guid.png" alt="guid.png" /></dt><dd>Figure&#58; GUID for User Steven Andrews</dd></dl><p class="ssw15-rteElement-P">When adding a user to CRM they are assigned with an Employee ID, this is linked to the AD account’s GUID.</p><dl class="image"><dt>​​<img src="/PublishingImages/aduser.png" alt="aduser.png" /></dt><dd>Figure&#58; AD User StevenAndrews is tied to STA Employee ID through AD GUID</dd></dl><p class="ssw15-rteElement-P">When a user leaves many companies go through the process of disabling the CRM account and then deleting the AD User.<br>The problem that arises from deleting the AD user is that if the Employee that left comes back to the company and a new AD account is created for them, they are no longer able to be associated with the previously created CRM account. Instead they will need a new CRM user with a different Employee ID.</p><p class="ssw15-rteElement-P">This in turn make reporting on a user that has returned more difficult. So to get around this it is disabling and moving the user to a &quot;Disable Users&quot;&#160;Organizational Unit (OU) in AD is much easier, so that in the event that the return, the AD and CRM user can just be re-enabled.&#160;<br></p>


