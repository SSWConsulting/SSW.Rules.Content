---
type: rule
archivedreason: 
title: Connection Stream - Do you use a UDL when getting database settings?
guid: d35608be-bccb-495f-ac6c-22285b72b1e5
uri: connection-stream---do-you-use-a-udl-when-getting-database-settings
created: 2012-11-27T09:22:39.0000000Z
authors: []
related: []

---


<p>Why do people always invent ways of getting the same old server name and a database name? Look at this image from <a href="http&#58;//www.ssw.com.au/ssw/Standards/DeveloperGeneral/SQLservertools.aspx#SpeedFerret">Speed Ferret</a> - one of my favorite SQL Server utilities.</p>
<br><excerpt class='endintro'></excerpt><br>
​<dl class="badImage"><dt><img alt="Custom database connection screen " src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/CustomDatabaseConnectionScreen.jpg" /></dt>
<dd>Figure&#58; Bad Example - Custom database connection screen in Speed Ferret</dd></dl>
<div>While a nice form, it would have taken quite some developer time to get it right. Not only that, it is a little bit different than what a user has seen before. Now look at this UDL from one of our utilities <a href="http&#58;//www.ssw.com.au/ssw/SQLAuditor">SSW SQL Auditor</a>&#58;</div>
<dl class="goodImage"><dt><img alt="Standard Microsoft UDL dialog" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/StandardMSUDLDialog.jpg" /></dt>
<dd>Figure&#58; Good Example - Standard Microsoft UDL dialog</dd></dl>
<div>Every developer has seen this before - so use it. Better still, it is only a few lines of code&#58; <a href="https&#58;//gist.github.com/SSWConsulting/60cce3f7a65665d7dae2#file-b-open-udl-dialog-dh">B-Open UDL Dialog-DH.txt</a> </div>
<dl class="image"><dt><img alt=" Visual Studio .NET 2005 Microsoft are yet to release an API" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/ReleaseAPI.jpg" /></dt>
<dd>Figure&#58; Coming in Visual Studio .NET 2005 Microsoft are yet to release an API to do this</dd></dl>
<div><a href="http&#58;//www.ssw.com.au/ssw/Standards/BetterSoftwareSuggestions/MSForm.aspx#InvokingOLEBDataLinkPropertiesDialog">Need extra information?</a></div>
<h4>Exception</h4>
<div>The above cannot be used when you want the user to create a new database. Microsoft does not supply an out of the box UI and there is no third party solution. Only in this case you have to create your own form.</div>
<dl class="image"><dt><img alt="SQL Deploy uses its own custom form " src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/SQLDeploy.jpg" /></dt>
<dd>Figure&#58; SQL Deploy uses its own custom form for &quot;selecting&quot; a database name</dd></dl>



