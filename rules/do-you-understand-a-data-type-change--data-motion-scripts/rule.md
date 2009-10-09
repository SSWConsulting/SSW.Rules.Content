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


  <p>We have a 'Gender' column (that is a Boolean) storing 0's and 1's. All works well for a while.</p>
<dl class="image">
    <dt><img alt="" src="/Standards/SoftwareDevelopment/RulesToBetterSQLServerSchemaDeployment/PublishingImages/TableBit.jpg" /> </dt>
    <dd>Figure&#58; Anything wrong this Gender column?&#160; </dd>
</dl>
Later you learn you need to change the data type to char(2) to support 'M', 'F', 'T', 'NA' and 'U'
<dl class="image">
    <dt><img alt="" src="/Standards/SoftwareDevelopment/RulesToBetterSQLServerSchemaDeployment/PublishingImages/CasterSemenya.jpg" /> </dt>
    <dd>Figure&#58; Caster Semenya has taught us a thing or two about the right data type for Gender </dd>
</dl>
<br>
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
    <dd>Figure&#58; Changing the data type and data required a&#160;<a href="/Standards/SoftwareDevelopment/RulesToBetterSQLServerSchemaDeployment/Pages/DoYouHaveAnUnderstandingOfSchemaChangesAndTheirIncreasingComplexity.aspx">&quot;Data Motion Script&quot;</a></dd>
</dl>



