---
type: rule
archivedreason: 
title: Do you understand a data type change = "Data Motion Scripts"?
guid: 72e85813-bbc1-4426-8108-4a5d7f559b7a
uri: do-you-understand-a-data-type-change-data-motion-scripts
created: 2009-10-07T00:12:39.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Martin Hinshelwood
  url: https://ssw.com.au/people/martin-hinshelwood
- title: Duncan Hunter
  url: https://ssw.com.au/people/duncan-hunter
- title: Brendan Richards
  url: https://ssw.com.au/people/brendan-richards
- title: Thiago Passos
  url: https://ssw.com.au/people/thiago-passos
related: []
redirects:
- do-you-understand-a-data-type-change-＂data-motion-scripts＂

---


Scripting out a schema change is easy, worrying about data is not. "'Data motion" refers to a change in the meaning of data, which will require scripts which touch data and schema. <br>
<br>
Let's look at an example: 

<br><excerpt class='endintro'></excerpt><br>
<p> We have a 'Gender' column (that is a Boolean) storing 0's and 1's. All works well for a while.</p><dl class="image"><dt> 
      <img src="TableBit.jpg" alt="" />
   </dt><dd>Figure: Anything wrong this Gender column?  </dd></dl> Later you learn you need to change the data type to char(2) to support 'M', 'F', 'T', 'NA' and 'U' 
<dl class="image"><dt> 
      <img src="CasterSemenya.jpg" alt="" />
   </dt><dd>Figure: Caster Semenya has taught us a thing or two about the right data type for Gender </dd></dl> The data then must be migrated to the new data type this way: 
<ol><li>Rename 'Gender' to 'ztGender' * </li><li>Add a new column 'Gender' with type char(2) </li><li>Insert the existing data from 'ztGender' to 'Gender' (map 0 to 'F' and 1 to 'M') </li><li>Delete the column ztGender* </li></ol> *Note: zt stands for Temporary 
<dl class="image"><dt> 
      <img src="TableChar.jpg" alt="" />
   </dt><dd>Figure: Changing the data type and data required a <a href="/Pages/DoYouHaveAnUnderstandingOfSchemaChangesAndTheirIncreasingComplexity.aspx" shape="rect">"Data Motion Script"</a> </dd></dl><p>Visual Studio does not automatically support this scenario, as data type changes are not part of the refactoring tools. However, if you add pre and post scripting events to handle the data type change the rest of the changes are automatically handled for you.</p><dl class="image"><dt>
      <img src="DataDude-BadExample.jpg" alt="" />
   </dt><dd>Figure: Don't use Data Dude</dd></dl><p>note: In order to achieve this you MUST use the built in Refactor tools as it create a log of all the refactors in order. This helps Visual Studio generate the schema compare and make sure no data is lost. </p><p>There are few options available to perform data type change correctly:</p><ol style="list-style-position:outside;"><ol><ol><li style="list-style-position:outside;"> 
            <strong>​​​​​Use manua​l scripts.</strong> All data type changes including data migration can be performed by writing scripts manualy. This way you have full control over the change. It is recommended to use 
            <a href="http://sqldeploy.com/">SQLDeploy</a> or 
            <a href="http://dbup.github.io/">DbUp</a> to automate script deployment and keep track of all database changes.​</li><li style="list-style-position:outside;"> 
            <strong>​Use Database Project.</strong> As mentioned above​, Visual Studio does not support data type changes out of the bo​x and should not be used to perform this kind of task. </li><li style="list-style-position:outside;">​​​​​​​​​<strong>Use Entity Framework (EF) Code First Migrations.</strong> If your application uses Entity Framework Code First, then it is strongly recommended to use Migrations feature.<br>​Using EF Code First Migrations is comparable to using one of the below combinations:<br>- ​<a href="http://dbup.github.io/">DBUp</a> + 
            <a href="https://www.nuget.org/packages/SSW.SqlVerify.EF/">SQL verify</a><br>- 
            <a href="https://technet.microsoft.com/en-us/library/ee210549%28v=sql.110%29.aspx">DAC Support For SQL Server Objects and Versions</a>  (.dacpac files)<br>- 
            <a href="http://sqldeploy.com/">SQL Deploy ​​​</a><br>​<br></li></ol></ol></ol><p class="ssw15-rteElement-CodeArea">public partial class GenderToString : DbMigration<br>    {<br>        public override void Up()<br>        {<br>            AlterColumn("dbo.Customers", "Gender", c =&gt; c.String(maxLength: 2));<br>        }<br>        
   <br>        public override void Down()<br>        {<br>            AlterColumn("dbo.Customers", "Gender", c =&gt; c.Boolean(nullable: false));<br>        }<br>    }</p><dd class="ssw15-rteElement-FigureBad">Bad Example - the default scaffolded migration will not perform any mapping of your data</dd><p> </p>
<p class="ssw15-rteElement-CodeArea">public partial class GenderToString : DbMigration<br> {<br> public override void Up()<br> {<br> AddColumn("dbo.Customers", "GenderTemp", c =&gt; c.Boolean(nullable: false));<br> Sql("UPDATE [dbo].[Customers] set GenderTemp = Gender");<br> DropColumn("dbo.Customers", "Gender");<br> AddColumn("dbo.Customers", "Gender", c =&gt; c.String(maxLength: 2));<br> Sql("UPDATE [dbo].[Customers] set Gender = 'M' where GenderTemp=1");<br> Sql("UPDATE [dbo].[Customers] set Gender = 'F' where GenderTemp=0");<br> DropColumn("dbo.Customers", "GenderTemp");<br> }</p><dd class="ssw15-rteElement-FigureGood">​Good Example - Data motion with EF Migrations<br></dd>


