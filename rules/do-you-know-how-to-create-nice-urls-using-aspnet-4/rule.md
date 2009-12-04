---
type: rule
title: Do you know how to create nice URLs using ASP.NET 4?
uri: do-you-know-how-to-create-nice-urls-using-aspnet-4
created: 2009-08-24T02:07:36.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> This field should not be null (Remove me when you edit this field). </span>


  <dl class="badImage">
    <dt><img alt="Bad example – This URL is impossible to remember for your users, and even search don’t like these URLs" src="/Standards/WebSites/RulesToBetterWebsiteDevelopmentASPDotNet/PublishingImages/BadURL.jpg" /> </dt>
    <dd>Figure&#58; Bad example – This URL is impossible to remember for your users, and even search don’t like these URLs </dd>
</dl>
<dl class="goodImage">
    <dt><img alt="Good example – Nice clean URL, easy to remember, easy to guess where I am and good for search engines" src="/Standards/WebSites/RulesToBetterWebsiteDevelopmentASPDotNet/PublishingImages/GoodURL.jpg" /> </dt>
    <dd>Figure&#58; Good example – Nice clean URL, easy to remember, easy to guess where I am and good for search engines </dd>
</dl>
<p>With ASP.NET 4 it is easy to create this URLs. The ASP.NET team includes routing features, known from the MVC web framework.<br>
Add a route in Global.asax </p>
<dl class="goodCode">
    <dt>
    <pre>protected void <span style="font-family&#58;'courier new';font-size&#58;8pt;">Application_Start</span>(object sender, EventArgs e)<br>&#123;<br>    //RouteTable and PageRouteHandler are in System.Web.Routing<br>    RouteTable.Routes.Add(&quot;ProductRoute&quot;,<br>        new Route(&quot;products/&#123;productname&#125;&quot;,<br>        new PageRouteHandler(&quot;~/ssw/Products/ProdCategoryList.aspx&quot;)));<br>&#125;</pre>
    </dt>
    <dd>Figure&#58; Example on how to route www.ssw.com.au/products/&#123;everything&#125; to the www.ssw.com.au/ssw/Products/ProdCategoryList.aspx page </dd>
</dl>
<p><b>Note</b>&#58; There is no dependency on the MVC framework in order to use this code.<br>
<b>Note</b>&#58; IIS7 has a module called <a href="http&#58;//learn.iis.net/page.aspx/460/using-url-rewrite-module/">URL rewrite module</a> that can do this functionality without changing any code. Just a configuration of a &quot;Rule&quot; in the IIS Manager. </p>



