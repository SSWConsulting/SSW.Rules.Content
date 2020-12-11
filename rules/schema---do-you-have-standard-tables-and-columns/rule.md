---
type: rule
archivedreason: 
title: Schema - Do you have standard Tables and Columns?
guid: 0a8b7eec-9b71-478b-b90e-6af7ac64df27
uri: schema---do-you-have-standard-tables-and-columns
created: 2019-11-05T22:52:15.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


​​1. All tables should have the following fields:<br><div><table cellspacing="0" width="100%" class="ssw15-rteTable-default"><tbody><tr><td class="ssw15-rteTable-default" style="width:50%;"><strong>Field</strong></td><td class="ssw15-rteTable-default" style="width:50%;"><strong>SQL Server Field Properties</strong></td></tr><tr><td class="ssw15-rteTable-default">CreatedUtc</td><td class="ssw15-rteTable-default">datetime2 Allow Nulls=False Default=GETUTCDATE()</td></tr><tr><td class="ssw15-rteTable-default">CreatedUserId</td><td class="ssw15-rteTable-default">Foreign Key to Users table, Allow Nulls=False</td></tr><tr><td class="ssw15-rteTable-default">ModifiedUtc</td><td class="ssw15-rteTable-default">datetime2 Allow Nulls=False Default=GETUTCDATE()</td></tr><tr><td class="ssw15-rteTable-default">ModifiedUserId</td><td class="ssw15-rteTable-default">Foreign Key to Users table, Allow Nulls=False</td></tr><tr><td class="ssw15-rteTable-default">Concurrency</td><td class="ssw15-rteTable-default">rowversion Allow Nulls=False<br></td></tr></tbody></table><br></div>
<br><excerpt class='endintro'></excerpt><br>
<p>​The first three are examples of bad table records. The last one is an example of how this table structure should be entered.<br>
</p><dl class="image"><dt><img src="imgGoodBadPracticesExampleSQLFields.png" alt="imgGoodBadPracticesExampleSQLFields.png" style="width:750px;height:121px;" /></dt><dd>Figure: 3 bad examples and 1 good example of Row auditing</dd></dl>​
<p>
   <b>Note #1:</b> Never set the CreatedUtc field - instead use a default GETUTCDATE()<br><b>Note #2:</b> These fields offer basic row auditing that will cover the majority of applications. When an application has specific auditing requirements, they should be analysed to see if this approach is sufficient.</p><p>2. All databases should have a table with one record to store application Defaults. This table should be called 'Control'.<br>If the settings are not application-wide, but just for that user then an XML (do not use an INI file) for simple stuff might be better. Examples are saving the 'User' for logon, 'Select Date Range' for a report, form positions, etc.</p><p>.NET programs have an Application.Configuration which exports to XML file (app.config) automatically. It works very well, and deployment is very simple. It's integrated right into the Visual Studio.NET designer as well.<br><br>3. All databases should have a version table to record structural changes to tables. See <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=dec3b0f2-a632-4842-ba6c-e8c7fb2ccf16">SSW Rules to Better Code​</a><br> <br>4. Lookup tables that have just two columns should be consistent and follow this convention: CategoryId (int) and CategoryName (varchar(100)).</p><p>The benefit is that a generic lookup form can be used. You will just need the generic lookup form pass in the TableName and Column1 and Column2.</p><p>
   <b>Note #3:</b> The problem with the naming is the primary keys don't match<br><b>Note #4:</b> The benefit with the character primary key columns is that queries and query strings have meaning Eg. http://www.ssw.com.au/ssw/Download/Download.aspx?GroupCategoryID=5BUS from this URL I can guess that it is in the business category.<br></p>


