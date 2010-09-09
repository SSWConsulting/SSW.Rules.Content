---
type: rule
title: Do you know the best way to take SharePoint data offline?
uri: do-you-know-the-best-way-to-take-sharepoint-data-offline
created: 2009-12-15T07:50:38.0000000Z
authors:
- id: 8
  title: John Liu

---



<span class='intro'> In SharePoint 2010, there are quite a few tools that we can use to take SharePoint data offline. Let’s look at our options&#58;<br>
<ul>
    <li>use Outlook to synchronize document libraries, calendar and contacts offline. </li>
    <li>use Excel to take read-only copies of list data offline. </li>
    <li>&#160;use Access to take list data offline – Access also lets you edit offline and synchronize back. </li>
    <li>&#160;use SharePoint Workspace (this was Groove) to take entire Site offline, unfortunately this doesn’t work for calendars. </li>
</ul>
 </span>

We think the best way is to use Workspace instead of Outlook&#58;<br>
<ol>
    <li>SharePoint Workspace synchronize an entire site<br>
    a. So when lists are renamed it knows about it.<br>
    b. It also knows about new lists that are added to a SharePoint site <img alt="" class="ms-rteCustom-ImageArea" src="/Standards/SoftwareDevelopment/RulesToBetterSharePoint/PublishingImages/Synchronize.jpg" /><span class="ms-rteCustom-FigureNormal">Figure&#58; SharePoint Workspace synchronizing an entire site </span></li>
    <li>Outlook can be quite busy when synchronizing to Exchange server; it is good to not burden it with more work. </li>
</ol>
While SharePoint Workspace is quite good, we don’t like to store lists in it&#58;<br>
<ol>
    <li>Access has better filtering, sorting options when offline </li>
</ol>



