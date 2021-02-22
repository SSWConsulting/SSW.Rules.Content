---
type: rule
archivedreason: 
title: Do you use Gzip?
guid: 90f6c345-3fee-4f69-bda3-d16b31447142
uri: do-you-use-gzip
created: 2019-05-17T03:05:06.0000000Z
authors:
- title: Barry Sanders
  url: https://ssw.com.au/people/barry-sanders
related: []
redirects: []

---


​Gzip is a file format and a software application used for file compression and decompression.<br>Gzip can reduce file size and storage space, and reduce transmission time when transferring files over the network. It runs on both Linux and Windows.<div><br></div>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-P">​Use PageSpeed Insights extension in Chrome to determine if your site will benefit from using Gzip. </p><p class="ssw15-rteElement-P">For more information about how to use PageSpeed to find which files on your site would benefit from being compressed with Gzip see <a href=/do-you-use-pagespeed target="_blank">Do-you-use-PageSpeed</a>.​<br></p><p class="ssw15-rteElement-P"><strong>​<br>​</strong><strong>Three ways to add Gzip compression to your site: ​</strong></p><p class="ssw15-rteElement-P">Use one of the methods described below to add Gzip compression to your site ASP.Net/Angular website</p><p class="ssw15-rteElement-Tip">​<br></p><ul><li>Method 1: Turn on "Dynamic Content Compression" In IIS Server. <img src="2.png" alt="2.png" style="background-color:initial;margin:5px;width:808px;" />Figure: Choose the website which you want to use Gzip and click on Compression.​​​​<img src="3.png" alt="3.png" style="background-color:initial;margin:5px;width:808px;" />Figure: Install "dynamic content compression" if you haven't installed it.​<br></li> 
   <br> ​​<br> In 
   <strong>Control Panel</strong> navigate to 
   <strong> All Control Panel Items | Programs and Features </strong>, and click 
   <strong>Turn Windows features on or off</strong>.<br>Choose 
   <strong>Internet Information Services | Web Management Tools | World Wide Web Services | Performance Features | Dynamic Content  ​</strong><strong>Compression</strong>.<img src="4.png" alt="4.png" style="background-color:initial;margin:5px;width:808px;" />Figure : Click "Ok" to<span style="background-color:initial;"> install it.</span><span style="background-color:initial;">​</span><span style="background-color:initial;">​</span><img src="5.png" alt="5.png" style="background-color:initial;margin:5px;width:808px;" />Figure: now enable dynamic content compression for your site. 
   <div> 
      <br> 
      <ul><li>​​<strong>​</strong>​Method 2:  Using “Gzipper” in your Angular website​<br></li> Follow  
         <span style="background-color:initial;"> 
            <a href="https://www.npmjs.com/package/gzipper">https://www.npmjs.com/package/gzipper</a> .(but it still need IIS Server enable static content compression.) </span>
         <span style="background-color:initial;">​<br></span>Using "npm i gzipper g" to install "gzipper" first. Add to scripts in your package.json​​​​<br><img src="7.png" alt="7.png" style="margin:5px;width:808px;" /><br><br><img src="6.png" alt="6.png" style="margin:5px;width:808px;" />Figure: "Finish configuration like that. 
         <br><br>
         <li>Method 3: ​​​​​​​​​​Using ASP.NET code in MVC​<br></li> Refer to 
         <span style="background-color:initial;"> 
            <a href="https://www.codeproject.com/Tips/1080065/Improve-the-Performance-of-ASP-NET-MVC-Web-Applica">https://www.codeproject.com/Tips/1080065/Improve-the-Performance-of-ASP-NET-MVC-Web-Applica</a> . ​ 
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
{
    public class CompressAttribute : ActionFilterAttribute
    {
        public override void OnResultExecuting(ResultExecutingContext filterContext)
        {
            HttpRequestBase request = filterContext.HttpContext.Request;

            string acceptEncoding = request.Headers["Accept-Encoding"];

            if (string.IsNullOrEmpty(acceptEncoding)) return;

            acceptEncoding = acceptEncoding.ToUpperInvariant();

            HttpResponseBase response = filterContext.HttpContext.Response;

            if (acceptEncoding.Contains("GZIP"))
            {
                response.AppendHeader("Content-encoding", "gzip");
                response.Filter = new GZipStream(response.Filter, CompressionMode.Compress);
            }
            else if (acceptEncoding.Contains("DEFLATE"))
            {
                response.AppendHeader("Content-encoding", "deflate");
                response.Filter = new DeflateStream(response.Filter, CompressionMode.Compress);
            }
        }
    }
}​​
</code>
</pre> 
            <pre>                                          
<code class="language-sh">
[Compress] 
 public ActionResult About() ​
 { 
    ViewBag.Message = "Your application description"; 
    return View(); 
 } 
</code>​​
</pre> </span><span style="background-color:initial;"><pre><img src="5.28.6.png" alt="5.28.6.png" style="margin:5px;width:808px;" /><br></pre></span><dd class="ssw15-rteElement-FigureBad">​Figure: Bad Example​, files with large size and slow load time.<br>​<br></dd><p class="ssw15-rteElement-P">​​​<img src="5.28.7.png" alt="5.28.7.png" style="margin:5px;width:808px;" /><br></p><dd class="ssw15-rteElement-FigureGood">​​​​Figure: Good Example​, gzipped files with smaller size and faster load time.<br><br></dd><br></ul>​<br><br><br><br></div></ul>


