---
type: rule
archivedreason: 
title: Do you know how to use Connection String in .NET 2.0?
guid: 2dec2ea4-3359-4bb0-8f30-c278c8735670
uri: do-you-know-how-to-use-connection-string-in-net-20
created: 2009-05-08T08:53:04.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 17
  title: Ryan Tee
related: []

---

In .NET 1.1 we used to store our connection string in a configuration file like this:   
<!--endintro-->


<dl class="goodCode">    <dt style="width:92.01%;height:134px;">
    <pre><configuration><br>     <appsettings><br>          <add key="ConnectionString" value="integrated security=true;<br>           data source=(local);initial catalog=Northwind"></add><br>     </appsettings><br></configuration></pre>
    &lt;/dt&gt;
</dt></dl>
and access this connection string in code like this:
<dl class="badCode">    <dt style="width:92.01%;height:74px;">
    <pre>SqlConnection sqlConn = <br>new SqlConnection(System.Configuration.ConfigurationSettings.<br>AppSettings["ConnectionString"]);                        </pre>
    &lt;/dt&gt;
    <dd>Bad example - old ASP.NET 1.1 way, untyped and prone to error. </dd></dl>
In .NET 2.0 you can access it in another way

Step 1: Setup your settings in your common project. E.g. Northwind.Common
<dl class="image">    &lt;dt&gt;<img style="border-bottom:0px solid;border-left:0px solid;border-top:0px solid;border-right:0px solid;" border="0" alt="Settings in Project Properties" src="ConnStringNET2_Settings.jpg"> &lt;/dt&gt;
    <dd>Figure: Settings in Project Properties</dd></dl>
Step 2: Open up the generated App.config under your common project. E.g. Northwind.Common/App.config
<dl class="image">    &lt;dt&gt;<img style="border-bottom:0px solid;border-left:0px solid;border-top:0px solid;border-right:0px solid;" border="0" alt="Auto generated app.config" src="ConnStringNET2_CommonApp.GIF"> &lt;/dt&gt;
    <dd>Figure: Auto generated app.config</dd></dl>
Step 3: ~~Copy the content into your entry applications app.config. E.g. Northwind.WindowsUI/App.config~~ The new setting has been updated to app.config automatically in .NET 2.0
<dl class="badCode">    <dt style="width:92.31%;height:184px;">
    <pre> <configuration><br>      <connectionstrings><br>         <add name="Common.Properties.Settings.NorthwindConnectionString"></add><br>              connectionString="Data Source=(local);Initial Catalog=Northwind;<br>              Integrated Security=True"<br>              providerName="System.Data.SqlClient" /><br>        </connectionstrings><br> </configuration>                        </pre>
    &lt;/dt&gt;
</dt></dl>
Then you can access the connection string like this in C#
<dl class="goodCode">    <dt style="width:93.36%;height:59px;">
    <pre>SqlConnection sqlConn =<br> new SqlConnection(Common.Properties.Settings.Default.NorthwindConnectionString);                                </pre>
    &lt;/dt&gt;
    <dd>Good example - access our connection string by strongly typed generated settings class. </dd></dl>

::: greybox

Please note these steps does not work for web site model in Visual Studio 2005. However, they work for other projects such as Windows Form, Console application, Class Library and Web Application Project.

This is not an issue in a well designed website, since it's connection string will be defined in the  **data layer** and you can overwrite this connection string in your web.config.

:::
