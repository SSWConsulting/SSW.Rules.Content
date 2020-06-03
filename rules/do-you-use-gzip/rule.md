---
type: rule
title: Do you use Gzip?
uri: do-you-use-gzip
created: 2019-05-17T03:05:06.0000000Z
authors:
- id: 82
  title: Barry Sanders

---



<span class='intro'> ​Gzip&#160;is a&#160;file format&#160;and a&#160;software application&#160;used for&#160;file compression and decompression.<br>Gzip can reduce file size and storage space, and reduce transmission time when transferring files over the network. It runs on both Linux and Windows.<div><br></div> </span>

<p class="ssw15-rteElement-P">​Use PageSpeed Insights extension in Chrome to determine if your site will benefit from using Gzip.&#160;</p><p class="ssw15-rteElement-P">For more information about how to use PageSpeed to find which files on your site would benefit from being compressed with Gzip&#160;see <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=82583a25-2994-48ec-b061-bea6b6ed48fe" target="_blank">Do-you-use-PageSpeed</a>.​<br></p><p class="ssw15-rteElement-P"><strong>​<br>​</strong><strong>Three ways to add Gzip compression to your site&#58; ​</strong></p><p class="ssw15-rteElement-P">Use one of the methods described below to add Gzip compression to your site ASP.Net/Angular website</p><p class="ssw15-rteElement-Tip">​<br></p><ul><li>Method 1&#58;&#160;Turn on &quot;Dynamic Content Compression&quot; In IIS Server.&#160;<img src="/SiteAssets/do-you-use-gzip/2.png" alt="2.png" style="background-color&#58;initial;margin&#58;5px;width&#58;808px;" />Figure&#58; Choose&#160;the website which you want to use Gzip and click on Compression.​​​​<img src="/SiteAssets/do-you-use-gzip/3.png" alt="3.png" style="background-color&#58;initial;margin&#58;5px;width&#58;808px;" />Figure&#58; Install &quot;dynamic content compression&quot; if you haven't installed it.​<br></li> 
   <br> ​​<br> In 
   <strong>Control Panel</strong> navigate to 
   <strong> All Control Panel Items | Programs and Features </strong>, and click 
   <strong>Turn Windows features on or off</strong>.<br>Choose 
   <strong>Internet Information Services | Web Management Tools | World Wide Web Services | Performance Features | Dynamic Content &#160;​</strong><strong>Compression</strong>.<img src="/SiteAssets/do-you-use-gzip/4.png" alt="4.png" style="background-color&#58;initial;margin&#58;5px;width&#58;808px;" />Figure&#160;&#58; Click &quot;Ok&quot; to<span style="background-color&#58;initial;"> install it.</span><span style="background-color&#58;initial;">​</span><span style="background-color&#58;initial;">​</span><img src="/SiteAssets/do-you-use-gzip/5.png" alt="5.png" style="background-color&#58;initial;margin&#58;5px;width&#58;808px;" />Figure&#58; now enable dynamic content compression for your site. 
   <div> 
      <br> 
      <ul><li>​​<strong>​</strong>​Method 2&#58;&#160;&#160;Using “Gzipper” in your Angular website​<br></li> Follow&#160; 
         <span style="background-color&#58;initial;"> 
            <a href="https&#58;//www.npmjs.com/package/gzipper">https&#58;//www.npmjs.com/package/gzipper</a>&#160;.(but it still need IIS Server enable static content compression.) </span>
         <span style="background-color&#58;initial;">​<br></span>Using &quot;npm i gzipper g&quot; to install &quot;gzipper&quot; first. Add to scripts in your package.json​​​​<br><img src="/SiteAssets/do-you-use-gzip/7.png" alt="7.png" style="margin&#58;5px;width&#58;808px;" /><br><br><img src="/SiteAssets/do-you-use-gzip/6.png" alt="6.png" style="margin&#58;5px;width&#58;808px;" />Figure&#58; &quot;Finish configuration like that. 
         <br><br>
         <li>Method 3&#58;&#160;​​​​​​​​​​Using ASP.NET code in MVC​<br></li> Refer to 
         <span style="background-color&#58;initial;"> 
            <a href="https&#58;//www.codeproject.com/Tips/1080065/Improve-the-Performance-of-ASP-NET-MVC-Web-Applica">https&#58;//www.codeproject.com/Tips/1080065/Improve-the-Performance-of-ASP-NET-MVC-Web-Applica</a>&#160;. ​ 
            <span> To implement this in ASP.NET MVC, we can utilize ActionFilterAttribute and override either OnActionExecuting or OnResultExecuting method. The below code snippet is being used to check whether the current request browser can accept GZIP/DEFLATE encoding by looking at Accept-Encoding request header. If it finds GZIP encoding in this header, then we would set gzip in Content-encoding in response header and if it supports DEFLATE, then this code would set deflate in Content-encoding.</span>
            <pre>               

​<code class="language-sh">
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

            string acceptEncoding = request.Headers[&quot;Accept-Encoding&quot;];

            if (string.IsNullOrEmpty(acceptEncoding)) return;

            acceptEncoding = acceptEncoding.ToUpperInvariant();

            HttpResponseBase response = filterContext.HttpContext.Response;

            if (acceptEncoding.Contains(&quot;GZIP&quot;))
            &#123;
                response.AppendHeader(&quot;Content-encoding&quot;, &quot;gzip&quot;);
                response.Filter = new GZipStream(response.Filter, CompressionMode.Compress);
            &#125;
            else if (acceptEncoding.Contains(&quot;DEFLATE&quot;))
            &#123;
                response.AppendHeader(&quot;Content-encoding&quot;, &quot;deflate&quot;);
                response.Filter = new DeflateStream(response.Filter, CompressionMode.Compress);
            &#125;
        &#125;
    &#125;
&#125;​​
</code>
</pre> 
            <pre>                                          
<code class="language-sh">
[Compress] 
 public ActionResult About() ​
 &#123; 
    ViewBag.Message = &quot;Your application description&quot;; 
    return View(); 
 &#125; 
</code>​​
</pre> </span><span style="background-color&#58;initial;"><pre><img src="/SiteAssets/do-you-use-gzip/5.28.6.png" alt="5.28.6.png" style="margin&#58;5px;width&#58;808px;" /><br></pre></span><dd class="ssw15-rteElement-FigureBad">​Figure&#58; Bad&#160;Example​, files with large size and slow load&#160;time.<br>​<br></dd><p class="ssw15-rteElement-P">​​​<img src="/SiteAssets/do-you-use-gzip/5.28.7.png" alt="5.28.7.png" style="margin&#58;5px;width&#58;808px;" /><br></p><dd class="ssw15-rteElement-FigureGood">​​​​Figure&#58; Good Example​, gzipped&#160;files with smaller&#160;size&#160;and faster load time.<br><br></dd><br></ul>​<br><br><br><br></div></ul>


