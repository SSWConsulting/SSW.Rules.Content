---
type: rule
archivedreason: 
title: Do you know how to remove old Boot to VHD entries?
guid: 7024b36a-9bad-4d5c-973b-3882a723f51d
uri: do-you-know-how-to-remove-old-boot-to-vhd-entries
created: 2011-04-13T06:49:09.0000000Z
authors:
- id: 21
  title: Matthew Hodgkins
related: []

---


When you have finished with the VHD for the presentation you will want to remove the boot entries that were created for the VHD.

<br><excerpt class='endintro'></excerpt><br>

  <ol>
    <li>Open an administrative command prompt</li>
    <li>View all the boot entries by typing&#58; <font class="ms-rteCustom-CodeArea" size="+0">bcdedit</font> <img alt="The list Boot entries after running bcdedit" src="/PublishingImages/fig6-listbootentries.png" /><br>
    <font class="ms-rteCustom-FigureNormal" size="+0">Figure - The list Boot entries after running bcdedit<br>
    </font></li>
    <li>Using the <strong>identifier</strong> from the previous step you can now run the following command to delete the entry&#58;<br>
    <font class="ms-rteCustom-CodeArea" size="+0">bcdedit /delete <strong>&#123;identifier&#125;</strong></font><img style="width&#58;677px;height&#58;219px;" alt="The boot entry has now been deleted" src="/PublishingImages/fig7-deletingthebootentry.png" /><br>
    <font class="ms-rteCustom-FigureNormal" size="+0">Figure -&#160;The boot entry has now been deleted</font></li>
</ol>
You can now delete or move your VHD file and you will not get any errors when booting your laptop.



