---
type: rule
title: Do you know how to delete a Team Project Collection?
uri: do-you-know-how-to-delete-a-team-project-collection
created: 2011-02-01T04:35:31.0000000Z
authors:
- id: 21
  title: Matthew Hodgkins

---



<span class='intro'> When you initially setup a TFS server, you may add a Team Project Collection for testing purposes. After you have confirmed TFS, SharePoint and Reporting services is all working, you want to remove the test collection you made, but alas, there is no Delete option for project collections.  </span>

<img src="tfs-admin-no-delete.png" alt="" /> <br><font class="ms-rteCustom-FigureNormal" size="+0">Figure&#58; There is no way to delete the Team Project Collection from the TFS Administration console.<br></font><br>To delete the unwanted Team Project Collection&#58;<br><ol><li>On your TFS server, open an <strong>Administrative Command Prompt</strong> </li>
<li>Change into the TFS Tools Directory. Type&#58;<br><strong>cd &quot;%programfiles%\microsoft team foundation server 2010\tools&quot;</strong> </li>
<li>Type in the following (replacing [COLLECTION NAME] with the collection you want to delete)&#58;<br><strong>TFSConfig Collection /delete /collectionName&#58;[COLLECTION NAME]<br></strong></li></ol>
<p><img src="tfs-admin-delete-collection.png" alt="" /><br><font class="ms-rteCustom-FigureNormal" size="+0">Figure&#58; Use the TFSConfig tool to delete a Team Project </font><font class="ms-rteCustom-FigureNormal" size="+0">Collection</font>If you created a SharePoint Portal for your Team Project Collection, you should clean it up as well.</p>
<ol><li>Open the URL of your Team Project Collections SharePoint portal (eg. http&#58;//northwind.com.au/tfs/TestProjectCollection) </li>
<li>Select <strong>Site Actions</strong> | <strong>Site Settings</strong> on the right </li>
<li>Under the <strong>Site Administration</strong> subheading, click on <strong>Delete this site</strong> </li>
<li>Confirm the deletion </li></ol>
<p>If you created a Reports site for your Team Project Collection, you should clean it up as well.</p>
<ol><li>Open the URL of your Reporting Services page (eg. http&#58;//tfs.ssw.com.au/Reports/) </li>
<li>Click on the <strong>TfsReports</strong> folder </li>
<li>Click on the name of the Team Project Collections folder </li>
<li>Click <strong>Properties </strong>in the top navigation </li>
<li>Click on <strong>Delete</strong> </li></ol>
<p>Now your TFS server is nice and clean and fit for production.</p>


