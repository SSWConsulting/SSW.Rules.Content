---
type: rule
title: Do you allow users to check for a new version easily?
uri: do-you-allow-users-to-check-for-a-new-version-easily
created: 2009-02-28T09:42:15.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> 
  <p>It is important to give users the ability to check for a new version of the application they are using. And once located it should be easily downloaded and installed.&#160;You need&#58;&#160;</p>
<ol>
    <li>A visual identifier such as&#160;a tick or a cross on the main menu </li>
    <li>A&#160;&quot;Check for Updates&quot; option in our Help menu. </li>
</ol>
 </span>


  <p>Remember&#58; </p>
<ul>
    <li>This is mainly for Windows Forms, but you can do the same for new versions of Web Applications - e.g. a knowledge base package or Reporting Services Application. </li>
    <li>You can do a complete check of your PC at the click of a button using <a href="http&#58;//www.ssw.com.au/ssw/Diagnostics/Default.aspx">SSW Diagnostics</a>. </li>
    <li>Since this check occurs over the web, you should use <a href="http&#58;//www.ssw.com.au/ssw/Standards/Rules/RulesToBetterWindowsForms.aspx#GuiThreading">threading</a> to avoid slowing down the forms responsiveness. This is a generic component that is available in the <a href="http&#58;//www.ssw.com.au/ssw/NETToolkit/Default.aspx">SSW .NET Toolkit</a>. </li>
    <li>If the UI is a Windows Service, be aware that they don't open up the UI very often. Therefore you can't rely on this method. In a coming release Diagnostics will ask for your email and let you know when updates are available for you PC. </li>
</ul>
<img class="ms-rteCustom-ImageArea" style="border&#58;0px solid;" alt="Check for Updates" src="MSN.gif" border="0" /><span class="ms-rteCustom-FigureBad">Figure&#58; BAD UI - a nagging message box that forces the User to click OK </span><br>
<img style="border&#58;0px solid;" alt=" " src="GoodUI.gif" border="0" /> <span class="ms-rteCustom-FigureGood">Figure&#58; Show a Tick when the application is up to date </span><br>
<img class="ms-rteCustom-ImageArea" alt=" " src="BadUI.gif" border="0" /> <span class="ms-rteCustom-FigureGood">Figure&#58; Show a Cross when the application is out of date</span> <br>
<p>To keep the consistent look and consistent code, we have implemented our version checker as a user control.</p>
<img class="ms-rteCustom-ImageArea" style="border&#58;0px solid;" alt=" " src="VersionStatusControl.gif" border="0" /> <font class="ms-rteCustom-FigureNormal">Figure&#58; SSW.Framework.WindowsUI.VersionStatus </font>
<p>As it is a user control, we can easily implement this in all our applications. We just need to place the user control on the winform, and have the ProductDownloadID and ProductLatestVersionURL entered with the correct values.</p>
<img style="border&#58;0px solid;" alt=" " src="VersionStatusProperties.gif" border="0" /> <font class="ms-rteCustom-FigureNormal">Figure&#58; Enter the ProductDownloadID and ProductLatestVersionURL&#160;&#160; </font>
<p><img class="ms-rteCustom-ImageArea" style="border&#58;0px solid;" alt="Check for Updates" src="CheckForUpdate.gif" border="0" /></p>
<font class="ms-rteCustom-FigureGood">Figure&#58; Include 'Check for Updates' in your applications </font>



