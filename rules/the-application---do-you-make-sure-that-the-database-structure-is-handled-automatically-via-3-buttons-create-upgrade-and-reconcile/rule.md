---
type: rule
title: The application - Do you make sure that the database structure is handled automatically via 3 buttons "Create", "Upgrade" and "Reconcile"?
uri: the-application---do-you-make-sure-that-the-database-structure-is-handled-automatically-via-3-buttons-create-upgrade-and-reconcile
created: 2009-10-06T00:19:11.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> 
  <p>You get an error message reported from a user like&#58; </p>
<blockquote><i>&#160;&#160;&#160; When I click the Save button on the product form it gives an error message about a missing field.</i></blockquote>
<dl class="image">
    <dt><img alt="" src="/PublishingImages/ObamaThinking.jpg" /> </dt>
    <dd>Figure&#58; The developer thinks &quot;what could be wrong&quot; </dd>
</dl>
<dl class="image">
    <dt><img alt="" src="/PublishingImages/WorksOnMyMachine.png" /> </dt>
    <dd>Figure&#58; The developer tests then&#160;replies &quot;Works on my machine&quot; </dd>
</dl>
<p>You try and reproduce it on your version in the office and everything works perfectly.<br>
<br>
You suspect that the customer probably has changed the schema. So you start drafting an email to the user like&#58; </p>
 </span>


  <div class="greyBox">Mary, I need you to send me your database schema as it might be different from what it should be. Can you&#58;<br>
<ol>
    <li>Open up Enterprise Manager in you are on SQL 2000 (or open SQL Management Studio if you are on SQL 2005, 2008 or 2010) </li>
    <li>Open the first tree </li>
    <li>Open the second tree </li>
    <li>Select your server </li>
    <li>Open that tree </li>
    <li>Select Databases </li>
    <li>Open that tree </li>
    <li>Select the database called Northwind </li>
    <li>Right click it and choose All Tasks, then <b>Generate SQL Script</b> </li>
    <li>Then select the options </li>
    <li>etc </li>
    <li>Then when I get this I will compare and I will make a script file for you to run and fix the problem </li>
</ol>
</div>
<p>STOP! STOP! STOP!<br>
It would be much better to just say&#58;</p>
<blockquote><i>Mary, click the &quot;Reconcile&quot; button and it will tell us what is wrong</i></blockquote>
<p>Bottom line is the customers' database schema should always be correct, should be managed automatically by the app and if it is not, it is their problem.</p>
<p>Therefore, you should deliver an application with the buttons &quot;Create&quot;, Upgrade&quot; and &quot;Reconcile&quot;, accessible via &quot;Tools - Options&quot; and a &quot;Database&quot; tab. We do this by using SSW SQL Deploy and throwing on the inherited user-control from the SSW.SQLDeploy.Options project.</p>
<p>For more information see <a href="http&#58;//www.ssw.com.au/ssw/Standards/DeveloperGeneral/SQLservertools.aspx#SQLDeploy">Best Tools for SQL Server</a></p>
It looks like this<br>
<img class="ms-rteCustom-ImageArea" alt="Reconcile" src="/PublishingImages/Reconcile.jpg" /> <span class="ms-rteCustom-FigureGood">Figure&#58; When weird errors are happening at a client, you need a &quot;Reconcile&quot; button in your application. This compares the current scripts, to the client's database and tells you if things are not right</span> <img class="ms-rteCustom-ImageArea" alt="New database dialog" src="/PublishingImages/NewDatabaseDialog.jpg" /> <span class="ms-rteCustom-FigureGood">Figure&#58; First time your client opens the application, they will need to Creating a database. It should be as easy as clicking &quot;Create&quot;</span>
<div class="greyBox">As a developer, I promise to do these 3 things&#58;
<ol>
    <li>Save every SQL change I do as a script </li>
    <li>Make sure the application I develop, has 3 buttons, &quot;Create&quot;, &quot;Update&quot; and &quot;Reconcile&quot; </li>
    <li>Never ask a client to run a script </li>
</ol>
</div>
<dl class="image">
    <dt><img alt="" src="/PublishingImages/ObamSwearing.jpg" /> </dt>
    <dd>Figure&#58; Adam makes all his new developers swear in and repeat this </dd>
</dl>



