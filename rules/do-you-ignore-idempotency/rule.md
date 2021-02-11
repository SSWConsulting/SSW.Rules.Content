---
type: rule
archivedreason: 
title: Do you ignore Idempotency?
guid: 03c90188-ef1c-4ecf-a58f-32f1a331de42
uri: do-you-ignore-idempotency
created: 2009-10-05T06:03:28.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

Many developers worry about Idempotency. They make sure that their scripts can run multiple times without it affecting the database, upon subsequent running of the script.

This usually involves a check at the start to see if the object exists or not. 
 eg. If this table exists, then don't create the table.

 Seems popular, seems like a good idea, right?  Wrong! And here is why.

<!--endintro-->

Database scripts should be run in order (into separate sequential files), as per the rule [Do you script out all changes?](http://www.ssw.com.au/ssw/standards/rules/rulestobettersqlserverdatabases.aspx#ScriptOutChanges)

 Therefore developers should not worry about idempotency, as the script will run in the order it was created. Actually, if they are doing this, then  **\*they want to see the errors\*** . It means that the database is not in the state that they expect.



```
IF EXISTS (SELECT 1 FROM 
               INFORMATION_SCHEMA.TABLES 
           WHERE 
               TABLE_TYPE='BASE TABLE' AND 
               TABLE_NAME='Employees'
           ) 
    ALTER TABLE [dbo].[Employees]( …… ) ON [PRIMARY] 
ELSE 
    CREATE TABLE [dbo].[Employees]( …… ) ON [PRIMARY]
```




::: bad
Bad example – worrying about the idempotency should not be done, if you plan to run your scripts in the order they were created  
:::
 


```
CREATE TABLE [dbo].[Employees](
    ……
) ON [PRIMARY]
```




::: good
Good example – not worrying about the idempotency. If errors occur we don’t want them to be hidden + it is easier to read  
:::


![Figure: Viagra isn't the cure to your Idempotency problems](ViagraPill.jpg)  
       See the concept of [Idempotence on WikiPedia](http://en.wikipedia.org/wiki/Idempotence)
