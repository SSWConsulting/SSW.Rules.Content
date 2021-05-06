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

In .NET 5, we use **Azure Key Vault** to securely store our connection strings away from prying eyes.

Azure Key Vault is great for keeping your secrets secret because you can control access to the vault via Access Policies. The access policies allows you to add Users and Applications with customized permissions. Make sure you enable the System assigned identity for your App Service, this is required for adding it to Key Vault via Access Policies.

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
public void ConfigureServices(IServiceCollection services)
{
    services.AddControllers();
    services.AddDbContext<ApplicationDbContext>(
        options => options.UseSqlServer("name=ApplicationSettings:SqlConnectionString"));
}
```

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

```cs
// In ApplicationSecrets.cs
public class ApplicationSecrets
{
    public string SqlConnectionString { get; set; }
    public string LicenseKey { get; set; }
}
```

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

```cs
// In MyDataService.cs
public class MyDataService
{
    public readonly string _connectionString;
    public MyDataService(ApplicationSettings settings)
    {
        // In Production, your connection string will be read from KeyVault
        _connectionString = settings.SqlConnectionString;
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

Then you can integrate Key Vault directly into your [ASP.NET Core application configuration](https://docs.microsoft.com/en-us/aspnet/core/security/key-vault-configuration?view=aspnetcore-5.0). This allows you to access Key Vault secrets via 'IConfiguration'. 

```cs
public static IHostBuilder CreateHostBuilder(string[] args) =>
    Host.CreateDefaultBuilder(args)
        .ConfigureWebHostDefaults(webBuilder =>
        {
            webBuilder
                .UseStartup<Startup>()
                .ConfigureAppConfiguration((context, config) =>
                {
                    // Note: If you want to use Key Vault from your local machine, comment out the following line, or modify your ASPNETCORE_ENVIRONMENT environment variable to be "Production"
                    if (context.HostingEnvironment.IsProduction())
                    {
                        IConfigurationRoot builtConfig = config.Build();
                        
                        // If you are attempting to use Key Vault from your local machine, make sure to log into azure via `az login`.
                        // Also make sure you have added your user to Key Vault via the access policy blade.
                        TokenCredential cred = context.HostingEnvironment.IsProduction() ? new DefaultAzureCredential(false) : new AzureCliCredential();
                        
                        var keyvaultUri = new Uri($"https://{builtConfig["KeyVaultName"]}.vault.azure.net/");
                        var secretClient = new SecretClient(keyvaultUri, cred);
                        config.AddAzureKeyVault(secretClient, new KeyVaultSecretManager());
                    }
                });
        });
```
::: good
Integrating Key Vault with your .NET application
:::

Optional: To go a step further, we can bolt Azure Key Vault directly into [Azure App Configuration service](https://docs.microsoft.com/en-us/azure/azure-app-configuration/overview). 

The benefit of doing this is so that you can control exactly which Key Vault secrets (and their versions) are made available to our application. We add Key Vault Secrets by using Key Vault references.

A second major benefit for using Azure AppConfiguration is that you gain powerful Feature Flaging capabilities. 

Once we bootstrap our application to with Azure AppConfiguration Service, we can still access our app settings and secrets via IConfiguration. 

Watch SSW's William Liebenberg explain Connection Strings and Key Vault in more detail:

`youtube: https://www.youtube.com/embed/-aTlON-UCVM`

