---
type: rule
title: Do you confirm there is no data lost after the migration
uri: do-you-confirm-there-is-no-data-lost-after-the-migration
created: 2010-12-23T07:18:06.0000000Z
authors:
- id: 21
  title: Matthew Hodgkins

---



<span class='intro'> 
  <p>After you have finished migrating the database, it is extremely important to verify that no data has been lost in the move. The quickest way to do this is to compare the SharePoint 2007 and the SharePoint 2010 server <b>All Site Content</b> pages and confirm that the item numbers match&#58;</p>
<p>&#160;<img alt="" src="AllSiteContentCount.png" /></p>
<p class="ms-rteCustom-FigureNormal"><b>Figure 7 – In the &quot;All Site Content&quot; pages library, ensure the ‘item’ numbers exactly match between SharePoint 2007 and SharePoint 2010</b></p>
<ol>
    <li>Look at your report from the SharePoint 2007 server </li>
    <li>On the SharePoint 2010 server, open the site collection you just migrated to</li>
    <li>Select <b>Site Actions | Site Settings</b></li>
    <li>Select <b>All Site Content</b></li>
    <li>Compare item numbers with 2007</li>
</ol>
<p>Repeat this process for all sub-sites of the site collection you migrated.</p>
 </span>




