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
### Basic Configuration:

1. **appsettings.json Configuration**<br />
   To configure YARP in an ASP.NET application, define routes and clusters in the configuration section of appsettings.json, typically using a custom section name such as 'ReverseProxy'.

```json
// appsettings.json

{
  "ReverseProxy": {
    "Routes": {
      "webAppLegacyServePath": {
        "ClusterId": "webAppLegacyClusterId",
        "Match": {
          "Path": "/legacyWebapp/{**catch-all}"
        }
      },

    },
    "Clusters": {
      "webAppLegacyClusterId": {
        "Destinations": {
          "webAppLegacyServePath": {
            "Address": "http://localhost:5001"
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
### Code-based Configuration (Recommended)

We can configure YARP using a code-based approach. It is recommended to load proxy configuration through the programmatic implementation of **[IProxyConfigProvider](https://microsoft.github.io/reverse-proxy/articles/config-providers.html#in-memory-config)**. This approach is particularly useful when there's a requirement for a dynamic proxy configuration tailored to specific application needs. 

<!--StartFragment-->

**Advantages:**

* **Dynamic configuration updates:** In-memory configuration allows to store configuration in the application's memory, making it dynamically accessible for modifications and updates. 
  It improves the **performance** by significantly reducing the time required to apply configuration updates and **reduces the latency** by eliminating the need for the application to restart or for service disruptions.


* **Strong typing:** Code-based configuration allows to define configuration using strongly typed objects, which eliminates the risk of typos or misconfigurations. This improves code maintainability and reduces the likelihood of runtime errors.


**Disadvantages:**
* **Boilerplate code:** Boilerplate code increases the overall size and complexity of the codebase.



**1. Defining routes and clusters:**<br />


```CSharp
        var webRoutes = new List<RouteConfig>
        {
                // Route for Legacy WebApp
                new()
                {
                    RouteId = "webAppLegacyServePath",
                    ClusterId = webAppLegacyClusterId,
                    Match = new RouteMatch
                    {
                        Path = "/legacyWebapp/{**catch-all}",
                    },
                },
        };

        var webClusters = new List<ClusterConfig>
        {  
            // Cluster for Legacy WebApp

            new()
            {
                ClusterId = webAppLegacyClusterId,
                Destinations = new Dictionary<string, DestinationConfig>
                {
                    {"webAppLegacyServePath", new DestinationConfig{ Address = webAppLegacyAddress } }
                }
            },
        };



```

</br>





**2. Load in-memory configuration:**<br />
```CSharp
        services
            .AddReverseProxy()
            .Services.AddSingleton<IProxyConfigProvider>(
            new YarpInMemoryConfiguration(webRoutes, webClusters));



```
#### Checkout the [Yarp Sample Solution]((https://github.com/ozairashfaqueSSW/YarpSampleSolution/)) to learn more about how it works.