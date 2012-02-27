---
type: rule
archivedreason: 
title: Do you know how to delete orphaned users from the People Picker?
guid: c31997cb-b93b-42a7-8c6c-41efeea1d0db
uri: do-you-know-how-to-delete-orphaned-users-from-the-people-picker
created: 2012-02-27T15:49:49.0000000Z
authors: []
related: []

---


The SharePoint &quot;People Picker&quot; is a great tool for quickly selecting users of your SharePoint site. It allows you to quickly select users from your organization by browsing Active Directory.
<br><excerpt class='endintro'></excerpt><br>
<img src="/ITAndNetworking/SharePoint/PublishingImages/PeoplePicker.jpg" class="ms-rteCustom-ImageArea" alt="" /><br>
<font size="-0" class="ms-rteCustom-FigureNormal">Figure&#58; The People Picker</font>
<p>Unfortunately, if you have added users directly to your site collection, and later deleted or disabled them from Active Directory, you will notice that these orphaned users will still appear in your People Picker. This will eventually clutter up your People Picker.</p>
<img src="/ITAndNetworking/SharePoint/PublishingImages/PeoplePicker-deleted.jpg" class="ms-rteCustom-ImageArea" alt="" /><br>
<font size="-0" class="ms-rteCustom-FigureNormal">Figure&#58; A user in the People Picker that was deleted from Active Directory</font>
<img src="/ITAndNetworking/SharePoint/PublishingImages/PeoplePicker-searching.jpg" class="ms-rteCustom-ImageArea" alt="" /><br>
<font size="-0" class="ms-rteCustom-FigureNormal">Figure&#58; Searching in Active Directory for the user shows the user is in fact deleted</font>
<p>To remove these orphaned users, as a SharePoint Administrator, you can open the following URL (where www.northwind.com is your SharePoint URL)&#58;</p>
<ul>
<li>http&#58;//www.northwind.com/_catalogs/users/simple.aspx </li>
</ul>
<p>On this page you will find a list of all the users that are members of your site collection, including the orphaned users. </p>
<img src="/ITAndNetworking/SharePoint/PublishingImages/PeoplePicker-found.jpg" class="ms-rteCustom-ImageArea" alt="" /><br>
<font size="-0" class="ms-rteCustom-FigureNormal">Figure&#58; We have found our orphaned user!</font>
<p>To remove the user simply click on the <strong>Username</strong> | Click <strong>Delete User from Site Collection</strong>. This will instantly remove the user from the People Picker.</p>



