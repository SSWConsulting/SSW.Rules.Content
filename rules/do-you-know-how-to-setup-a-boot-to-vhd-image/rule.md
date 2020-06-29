---
type: rule
title: Do you know how to setup a Boot to VHD Image?
uri: do-you-know-how-to-setup-a-boot-to-vhd-image
created: 2011-04-13T05:26:11.0000000Z
authors:
- id: 21
  title: Matthew Hodgkins

---



<span class='intro'> Using Boot to VHD is very similar to dual-booting your machine, except that you do not have to partition your hard drive. It also has performance benefits over using a Hyper-V server for presentations. 
 </span>


  <strong>Pre-Requisites</strong>
  <br>
<br>
<ul>
    <li>The presentation computer running Window 7</li>
    <li>A SysPreped VHD image to be deployed onto the presentation computer</li>
</ul>
<ol>
    <li>Copy a SysPreped VHD image to the laptop to be used for the presentation.</li>
    <li>Open an Administrative command prompt.</li>
    <li>Type&#58;<br>
    <font class="ms-rteCustom-CodeArea" size="+0">bcdedit /copy &#123;default&#125; /d “Demo-NameOfDemo”</font><img alt="Creating the entry using BCDEdit shows your GUID" src="fig1-creatingentry.png" /><br>
    <font class="ms-rteCustom-FigureNormal" size="+0">Figure - Creating the entry using BCDEdit shows your GUID</font></li>
    <li>Type&#58;<br>
    <font class="ms-rteCustom-CodeArea" size="+0">bcdedit /set &lt;GUID&gt; <strong>device </strong>vhd=[D&#58;]\VM-DEV-SharePoint_2010_Public_Beta.vhd</font><br>
    <strong>D&#58;\</strong> is the drive the VHD is located and <strong>VM-DEV-SharePoint_2010_Public_Beta.vhd</strong> is the location of your VHD file. Make sure you replace <strong>&lt;GUID&gt; </strong>with the GUID you got in the previous step.</li>
    <li>Type&#58;<br>
    <font class="ms-rteCustom-CodeArea" size="+0">bcdedit /set &lt;GUID&gt; <strong>osdevice </strong>vhd=[D&#58;]\VM-DEV-SharePoint_2010_Public_Beta.vhd</font><br>
    <strong>D&#58;\</strong> is the drive the VHD is located and <strong>VM-DEV-SharePoint_2010_Public_Beta.vhd</strong> is the location of your VHD file. Make sure you replace <strong>&lt;GUID&gt; </strong>with the GUID you got in the previous step.</li>
    <li>Type&#58;<br>
    <font class="ms-rteCustom-CodeArea" size="+0">bcdedit /set &lt;GUID&gt; detecthal on</font><img alt="Each time you run a BCDEdit command it should return &quot;The operation completed successfully&quot;" src="fig2-addguids.png" /><br>
    <font class="ms-rteCustom-FigureNormal" size="+0">Figure -&#160;Each time you run a BCDEdit command it should return &quot;The operation completed successfully&quot;</font></li>
    <li>Reboot the computer and now you will have the option to choose between Windows 7 and the new Boot to VHD image.</li>
</ol>



