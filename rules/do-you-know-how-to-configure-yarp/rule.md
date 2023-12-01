---
type: rule
title: Do you know how to configure YARP?
uri: do-you-know-how-to-configure-yarp
authors:
  - title: Ozair Ashfaque
    url: https://www.ssw.com.au/people/ozair-ashfaque/
  - title: William Liebenberg
    url: https://www.ssw.com.au/people/william-liebenberg/
  - title: Christian Morford-Waite
    url: https://www.ssw.com.au/people/christian-morford-waite/
  - title: Tom Iwainski
    url: https://www.ssw.com.au/people/thomas-iwainski/
created: 2023-11-23T00:22:39.667Z
guid: aafa30ed-c8d2-43f0-b2f2-ea58cee706ca
---
### Code-based Configuration (Recommended)

We can configure YARP using a code-based approach. It is recommended to load proxy configuration through the programmatic implementation of **[IProxyConfigProvider](https://microsoft.github.io/reverse-proxy/articles/config-providers.html#in-memory-config)**. This approach is particularly useful when there's a requirement for a dynamic proxy configuration tailored to specific application needs. 

<!--StartFragment-->

**Advantages:**

* **Dynamic configuration updates:** In-memory configuration allows to store configuration in the application's memory, making it dynamically accessible for modifications and updates. 
  It improves the **performance** by significantly reducing the time required to apply configuration updates and **reduces the latency** by eliminating the need for the application to restart or for service disruptions.


* **Strong typing:** Code-based configuration allows to define configuration using strongly typed objects, which eliminates the risk of typos or misconfigurations. This improves code maintainability and reduces the likelihood of runtime errors.
* **Improved testability:** Code-based configuration can be easily mocked and tested, making it easier to write comprehensive tests for your application.

**Disadvantages:**
* **Boilerplate code:** It requires a boilerplate code to define and manage the configuration.








**1. Add In-Memory Configuration:**<br />
Configure in-memory configuration for YARP. Unlike static configurations, in-memory updates enable the YARP proxy to dynamically adapt routes and clusters during runtime without necessitating a restart of the application.<br />
The following snippet shows a custom provider that implements GetConfig() from **IProxyConfigProvider**:

```CSharp

```

</br>

Add a nested class that represents the in-memory configuration of YARP with three properties: **Routes**, **Clusters**, and **ChangeToken**. The **Routes** property stores the list of routes, the **Clusters** stores the list of clusters, and the **ChangeToken** property is a cancellation token that can be used to be notified when the configuration changes.</br>
The following snippet shows the **InMemoryConfig** class with an internal mehod **SignalChange()**. This method is called when the configuration is updated. It cancels the cancellation token, which signals to any listeners that the configuration has changed.

```cs
// YarpInMemoryConfiguration.cs

private class InMemoryConfig : IProxyConfig
{
    private readonly CancellationTokenSource _cts = new();

    public InMemoryConfig(IReadOnlyList<RouteConfig> routes, IReadOnlyList<ClusterConfig> clusters)
    {
        Routes = routes;
        Clusters = clusters;
        ChangeToken = new CancellationChangeToken(_cts.Token);
    }

    public IReadOnlyList<RouteConfig> Routes { get; }

    public IReadOnlyList<ClusterConfig> Clusters { get; }

    public IChangeToken ChangeToken { get; }

    internal void SignalChange() => _cts.Cancel();
}
```

</br>Add Update method to update the in-memory configuration with the provided routes and clusters. Also add **SignalChanged()** to signals a change in config to nofitfy the change in the configuration. </br>
The following snippet shows the **Update(IReadOnlyList<RouteConfig> routes, IReadOnlyList<ClusterConfig> clusters)** 

```CSharp
// YarpInMemoryConfiguration.cs

public class YarpInMemoryConfiguration : IProxyConfigProvider
{
    private volatile InMemoryConfig _config;
    public IProxyConfig GetConfig() => _config;

    public void Update(IReadOnlyList<RouteConfig> routes, IReadOnlyList<ClusterConfig> clusters)
    {
        var oldConfig = _config;
        _config = new InMemoryConfig(routes, clusters);
        oldConfig.SignalChange();
    }
}
```

</br>The following is a full code snippet of **YarpInMemoryConfiguration** class:

```cs
// YarpInMemoryConfiguration.cs

public class YarpInMemoryConfiguration : IProxyConfigProvider
{
    private volatile InMemoryConfig _config;

    public YarpInMemoryConfiguration(IReadOnlyList<RouteConfig> routes, IReadOnlyList<ClusterConfig> clusters)
    {
        _config = new InMemoryConfig(routes, clusters);
    }

    public IProxyConfig GetConfig() => _config;

    public void Update(IReadOnlyList<RouteConfig> routes, IReadOnlyList<ClusterConfig> clusters)
    {
        var oldConfig = _config;
        _config = new InMemoryConfig(routes, clusters);
        oldConfig.SignalChange();
    }

    private class InMemoryConfig : IProxyConfig
    {
        private readonly CancellationTokenSource _cts = new();

        public InMemoryConfig(IReadOnlyList<RouteConfig> routes, IReadOnlyList<ClusterConfig> clusters)
        {
            Routes = routes;
            Clusters = clusters;
            ChangeToken = new CancellationChangeToken(_cts.Token);
        }

        public IReadOnlyList<RouteConfig> Routes { get; }

        public IReadOnlyList<ClusterConfig> Clusters { get; }

        public IChangeToken ChangeToken { get; }

        internal void SignalChange() => _cts.Cancel();
    }
}
```

</br>**2. Add Dynamic YARP Configuration:**<br />
To configure YARP dynamically, provide destination address in **appsetting.json** configuration.</br>
The following is a code snippet for configuring destination paths for **WebUI** and **WebApp**.

```json
// appsettings.json

"ReverseProxy": {
  "WebUIServeAddress": "https://localhost:44300",
  "WebAppServeAddress": "https://localhost:44310"
},
```

</br>Create model for above configurations for getting the addresses.

```cs
// ReverseProxySetting.cs

public class ReverseProxySetting
{
    public const string Key = "ReverseProxy";

    public string WebUIServeAddress { get; set; } = string.Empty;

    public string WebAppServeAddress { get; set; } = string.Empty;

}
```

</br>Use **IReverseProxyBuilder** to register in-memory configuration class as singleton. </br>
The following is the code snippet for defining **LoadFromMemory(this IReverseProxyBuilder builder,
            IReadOnlyList<RouteConfig> routes,
            IReadOnlyList<ClusterConfig> clusters)** and registering the **YarpInMemoryConfiguration** class as singleton.

```cs
// LocalDevYarpConfigExtensions.cs

private static IReverseProxyBuilder LoadFromMemory(this IReverseProxyBuilder builder,
    IReadOnlyList<RouteConfig> routes,
    IReadOnlyList<ClusterConfig> clusters)
{
    builder.Services.AddSingleton<IProxyConfigProvider>(new YarpInMemoryConfiguration(routes, clusters));
    return builder;
}
```

</br>Define clusterIds to uniquely identify the destination address for each matching route.</br>
The following is a code snippet of **LocalDevYarpConfigExtensions** class for defining cluster ids for **WebUI** and **WebApp**:

```cs
// LocalDevYarpConfigExtensions.cs

public static class LocalDevYarpConfigExtensions
{

    private const string webUiClusterId = "webUi";

    private const string webAppClusterId = "webApp";
}
```

</br>Use **IConfiguration** to get reverse proxy settings from appsettings.json.
The following is code snippet of retrieving **ReverseProxy** using **ReverseProxySetting** model:

```cs
// LocalDevYarpConfigExtensions.cs

 public static void AddSpaYarp(IConfiguration configuration)
 {
     ReverseProxySetting? config = configuration.GetSection(ReverseProxySetting.Key).Get<ReverseProxySetting>();
 }
```

</br>Define the routes using YARP's **RouteConfig**.</br>
The following is a code snippet of **routes** for **WebUI** and **WebApp**:

```cs
// LocalDevYarpConfigExtensions.cs

var webRoutes = new List<RouteConfig>
            {
                // Route for WebUI App
                new RouteConfig
                {
                    RouteId = "webUIServePath",
                    ClusterId = webUiClusterId,
                    Match = new RouteMatch
                    {
                        Path = "/api/v2/{**catch-all}",
                    },
                },

                // Route for WebApp App
                new RouteConfig
                {
                    RouteId = "webAppServePath",
                    ClusterId = webAppClusterId,
                    Match = new RouteMatch
                    {
                        Path = "/api/{**catch-all}",
                    },
                },
            };
```

</br>Define the clustes using YARP's **ClusterConfig**.</br>
The following is a code snippet of **clusters** for **WebUI** and **WebApp**:

```cs
// LocalDevYarpConfigExtensions.cs

var webClusters = new List<ClusterConfig>
            {
                new ClusterConfig
                {
                    ClusterId = webUiClusterId,
                    Destinations = new Dictionary<string, DestinationConfig>
                    {
                        { "webUIServePath", new DestinationConfig { Address = webUiAddress } }
                    }
                },

                new ClusterConfig
                {
                    ClusterId = webAppClusterId,
                    Destinations = new Dictionary<string, DestinationConfig>
                    {
                        { "webAppServePath", new DestinationConfig { Address = webAppAddress } }
                    }
                },

            };
```

</br>Use **IServiceCollection** to inject routes and clusters list in in-memory service instance using **AddReverseProxy()**
The following is a code snippet of  injecting routes and clusters to **LoadFromMemory()** method:

```cs
// LocalDevYarpConfigExtensions.cs

public static void AddSpaYarp(this IServiceCollection services,
     IConfiguration configuration)
{
    services.AddReverseProxy().LoadFromMemory(
      webRoutes.ToList(),
      webClusters.ToList());
}
```

</br>Here is a full code snippet of **LocalDevYarpConfigExtensions** class for YARP configuration:

```cs
// LocalDevYarpConfigExtensions.cs

public static class LocalDevYarpConfigExtensions
{

    private const string webUiClusterId = "webUi";

    private const string webAppClusterId = "webApp";

    public static void AddSpaYarp(this IServiceCollection services,
        IConfiguration configuration)
    {
        ReverseProxySetting? config = configuration.GetSection(ReverseProxySetting.Key).Get<ReverseProxySetting>();

        string webUiAddress = config?.WebUIServeAddress ?? throw new ArgumentNullException(nameof(ReverseProxySetting),
                                    $@"Missing config {ReverseProxySetting.Key} for WebUI");

        string webAppAddress = config?.WebAppServeAddress ?? throw new ArgumentNullException(nameof(ReverseProxySetting),
                                    $@"Missing config {ReverseProxySetting.Key} for WebApp");


        var webRoutes = new List<RouteConfig>
            {
                // Route for WebUI App
                new RouteConfig
                {
                    RouteId = "webUIServePath",
                    ClusterId = webUiClusterId,
                    Match = new RouteMatch
                    {
                        Path = "/api/v2/{**catch-all}",
                    },
                },

                // Route for WebApp App
                new RouteConfig
                {
                    RouteId = "webAppServePath",
                    ClusterId = webAppClusterId,
                    Match = new RouteMatch
                    {
                        Path = "/api/{**catch-all}",
                    },
                },
            };

        var webClusters = new List<ClusterConfig>
            {
                // Cluster for WebUI App
                new ClusterConfig
                {
                    ClusterId = webUiClusterId,
                    Destinations = new Dictionary<string, DestinationConfig>
                    {
                        { "webUIServePath", new DestinationConfig { Address = webUiAddress } }
                    }
                },

                // Cluster for WebApp App
                new ClusterConfig
                {
                    ClusterId = webAppClusterId,
                    Destinations = new Dictionary<string, DestinationConfig>
                    {
                        { "webAppServePath", new DestinationConfig { Address = webAppAddress } }
                    }
                },

            };

        // Injecting the routes and clusters in YarpInMemoryConfiguration class
        services.AddReverseProxy().LoadFromMemory(
          webRoutes.ToList(),
          webClusters.ToList());
    }
}    
```

### Basic Configuration:

1. **appsettings.json Configuration**<br />
   To configure YARP in an ASP.NET application, define routes and clusters in the configuration section of appsettings.json, typically using a custom section name such as 'ReverseProxy'.

```json
// appsettings.json

{
  "ReverseProxy": {
    "Routes": {
      "webUIServePath": {
        "ClusterId": "webUi",
        "Match": {
          "Path": "/api/v2/{**catch-all}"
        }
      },
      "webAppServePath": {
        "ClusterId": "webApp",
        "Match": {
          "Path": "/api/{**catch-all}"
        }
      }
    },
    "Clusters": {
      "webUi": {
        "Destinations": {
          "webUIServePath": {
            "Address": "http://localhost:5001"
          }
        }
      },
      "webApp": {
        "Destinations": {
          "webAppServePath": {
            "Address": "http://localhost:5002"
          }
        }
      },
    }
  }
}
```

2. **Load Configuration in ASP.NET Application:**<br />
   To configure a YARP reverse proxy, load settings from the "ReverseProxy" configuration section of appsettings.

```cs
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddReverseProxy().LoadFromConfig(builder.Configuration.GetSection("ReverseProxy"));
```

3. **Add MapReverseProxy() Middleware:**<br />
   Configure MapReverseProxy() middleware in the application's pipeline to handle incoming requests.

```cs
var app = builder.Build();
app.MapReverseProxy();
app.Run();
```