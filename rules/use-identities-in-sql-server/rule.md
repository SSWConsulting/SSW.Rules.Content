---
type: rule
archivedreason: 
title: Data - Do you use Identities in SQL Server?
guid: fdf8110f-4d46-4459-b97c-a825bab3efed
uri: use-identities-in-sql-server
created: 2019-11-25T19:08:06.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- data-do-you-use-identities-in-sql-server

---


<p class="ssw15-rteElement-P">​​​​This one is going to be a controversial one. But the bottom line is every now and then you want to do something and then you curse and wish your database didn't have&#160;identities. So why use them? Let's look at the problems first&#58;​​​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<dd class="ssw15-rteElement-FigureBad">​Con​s&#58;</dd><ul><li>You can't manually change a Primary Key and let the Cascade Update do its work, eg. an InvoiceID</li><li>Hassles when importing data into related tables where you want to control the Primary Key eg. Order and Order Details</li><li>Replication you will get conflicts</li></ul><p>​In Microsoft Access you have autonumbers and there is no way around them so never use them.<br>But in SQL Server you have identities and we have these procs&#58;<br></p><ul><li>DBCC CHECKIDENT - Checks the current identity value for the specified table and, if needed, corrects the identity value</li><li>SET IDENTITY_INSERT &#123; table &#125; &#123; ON | OFF &#125; - Allows explicit values to be inserted into the identity column of a table</li></ul><dd class="ssw15-rteElement-FigureGood">Pros&#58;​​<br></dd><ul><li>Less programming - letting the database take care of it</li><li>Replication (identities are supported by SQL Server with ranges so when you want replication, no coding</li><li>Avoiding concurrency errors on high INSERT systems so no coding</li></ul><p>So the only Con left is the importing of data but we can use one of the above procs to get around it. See grey box.</p><h3 class="ssw15-rteElement-H3">The best way to import messy data into SQL Server (with Identities)​<br></h3><p>Eg. inserting data to the Orders and Orders Details table&#58;<br></p><p class="ssw15-rteElement-CodeArea">​Use an .adp to copy the first record to Excel<br>Get the data into the same column orders<br>--<br>SET IDENTITY_INSERT Orders ON --this will allow manual identity INSERTS<br>Copy and Paste Append the Orders<br>SET IDENTITY_INSERT Orders OFF --as it can only be on for one table at a time<br>--<br>SET IDENTITY_INSERT [Order Details] ON --this will allow manual identity INSERTS<br>Copy and Paste Append the [Order Details]<br>SET IDENTITY_INSERT [Order Details] OFF​​<br></p><h3 class="ssw15-rteElement-H3">Automatic Identity Range Handling​<br></h3><p>The simplest way of handling identity ranges across replicas is to allow SQL Server 2000 to manage identity range handling for you. To use automatic identity range handling, you must first enable the feature at the time the publication is created, assign a set of initial Publisher and Subscriber identity range values, and then assign a threshold value that determines when a new identity range is created.<br>For example, assigning an identity range from 1000 through 2000 to a Publisher, and a range from 2001 through 3000 to an initial Subscriber a range from 3001 to 4000 to the next publisher etc.​<br></p>


