---
type: rule
archivedreason: 
title: Do you give users the friendlier Access Request dialog?
guid: b65647bb-64b2-4dea-9f72-b68f7ecc1fb5
uri: do-you-use-access-request-on-your-sharepoint-site
created: 2013-07-16T02:20:38.0000000Z
authors:
- title: Adam Cogan
  url: /people/adam-cogan
- title: William Yin
  url: /people/william-yin
related: []
redirects:
- do-you-give-users-the-friendlier-access-request-dialog

---

Instead of displaying a direct " **Access Denied** " warning info, you can allow end users to send an " **Access Request** ".
<img alt="PermissionRequest.jpg" src="PermissionRequest.jpg" style="margin:5px;width:650px;"> **Figure: Joanna is requesting access to SharePoint site** 

<!--endintro-->

The "request manager" will receive an email:
![RequestNotificationEmail.png](637cf8_RequestNotificationEmail.png) **Figure: Request Notification Email Sample** The link in the email will navigate administrator to the  **Pending Requests** list:![](LinkToPendingRequestsList.png) **Figure: Pending Requests List** 
After reading the request infomation, the administrator can "Approve" or "Decline" the request, or he can start a conversation with the request user on the  **Pending Requests** list directly to inquire more information:
![](StartAConversatioinOnPendingList.png) **Figure: possible actions for requests (Approve, Decline or start a conversation with the request user)** 


To setup permission request for a SharePoint site collection, go to " **Site Settings (Gear Wheel icon)** |  **Site Permissions** ":
![](SetupPermissionRequest.png) **Figure: Open "Access Request" setting** 


**Limition:** 
This "Access Request" only works for authenticated users to inquire more access permission, that means if your site allows "anonymous access", then an anonymous user cannot send "access request" as he doesn't have an identify to be assigned more access permission.
