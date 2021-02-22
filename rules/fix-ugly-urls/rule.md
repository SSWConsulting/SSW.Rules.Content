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
related: []
redirects:
- do-you-fix-your-ugly-urls

---


<p>​Ugly URL's don't only make it difficult for users to browse your site, they can also impact your Google rankings.<br></p><p class="ssw15-rteElement-GreyBox">http://www.northwind.com/MyInternalDB/UserDatabase/ProductList.aspx?productname=Access</p><dd class="ssw15-rteElement-FigureBad">Figure: If you have a nasty URL like this...​​</dd><p>You should fix it up to look more like this:</p><p class="ssw15-rteElement-GreyBox">http://www.northwind.com/products/access​</p><div><dd class="ssw15-rteElement-FigureGood">Figure: Users could even guess the URL​​<br></dd></div>
<br><excerpt class='endintro'></excerpt><br>
<ol><li>Add in Global.asax a route<br></li><p class="ssw15-rteElement-CodeArea">protected void Application_Start(object sender, EventArgs e) <br>{ <br>//RouteTable and PageRouteHandler are in System.Web.Routing <br>RouteTable.Routes.Add("ProductRoute", new Route("products/{productname}", new PageRouteHandler("~/MyInternalDB/UserDatabase/ProductList.aspx.aspx"))); <br>}</p><p> 
      <strong>Figure: OK example - create a static route if you only have a few rewrites</strong></p><li>Use the URL Rewriting Module for IIS7 <br>
   <dl class="image"><dt><img src="IIS7Rewrite.jpg" alt="IIS7Rewrite.jpg" style="width:700px;height:537px;" /></dt><dd>Figure: Good example - An IIS7 Rewrite is much easier to manage</dd></dl></li>
</ol>​


