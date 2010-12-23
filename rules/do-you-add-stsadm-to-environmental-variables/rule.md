---
type: rule
archivedreason: 
title: Do you add stsadm to environmental variables
guid: 2a02a6a0-a3ff-40ce-abe3-40bace029c00
uri: do-you-add-stsadm-to-environmental-variables
created: 2010-12-23T01:48:27.0000000Z
authors:
- id: 21
  title: Matthew Hodgkins
- id: 9
  title: William Yin
- id: 8
  title: John Liu
related: []

---



  <p>In SharePoint 2007, it is a good idea to add the path to stsadm.exe into the environment variables on a SharePoint server so you can open a command prompt and run the tool from anywhere.</p>
<p><img alt="" src="/PublishingImages/stsadm.png" /><br>
<font class="ms-rteCustom-FigureNormal" size="+0">Figure&#58; you should be able to quickly type ‘stsadm’. Believe me you will be typing it enough!</font>In SharePoint 2010, you can skip quite a few steps by using the PowerShell Console.<br>
<br>
<img alt="" src="/PublishingImages/SP2010PowerShell.png" /><br>
<font class="ms-rteCustom-FigureNormal" size="+0">Figure&#58; Using SharePoint 2010 Management Shell</font></p>

<br><excerpt class='endintro'></excerpt><br>

  <p>
    <strong>More Information</strong> for SharePoint 2007</p>
<ol>
    <li>In the start menu type <b>Edit the system environment variables </b>and run the tool<img alt="" src="/PublishingImages/EnvVariables.png" />&#160;<br>
    Figure 1 - Search for &quot;Edit the system environment variables” in the Start Menu </li>
    <li>In the <b>System variables </b>section, select <b>Path </b>and click <b>Edit<br>
    </b><img alt="" src="/PublishingImages/EnvVariables2.png" />&#160;<br>
    Figure 2 - Under System Variables | Select Path | Click Edit </li>
    <li>Add the path at the end of the <b>Variable Value</b>
    <ol>
        <li>For a SharePoint 2007 Server, enter&#58;<br>
        <b>;C&#58;\Program Files\Common Files\Microsoft Shared\Web Server Extensions\12\bin</b> </li>
    </ol>
    </li>
    <li>You may need to reboot the server </li>
    <li>You can now run <b>stsadm </b>from anywhere in the command prompt </li>
</ol>
<p>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; </p>



