---
type: rule
title: Do you ignore Idempotency?
uri: do-you-ignore-idempotency
created: 2009-10-05T06:03:28.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> This field should not be null (Remove me when you edit this field). </span>


  <p>Database scripts should be run in order (into separate sequential files),&#160;as per the rule&#160;<a shape="rect" href="http&#58;//www.ssw.com.au/ssw/standards/rules/rulestobettersqlserverdatabases.aspx#ScriptOutChanges">Do you script out all changes?</a><br>
<br>
Therefore developers should not worry about idempotency, as the script will run in the order it was created. Actually, if they are doing this, then <strong>*they want to see the errors*</strong>. It means that the database is not in the state that they expect.</p>
<font class="ms-rteCustom-CodeArea" size="+0">
<pre>IF EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES 
           WHERE TABLE_TYPE='BASE TABLE' AND  TABLE_NAME='Employees') 
    ALTER TABLE [dbo].[Employees]( …… ) ON [PRIMARY] 
ELSE 
    CREATE TABLE [dbo].[Employees]( …… ) ON [PRIMARY]
</pre>
</font><font class="ms-rteCustom-FigureBad" size="+0">Bad example – worrying about the idempotency&#160;should not be done, if you plan to run your scripts in the order they were created</font> <font class="ms-rteCustom-CodeArea" size="+0">
<pre>CREATE TABLE [dbo].[Employees](
    ……
) ON [PRIMARY]
</pre>
</font><font class="ms-rteCustom-FigureGood" size="+0">Good example – not worrying about the idempotency. If errors occur we don’t want them to be hidden + it is easier to read</font> See the concept of&#160;<span style="font-family&#58;'calibri','sans-serif';font-size&#58;11pt;"><a shape="rect" href="http&#58;//en.wikipedia.org/wiki/Idempotence"><span style="font-family&#58;'calibri','sans-serif';font-size&#58;11pt;">Idempotence on WikiPedia</span></a></span> 



