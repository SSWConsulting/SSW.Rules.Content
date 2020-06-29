---
type: rule
title: Do you configure your web applications to use application specific accounts for database access?
uri: do-you-configure-your-web-applications-to-use-application-specific-accounts-for-database-access
created: 2015-02-18T23:55:56.0000000Z
authors:
- id: 43
  title: Michael Demarco

---



<span class='intro'> <p>​​Do you configure your web applications to use application specific accounts for database access?&#160; </p><p>An application's database access profile should be as restricted as possible, so that in the case that it is compromised, the damage will be limited.&#160; </p><p>Application database access should be also be restricted to only the application's database, and none of the other databases on the server</p> </span>

<p> 
   <img alt="administratorlogininitsconnectionstring.png" src="administratorlogininitsconnectionstring.png" style="margin&#58;5px;width&#58;650px;" />&#160;</p><dd class="ssw15-rteElement-FigureBad">Bad Example – Contract Manager Web Application using the administrator login in its connection string&#160;</dd><p class="ssw15-rteElement-FigureBad"> 
   <strong><font color="#555555"></font></strong>&#160;</p><p class="ssw15-rteElement-FigureBad"> 
   <img alt="databaseuserconfiguredintheconnectionstring.png" src="databaseuserconfiguredintheconnectionstring.png" style="margin&#58;5px;width&#58;650px;" />&#160;</p><dd class="ssw15-rteElement-FigureGood">&#160; 
   <p>Good Example – Application specific database user configured in the connection string</p></dd><p>Most web applications need full read and write access to one database.&#160; In the case of EF Code first migrations, they might also need DDL admin rights.&#160; These roles are built in database roles&#58;</p><table width="100%" class="ssw15-rteTable-default" cellspacing="0"><tbody><tr><td class="ssw15-rteTable-default" style="width&#58;20%;"> 
            <strong>&#160;db_ddladmin</strong></td><td class="ssw15-rteTable-default" style="width&#58;80%;">Members of the&#160;<strong>db_ddladmin</strong>&#160;fixed database role can run any Data Definition Language (DDL) command in a database.</td></tr><tr><td class="ssw15-rteTable-default"> 
            <strong>&#160;db_datawriter</strong></td><td class="ssw15-rteTable-default">Members of the&#160;<strong>db_datawriter</strong>&#160;fixed database role can add, delete, or change data in all user tables.</td></tr><tr><td class="ssw15-rteTable-default"> 
            <strong>&#160;db_datareader</strong></td><td class="ssw15-rteTable-default">Members of the&#160;<strong>db_datareader&#160;</strong>fixed database role can read all data from all user tables.</td></tr></tbody></table><p> 
   <strong>Table&#58; Database roles taken from </strong>
   <a href="https&#58;//msdn.microsoft.com/en-us/library/ms189121.aspx">
      <span style="text-decoration&#58;underline;">
         <strong>Database-Level Roles</strong></span></a> 
</p><p>If you are running a web application on Azure as you should configure you application to use its own specific account that has some restrictions.&#160; The following script demonstrates setting up an sql user for myappstaging and another for myappproduction that also use EF code first migrations&#58;</p><blockquote><p>
      <font color="#0000ff" face="Consolas" size="2"><font color="#0000ff" face="Consolas" size="2"><font color="#0000ff" face="Consolas" size="2">USE</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font>
      <font color="#0000ff" face="Consolas" size="2">
         <font color="#0000ff" face="Consolas" size="2">
            <font color="#0000ff" face="Consolas" size="2">master</font></font></font></p>
   <font color="#0000ff" face="Consolas" size="2"><font color="#0000ff" face="Consolas" size="2"><font color="#0000ff" face="Consolas" size="2">
            <p>GO</p> </font></font></font>
   <font face="Consolas" size="2">
      <font color="#000000" face="Consolas" size="2"> </font></font>
   <font face="Consolas" size="2">
      <font face="Consolas" size="2">
         <font face="Consolas" size="2"></font></font></font>
   <p>
      <font color="#0000ff" face="Consolas" size="2">
         <font color="#0000ff" face="Consolas" size="2">
            <font color="#0000ff" face="Consolas" size="2">CREATE</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font>
      <font color="#0000ff" face="Consolas" size="2">
         <font color="#0000ff" face="Consolas" size="2">
            <font color="#0000ff" face="Consolas" size="2">LOGIN</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> myappstaging </font></font>
      <font color="#0000ff" face="Consolas" size="2">
         <font color="#0000ff" face="Consolas" size="2">
            <font color="#0000ff" face="Consolas" size="2">WITH</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font>
      <font color="#0000ff" face="Consolas" size="2">
         <font color="#0000ff" face="Consolas" size="2">
            <font color="#0000ff" face="Consolas" size="2">PASSWORD</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font>
      <font color="#808080" face="Consolas" size="2">
         <font color="#808080" face="Consolas" size="2">
            <font color="#808080" face="Consolas" size="2">=</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font>
      <font color="#ff0000" face="Consolas" size="2">
         <font color="#ff0000" face="Consolas" size="2">
            <font color="#ff0000" face="Consolas" size="2">'************'</font></font></font><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2">;</font></font></font></p>
   <font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"> </font></font></font>
   <font color="#0000ff" face="Consolas" size="2">
      <font color="#0000ff" face="Consolas" size="2">
         <font color="#0000ff" face="Consolas" size="2"></font></font></font>
   <p>
      <font color="#0000ff" face="Consolas" size="2">
         <font color="#0000ff" face="Consolas" size="2">
            <font color="#0000ff" face="Consolas" size="2">GO</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2">  </font></font></p>
   <font face="Consolas" size="2">
      <font face="Consolas" size="2"> </font></font>
   <font color="#0000ff" face="Consolas" size="2">
      <font color="#0000ff" face="Consolas" size="2">
         <font color="#0000ff" face="Consolas" size="2"></font></font></font>
   <p>
      <font color="#0000ff" face="Consolas" size="2">
         <font color="#0000ff" face="Consolas" size="2">
            <font color="#0000ff" face="Consolas" size="2">CREATE</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font>
      <font color="#0000ff" face="Consolas" size="2">
         <font color="#0000ff" face="Consolas" size="2">
            <font color="#0000ff" face="Consolas" size="2">USER</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> myappstaging </font></font>
      <font color="#0000ff" face="Consolas" size="2">
         <font color="#0000ff" face="Consolas" size="2">
            <font color="#0000ff" face="Consolas" size="2">FROM</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font>
      <font color="#0000ff" face="Consolas" size="2">
         <font color="#0000ff" face="Consolas" size="2">
            <font color="#0000ff" face="Consolas" size="2">LOGIN</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> myappstaging</font></font><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2">;</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font></p>
   <font face="Consolas" size="2">
      <font face="Consolas" size="2"> </font></font>
   <font color="#0000ff" face="Consolas" size="2">
      <font color="#0000ff" face="Consolas" size="2">
         <font color="#0000ff" face="Consolas" size="2"></font></font></font>
   <p>
      <font color="#0000ff" face="Consolas" size="2">
         <font color="#0000ff" face="Consolas" size="2">
            <font color="#0000ff" face="Consolas" size="2">GO</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2">  </font></font></p>
   <font face="Consolas" size="2">
      <font face="Consolas" size="2"> </font></font>
   <font color="#0000ff" face="Consolas" size="2">
      <font color="#0000ff" face="Consolas" size="2">
         <font color="#0000ff" face="Consolas" size="2"></font></font></font>
   <p>
      <font color="#0000ff" face="Consolas" size="2">
         <font color="#0000ff" face="Consolas" size="2">
            <font color="#0000ff" face="Consolas" size="2">USE</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> myapp</font></font><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2">-</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2">staging</font></font><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2">-</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2">db</font></font><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2">;</font></font></font></p>
   <font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"> </font></font></font>
   <font color="#0000ff" face="Consolas" size="2">
      <font color="#0000ff" face="Consolas" size="2">
         <font color="#0000ff" face="Consolas" size="2"></font></font></font>
   <p>
      <font color="#0000ff" face="Consolas" size="2">
         <font color="#0000ff" face="Consolas" size="2">
            <font color="#0000ff" face="Consolas" size="2">GO</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2">  </font></font></p>
   <font face="Consolas" size="2">
      <font face="Consolas" size="2"> </font></font>
   <font color="#0000ff" face="Consolas" size="2">
      <font color="#0000ff" face="Consolas" size="2">
         <font color="#0000ff" face="Consolas" size="2"></font></font></font>
   <p>
      <font color="#0000ff" face="Consolas" size="2">
         <font color="#0000ff" face="Consolas" size="2">
            <font color="#0000ff" face="Consolas" size="2">CREATE</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font>
      <font color="#0000ff" face="Consolas" size="2">
         <font color="#0000ff" face="Consolas" size="2">
            <font color="#0000ff" face="Consolas" size="2">USER</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> myappstaging </font></font>
      <font color="#0000ff" face="Consolas" size="2">
         <font color="#0000ff" face="Consolas" size="2">
            <font color="#0000ff" face="Consolas" size="2">FROM</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font>
      <font color="#0000ff" face="Consolas" size="2">
         <font color="#0000ff" face="Consolas" size="2">
            <font color="#0000ff" face="Consolas" size="2">LOGIN</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> myappstaging</font></font><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2">;</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font></p>
   <font face="Consolas" size="2">
      <font face="Consolas" size="2"> </font></font>
   <font color="#0000ff" face="Consolas" size="2">
      <font color="#0000ff" face="Consolas" size="2">
         <font color="#0000ff" face="Consolas" size="2">
            <p>GO</p> </font></font></font>
   <font face="Consolas" size="2">
      <font color="#000000" face="Consolas" size="2"> </font></font>
   <font face="Consolas" size="2">
      <font face="Consolas" size="2">
         <font face="Consolas" size="2"></font></font></font>
   <p>
      <font color="#0000ff" face="Consolas" size="2">
         <font color="#0000ff" face="Consolas" size="2">
            <font color="#0000ff" face="Consolas" size="2">EXEC</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font>
      <font color="#800000" face="Consolas" size="2">
         <font color="#800000" face="Consolas" size="2">
            <font color="#800000" face="Consolas" size="2">sp_addrolemember</font></font></font><font color="#0000ff" face="Consolas" size="2"><font color="#0000ff" face="Consolas" size="2"><font color="#0000ff" face="Consolas" size="2"> </font></font></font>
      <font color="#ff0000" face="Consolas" size="2">
         <font color="#ff0000" face="Consolas" size="2">
            <font color="#ff0000" face="Consolas" size="2">'db_datareader'</font></font></font><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2">,</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> myappstaging</font></font><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2">;</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font></p>
   <font face="Consolas" size="2">
      <font face="Consolas" size="2"> </font></font>
   <font color="#0000ff" face="Consolas" size="2">
      <font color="#0000ff" face="Consolas" size="2">
         <font color="#0000ff" face="Consolas" size="2"></font></font></font>
   <p>
      <font color="#0000ff" face="Consolas" size="2">
         <font color="#0000ff" face="Consolas" size="2">
            <font color="#0000ff" face="Consolas" size="2">EXEC</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font>
      <font color="#800000" face="Consolas" size="2">
         <font color="#800000" face="Consolas" size="2">
            <font color="#800000" face="Consolas" size="2">sp_addrolemember</font></font></font><font color="#0000ff" face="Consolas" size="2"><font color="#0000ff" face="Consolas" size="2"><font color="#0000ff" face="Consolas" size="2"> </font></font></font>
      <font color="#ff0000" face="Consolas" size="2">
         <font color="#ff0000" face="Consolas" size="2">
            <font color="#ff0000" face="Consolas" size="2">'db_datawriter'</font></font></font><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2">,</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> myappstaging</font></font><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2">;</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font></p>
   <font face="Consolas" size="2">
      <font face="Consolas" size="2"> </font></font>
   <font color="#0000ff" face="Consolas" size="2">
      <font color="#0000ff" face="Consolas" size="2">
         <font color="#0000ff" face="Consolas" size="2"></font></font></font>
   <p>
      <font color="#0000ff" face="Consolas" size="2">
         <font color="#0000ff" face="Consolas" size="2">
            <font color="#0000ff" face="Consolas" size="2">EXEC</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font>
      <font color="#800000" face="Consolas" size="2">
         <font color="#800000" face="Consolas" size="2">
            <font color="#800000" face="Consolas" size="2">sp_addrolemember</font></font></font><font color="#0000ff" face="Consolas" size="2"><font color="#0000ff" face="Consolas" size="2"><font color="#0000ff" face="Consolas" size="2"> </font></font></font>
      <font color="#ff0000" face="Consolas" size="2">
         <font color="#ff0000" face="Consolas" size="2">
            <font color="#ff0000" face="Consolas" size="2">'db_ddladmin'</font></font></font><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2">,</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> myappstaging</font></font><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2">;</font></font></font></p>
   <font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"> </font></font></font>
   <font face="Consolas" size="2">
      <font face="Consolas" size="2"></font></font></blockquote><p>
 <strong>Script&#58; Example script to create a service user for myappstaging</strong></p><p><strong>Note&#58; If you are using stored procedures, you will also need to grant execute permissions to the user.&#160; E.g.&#58;</strong></p><blockquote dir="ltr" style="margin-right&#58;0px;"><p><font color="#0000ff" face="Consolas" size="2"><font color="#0000ff" face="Consolas" size="2"><font color="#0000ff" face="Consolas" size="2">GRANT</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font><font color="#0000ff" face="Consolas" size="2"><font color="#0000ff" face="Consolas" size="2"><font color="#0000ff" face="Consolas" size="2">EXECUTE</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font><font color="#0000ff" face="Consolas" size="2"><font color="#0000ff" face="Consolas" size="2"><font color="#0000ff" face="Consolas" size="2">TO</font></font></font><font face="Consolas" size="2"><font face="Consolas" size="2"> </font></font><font face="Consolas" size="2">myappstaging</font><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"><font color="#808080" face="Consolas" size="2"></font></font></font></p></blockquote><p class="ssw15-rteElement-GreyBox">Data Source=tcp&#58;xyzsqlserver.database.windows.net,1433; Initial Catalog=myapp-staging-db; User <a href="mailto&#58;ID=myappstaging@xyzsqlserver">ID=myappstaging@xyzsqlserver</a>; Password='*************'&#160;</p><p>​<strong>Figure&#58; Example connection string</strong></p>


