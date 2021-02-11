---
type: rule
archivedreason: 
title: Do you configure your web applications to use application specific accounts for database access?
guid: 7a886ddf-5a56-48cb-89bd-3b47fd90e329
uri: do-you-configure-your-web-applications-to-use-application-specific-accounts-for-database-access
created: 2015-02-18T23:55:56.0000000Z
authors:
- title: Michael Demarco
  url: https://ssw.com.au/people/michael-demarco
related: []
redirects: []

---

Do you configure your web applications to use application specific accounts for database access?

An application's database access profile should be as restricted as possible, so that in the case that it is compromised, the damage will be limited.

Application database access should be also be restricted to only the application's database, and none of the other databases on the server

<!--endintro-->

![](administratorlogininitsconnectionstring.png)


::: bad
Bad Example – Contract Manager Web Application using the administrator login in its connection string  
:::

**<font color="#555555"></font>**

![](databaseuserconfiguredintheconnectionstring.png)


::: good

Good Example – Application specific database user configured in the connection string

:::

Most web applications need full read and write access to one database.  In the case of EF Code first migrations, they might also need DDL admin rights.  These roles are built in database roles:


| **db\_ddladmin**  | Members of the  **db\_ddladmin** fixed database role can run any Data Definition Language (DDL) command in a database. |
| --- | --- |
| **db\_datawriter**  | Members of the  **db\_datawriter** fixed database role can add, delete, or change data in all user tables. |
| **db\_datareader**  | Members of the  **db\_datareader** fixed database role can read all data from all user tables. |


**Table: Database roles taken from** [**Database-Level Roles**](https://msdn.microsoft.com/en-us/library/ms189121.aspx)

If you are running a web application on Azure as you should configure you application to use its own specific account that has some restrictions.  The following script demonstrates setting up an sql user for myappstaging and another for myappproduction that also use EF code first migrations:


> <font color="#0000ff" face="Consolas" size="2"><font color="#0000ff" face="Consolas" size="2"><font color="#0000ff" face="Consolas" size="2">USE</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font><font color="#0000ff" face="Consolas" size="2">         <font color="#0000ff" face="Consolas" size="2">
>             <font color="#0000ff" face="Consolas" size="2">master</font></font></font>
> <font color="#0000ff" face="Consolas" size="2"><font color="#0000ff" face="Consolas" size="2"><font color="#0000ff" face="Consolas" size="2">
>             <p>GO</p> </font></font></font><font face="Consolas" size="2">      <font color="#000000" face="Consolas" size="2"> </font></font><font face="Consolas" size="2">      <font face="Consolas" size="2">
>          <font face="Consolas" size="2"></font></font></font>
> <font color="#0000ff" face="Consolas" size="2">         <font color="#0000ff" face="Consolas" size="2">
>             <font color="#0000ff" face="Consolas" size="2">CREATE</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font><font color="#0000ff" face="Consolas" size="2">         <font color="#0000ff" face="Consolas" size="2">
>             <font color="#0000ff" face="Consolas" size="2">LOGIN</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> myappstaging </font></font><font color="#0000ff" face="Consolas" size="2">         <font color="#0000ff" face="Consolas" size="2">
>             <font color="#0000ff" face="Consolas" size="2">WITH</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font><font color="#0000ff" face="Consolas" size="2">         <font color="#0000ff" face="Consolas" size="2">
>             <font color="#0000ff" face="Consolas" size="2">PASSWORD</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font><font color="#808080" face="Consolas" size="2">         <font color="#808080" face="Consolas" size="2">
>             <font color="#808080" face="Consolas" size="2">=</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font><font color="#ff0000" face="Consolas" size="2">         <font color="#ff0000" face="Consolas" size="2">
>             <font color="#ff0000" face="Consolas" size="2">'************'</font></font></font><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2">;</font></font></font>
> <font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"> </font></font></font><font color="#0000ff" face="Consolas" size="2">      <font color="#0000ff" face="Consolas" size="2">
>          <font color="#0000ff" face="Consolas" size="2"></font></font></font>
> <font color="#0000ff" face="Consolas" size="2">         <font color="#0000ff" face="Consolas" size="2">
>             <font color="#0000ff" face="Consolas" size="2">GO</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2">  </font></font>
> <font face="Consolas" size="2">      <font face="Consolas" size="2"> </font></font><font color="#0000ff" face="Consolas" size="2">      <font color="#0000ff" face="Consolas" size="2">
>          <font color="#0000ff" face="Consolas" size="2"></font></font></font>
> <font color="#0000ff" face="Consolas" size="2">         <font color="#0000ff" face="Consolas" size="2">
>             <font color="#0000ff" face="Consolas" size="2">CREATE</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font><font color="#0000ff" face="Consolas" size="2">         <font color="#0000ff" face="Consolas" size="2">
>             <font color="#0000ff" face="Consolas" size="2">USER</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> myappstaging </font></font><font color="#0000ff" face="Consolas" size="2">         <font color="#0000ff" face="Consolas" size="2">
>             <font color="#0000ff" face="Consolas" size="2">FROM</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font><font color="#0000ff" face="Consolas" size="2">         <font color="#0000ff" face="Consolas" size="2">
>             <font color="#0000ff" face="Consolas" size="2">LOGIN</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> myappstaging</font></font><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2">;</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font>
> <font face="Consolas" size="2">      <font face="Consolas" size="2"> </font></font><font color="#0000ff" face="Consolas" size="2">      <font color="#0000ff" face="Consolas" size="2">
>          <font color="#0000ff" face="Consolas" size="2"></font></font></font>
> <font color="#0000ff" face="Consolas" size="2">         <font color="#0000ff" face="Consolas" size="2">
>             <font color="#0000ff" face="Consolas" size="2">GO</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2">  </font></font>
> <font face="Consolas" size="2">      <font face="Consolas" size="2"> </font></font><font color="#0000ff" face="Consolas" size="2">      <font color="#0000ff" face="Consolas" size="2">
>          <font color="#0000ff" face="Consolas" size="2"></font></font></font>
> <font color="#0000ff" face="Consolas" size="2">         <font color="#0000ff" face="Consolas" size="2">
>             <font color="#0000ff" face="Consolas" size="2">USE</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> myapp</font></font><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2">-</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2">staging</font></font><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2">-</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2">db</font></font><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2">;</font></font></font>
> <font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"> </font></font></font><font color="#0000ff" face="Consolas" size="2">      <font color="#0000ff" face="Consolas" size="2">
>          <font color="#0000ff" face="Consolas" size="2"></font></font></font>
> <font color="#0000ff" face="Consolas" size="2">         <font color="#0000ff" face="Consolas" size="2">
>             <font color="#0000ff" face="Consolas" size="2">GO</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2">  </font></font>
> <font face="Consolas" size="2">      <font face="Consolas" size="2"> </font></font><font color="#0000ff" face="Consolas" size="2">      <font color="#0000ff" face="Consolas" size="2">
>          <font color="#0000ff" face="Consolas" size="2"></font></font></font>
> <font color="#0000ff" face="Consolas" size="2">         <font color="#0000ff" face="Consolas" size="2">
>             <font color="#0000ff" face="Consolas" size="2">CREATE</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font><font color="#0000ff" face="Consolas" size="2">         <font color="#0000ff" face="Consolas" size="2">
>             <font color="#0000ff" face="Consolas" size="2">USER</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> myappstaging </font></font><font color="#0000ff" face="Consolas" size="2">         <font color="#0000ff" face="Consolas" size="2">
>             <font color="#0000ff" face="Consolas" size="2">FROM</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font><font color="#0000ff" face="Consolas" size="2">         <font color="#0000ff" face="Consolas" size="2">
>             <font color="#0000ff" face="Consolas" size="2">LOGIN</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> myappstaging</font></font><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2">;</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font>
> <font face="Consolas" size="2">      <font face="Consolas" size="2"> </font></font><font color="#0000ff" face="Consolas" size="2">      <font color="#0000ff" face="Consolas" size="2">
>          <font color="#0000ff" face="Consolas" size="2">
>             <p>GO</p> </font></font></font><font face="Consolas" size="2">      <font color="#000000" face="Consolas" size="2"> </font></font><font face="Consolas" size="2">      <font face="Consolas" size="2">
>          <font face="Consolas" size="2"></font></font></font>
> <font color="#0000ff" face="Consolas" size="2">         <font color="#0000ff" face="Consolas" size="2">
>             <font color="#0000ff" face="Consolas" size="2">EXEC</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font><font color="#800000" face="Consolas" size="2">         <font color="#800000" face="Consolas" size="2">
>             <font color="#800000" face="Consolas" size="2">sp_addrolemember</font></font></font><font color="#0000ff" face="Consolas" size="2"><font color="#0000ff" face="Consolas" size="2"><font color="#0000ff" face="Consolas" size="2"> </font></font></font><font color="#ff0000" face="Consolas" size="2">         <font color="#ff0000" face="Consolas" size="2">
>             <font color="#ff0000" face="Consolas" size="2">'db_datareader'</font></font></font><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2">,</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> myappstaging</font></font><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2">;</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font>
> <font face="Consolas" size="2">      <font face="Consolas" size="2"> </font></font><font color="#0000ff" face="Consolas" size="2">      <font color="#0000ff" face="Consolas" size="2">
>          <font color="#0000ff" face="Consolas" size="2"></font></font></font>
> <font color="#0000ff" face="Consolas" size="2">         <font color="#0000ff" face="Consolas" size="2">
>             <font color="#0000ff" face="Consolas" size="2">EXEC</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font><font color="#800000" face="Consolas" size="2">         <font color="#800000" face="Consolas" size="2">
>             <font color="#800000" face="Consolas" size="2">sp_addrolemember</font></font></font><font color="#0000ff" face="Consolas" size="2"><font color="#0000ff" face="Consolas" size="2"><font color="#0000ff" face="Consolas" size="2"> </font></font></font><font color="#ff0000" face="Consolas" size="2">         <font color="#ff0000" face="Consolas" size="2">
>             <font color="#ff0000" face="Consolas" size="2">'db_datawriter'</font></font></font><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2">,</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> myappstaging</font></font><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2">;</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font>
> <font face="Consolas" size="2">      <font face="Consolas" size="2"> </font></font><font color="#0000ff" face="Consolas" size="2">      <font color="#0000ff" face="Consolas" size="2">
>          <font color="#0000ff" face="Consolas" size="2"></font></font></font>
> <font color="#0000ff" face="Consolas" size="2">         <font color="#0000ff" face="Consolas" size="2">
>             <font color="#0000ff" face="Consolas" size="2">EXEC</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font><font color="#800000" face="Consolas" size="2">         <font color="#800000" face="Consolas" size="2">
>             <font color="#800000" face="Consolas" size="2">sp_addrolemember</font></font></font><font color="#0000ff" face="Consolas" size="2"><font color="#0000ff" face="Consolas" size="2"><font color="#0000ff" face="Consolas" size="2"> </font></font></font><font color="#ff0000" face="Consolas" size="2">         <font color="#ff0000" face="Consolas" size="2">
>             <font color="#ff0000" face="Consolas" size="2">'db_ddladmin'</font></font></font><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2">,</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> myappstaging</font></font><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2">;</font></font></font>
> <font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"> </font></font></font><font face="Consolas" size="2">      <font face="Consolas" size="2"></font></font>


**Script: Example script to create a service user for myappstaging**

**Note: If you are using stored procedures, you will also need to grant execute permissions to the user.  E.g.:**


> <font color="#0000ff" face="Consolas" size="2"><font color="#0000ff" face="Consolas" size="2"><font color="#0000ff" face="Consolas" size="2">GRANT</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font><font color="#0000ff" face="Consolas" size="2"><font color="#0000ff" face="Consolas" size="2"><font color="#0000ff" face="Consolas" size="2">EXECUTE</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font><font color="#0000ff" face="Consolas" size="2"><font color="#0000ff" face="Consolas" size="2"><font color="#0000ff" face="Consolas" size="2">TO</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font><font face="Consolas" size="2">myappstaging</font><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"></font></font></font>



::: greybox
Data Source=tcp:xyzsqlserver.database.windows.net,1433; Initial Catalog=myapp-staging-db; User ID=myappstaging@xyzsqlserver; Password='\*\*\*\*\*\*\*\*\*\*\*\*\*'  
:::

**Figure: Example connection string**
