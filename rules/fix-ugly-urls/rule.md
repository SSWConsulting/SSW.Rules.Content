---
type: rule
archivedreason: 
title: Do you fix your ugly URL's?
guid: df6b61c4-c808-4f80-bca9-7ea7eace8067
uri: fix-ugly-urls
created: 2015-11-10T21:02:11.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Camilla Rosa Silva
  url: https://ssw.com.au/people/camilla-rosa-silva
related: 
- use-dashes-in-urls
- create-friendly-short-urls
redirects:
- do-you-fix-your-ugly-urls

---

Ugly URL's don't only make it difficult for users to browse your site, they can also impact your Google rankings.

::: greybox
northwind.com/MyInternalDB/UserDatabase/ProductList.aspx?productname=Access  
:::
::: bad
Figure: A nasty URL...  
:::

You should fix it up to look more like this:

::: greybox
northwind.com/products/access  
:::
::: good
Figure: Users could even guess this nice URL
:::

<!--endintro-->

1. Add in Global.asax a route

``` aspnet
protected void Application_Start(object sender, EventArgs e) 
{ 
//RouteTable and PageRouteHandler are in System.Web.Routing 
RouteTable.Routes.Add("ProductRoute", new Route("products/{productname}", new PageRouteHandler("~/MyInternalDB/UserDatabase/ProductList.aspx.aspx"))); 
}
```
::: ok
Figure: OK example - create a static route if you only have a few rewrites**
:::

2. Use the URL Rewriting Module for IIS7 

::: good  
![Figure: Good example - An IIS7 Rewrite is much easier to manage](IIS7Rewrite.jpg)  
:::
