---
type: rule
archivedreason: 
title: Do you know that developers should do all their custom work in their own SharePoint development environment?
guid: 0f25f858-e4d5-47a0-a237-3f17e743a858
uri: do-you-know-that-developers-should-do-all-their-custom-work-in-their-own-sharepoint-development-environment
created: 2009-04-20T09:00:40.0000000Z
authors:
- title: John Liu
  url: https://ssw.com.au/people/john-liu
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

This is to prevent their work affecting other developers. During development, you can expect many of these things to happen: 

* IIS resets may need to be done frequently, which stops the SharePoint website working.
* Custom web parts can easily introduce memory leaks which can stop SharePoint working.
* You may be running development SharePoint in debugging mode which would hold the server thread.
* You may be reading event or error logs that are being polluted by other developers simultaneously.


Thus, all SharePoint customization and development must be done on a Virtual Machine. No ifs, no buts.

1. It's very important to correctly setup a SharePoint environment for development. Correctly configured, this will save you a lot of trouble later on.
2. From time to time, you can seriously screw/damage a SharePoint installation during development and it is best not to install SharePoint on your day-to-day machine.
3. Additionally, when you start a new SharePoint project you don't want to carry all the baggage from previous customizations that could potentially affect your new project.


<!--endintro-->

There are many other benefits of using a virtual machine for development

1. Virtual machines can be fired up and shut down easily
2. Virtual machines can run faster, via being located on a different server and thus it doesn't waste developers' own computer resources
3. Virtual machines can be copied and brought to a client for demonstration or testing
4. They are the best way to quickly test or experiment with something new
5. Virtual machines can frees up resources on the host, so it doesn’t waste resource when developers are not working on SharePoint
6. Virtual machines can be easily cloned to scale up the development team
7. Virtual machines enable developers to work in Windows Server 2003 / 2008 environment so they will be aware of the configuration issue when deploying to staging and production


There are few considerations when using Virtual Machines:

1. Need to activate additional servers
2. Need at least 2 GB of RAM for SharePoint 2007
3. Need at least 4 GB of RAM for SharePoint 2010
4. Virtual PC does not support 64 bit Operating Systems 
    * If you’re using Windows 7 or Vista, we recommend using ‘boot to VHD’ or VMWare


If you are after a clean, pre-configured SharePoint server image to test SharePoint, the easiest way is to download a trial VM from Microsoft
**Tip:**  [More info on setting up SharePoint VM](http&#58;//www.ssw.com.au/ssw/Standards/DeveloperSharePoint/VMDevelopment.aspx)
