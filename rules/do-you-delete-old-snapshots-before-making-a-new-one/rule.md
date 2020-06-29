---
type: rule
title: Do you delete old snapshots before making a new one?
uri: do-you-delete-old-snapshots-before-making-a-new-one
created: 2011-02-14T06:24:04.0000000Z
authors:
- id: 21
  title: Matthew Hodgkins

---



<span class='intro'> Snapshots are a very handy tool for a System Administrator, but they can quickly turn into a nightmare if they are not managed properly. Snapshots take far more hard drive space than a virtual machine without, and if you don’t clean up your snapshots you may run out of drive space. 
 </span>


  <img width="631" height="185" alt="Snapshots are useful, but they can take up a lot of space" src="snapshot-avhds.jpg" /> <br>
<font class="ms-rteCustom-FigureNormal" size="+0">Figure&#58;&#160;Snapshots are useful, but they can take up a lot of space</font>
<p>When you delete a snapshot you can no longer restore the virtual machine to the point in time the snapshot was taken. Deleting a snapshot does not affect any other snapshots, nor will it affect the current state of the virtual machine.</p>
<p>Set yourself a calendar reminder 3 weeks after you make a snapshot so you remember to apply the snapshot to the Virtual Machine (assuming you are happy with the virtual machine after the snapshot).</p>
<ol>
    <li>In the <strong>Hyper-V Manager</strong>, click on the virtual machine you want to apply the snapshot to </li>
    <li>In the <strong>Snapshots </strong>window, right click on the snapshot you wish to apply and click <strong>Delete Snapshot…</strong> </li>
    <li>Confirm the snapshot deletion. </li>
    <li>Wait for the merge process to complete (this may take a while if you have had the snapshot running for a long time and it has grown large in size). </li>
</ol>



