---
type: rule
title: Do you use the right SharePoint development environment?
seoDescription: Set up a suitable SharePoint development environment using
  virtual machines or Visual Studio Code for efficient and flexible testing.
uri: sharepoint-development-environment
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: John Liu
    url: https://ssw.com.au/people/john-liu
  - title: Jean Thirion
    url: https://ssw.com.au/people/jean-thirion
related:
  - sharepoint-search
  - sharepoint-development
redirects:
  - why-do-we-use-vm-for-sharepoint-development
  - do-you-use-the-right-sharepoint-development-environment
created: 2009-02-26T02:03:30.000Z
archivedreason: null
guid: 3af8b6aa-2559-45aa-a7ab-6a30bebd0866
---

Development for SharePoint is very different depending upon whether you are online or using On-Premises SharePoint.

<!--endintro-->

## For SharePoint Online

All you need is VSCode – all modern customizations are doing using the [SharePoint Framework (SPFx)](https://docs.microsoft.com/en-us/sharepoint/dev/spfx/sharepoint-framework-overview?WT.mc_id=M365-MVP-33518).

💡 Best practice is to isolate your code as much as possible during development/staging. Unfortunately it's not easy to come up with a full-blown dedicated Test Tenant.\
As a minimum, make sure you test all your custom code in a dedicated Site Collection to avoid as much side effects as possible.

See our rule to modern [SharePoint Development](https://www.ssw.com.au/rules/sharepoint-development).

## For SharePoint 2016, 2019 or SE

1. It's very important to correctly setup a SharePoint environment for development. Correctly configured, this will save you a lot of trouble later on
2. From time to time, you can seriously damage a SharePoint installation during development and it is best not to install SharePoint on your everyday working machine. Additionally, when you start a new SharePoint project you don't want to carry all the luggage from a previous customization that could potentially affect your new project
3. Virtual machines can be fired up and shut down easily
4. Virtual machines can be relocated on a different server and thus it doesn't waste developers' own computer resources
5. Virtual machines can be copied and brought to a client for demonstration
6. Very easy for someone to quickly create a new SharePoint server to quickly test or experiment with SharePoint
7. Bad - There might be more work required to activate additional servers. SharePoint Farms are a lot of work. E.g. Search Server VMs
