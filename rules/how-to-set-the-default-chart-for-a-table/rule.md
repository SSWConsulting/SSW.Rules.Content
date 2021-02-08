---
type: rule
archivedreason: 
title: Do you know how to set the default chart for a table (previously known as an entity)?
guid: a7a94278-db58-47f4-a809-9df55a4788c5
uri: how-to-set-the-default-chart-for-a-table
created: 2021-02-08T15:59:38.0000000Z
authors:
- title: Mehmet Ozdemir
  url: https://ssw.com.au/people/mehmet-ozdemir
related: []
redirects:
- do-you-know-how-to-set-the-default-chart-for-a-table-previously-known-as-an-entity
- do-you-know-how-to-set-the-default-chart-for-a-table-(previously-known-as-an-entity)

---


<p class="ssw15-rteElement-P">​Model-driven apps allow you to create multiple charts per table, ordinarily, the first chart is the default chart when opening the charts pane. Setting a system-wide default chart takes a bit more work.&#160;​<span style="color&#58;#444444;">​</span></p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="image"><dt><img src="/PublishingImages/default-chart-1.png" alt="default-chart-1.png" /></dt><dd>Figure&#58; The first chart in the list is the default&#160;</dd></dl><p>In the example above “Leads by Rating&quot; is the be the default system-level chart of the Lead table. Some additional work is required to change the default. The easiest way of doing this is with 
   <a href="https&#58;//www.xrmtoolbox.com/">XRMToolBox</a> and the 
   <a href="https&#58;//crmchartguy.com/2017/06/10/edit-charts-in-the-xrmtoolbox-for-dynamics-365/">Advanced Chart Editor</a> plugin.&#160;</p><ol><li>Open the Advanced Chart Editor, Load Entities, and Navigate to the table<br>
   <dl class="image"><dt><img src="/PublishingImages/default-chart-2.png" alt="default-chart-2.png" /></dt></dl></li><li>If changing the default chart to Leads by Source, select chart and export it<br>
   <dl class="image"><dt><img src="/PublishingImages/default-chart-3.png" alt="default-chart-3.png" /></dt></dl></li><li>Open the exported XML file in the text editor of your choice, and change the <b>isdefault</b> element to “true&quot; and save the file<br>
   <dl class="image"><dt><img src="/PublishingImages/default-chart-4.png" alt="default-chart-4.png" /><br></dt></dl></li><li>Import the modified XML back into the Advanced Chart Editor and publish the changes<br>
   <dl class="image"><dt><img src="/PublishingImages/default-chart-5.png" alt="default-chart-5.png" /></dt></dl></li><li>Refresh the Table view, the updated chart should be the default chart in the list<br>
   <dl class="image"><dt><img src="/PublishingImages/default-chart-6.png" alt="default-chart-6.png" />​<br></dt></dl></li></ol><p><b>Note&#58;</b> If the chart that was modified to be the new default is not at the top of the list, check the first chart in the list by exporting it and confirming the 
   <strong>isdefault </strong>element is set to false. &#160;</p><p>Where there are two charts with the 
   <strong>isdefault </strong>element set to true, these default charts will be at the top of the list and sorted alphabetically. &#160;</p><p>For example, if “Lead by Rating&quot; and “Lead by Source&quot; are both set as default then they would both be at the top and sorted alphabetically. The remaining charts would then be sorted alphabetically. &#160;</p><p>This can be desirable in some instances.&#160;</p><dl class="image"><dt><img src="/PublishingImages/default-chart-7.png" alt="default-chart-7.png" /></dt><dd>Figure&#58; Two sorts, first alphabetical sort for the defaults, second alphabetical sort for the remaining charts&#160;</dd></dl>


