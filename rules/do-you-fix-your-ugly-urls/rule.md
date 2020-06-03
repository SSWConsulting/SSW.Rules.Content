---
type: rule
title: Do you fix your ugly URL's?
uri: do-you-fix-your-ugly-urls
created: 2015-11-10T21:02:11.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 83
  title: Camilla Rosa Silva

---



<span class='intro'> <p>​Ugly URL's don't only make it difficult for users to browse your site, they can also impact your Google rankings.<br></p><p class="ssw15-rteElement-GreyBox">http&#58;//www.northwind.com/MyInternalDB/UserDatabase/ProductList.aspx?productname=Access</p><dd class="ssw15-rteElement-FigureBad">Figure&#58; If you have a nasty URL like this...​​</dd><p>You should fix it up to look more like this&#58;</p><p class="ssw15-rteElement-GreyBox">http&#58;//www.northwind.com/products/access​</p><div><dd class="ssw15-rteElement-FigureGood">Figure&#58; Users could even guess the URL​​<br></dd></div> </span>

<ol><li>Add in Global.asax a route<br></li><p class="ssw15-rteElement-CodeArea">protected void Application_Start(object sender, EventArgs e) <br>&#123; <br>//RouteTable and PageRouteHandler are in System.Web.Routing <br>RouteTable.Routes.Add(&quot;ProductRoute&quot;, new Route(&quot;products/&#123;productname&#125;&quot;, new PageRouteHandler(&quot;~/MyInternalDB/UserDatabase/ProductList.aspx.aspx&quot;))); <br>&#125;</p><p> 
      <strong>Figure&#58; OK example - create a static route if you only have a few rewrites</strong></p><li>Use the URL Rewriting Module for IIS7 <br>
   <dl class="image"><dt><img src="/PublishingImages/IIS7Rewrite.jpg" alt="IIS7Rewrite.jpg" style="width&#58;700px;height&#58;537px;" /></dt><dd>Figure&#58; Good example - An IIS7 Rewrite is much easier to manage</dd></dl></li>
</ol>​


