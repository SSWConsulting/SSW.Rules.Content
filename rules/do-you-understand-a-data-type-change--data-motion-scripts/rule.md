---
type: rule
title: Do you understand a data type change = "Data Motion Scripts"?
uri: do-you-understand-a-data-type-change--data-motion-scripts
created: 2009-10-07T00:12:39.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 14
  title: Martin Hinshelwood
- id: 44
  title: Duncan Hunter
- id: 34
  title: Brendan Richards
- id: 53
  title: Thiago Passos

---



<span class='intro'> Scripting out a schema change&#160;is easy, worrying about data is not. &quot;'Data motion&quot; refers to a change in the meaning of data, which will require scripts which touch data and schema. <br>
<br>
Let's look at an example&#58; 
 </span>


  <p>&#160;We have a 'Gender' column (that is a Boolean) storing 0's and 1's. All works well for a while.</p>
<dl class="image">
    <dt><img alt="" src="/Standards/SoftwareDevelopment/RulesToBetterSQLServerSchemaDeployment/PublishingImages/TableBit.jpg" /> </dt>
    <dd>Figure&#58; Anything wrong this Gender column?&#160; </dd>
</dl>
Later you learn you need to change the data type to char(2) to support 'M', 'F', 'T', 'NA' and 'U'
<dl class="image">
    <dt><img alt="" src="/Standards/SoftwareDevelopment/RulesToBetterSQLServerSchemaDeployment/PublishingImages/CasterSemenya.jpg" /> </dt>
    <dd>Figure&#58; Caster Semenya has taught us a thing or two about the right data type for Gender </dd>
</dl>
The data then must be migrated to the new data type this way&#58;
<ol>
    <li>Rename 'Gender' to 'ztGender' * </li>
    <li>Add a new column 'Gender' with type char(2) </li>
    <li>Insert the existing data from 'ztGender' to 'Gender' (map 0 to 'F' and 1 to 'M') </li>
    <li>Delete the column ztGender* </li>
</ol>
*Note&#58; zt stands for Temporary
<dl class="image">
    <dt><img alt="" src="/Standards/SoftwareDevelopment/RulesToBetterSQLServerSchemaDeployment/PublishingImages/TableChar.jpg" /> </dt>
    <dd>Figure&#58; Changing the data type and data required a&#160;<a shape="rect" href="/Standards/SoftwareDevelopment/RulesToBetterSQLServerSchemaDeployment/Pages/DoYouHaveAnUnderstandingOfSchemaChangesAndTheirIncreasingComplexity.aspx">&quot;Data Motion Script&quot;</a> </dd>
</dl>
<p>Visual Studio&#160;does not automatically support this scenario, as data type changes are not part of the refactoring tools. However, if you add pre and post scripting events to handle the data type change the rest of the changes are automatically handled for you.</p>
<img alt="" src="/Standards/SoftwareDevelopment/RulesToBetterSQLServerSchemaDeployment/PublishingImages/DataDude-BadExample.jpg" /><br>
&#160;<font class="ms-rteCustom-FigureGood" size="+0">Bad Example - Don't use Data Dude<br>
</font>note&#58; In order to achieve this you MUST use the built in Refactor tools as it create a log of all the refactors in order. This helps Visual Studio generate the schema compare and make sure no data is lost.



