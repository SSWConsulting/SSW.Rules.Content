---
type: rule
archivedreason: 
title: Do you use View Models instead of ViewData?
guid: ad2abb14-7013-4ab0-ac89-d362914640d5
uri: do-you-use-view-models-instead-of-viewdata
created: 2013-03-07T18:23:38.0000000Z
authors:
- title: Damian Brady
  url: https://ssw.com.au/people/damian-brady
related: []
redirects: []

---


<p>MVC provides a ViewData collection in which you can store miscellaneous pieces of information to pass to the View.&#160; It’s also accessible it as a Dynamic object by using the ViewBag.&#160; However, you should avoid using ViewData or ViewBag because it isn’t type-safe and relies on <a href="http&#58;//en.wikipedia.org/wiki/Magic_string">Magic Strings</a>.</p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="badImage"><dt><div class="greyBox"><pre>public ActionResult Index() &#123;
  ViewData[&quot;Message&quot;] = &quot;Some Message&quot;;
  return View();
&#125;
 
&lt;h1&gt;&lt;%&#58; ViewData[&quot;Message&quot;] &amp;&gt;&lt;/h1&gt;

</pre></div></dt><dd>Figure&#58; Bad Example – ViewData being used to pass information to the View isn’t type-safe</dd></dl><dl class="goodImage"><dt><div class="greyBox"><pre>public ActionResult Index() &#123;
  var model = new IndexViewModel();
  model.Message = &quot;Some Message&quot;;
  return View();
&#125;
 
&lt;h1&gt;&lt;%&#58; Model.Message %&gt;&lt;/h1&gt;

</pre></div></dt><dd>Figure&#58; Good Example – Using a ViewModel is a safer way to pass data</dd></dl>


