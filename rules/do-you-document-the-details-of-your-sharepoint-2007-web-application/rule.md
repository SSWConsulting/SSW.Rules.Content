---
type: rule
archivedreason: 
title: Do you document the details of your SharePoint 2007 web application
guid: 58ecd81e-d3ac-4599-989f-7172773d1c0c
uri: do-you-document-the-details-of-your-sharepoint-2007-web-application
created: 2010-12-23T03:00:52.0000000Z
authors:
- title: William Yin
  url: https://ssw.com.au/people/william-yin
- title: Matthew Hodgkins
  url: https://ssw.com.au/people/matthew-hodgkins
related: []
redirects: []

---

When you move to SharePoint 2010, you will need to know the settings you had on your 2007 server.
Therefore document all the settings from the SharePoint 2007 server, that you will need to re-create on the SharePoint 2010 server.

<!--endintro-->

Fill in the following table. You will use this later when creating the new web application in SharePoint 2010.

| **SharePoint 2010 Web Application Option** | **Where To Find This In SharePoint 2007** | **Answer** |
| --- | --- | --- |
| Authentication Provider | Use  **classic**  unless you know you need  **claims based authentication
** Note: this is a new feature in SharePoint 2010. |  |
| New IIS website Name | Application Management | Web application list |  **Name Field** |  |
| Port | Application Management | Web application list |  **URL Field** .
                     Port number will be listed on end of URL (if nothing its port 80) |  |
| Host Header | Application Management | Web application list |  **URL Field**  if a DNS name is used (not just the NetBIOS name).
                     If a DNS name is  **NOT**  used, leave this blank. |  |
| Authentication Provider | Application Management | Authentication Providers | (Click On the default zone if applicable) |  **IIS Authentication Settings**  field. |  |
| Allow Anonymous | Application Management | Authentication Providers | (Click On the default zone if applicable) |  **Anonymous Access**  field. |  |
| Use Secure Sockets Layer | Check whether the SharePoint site URL like “ **https** ://\*\*\*” |  |
| Public URL | Automatically updated from Host Header |  |
| Application pool name | Leave defaults |  |
| Security account for this application pool | Leave defaults |  |
| Database Name | Zz the database name so you know this will be replaced (read [zzOldFiles](/do-you-zz-old-files-rather-than-deleting-them))

 |  |
