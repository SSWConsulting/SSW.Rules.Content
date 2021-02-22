---
type: rule
archivedreason: 
title: Do you write integration tests to validate your web links?
guid: dfa6be65-2251-442d-8a9e-ead15d505dce
uri: write-integration-tests-to-validate-your-web-links
created: 2020-03-11T22:50:56.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-write-integration-tests-to-validate-your-web-links

---


If you store your URL references in the application settings, you can create integration tests to validate them.<br>
<br><excerpt class='endintro'></excerpt><br>
<dl class="image"><dt>​<img src="testURLSettings.gif" alt="testURLSettings.gif" style="width:750px;" />​</dt><dd>Figure: URL for link stored in application settings</dd></dl><p>
   <b>​Sample Code: How to test the URL</b></p><p class="ssw15-rteElement-CodeArea">	[Test]<br> public void urlRulesToBetterInterfaces()<br> {<br> HttpStatusCode result = WebAccessTester.GetWebPageStatusCode(Settings.Default.urlRulesToBetterInterfaces);<br> Assert.IsTrue(result == HttpStatusCode.OK, result.ToString());<br> }</p><p>	
   <br>
   <b>Sample Code: Method used to verify the Page</b><br></p><p class="ssw15-rteElement-CodeArea">	 public class WebAccessTester<br> { 
   <br> public static HttpStatusCode GetWebPageStatusCode(string url)<br> {<br> HttpWebRequest req = ((HttpWebRequest)(WebRequest.Create(url)));<br> req.Proxy = new WebProxy();<br> req.Proxy.Credentials = CredentialCache.DefaultCredentials;<br> HttpWebResponse resp = null;<br> try<br> {<br> resp = ((HttpWebResponse)(req.GetResponse()));<br> if (resp.StatusCode == HttpStatusCode.OK)<br> {<br> if (url.ToLower().IndexOf("redirect") == -1 && url.ToLower().IndexOf(resp.ResponseUri.AbsolutePath.ToLower()) == -1)<br> {<br> return HttpStatusCode.NotFound;<br> }<br> }<br> }<br> catch (System.Exception ex)<br> {JavaScript<br> while (!(ex == null))<br> {<br> Console.WriteLine(ex.ToString());<br> Console.WriteLine("INNER EXCEPTION");<br> ex = ex.InnerException;<br> }<br> }<br> finally<br> {<br> if (!(resp == null))<br> {<br> resp.Close();<br> }<br> }<br> return resp.StatusCode;<br> }<br> }</p><p> ​<br></p>


