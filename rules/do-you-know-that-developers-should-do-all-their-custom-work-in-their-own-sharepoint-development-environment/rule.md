---
type: rule
title: Do you know that developers should do all their custom work in their own SharePoint development environment?
uri: do-you-know-that-developers-should-do-all-their-custom-work-in-their-own-sharepoint-development-environment
created: 2009-04-20T09:00:40.0000000Z
authors:
- id: 8
  title: John Liu
- id: 1
  title: Adam Cogan

---



<span class='intro'> This is to prevent their work affecting other developers. During development, you can expect many of these things to happen&#58; <br>
<ul>
    <li>IIS resets may need to be done frequently, which stops the SharePoint website working. </li>
    <li>Custom webparts can easily introduce memory leaks which can stop SharePoint working. </li>
    <li>You may be running development SharePoint in debugging mode which would hold the server thread. </li>
    <li>You may be reading event or error logs that are being polluted by other developers simultaneously. </li>
</ul>
<p>Thus, all SharePoint customization and development must be done on a Virtual Machine. No ifs, no buts.</p>
<ol>
    <li>It's very important to correctly setup a SharePoint environment for development. Correctly configured, this will save you a lot of trouble later on. </li>
    <li>From time to time, you can seriously screw/damage a SharePoint installation during development and it is best not to install SharePoint on your day-to-day machine. </li>
    <li>Additionally, when you start a new SharePoint project you don't want to carry all the baggage from previous customizations that could potentially affect your new project. </li>
</ol>
<p>&#160;</p>
 </span>


  <p>There are many other benefits of using a virtual machine for development</p>
<ol>
    <li>Virtual machines can be fired up and shut down easily </li>
    <li>Virtual machines can run faster, via being located on a different server and thus it doesn't waste developers' own computer resources </li>
    <li>Virtual machines can be copied and brought to a client for demonstration or testing </li>
    <li>They are the best way to quickly test or experiment with something new </li>
    <li>Virtual machines can frees up resources on the host, so it doesn’t waste resource when developers are not working on SharePoint </li>
    <li>Virtual machines can be easily cloned to scale up the development team </li>
    <li>Virtual machines enable developers to work in Windows Server 2003 / 2008 environment so they will be aware of the configuration issue when deploying to staging and production </li>
</ol>
<p>There are few consideration when using Virtual Machines&#58;</p>
<ol>
    <li>Need to activate additional servers </li>
    <li>Need at least 2 GB of RAM for SharePoint 2007 </li>
    <li>Need at least 4 GB of RAM for SharePoint 2010</li>
    <li>Virtual PC does not support 64 bit of RAM
    <ul>
        <li>If you’re using Windows 7 or Vista, we recommend using ‘boot to VHD’ or VMWare </li>
    </ul>
    </li>
</ol>
<p>If you are after a clean, pre-configured SharePoint server image to test SharePoint, the easiest way is to <a href="http&#58;//www.microsoft.com/downloads/details.aspx?FamilyID=67f93dcb-ada8-4db5-a47b-df17e14b2c74&amp;displaylang=en" class="ms-rteCustom-External">download a trial VM from Microsoft</a></p>
<a href="http&#58;//www.ssw.com.au/ssw/Standards/DeveloperSharePoint/VMDevelopment.aspx">More info on setting up SharePoint VM</a> 



