---
type: rule
archivedreason: 
title: Do you fix your ugly URL's?
guid: df6b61c4-c808-4f80-bca9-7ea7eace8067
uri: do-you-fix-your-ugly-urls
created: 2015-11-10T21:02:11.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 83
  title: Camilla Rosa Silva
related: []

---

Ugly URL's don't only make it difficult for users to browse your site, they can also impact your Google rankings.


::: greybox
http://www.northwind.com/MyInternalDB/UserDatabase/ProductList.aspx?productname=Access
:::



::: bad
Figure: If you have a nasty URL like this...
:::


You should fix it up to look more like this:


::: greybox
http://www.northwind.com/products/access
:::




::: good
Figure: Users could even guess the URL

:::



<!--endintro-->

1. Add in Global.asax a route
    protected void Application\_Start(object sender, EventArgs e) 
{ 
//RouteTable and PageRouteHandler are in System.Web.Routing 
RouteTable.Routes.Add("ProductRoute", new Route("products/{productname}", new PageRouteHandler("~/MyInternalDB/UserDatabase/ProductList.aspx.aspx"))); 
}
    **Figure: OK example - create a static route if you only have a few rewrites**
2. Use the URL Rewriting Module for IIS7 
<dl class="image">&lt;dt&gt;<img src="IIS7Rewrite.jpg" alt="IIS7Rewrite.jpg" style="width:700px;height:537px;">&lt;/dt&gt;<dd>Figure: Good example - An IIS7 Rewrite is much easier to manage</dd></dl>
