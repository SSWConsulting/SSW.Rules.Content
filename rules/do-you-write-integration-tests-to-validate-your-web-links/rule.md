---
type: rule
title: Do you write integration tests to validate your web links?
uri: do-you-write-integration-tests-to-validate-your-web-links
created: 2020-03-11T22:50:56.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> If you store your URL references in the application settings, you can create integration tests to validate them.<br> </span>

<dl class="image"><dt>​<img src="testURLSettings.gif" alt="testURLSettings.gif" style="width&#58;750px;" />​</dt><dd>Figure&#58; URL for link stored in application settings</dd></dl><p>
   <b>​Sample Code&#58; How to test the URL</b></p><p class="ssw15-rteElement-CodeArea">	[Test]<br> public void urlRulesToBetterInterfaces()<br> &#123;<br> HttpStatusCode result = WebAccessTester.GetWebPageStatusCode(Settings.Default.urlRulesToBetterInterfaces);<br> Assert.IsTrue(result == HttpStatusCode.OK, result.ToString());<br> &#125;</p><p>	
   <br>
   <b>Sample Code&#58; Method used to verify the Page</b><br></p><p class="ssw15-rteElement-CodeArea">	 public class WebAccessTester<br> &#123; 
   <br> public static HttpStatusCode GetWebPageStatusCode(string url)<br> &#123;<br> HttpWebRequest req = ((HttpWebRequest)(WebRequest.Create(url)));<br> req.Proxy = new WebProxy();<br> req.Proxy.Credentials = CredentialCache.DefaultCredentials;<br> HttpWebResponse resp = null;<br> try<br> &#123;<br> resp = ((HttpWebResponse)(req.GetResponse()));<br> if (resp.StatusCode == HttpStatusCode.OK)<br> &#123;<br> if (url.ToLower().IndexOf(&quot;redirect&quot;) == -1 &amp;&amp; url.ToLower().IndexOf(resp.ResponseUri.AbsolutePath.ToLower()) == -1)<br> &#123;<br> return HttpStatusCode.NotFound;<br> &#125;<br> &#125;<br> &#125;<br> catch (System.Exception ex)<br> &#123;JavaScript<br> while (!(ex == null))<br> &#123;<br> Console.WriteLine(ex.ToString());<br> Console.WriteLine(&quot;INNER EXCEPTION&quot;);<br> ex = ex.InnerException;<br> &#125;<br> &#125;<br> finally<br> &#123;<br> if (!(resp == null))<br> &#123;<br> resp.Close();<br> &#125;<br> &#125;<br> return resp.StatusCode;<br> &#125;<br> &#125;</p><p> ​<br></p>


