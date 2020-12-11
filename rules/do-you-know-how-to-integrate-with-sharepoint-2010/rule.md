---
type: rule
archivedreason: 
title: Do you know how to integrate with SharePoint 2010?
guid: 7e99fec6-a420-42c0-beeb-742b94eb5cf3
uri: do-you-know-how-to-integrate-with-sharepoint-2010
created: 2010-05-17T09:08:46.0000000Z
authors:
- id: 14
  title: Martin Hinshelwood
related: []

---

If you are going to be integrating TFS 2010 with SharePoint 2010 then there are a few things you need to do.   
<!--endintro-->

### Single Server Deployment

If you want to run SharePoint 2010 on the same box as TFS 2010 then make sure you install it  **before** you install TFS 2010. You will then have to use the custom configuration wizard so you can use the existing SharePoint instance.

### Multi-Server Deployment

If you are going to have SharePoint 2010 on a separate server to your TFS 2010 then you will need to again run the Custom configuration wizard, but you will also need to [<font color="#000080">Integrate your SharePoint 2010 instance with TFS 2010</font>](http&#58;//blog.hinshelwood.com/archive/2010/05/03/integrate-sharepoint-2010-with-team-foundation-server-2010.aspx).
