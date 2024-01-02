---
type: rule
archivedreason: 
title: Do you know how to setup a Boot to VHD Image?
guid: 5612c6fe-9235-4e16-a01f-1c53f454faf2
uri: do-you-know-how-to-setup-a-boot-to-vhd-image
created: 2011-04-13T05:26:11.0000000Z
authors:
- title: Matthew Hodgkins
  url: https://ssw.com.au/people/matthew-hodgkins
related: []
redirects: []

---

Using Boot to VHD is very similar to dual-booting your machine, except that you do not have to partition your hard drive. It also has performance benefits over using a Hyper-V server for presentations.   
<!--endintro-->
**Pre-Requisites** 


* The presentation computer running Windows
* A SysPreped VHD image to be deployed onto the presentation computer


1. Copy a SysPreped VHD image to the laptop to be used for the presentation.
2. Open an Administrative command prompt.
3. Type:

```bash
bcdedit /copy {default} /d “Demo-NameOfDemo”
```


![Creating the entry using BCDEdit shows your GUID](fig1-creatingentry.png)
**Figure - Creating the entry using BCDEdit shows your GUID**
4. Type:

```bash
bcdedit /set <GUID>  device vhd=[D:]\VM-DEV-SharePoint_2010_Public_Beta.vhd
```

**D:\** is the drive the VHD is located and  **VM-DEV-SharePoint\_2010\_Public\_Beta.vhd** is the location of your VHD file. Make sure you replace  **&lt;GUID&gt;** with the GUID you got in the previous step.
5. Type:

```bash
bcdedit /set <GUID>  osdevice vhd=[D:]\VM-DEV-SharePoint_2010_Public_Beta.vhd
```

**D:\** is the drive the VHD is located and  **VM-DEV-SharePoint\_2010\_Public\_Beta.vhd** is the location of your VHD file. Make sure you replace  **&lt;GUID&gt;** with the GUID you got in the previous step.
6. Type:


```bash
bcdedit /set <GUID> detecthal on
```


![Each time you run a BCDEdit command it should return ](fig2-addguids.png)
**Figure - Each time you run a BCDEdit command it should return "The operation completed successfully"**
7. Reboot the computer and now you will have the option to choose between Windows 7 and the new Boot to VHD image.
