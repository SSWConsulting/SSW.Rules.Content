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

Gzip is a file format and a software application used for file compression and decompression.
Gzip can reduce file size and storage space, and reduce transmission time when transferring files over the network. It runs on both Linux and Windows.



<!--endintro-->

Use PageSpeed Insights extension in Chrome to determine if your site will benefit from using Gzip.

For more information about how to use PageSpeed to find which files on your site would benefit from being compressed with Gzip see [Do-you-use-PageSpeed](/do-you-use-pagespeed).

**
** **Three ways to add Gzip compression to your site:**

Use one of the methods described below to add Gzip compression to your site ASP.Net/Angular website



* Method 1: Turn on "Dynamic Content Compression" In IIS Server. ![](2.png)Figure: Choose the website which you want to use Gzip and click on Compression.![](3.png)Figure: Install "dynamic content compression" if you haven't installed it.


In**Control Panel**navigate to**All Control Panel Items | Programs and Features**, and click**Turn Windows features on or off**.
Choose**Internet Information Services | Web Management Tools | World Wide Web Services | Performance Features | Dynamic Content****Compression**.![](4.png)Figure : Click "Ok" to install it.![](5.png)Figure: now enable dynamic content compression for your site.


    * Method 2:  Using “Gzipper” in your Angular website
Followhttps://www.npmjs.com/package/gzipper .(but it still need IIS Server enable static content compression.) 
Using "npm i gzipper g" to install "gzipper" first. Add to scripts in your package.json
![](7.png)

![](6.png)Figure: "Finish configuration like that.

    * Method 3: Using ASP.NET code in MVC
Refer tohttps://www.codeproject.com/Tips/1080065/Improve-the-Performance-of-ASP-NET-MVC-Web-Applica .  <br>             To implement this in ASP.NET MVC, we can utilize ActionFilterAttribute and override either OnActionExecuting or OnResultExecuting method. The below code snippet is being used to check whether the current request browser can accept GZIP/DEFLATE encoding by looking at Accept-Encoding request header. If it finds GZIP encoding in this header, then we would set gzip in Content-encoding in response header and if it supports DEFLATE, then this code would set deflate in Content-encoding.

```sh
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
}
```



```sh
[Compress] 
 public ActionResult About() 
 { 
    ViewBag.Message = "Your application description"; 
    return View(); 
 }
```

 
::: bad
Figure: Bad Example, files with large size and slow load time.


:::
        ![](5.28.7.png)

::: good
Figure: Good Example, gzipped files with smaller size and faster load time.


:::
