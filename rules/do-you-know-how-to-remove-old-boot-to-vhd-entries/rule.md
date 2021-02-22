---
type: rule
archivedreason: 
title: Do you know how to remove old Boot to VHD entries?
guid: 7024b36a-9bad-4d5c-973b-3882a723f51d
uri: do-you-know-how-to-remove-old-boot-to-vhd-entries
created: 2011-04-13T06:49:09.0000000Z
authors:
- title: Matthew Hodgkins
  url: https://ssw.com.au/people/matthew-hodgkins
related: []
redirects: []

---

When you have finished with the VHD for the presentation you will want to remove the boot entries that were created for the VHD.  
<!--endintro-->

1. Open an administrative command prompt
2. View all the boot entries by typing: 


```
bcdedit
```


 ![The list Boot entries after running bcdedit](fig6-listbootentries.png)
**Figure - The list Boot entries after running bcdedit
**
3. Using the  **identifier** from the previous step you can now run the following command to delete the entry:



```
bcdedit /delete  {identifier}
```


![The boot entry has now been deleted](fig7-deletingthebootentry.png)
**Figure - The boot entry has now been deleted**

 You can now delete or move your VHD file and you will not get any errors when booting your laptop.
