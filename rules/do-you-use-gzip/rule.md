---
type: rule
title: Do you use Gzip?
uri: do-you-use-gzip
created: 2019-05-17T03:05:06.0000000Z
authors:
- id: 82
  title: Barry Sanders

---



<span class='intro'> Gzip&#160;is a&#160;file format&#160;and a&#160;software application&#160;used for&#160;file compression and decompression.<br>Gzip can reduce file size and storage space, and reduce transmission time when transferring files over the network. It runs on both Linux and Windows.<br><br> </span>

<p class="ssw15-rteElement-P">
   <strong>How to use PageSpeed to find which files on your site would benefit from being compressed with Gzip?</strong></p><p class="ssw15-rteElement-Tip">
   <br>
</p><p class="ssw15-rteElement-P">
   <strong>what PageSpeed is?</strong><br></p><p class="ssw15-rteElement-P">PageSpeed can analyze the performance of your webpages and get specific suggestions on how to optimize them.</p><p class="ssw15-rteElement-P">
   <br>
   <strong>How to install PageSpeed?​</strong><br></p><p class="ssw15-rteElement-P">Install PageSpeed from&#160;<a href="https&#58;//chrome.google.com/webstore/category/extensions?hl=en-GB">https&#58;//chrome.google.com/webstore/category/extensions?hl=en-GB​</a><br>select PageSpeed, choose the following extension, and install it&#58;​<img src="/SiteAssets/do-you-use-gzip/2d.png" alt="2d.png" style="margin&#58;5px;width&#58;808px;" /><br><br></p><p class="ssw15-rteElement-P">Figure&#58; Try to Install PageSpeed Insights.<br></p><p class="ssw15-rteElement-P">
   <br>
</p><p class="ssw15-rteElement-P">
   <strong>How to use&#160;PageSpeed?</strong><br></p><p class="ssw15-rteElement-P">See in developer tool, you will have a new part named PageSpeed.<br></p><p class="ssw15-rteElement-P">
   <img src="/SiteAssets/do-you-use-gzip/use-pageSpeed.png" alt="use-pageSpeed.png" style="margin&#58;5px;width&#58;808px;" />
   <br>Figure&#58; Start your PageSpeed by clicking &quot;ANALYZE&quot;.​<br><br></p><p class="ssw15-rteElement-P">See the refresh results&#160;from PageSpeed.<br></p><p> 
   <img src="/SiteAssets/do-you-use-gzip/1.png" alt="1.png" style="margin&#58;5px;width&#58;808px;" />Figure&#58;&#160;Some files can be compressed more than 80%​<br><br></p><p class="ssw15-rteElement-P">
   <strong>Three ways to add Gzip compression to your site&#58; ​</strong><br></p><p class="ssw15-rteElement-P">Use one of the methods described below to add Gzip compression to your site ASP.Net/Angular website</p><p class="ssw15-rteElement-Tip">​<br></p><ul class="ssw15-rteElement-Tip"><li>Method 1&#58;&#160;Turn on &quot;Dynamic Content Compression&quot; In IIS Server.&#160;<img src="/SiteAssets/do-you-use-gzip/2.png" alt="2.png" style="background-color&#58;initial;margin&#58;5px;width&#58;808px;" />Figure&#58; Choose&#160;the website which you want to use Gzip and click on Compression.​​​​<img src="/SiteAssets/do-you-use-gzip/3.png" alt="3.png" style="background-color&#58;initial;margin&#58;5px;width&#58;808px;" />Figure&#58; Install &quot;dynamic content compression&quot; if you haven't installed it.​<br></li>
   <br> ​​<br> In 
   <strong>Control Panel</strong> navigate to 
   <strong> All Control Panel Items | Programs and Features </strong>, and click 
   <strong>Turn Windows features on or off</strong>.<br>Choose 
   <strong>Internet Information Services | Web Management Tools | World Wide Web Services | Performance Features | Dynamic Content &#160;​</strong><strong>Compression</strong>.<img src="/SiteAssets/do-you-use-gzip/4.png" alt="4.png" style="background-color&#58;initial;margin&#58;5px;width&#58;808px;" />Figure&#160;&#58; Click &quot;Ok&quot; to<span style="background-color&#58;initial;"> install it.</span><span style="background-color&#58;initial;">​</span><span style="background-color&#58;initial;">​</span><img src="/SiteAssets/do-you-use-gzip/5.png" alt="5.png" style="background-color&#58;initial;margin&#58;5px;width&#58;808px;" />Figure&#58; now enable dynamic content compression for your site. 
   <div>
      <br>
      <ul class="ssw15-rteElement-Tip"><li>​​<strong>​</strong>​Method 2&#58;&#160;&#160;Using “Gzipper” in your Angular website​<br></li> Follow&#160; 
         <span style="background-color&#58;initial;"><a href="https&#58;//www.npmjs.com/package/gzipper">https&#58;//www.npmjs.com/package/gzipper</a>&#160;.(but it still need IIS Server enable static content compression.) </span> 
         <span style="background-color&#58;initial;">​<br></span>Using &quot;npm i gzipper g&quot; to install &quot;gzipper&quot; first. Add to scripts in your package.json​​​​<br><img src="/SiteAssets/do-you-use-gzip/7.png" alt="7.png" style="margin&#58;5px;width&#58;808px;" /><br><br><img src="/SiteAssets/do-you-use-gzip/6.png" alt="6.png" style="margin&#58;5px;width&#58;808px;" />Figure&#58; &quot;Finish configuration like that. 
         <br>
         <br> 
         <li>Method 3&#58;&#160;​​​​​​​​​​Using ASP.NET code in MVC​<br></li> Refer to 
         <span style="background-color&#58;initial;"><a href="https&#58;//www.codeproject.com/Tips/1080065/Improve-the-Performance-of-ASP-NET-MVC-Web-Applica">https&#58;//www.codeproject.com/Tips/1080065/Improve-the-Performance-of-ASP-NET-MVC-Web-Applica</a>&#160;. ​ 
            <span> To implement this in ASP.NET MVC, we can utilize ActionFilterAttribute and override either OnActionExecuting or OnResultExecuting method. The below code snippet is being used to check whether the current request browser can accept GZIP/DEFLATE encoding by looking at Accept-Encoding request header. If it finds GZIP encoding in this header, then we would set gzip in Content-encoding in response header and if it supports DEFLATE, then this code would set deflate in Content-encoding.</span> 
<pre><code class="language-sh">
using System;
using System.Collections.Generic;
using System.IO.Compression;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace HTTPCompression.ActionFilters
&#123;
    public class CompressAttribute &#58; ActionFilterAttribute
    &#123;
        public override void OnResultExecuting(ResultExecutingContext filterContext)
        &#123;
            HttpRequestBase request = filterContext.HttpContext.Request;

            string acceptEncoding = request.Headers[<span class="hljs-string">&quot;Accept-Encoding&quot;</span>];

            <span class="hljs-keyword">if</span> (string.IsNullOrEmpty(acceptEncoding)) <span class="hljs-built_in">return</span>;

            acceptEncoding = acceptEncoding.ToUpperInvariant();

            HttpResponseBase response = filterContext.HttpContext.Response;

            <span class="hljs-keyword">if</span> (acceptEncoding.Contains(<span class="hljs-string">&quot;GZIP&quot;</span>))
            &#123;
                response.AppendHeader(<span class="hljs-string">&quot;Content-encoding&quot;</span>, <span class="hljs-string">&quot;gzip&quot;</span>);
                response.Filter = new GZipStream(response.Filter, CompressionMode.Compress);
            &#125;
            <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (acceptEncoding.Contains(<span class="hljs-string">&quot;DEFLATE&quot;</span>))
            &#123;
                response.AppendHeader(<span class="hljs-string">&quot;Content-encoding&quot;</span>, <span class="hljs-string">&quot;deflate&quot;</span>);
                response.Filter = new DeflateStream(response.Filter, CompressionMode.Compress);
            &#125;
        &#125;
    &#125;
&#125;
</code></pre>​
    [Compress]
    public ActionResult About()
    &#123;
        ViewBag.Message = &quot;Your application description page.&quot;;
    
        return View();
    &#125;
    
</span></ul>
      <a href="https&#58;//www.codeproject.com/Tips/1080065/Improve-the-Performance-of-ASP-NET-MVC-Web-Applica">​ 
         <p> 
            <br> 
            <br> 
            <br> 
         </p>​<br>​​</a></div></ul>


