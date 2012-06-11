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


<div><p>Run your daily backups to provide a safety net should things go wrong. &#160;</p>
<ol><li>Confirm that the TFS2008 databases were backed up last night. <span class="ms-rteCustom-CodeArea" style="border-bottom&#58;rgb(204,204,204) 1px solid;border-left&#58;rgb(204,204,204) 10px solid;padding-bottom&#58;5px;overflow-x&#58;auto;background-color&#58;rgb(238,238,238);margin&#58;10px 0px;padding-left&#58;10px;width&#58;786px;padding-right&#58;10px;display&#58;block;font-size&#58;12px;border-top&#58;rgb(204,204,204) 1px solid;border-right&#58;rgb(204,204,204) 1px solid;padding-top&#58;5px;">a.<span class="Apple-tab-span" style="white-space&#58;pre;"> </span>TfsActivityLogging<br>b.<span class="Apple-tab-span" style="white-space&#58;pre;"> </span>TfsBuild<br>c.<span class="Apple-tab-span" style="white-space&#58;pre;"> </span>TfsIntegration<br>d.<span class="Apple-tab-span" style="white-space&#58;pre;"> </span>TfsVersionControl<br>e.<span class="Apple-tab-span" style="white-space&#58;pre;"> </span>TfsWarehouse&#160;<br>f.<span class="Apple-tab-span" style="white-space&#58;pre;"> </span>TfsWorkItemTracking<br>g.<span class="Apple-tab-span" style="white-space&#58;pre;"> </span></span><span class="ms-rteCustom-CodeArea" style="border-bottom&#58;rgb(204,204,204) 1px solid;border-left&#58;rgb(204,204,204) 10px solid;padding-bottom&#58;5px;overflow-x&#58;auto;background-color&#58;rgb(238,238,238);margin&#58;10px 0px;padding-left&#58;10px;width&#58;786px;padding-right&#58;10px;display&#58;block;font-size&#58;12px;border-top&#58;rgb(204,204,204) 1px solid;border-right&#58;rgb(204,204,204) 1px solid;padding-top&#58;5px;">TfsWorkItemTrackingAttachments</span><span class="ms-rteCustom-FigureNormal" style="padding-bottom&#58;3px;margin&#58;3px 10px 10px 0px;padding-left&#58;0px;padding-right&#58;0px;display&#58;block;font-size&#58;12px;font-weight&#58;bold;padding-top&#58;0px;">Figure</span><span class="ms-rteCustom-FigureNormal" style="padding-bottom&#58;3px;margin&#58;3px 10px 10px 0px;padding-left&#58;0px;padding-right&#58;0px;display&#58;block;font-size&#58;12px;font-weight&#58;bold;padding-top&#58;0px;">&#58; If you can’t see the physical .bak file for all these, chase up your DBA<br><br></span></li>
<li>Create a backup of the TFS2008 databases by running your Daily Backup maintenance plan on TFS2008&#160;<br><span><img src="/TFS/RulesToBetterTFS2010Migration/PublishingImages/RunDailyBackup.png" alt="" /></span><br><span style="font-size&#58;12px;font-weight&#58;bold;">Figure&#58; Before starting, kick off the daily backups</span> </li></ol></div>
<br><excerpt class='endintro'></excerpt><br>



