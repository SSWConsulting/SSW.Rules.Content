---
type: rule
archivedreason: 
title: Do you know how to create nice URLs using ASP.NET 4?
guid: 43cdcd40-66f2-4111-843c-96dbdc1d8fc1
uri: do-you-know-how-to-create-nice-urls-using-asp-net-4
created: 2009-08-24T02:07:36.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---


There are a lot of reasons to have nice URLs for your website:
<ul>
    <li>Easy to remember </li>
    <li>Easy to navigate  </li>
    <li>Better for search engines </li>
</ul>

<br><excerpt class='endintro'></excerpt><br>

  <dl class="badImage">
    <dt><img alt="Bad example – This URL is impossible to remember for your users, and even search don’t like these URLs" src="BadURL.jpg" /> </dt>
    <dd>Figure: Bad example – This URL is impossible to remember for your users, and even search don’t like these URLs </dd>
</dl>
<dl class="goodImage">
    <dt><img alt="Good example – Nice clean URL, easy to remember, easy to guess where I am and good for search engines" src="GoodURL.jpg" /> </dt>
    <dd>Figure: Good example – Nice clean URL, easy to remember, easy to guess where I am and good for search engines </dd>
</dl>
<p>With ASP.NET 4 it is easy to create this URLs. The ASP.NET team includes routing features, known from the MVC web framework.<br>
Add a route in Global.asax </p>
<dl class="goodCode">
    <dt>
    <pre>protected void <span style="font-family:'courier new';font-size:8pt;">Application_Start</span>(object sender, EventArgs e)<br>{<br>    //RouteTable and PageRouteHandler are in System.Web.Routing<br>    RouteTable.Routes.Add("ProductRoute",<br>        new Route("products/{productname}",<br>        new PageRouteHandler("~/ssw/Products/ProdCategoryList.aspx")));<br>}​</pre>
    </dt>
    <dd>Figure: Example on how to route www.ssw.com.au/products/{everything} to the www.ssw.com.au/ssw/Products/ProdCategoryList.aspx page </dd>
</dl>
<p><b>Note</b>: There is no dependency on the MVC framework in order to use this code.<br>
<b>Note</b>: IIS7 has a module called <a href="http://www.iis.net/learn/extensions/url-rewrite-module/using-the-url-rewrite-module">URL rewrite module</a> that can do this functionality without changing any code. Just a configuration of a "Rule" in the IIS Manager. </p>



