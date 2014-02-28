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

<p>&#160;We have a 'Gender' column (that is a Boolean) storing 0's and 1's. All works well for a while.</p><dl class="image"><dt>
      <img src="/SoftwareDevelopment/RulesToBetterSQLServerSchemaDeployment/PublishingImages/TableBit.jpg" alt="" /> 
   </dt><dd>Figure&#58; Anything wrong this Gender column?&#160; </dd></dl> Later you learn you need to change the data type to char(2) to support 'M', 'F', 'T', 'NA' and 'U' 
<dl class="image"><dt>
      <img src="/SoftwareDevelopment/RulesToBetterSQLServerSchemaDeployment/PublishingImages/CasterSemenya.jpg" alt="" /> 
   </dt><dd>Figure&#58; Caster Semenya has taught us a thing or two about the right data type for Gender </dd></dl> The data then must be migrated to the new data type this way&#58; 
<ol><li>Rename 'Gender' to 'ztGender' * </li><li>Add a new column 'Gender' with type char(2) </li><li>Insert the existing data from 'ztGender' to 'Gender' (map 0 to 'F' and 1 to 'M') </li><li>Delete the column ztGender* </li></ol> *Note&#58; zt stands for Temporary 
<dl class="image"><dt>
      <img src="/SoftwareDevelopment/RulesToBetterSQLServerSchemaDeployment/PublishingImages/TableChar.jpg" alt="" /> 
   </dt><dd>Figure&#58; Changing the data type and data required a&#160;<a href="/SoftwareDevelopment/RulesToBetterSQLServerSchemaDeployment/Pages/DoYouHaveAnUnderstandingOfSchemaChangesAndTheirIncreasingComplexity.aspx" shape="rect">&quot;Data Motion Script&quot;</a> </dd></dl><p>Visual Studio&#160;does not automatically support this scenario, as data type changes are not part of the refactoring tools. However, if you add pre and post scripting events to handle the data type change the rest of the changes are automatically handled for you.</p> 
<img src="/SoftwareDevelopment/RulesToBetterSQLServerSchemaDeployment/PublishingImages/DataDude-BadExample.jpg" alt="" />
<br> 
<font class="ms-rteCustom-FigureGood" size="+0">Good Example - Don't use Data Dude<br> </font>
<p>note&#58; In order to achieve this you MUST use the built in Refactor tools as it create a log of all the refactors in order. This helps Visual Studio generate the schema compare and make sure no data is lost. </p><p>There are few options available to perform data type change correctly&#58;</p> 
<ol style="list-style-position&#58;outside;">
   <li>
      <strong>Use manua​l scripts.</strong> All data type changes including data migration can be performed by writing scripts manualy. This way you have full control over the change. It is recommended to use SQLDeploy or DbUp to automate script deployment and keep track of all database changes.</li><li>
      <strong>Use Database Project.</strong> As mentioned above​, Visual Studio does not support data type changes out of the bo​x and should not be used to perform this kind of task.&#160;</li><li>
      <strong>Use&#160;Entity Framework Code First Migrations.</strong> If your application uses Entity Framework&#160;Code First, then it is strongly recommended to use Migrations feature.​</li></ol><p class="ssw15-rteElement-CodeArea">public partial class GenderToString &#58; DbMigration<br>&#160;&#160;&#160; &#123;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; public override void Up()<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#123;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; AlterColumn(&quot;dbo.Customers&quot;, &quot;Gender&quot;, c =&gt; c.String(maxLength&#58; 2));<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#125;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; 
   <br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; public override void Down()<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#123;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; AlterColumn(&quot;dbo.Customers&quot;, &quot;Gender&quot;, c =&gt; c.Boolean(nullable&#58; false));<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#125;<br>&#160;&#160;&#160; &#125;</p><dd class="ssw15-rteElement-FigureBad">Bad&#160;Example - the default scaffolded migration will not perform any mapping of your data</dd><p>&#160;</p><p class="ssw15-rteElement-CodeArea">public partial class GenderToString &#58; DbMigration<br> &#123;<br> public override void Up()<br> &#123;<br> AddColumn(&quot;dbo.Customers&quot;, &quot;GenderTemp&quot;, c =&gt; c.Boolean(nullable&#58; false));<br> Sql(&quot;UPDATE [dbo].[Customers] set GenderTemp = Gender&quot;);<br> DropColumn(&quot;dbo.Customers&quot;, &quot;Gender&quot;);<br> AddColumn(&quot;dbo.Customers&quot;, &quot;Gender&quot;, c =&gt; c.String(maxLength&#58; 2));<br> Sql(&quot;UPDATE [dbo].[Customers] set Gender = 'M' where GenderTemp=1&quot;);<br> Sql(&quot;UPDATE [dbo].[Customers] set Gender = 'F' where GenderTemp=0&quot;);<br> DropColumn(&quot;dbo.Customers&quot;, &quot;GenderTemp&quot;);<br> &#125;</p>​​​ 
<dd class="ssw15-rteElement-FigureGood">​Good Example - Data motion with EF Migrations</dd>


