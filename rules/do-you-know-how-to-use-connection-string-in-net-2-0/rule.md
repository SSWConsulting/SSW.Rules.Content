---
type: rule
archivedreason:
title: Do you know how to use Connection Strings?
guid: 2dec2ea4-3359-4bb0-8f30-c278c8735670
uri: do-you-know-how-to-use-connection-strings
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


```xml
<configuration>
     <appSettings>
          <add key="ConnectionString" value ="integrated security=true;
           data source=(local);initial catalog=Northwind"/>
     </appSettings>
</configuration>
```


and access this connection string in code like this:


```cs
SqlConnection sqlConn = 
new SqlConnection(System.Configuration.ConfigurationSettings.
AppSettings["ConnectionString"]);
```

::: bad
Bad example - old ASP.NET 1.1 way, untyped and prone to error.  
:::
          
In .NET 2.0 we used strongly typed settings classes:

Step 1: Setup your settings in your common project. E.g. Northwind.Common

![Figure: Settings in Project Properties](ConnStringNET2\_Settings.jpg)  

Step 2: Open up the generated App.config under your common project. E.g. Northwind.Common/App.config

![Figure: Auto generated app.config](ConnStringNET2\_CommonApp.GIF)  

Step 3: ~~Copy the content into your entry applications app.config. E.g. Northwind.WindowsUI/App.config~~ The new setting has been updated to app.config automatically in .NET 2.0


```xml
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


```cs
SqlConnection sqlConn =
 new SqlConnection(Common.Properties.Settings.Default.NorthwindConnectionString);
```

::: bad
Bad example - access our connection string by strongly typed generated settings class...this is no longer the best way to do it 
:::

In .NET 5, we use Azure Key Vault to securely store our connection strings away from prying eyes:

::: good
![Secrets are safely stored in Azure Key Vault](keyvault.png)
:::


::: good
![Secrets are do not need to be used on developer's machines](funcsec-vaultindicator-header.jpg)
:::
