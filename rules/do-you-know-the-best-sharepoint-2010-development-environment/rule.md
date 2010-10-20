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



<span class='intro'> 
  <p>Developing in ASP.NET is easy, you just press F5, Visual Studio spins up instance of the Cassini web server, and you can see your work execute. Developing in SharePoint is much harder as you need access to a local SharePoint server to see your work run.</p>
<p>In SharePoint 2007 there are three options, in SharePoint 2010 they have added one more.</p>
<img alt="" class="ms-rteCustom-ImageArea" src="/PublishingImages/SetupSPEnviroment.jpg" /> <font class="ms-rteCustom-FigureNormal" size="+0">Figure&#58; Setting up the development environment in SharePoint can give you a headache</font> 
 </span>

Your development choices in SharePoint 2007 are&#58;
<ul>
    <li>Remote to a shared SharePoint development server <br>
    Tip&#58; This is best for people who do *not* need to have their own SharePoint server, such as designers, testers or content editors.<br>
    Problem #1&#58; By default you only get 2 concurrent accounts<br>
    Problem #2&#58; IISRESET clobbers other users. </li>
    <li>Run your own local virtual machine (VM)<br>
    Tip #1&#58; Use an external drive to make it faster<br>
    Tip #2&#58; Use SSD to go even faster &#58;) </li>
    <li>Use ‘Boot’ to VHD (Recommended - most trouble but best performance)<br>
    Note&#58; Only if you have Windows 7 as the host <br>
    See&#58; <a href="http&#58;//www.hanselman.com/blog/LessVirtualMoreMachineWindows7AndTheMagicOfBootToVHD.aspx">Less Virtual, More Machine - Windows 7 and the magic of Boot to VHD</a> </li>
</ul>
<p>One of the biggest problem is that SharePoint 2007 can only be installed on Windows Server and most developer machines do not run Windows Server as the host OS. Tweaks to install SharePoint to Vista were available, but considered risky – since your development environment does not fully reflect the production server.</p>
In SharePoint 2010 – the scenery has changed a little. These are all your options now&#58;<br>
<ul>
    <li>Remote to a shared SharePoint development server <br>
    Tip&#58; This is best for people who do *not* need to have their own SharePoint server, such as designers, testers or content editors.<br>
    Problem #1&#58; By default you only get 2 concurrent accounts<br>
    Problem #2&#58; IISRESET clobbers other users. </li>
    <li>Run your own local virtual machine (Not recommended – because SharePoint 2010 is 64-bit only) <br>
    Tip #1&#58; Use an external drive to make it faster<br>
    Tip #2&#58; Use SSD to go even faster &#58;)<br>
    Tip #3&#58; The 64-bit requirement means, you can’t use Virtual PC, and so you have to use either Hyper-V (which requires a Windows Server host), or VMWare<br>
    Tip #4&#58; The 64-bit requirement means, your host must be x64 to run the virtual machines in x64 </li>
    <li>Use ‘Boot’ to VHD (Recommended) <br>
    Note&#58; Only if you have Windows 7 as the host<br>
    See&#58; <a href="http&#58;//www.hanselman.com/blog/LessVirtualMoreMachineWindows7AndTheMagicOfBootToVHD.aspx">Less Virtual, More Machine - Windows 7 and the magic of Boot to VHD</a> </li>
    <li>Install SharePoint 2010 on your Windows 7 PC (Not Recommended)<br>
    You are not fully representing the production server </li>
</ul>
Are there any shortcuts for Silverlight developers (for SharePoint consumption)? <br>
<ul>
    <li>Yes, you can easily deploy a xap file to a document library. However, if you need to debug it you will need the SharePoint 2010 object model. <br>
    Tip&#58; You could minimise your exposure to the object model by using a Repository pattern, which would allow you to debug and test your application without SharePoint, but ultimately you will need to debug and test in SharePoint. </li>
</ul>
<img alt="" class="ms-rteCustom-ImageArea" src="/PublishingImages/UltimateSolution.jpg" /> <font class="ms-rteCustom-FigureNormal" size="+0">Figure&#58; The Ultimate solution for SharePoint development environments is to have another machine under your desk.</font> The Ultimate Solution <br>
<ul>
    <li>Get yourself a second machine (same as remote) </li>
    <li>But don’t share it with anyone else! </li>
</ul>



