---
type: rule
title: Do you know how to migrate the endpoints using YARP
uri: do-you-know-how-to-migrate-endpoints-using-yarp
authors:
  - title: Ozair Ashfaque
    url: https://www.ssw.com.au/people/ozair-ashfaque/
  - url: https://www.ssw.com.au/people/chris-clement/
    title: Chris Clement
  - url: https://www.ssw.com.au/people/william-liebenberg/
    title: William Liebenberg
created: 2023-12-04T21:40:59.980Z
guid: 1c2ee996-c6f0-43c6-b204-c5ac0f339c98
---
YARP (Yet Another Reverse Proxy) is useful for side-by-side increment migration using the strangler fig pattern.  It facilitates the seamless transition of traffic between the legacy ASP.NET application and its modern ASP.NET Core counterparts.
<!--endintro-->
#### How to migrate the endpoints:
Install the YARP nuget package in the new ASP.NET Core project and configure the YARP by providing routes and clusters either by providing [code-based configuration](https://www.ssw.com.au/rules/do-you-know-how-to-configure-yarp/#code-based-configuration-recommended) or [basic configuration](https://www.ssw.com.au/rules/do-you-know-how-to-configure-yarp/#basic-configuration) via App settings. 
Use **MapReverseProxy** middleware to map incoming requests to the corresponding legacy endpoint URLs.
```csharp
app.MapReverseProxy();
```
Migrate the controllers and endpoints from the legacy ASP.NET application to the new ASP.NET core application. Implement the **MapController** middleware to handle incoming requests for endpoints by first checking if the controllers exist in the ASP.NET Core application. If not, all remaining requests will be directed to the **MapReverseProxy** middleware.
```csharp


var builder = WebApplication.CreateBuilder(args);



builder.Services.AddControllers();
```  
Check out the [Yarp Sample Solution](https://github.com/ozairashfaqueSSW/YarpSampleSolution/tree/Side-by-side-incremental-migration-using-yarp) to learn more about how it works. 
        
