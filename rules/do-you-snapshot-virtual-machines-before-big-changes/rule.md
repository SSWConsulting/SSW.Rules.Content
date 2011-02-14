---
type: rule
archivedreason: 
title: Do you snapshot Virtual Machines before big changes?
guid: 4c2176dd-f101-43c5-b472-62f567080ea3
uri: do-you-snapshot-virtual-machines-before-big-changes
created: 2011-02-14T06:18:58.0000000Z
authors:
- id: 21
  title: Matthew Hodgkins
related: []

---



  <p>Snapshots are a very convent way to back up a system before a big change is made. It is important to note that Microsoft does not support snapshots of running systems. This is because a snapshot is taken of the system exactly as is, with open connections and interrupt requests. For more information on this you can read Brian Harry’s blog post here&#58; <a shape="rect" href="http&#58;//blogs.msdn.com/bharry/archive/2010/02/10/a-tfs-2010-upgrade-success-story.aspx">http&#58;//blogs.msdn.com/bharry/archive/2010/02/10/a-tfs-2010-upgrade-success-story.aspx</a></p>
<p>This is why you <strong>MUST </strong>shut down your server before taking a snapshot.</p>

<br><excerpt class='endintro'></excerpt><br>

  <ol>
    <li>Shutdown the virtual server</li>
    <li>In the <strong>Hyper-V Manager</strong>, ensure the Virtual Machine has the state of <strong>Off</strong></li>
    <li>Right click on the virtual machine you wish to snapshot and click <strong>Snapshot</strong></li>
    <li>The snapshot should run very quickly and you will notice the snapshot in the <strong>Snapshots </strong>area of the <strong>Hyper-V Manager<br>
    <br>
    <img alt="You will see the snapshots associated with a Virtual Machine when you click on them" src="/PublishingImages/snapshot-while-off.jpg" /></strong></li>
    <font class="ms-rteCustom-FigureGood" size="+0"><strong>You will see the snapshots associated with a Virtual Machine when you click on them<br>
    </strong></font><br>
    <li>You can start your server back up again</li>
</ol>



