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
  - title: Chris Clement
    url: https://www.ssw.com.au/people/chris-clement/
created: 2023-11-23T00:22:39.667Z
guid: aafa30ed-c8d2-43f0-b2f2-ea58cee706ca
---
YARP matches routes with specified request patterns and forwards them to their destination based on their clusters.

### Basic Configuration:

YARP can load proxy configuration from App settings.

1. **appsettings.json**<br />

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
   To configure a YARP reverse proxy, load settings from the configuration.

```cs
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddReverseProxy().LoadFromConfig(builder.Configuration.GetSection("ReverseProxy"));
```

3. **Add YARP Middleware:**<br />
   Configure MapReverseProxy() middleware in the application's pipeline to handle incoming requests.

```cs
var app = builder.Build();
app.MapReverseProxy();
app.Run();
```

### Code-based Configuration (Recommended)

We can configure YARP using a code-based approach. It's suggested to load the proxy configuration by using **[IProxyConfigProvider](https://microsoft.github.io/reverse-proxy/articles/config-providers.html#in-memory-config)**in your code. This is handy when you need a flexible proxy setup that matches your application's unique requirements. 

<!--StartFragment-->

**Advantages:**

* **Dynamic configuration updates:** In-memory configuration allows to store configuration in the application's memory, making it dynamically accessible for modifications and updates. 
  It improves the performance by significantly reducing the time required to apply configuration updates and reduces the latency by eliminating the need for the application to restart or for service disruptions.
* **Strong typing:** Code-based configuration allows to define configuration using strongly typed objects, which eliminates the risk of typos or misconfigurations. This improves code maintainability and reduces the likelihood of runtime errors.

**Disadvantages:**

* **Boilerplate code:** Need to add more code to support this approach, increasing the overall size and complexity of the codebase.

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

**2. Load configuration:**<br />

```CSharp
services
    .AddReverseProxy()
    .Services.AddSingleton<IProxyConfigProvider>(
    new YarpInMemoryConfiguration(webRoutes, webClusters));
// YarpInMemoryConfiguration is the boilerplate class, see the repo for more details.
```

Check out the [Yarp Sample Solution](https://github.com/ozairashfaqueSSW/YarpSampleSolution) to learn more about how it works and [Yarp Solution](https://github.com/ozairashfaqueSSW/YarpSampleSolution/tree/Side-by-side-incremental-migration-using-yarp) for side-by-side increment migration.