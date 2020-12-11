---
type: rule
archivedreason: 
title: Do you backup your databases?
guid: 51ffe26f-c0cf-418e-be78-e7e742be6e99
uri: do-you-backup-your-databases
created: 2009-11-07T23:06:18.0000000Z
authors: []
related: []

---


<div><p>Run your daily backups to provide a safety net should things go wrong.  </p>
<ol><li>Confirm that the TFS2008 databases were backed up last night. <span class="ms-rteCustom-CodeArea" style="border-bottom:rgb(204,204,204) 1px solid;border-left:rgb(204,204,204) 10px solid;padding-bottom:5px;overflow-x:auto;background-color:rgb(238,238,238);margin:10px 0px;padding-left:10px;width:786px;padding-right:10px;display:block;font-size:12px;border-top:rgb(204,204,204) 1px solid;border-right:rgb(204,204,204) 1px solid;padding-top:5px;"><p>a.<span class="Apple-tab-span" style="white-space:pre;"> </span>TfsActivityLogging<br>b.<span class="Apple-tab-span" style="white-space:pre;"> </span>TfsBuild<br>c.<span class="Apple-tab-span" style="white-space:pre;"> </span>TfsIntegration<br>d.<span class="Apple-tab-span" style="white-space:pre;"> </span>TfsVersionControl<br>e.<span class="Apple-tab-span" style="white-space:pre;"> </span>TfsWarehouse <br>f. TfsWorkItemTracking<br>g.<span class="Apple-tab-span" style="white-space:pre;"> </span>TfsWorkItemTrackingAttachments</p></span><span class="ms-rteCustom-FigureNormal" style="padding-bottom:3px;margin:3px 10px 10px 0px;padding-left:0px;padding-right:0px;display:block;font-size:12px;font-weight:bold;padding-top:0px;">Figure: If you can’t see the physical .bak file for all these, chase up your DBA</span></li>
<li>Create a backup of the TFS2008 databases by running your Daily Backup maintenance plan on TFS2008 <br><span><img src="RunDailyBackup.png" alt="" /></span><br><span style="font-size:12px;font-weight:bold;">Figure: Before starting, kick off the daily backups</span> </li></ol></div>
<br><excerpt class='endintro'></excerpt><br>



