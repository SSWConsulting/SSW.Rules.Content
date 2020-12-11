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

In SharePoint 2007, it is a good idea to add the path to stsadm.exe into the environment variables on a SharePoint server so you can open a command prompt and run the tool from anywhere.


![](stsadm.png)
<font class="ms-rteCustom-FigureNormal">Figure: you should be able to quickly type ‘stsadm’. Believe me you will be typing it enough!</font>In SharePoint 2010, you can skip quite a few steps by using the PowerShell Console.


![](SP2010PowerShell.png)
<font class="ms-rteCustom-FigureNormal">Figure: Using SharePoint 2010 Management Shell</font>

<!--endintro-->

**More Information** for SharePoint 2007

1. In the start menu type  **Edit the system environment variables** and run the tool
![](EnvVariables.png) 
<br>    Figure 1 - Search for "Edit the system environment variables” in the Start Menu
2. In the  **System variables** section, select  **Path** and click  **Edit
** 
![](EnvVariables2.png) 
<br>    Figure 2 - Under System Variables | Select Path | Click Edit
3. Add the path at the end of the  **Variable Value**
    1. For a SharePoint 2007 Server, enter:
**;C:\Program Files\Common Files\Microsoft Shared\Web Server Extensions\12\bin**
4. You may need to reboot the server
5. You can now run  **stsadm** from anywhere in the command prompt
