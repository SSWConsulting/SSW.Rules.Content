---
type: rule
archivedreason: 
title: Do you give users the friendlier Access Request dialog?
guid: b65647bb-64b2-4dea-9f72-b68f7ecc1fb5
uri: do-you-give-users-the-friendlier-access-request-dialog
created: 2013-07-16T02:20:38.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 9
  title: William Yin
related: []

---

Instead of displaying a direct " **Access Denied** " warning info, you can allow end users to send an " **Access Request** ".
<dl class="ssw15-rteElement-ImageArea"><img alt="PermissionRequest.jpg" src="PermissionRequest.jpg" style="margin:5px;width:650px;"></dl> **Figure: Joanna is requesting access to SharePoint site** 

<!--endintro-->

The "request manager" will receive an email:
<dl class="ssw15-rteElement-ImageArea"><img alt="RequestNotificationEmail.png" src="637cf8_RequestNotificationEmail.png" style="margin:5px;"></dl> **Figure: Request Notification Email Sample** <dl class="ssw15-rteElement-ImageArea">The link in the email will navigate administrator to the  <strong>Pending Requests</strong> list:</dl><dl class="ssw15-rteElement-ImageArea"><img alt="LinkToPendingRequestsList.png" src="LinkToPendingRequestsList.png" style="margin:5px;width:650px;"></dl> **Figure: Pending Requests List** 
After reading the request infomation, the administrator can "Approve" or "Decline" the request, or he can start a conversation with the request user on the  **Pending Requests** list directly to inquire more information:
<dl class="ssw15-rteElement-ImageArea"><img alt="StartAConversatioinOnPendingList.png" src="StartAConversatioinOnPendingList.png" style="margin:5px;width:650px;"></dl> **Figure: possible actions for requests (Approve, Decline or start a conversation with the request user)** 


To setup permission request for a SharePoint site collection, go to " **Site Settings (Gear Wheel icon)** |  **Site Permissions** ":
<dl class="ssw15-rteElement-ImageArea"><img alt="SetupPermissionRequest.png" src="SetupPermissionRequest.png" style="margin:5px;width:650px;"></dl> **Figure: Open "Access Request" setting** 


**Limition:** 
This "Access Request" only works for authenticated users to inquire more access permission, that means if your site allows "anonymous access", then an anonymous user cannot send "access request" as he doesn't have an identify to be assigned more access permission.
