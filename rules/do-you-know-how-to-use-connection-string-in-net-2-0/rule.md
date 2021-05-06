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
redirects: 
- do-you-know-how-to-use-connection-string-in-net-2-0

---

In .NET 5, we use **Azure Key Vault** to securely store our connection strings away from prying eyes.

Azure Key Vault is great for keeping your secrets secret because you can control access to the vault via Access Policies. The access policies allows you to add Users and Applications with customized permissions. Make sure you enable the System assigned identity for your App Service, this is required for adding it to Key Vault via Access Policies.

<!--endintro-->

::: good
![Key Vault Access Policies - Setting permissions for Applications and/or Users](access_policies.png)
:::

::: good
![Your WebApp Configuration - no passwords or secrets, just a name of the Key vault that it needs to access](configuration.png)
:::

::: good
![Enabling the System assigned identity for your App Service - this is required for adding it to Key Vault via Access Policies](identity.png)
:::

::: good
![SqlConnectionString stored in Key Vault. Note the ApplicationSecrets section is indicated by ApplicationSecrets-- instead of ApplicationSecrets:](secrets.png)
:::

```cs
public class MyDataService
{
    public readonly string _connectionString;
    public MyDataService(IConfiguration config)
    {
        // In Production, your connection string will be read from Key Vault instead of appsettings.json
        _connectionString = config["ApplicationSecrets:SqlConnectionString"];
    }
    private async Task<string> GetCustomerDetails(CustomerDetailsQuery request)
    {
        var sql = @"SELECT * FROM CustomerDetails WHERE CustomerId = @auctionId";
        await using var db = new SqlConnection(_connectionString);
        return (await db.QueryAsync<string>(sql,
            new
            {
                customerId = request.CustomerId
            })
            ).SingleOrDefault();
    }
}
```

::: good
Referencing a strongly typed connection string defined in application settings
:::

```cs
// In ApplicationSecrets.cs
public class ApplicationSecrets
{
    public string SqlConnectionString { get; set; }
    public string LicenseKey { get; set; }
}
```

::: good
The strongly typed class containing application secrets
:::

```cs
// In Startup.cs
// This method gets called by the runtime. Use this method to add services to the container.
public void ConfigureServices(IServiceCollection services)
{
    // Bind a concrete instance of ApplicationSecrets to the ApplicationSecrets section of your application's configuration providers (includes appsettings.json, appsettings.*.json, environment variables, key vault, and more).
    services.Configure<ApplicationSecrets>(Configuration.GetSection("ApplicationSecrets"));
    ...
}
```

::: good
Binding the application secrets section an instance of the `ApplicationSecrets` class
:::

```cs
// In MyDataService.cs
public class MyDataService
{
    public readonly ApplicationSecrets _settings;
    
    public MyDataService(ApplicationSecrets settings)
    {
        // In Production, your connection string will be read from Key Vault
        _settings = settings;
    }
    
    private async Task<string> GetCustomerDetails(CustomerDetailsQuery request)
    {
        var sql = @"SELECT * FROM CustomerDetails WHERE CustomerId = @auctionId";
        await using var db = new SqlConnection(_settings.SqlConnectionString);
        return (await db.QueryAsync<string>(sql,
            new
            {
                customerId = request.CustomerId
            })
            ).SingleOrDefault();
    }
}
```

::: good
Consuming strongly typed application secrets
:::

Then you can integrate Key Vault directly into your [ASP.NET Core application configuration](https://docs.microsoft.com/en-us/aspnet/core/security/key-vault-configuration?view=aspnetcore-5.0). This allows you to access Key Vault secrets via 'IConfiguration'. 

For an example, refer to this [repository](https://github.com/william-liebenberg/keyvault-example).

`youtube: https://www.youtube.com/embed/-aTlON-UCVM`

::: good 
Watch SSW's William Liebenberg explain Connection Strings and Key Vault in more detail
:::

### History of Connection Strings:

In .NET 1.1 we used to store our connection string in a configuration file like this:   

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
Historical example - old ASP.NET 1.1 way, untyped and prone to error.
:::

In .NET 2.0 we used strongly typed settings classes:

Step 1: Setup your settings in your common project. E.g. Northwind.Common

![Figure: Settings in Project Properties](ConnStringNET2\_Settings.jpg)  

Step 2: Open up the generated App.config under your common project. E.g. Northwind.Common/App.config

![Figure: Auto generated app.config](ConnStringNET2\_CommonApp.gif)  

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
Historical example - access our connection string by strongly typed generated settings class...this is no longer the best way to do it 
:::
