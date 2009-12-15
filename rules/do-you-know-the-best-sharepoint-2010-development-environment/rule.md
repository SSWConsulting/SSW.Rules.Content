---
type: rule
title: Do you know the best SharePoint 2010 development environment?
uri: do-you-know-the-best-sharepoint-2010-development-environment
created: 2009-12-15T06:34:40.0000000Z
authors:
- id: 8
  title: John Liu
- id: 1
  title: Adam Cogan
- id: 14
  title: Martin Hinshelwood

---



<span class='intro'> This field should not be null (Remove me when you edit this field). </span>

One of the biggest problem is that SharePoint can only be installed on Windows Server and most developer machines do not run Windows Server as the host OS.  Tweaks to install SharePoint to Vista were available but generally considered risky – since your development environment do not fully reflect the production server.<br>
In SharePoint 2010 – the scenery has changed slightly&#58;
<br>
<ul>
    <li>You can still remote to a shared SharePoint development server<br>
    a. This is best for people who don’t need to have their own SharePoint server, such as designers, testers or content editors.
    </li>
    <li><s>(CROSS) Run your own local virtual machine </s>(Not recommended)<br>
    a. This has gotten a lot trickier – since SharePoint 2010 is x64 only.<br>
    b.You can’t use Virtual PC, and so you have to use either Hyper-V (which requires a Windows Server host), or VMWare<br>
    c. Your host must be x64 to run the virtual machines in x64
    </li>
    <li>(TICK)You can boot to VHD (Win7 only, Recommended)<br>
    a.Build a SharePoint 2010 server on VHD<br>
    b.Sysprep the SharePoint server<br>
    c.Take the ‘cleaned’ VHD to your destination computer<br>
    d.Set up boot manager records to add VHD as a device<br>
    e.Set up boot manager records to allow the VHD device as a possible boot device<br>
    f.Restart the computer and select to boot into VHD<br>
    g.The sysprep’ed VHD will initialize and install devices specific to your current PC</li>
</ul>



