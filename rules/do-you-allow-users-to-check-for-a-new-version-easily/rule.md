---
type: rule
archivedreason: 
title: Do you allow users to check for a new version easily?
guid: 8da99121-3aed-464b-b4a6-51c176a17402
uri: do-you-allow-users-to-check-for-a-new-version-easily
created: 2009-02-28T09:42:15.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---


This field should not be null (Remove me when you edit this field).
<br><excerpt class='endintro'></excerpt><br>

  <p>Remember&#58; </p>
<ul>
    <li>This is mainly for Windows Forms, but you can do the same for new versions of Web Applications - e.g. a knowledge base package or Reporting Services Application. </li>
    <li>You can do a complete check of your PC at the click of a button using <a href="http&#58;//www.ssw.com.au/ssw/Diagnostics/Default.aspx">SSW Diagnostics</a>. </li>
    <li>Since this check occurs over the web, you should use <a href="http&#58;//www.ssw.com.au/ssw/Standards/Rules/RulesToBetterWindowsForms.aspx#GuiThreading">threading</a> to avoid slowing down the forms responsiveness. This is a generic component that is available in the <a href="http&#58;//www.ssw.com.au/ssw/NETToolkit/Default.aspx">SSW .NET Toolkit</a>. </li>
    <li>If the UI is a Windows Service, be aware that they don't open up the UI very often. Therefore you can't rely on this method. In a coming release Diagnostics will ask for your email and let you know when updates are available for you PC. </li>
</ul>
<img class="ms-rteCustom-ImageArea" style="border&#58;0px solid;" alt="Check for Updates" src="/Standards/Management/RulesToSuccessfulProjects/PublishingImages/MSN.gif" border="0" /><span class="ms-rteCustom-FigureBad">Figure&#58; BAD UI - a nagging message box that forces the User to click OK </span><br>
<img style="border&#58;0px solid;" alt=" " src="/Standards/Management/RulesToSuccessfulProjects/PublishingImages/GoodUI.gif" border="0" /> <span class="ms-rteCustom-FigureGood">Figure&#58; Show a Tick when the application is up to date </span><br>
<img class="ms-rteCustom-ImageArea" alt=" " src="/Standards/Management/RulesToSuccessfulProjects/PublishingImages/BadUI.gif" border="0" /> <span class="ms-rteCustom-FigureGood">Figure&#58; Show a Cross when the application is out of date</span> <br>
<p>To keep the consistent look and consistent code, we have implemented our version checker as a user control.</p>
<img class="ms-rteCustom-ImageArea" style="border&#58;0px solid;" alt=" " src="/Standards/Management/RulesToSuccessfulProjects/PublishingImages/VersionStatusControl.gif" border="0" /> <font class="ms-rteCustom-FigureNormal">Figure&#58; SSW.Framework.WindowsUI.VersionStatus </font>
<p>As it is a user control, we can easily implement this in all our applications. We just need to place the user control on the winform, and have the ProductDownloadID and ProductLatestVersionURL entered with the correct values.</p>
<img style="border&#58;0px solid;" alt=" " src="/Standards/Management/RulesToSuccessfulProjects/PublishingImages/VersionStatusProperties.gif" border="0" /> <font class="ms-rteCustom-FigureNormal">Figure&#58; Enter the ProductDownloadID and ProductLatestVersionURL&#160;&#160; </font>
<p><img class="ms-rteCustom-ImageArea" style="border&#58;0px solid;" alt="Check for Updates" src="/Standards/Management/RulesToSuccessfulProjects/PublishingImages/CheckForUpdate.gif" border="0" /></p>
<font class="ms-rteCustom-FigureGood">Figure&#58; Include 'Check for Updates' in your applications </font>



