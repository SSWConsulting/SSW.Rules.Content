---
type: rule
title: Do you bundle and minify your JavaScript?
uri: do-you-bundle-and-minify-your-javascript
created: 2012-07-18T17:35:19.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>Did you know you can improve the speed of your MVC app by using a built in feature called bundling and minification.</p> </span>

<p>Bundling allows you to&#58;</p>
<ol>
<li>Specify the JavaScript files you want to include in your app and the order in which they are loaded </li>
<li>Put them into 1 JavaScript file reducing calls to the server. </li>
</ol>
<p>The next part of the process is minification. This means that all the whitespace is removed from the JavaScript files and long variables names are shortened where possible to decrease the size of the package.<br>
All this adds up to a faster MVC app and a better user experience.</p>

<span class="ms-rteCustom-CodeArea">
<p>Layout.cshtml</p>
&lt;script type=&quot;text/javascript&quot; src=&quot;/SoftwareDevelopment/RulesToBetterMVC/Pages/@Url.Content(&quot;&gt;&lt;/script&gt;<br> 
&lt;script type=&quot;text/javascript&quot; src=&quot;/SoftwareDevelopment/RulesToBetterMVC/Pages/@Url.Content(&quot;&gt;&lt;/script&gt;<br> 
&lt;script type=&quot;text/javascript&quot; src=&quot;/SoftwareDevelopment/RulesToBetterMVC/Pages/@Url.Content(&quot;&gt;&lt;/script&gt;<br>  
&lt;script type=&quot;text/javascript&quot; src=&quot;/SoftwareDevelopment/RulesToBetterMVC/Pages/@Url.Content(&quot;&gt;&lt;/script&gt;<br> 
&lt;script type=&quot;text/javascript&quot; src=&quot;/SoftwareDevelopment/RulesToBetterMVC/Pages/@Url.Content(&quot;&gt;&lt;/script&gt;<br> 
&lt;script type=&quot;text/javascript&quot; src=&quot;/SoftwareDevelopment/RulesToBetterMVC/Pages/@Url.Content(&quot;&gt;&lt;/script&gt;<br> 
</span>
<span class="ms-rteCustom-FigureBad">Figure&#58; Scripts are specified in the view</span>


<span class="ms-rteCustom-CodeArea">
<p>BundleConfig.cs</p>
public static void RegisterBundles(BundleCollection bundles)<br> 
        &#123;<br> 
            bundles.Add(new ScriptBundle(&quot;~/bundles/SSW&quot;).Include(<br> 
                        &quot;~/Scripts/2011.3.1115/jquery-1.6.4.min.js&quot;, <br> 
                        &quot;~/Scripts/jquery-ui-1.8.16.min.js&quot;,<br> 
                        &quot;~/Scripts/jquery.formatCurrency-1.4.0.min.js&quot;,<br> 
                        &quot;~/Scripts/date.js&quot;,<br> 
                        &quot;~/Scripts/jquery.watermark.min.js&quot;,<br> 
                        &quot;~/Scripts/jquery.cross-slide.min.js&quot;));<br> 
        &#125;<br> 
 
<p>Layout.cshtml</p>
@Scripts.Render(&quot;~/bundles/ssw&quot;)
</span>
<span class="ms-rteCustom-FigureGood">Figure&#58; A bundle is created in the bundle config and then referenced in the view</span>




