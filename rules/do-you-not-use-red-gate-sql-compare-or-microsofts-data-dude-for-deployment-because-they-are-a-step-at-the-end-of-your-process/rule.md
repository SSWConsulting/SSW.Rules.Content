---
type: rule
title: Do you *not* use Red-Gate SQL Compare (or Microsoft's Data Dude) for deployment (because they are a step at the end of your process)?
uri: do-you-not-use-red-gate-sql-compare-or-microsofts-data-dude-for-deployment-because-they-are-a-step-at-the-end-of-your-process
created: 2009-10-05T23:21:49.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> SQL Compare is a good tool to find out the differences between two databases. It can help you answer the question &quot;Is your database the same as mine?&quot;. <br>
<br>
Let's see what it is good at. 
 </span>


  <dl class="image">
    <dt><img alt="" src="SQLCompareSync.png" /> </dt>
    <dd>Figure&#58; You can use SQL Compare to make two databases the same </dd>
</dl>
<dl class="image">
    <dt><img alt="" src="SQLCompareTables.png" /> </dt>
    <dd>Figure&#58; SQL Compare clearly shows some tables are missing </dd>
</dl>
<p>So if you want to compare 2 databases&#160;SQL Compare (or Data Dudes Compare)&#160;is great tools. They even let you synchronize sweetly between these 2 databases. However, if you are doing this at the end of your release cycle, you have a problem.&#160;&#160;Your schema deployment process is broken.</p>
<p>What you should be doing is seeing your <a shape="rect" href="/Pages/DoYouHaveASchemaMaster.aspx" title="Database Schema Master">Schema Master</a> each time you have a new .sql file. You do this during the development process, not at the end in the package and deployment process. </p>
<dl class="image">
    <dt><img alt="" src="SQLScriptInTFS.png" /> </dt>
    <dd>Figure&#58; Give your SQL scripts to 'Schema Master' who will,&#160;check them into TFS, then run them </dd>
</dl>
<font class="ms-rteCustom-YellowBorderBox" size="+0">Note&#58; We have a tool called <a shape="rect" href="http&#58;//www.ssw.com.au/ssw/SQLDeploy/">SQL Deploy</a> to help with automatic deployment.</font> 



