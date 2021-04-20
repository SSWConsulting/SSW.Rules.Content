---
type: rule
archivedreason: .NET 2.0 is deprecated
title: Do you know how to use Connection String in .NET 2.0?
guid: 2dec2ea4-3359-4bb0-8f30-c278c8735670
uri: do-you-know-how-to-use-connection-string-in-net-2-0
created: 2009-05-08T08:53:04.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ryan Tee
  url: https://ssw.com.au/people/ryan-tee
related: []
redirects: []

---

In .NET 1.1 we used to store our connection string in a configuration file like this:   
<!--endintro-->




```
<configuration>
     <appSettings>
          <add key="ConnectionString" value ="integrated security=true;
           data source=(local);initial catalog=Northwind"/>
     </appSettings>
</configuration>
```


and access this connection string in code like this:


```
SqlConnection sqlConn = 
new SqlConnection(System.Configuration.ConfigurationSettings.
AppSettings["ConnectionString"]);
```

          Bad example - old ASP.NET 1.1 way, untyped and prone to error.   
In .NET 2.0 you can access it in another way

Step 1: Setup your settings in your common project. E.g. Northwind.Common

![Figure: Settings in Project Properties](ConnStringNET2\_Settings.jpg)  

Step 2: Open up the generated App.config under your common project. E.g. Northwind.Common/App.config

![Figure: Auto generated app.config](ConnStringNET2\_CommonApp.GIF)  

Step 3: ~~Copy the content into your entry applications app.config. E.g. Northwind.WindowsUI/App.config~~ The new setting has been updated to app.config automatically in .NET 2.0


```
<configuration>
      <connectionStrings>
         <add name="Common.Properties.Settings.NorthwindConnectionString"
              connectionString="Data Source=(local);Initial Catalog=Northwind;
              Integrated Security=True"
              providerName="System.Data.SqlClient" />
        </connectionStrings>
 </configuration>
```


Then you can access the connection string like this in C#


```
SqlConnection sqlConn =
 new SqlConnection(Common.Properties.Settings.Default.NorthwindConnectionString);
```

          Good example - access our connection string by strongly typed generated settings class.   

::: greybox

Please note these steps does not work for web site model in Visual Studio 2005. However, they work for other projects such as Windows Form, Console application, Class Library and Web Application Project.

This is not an issue in a well designed website, since it's connection string will be defined in the  **data layer** and you can overwrite this connection string in your web.config.

:::
