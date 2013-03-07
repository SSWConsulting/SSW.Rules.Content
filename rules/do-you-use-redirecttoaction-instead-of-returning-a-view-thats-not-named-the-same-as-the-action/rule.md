---
type: rule
title: Do you use RedirectToAction instead of returning a view that’s not named the same as the action?
uri: do-you-use-redirecttoaction-instead-of-returning-a-view-thats-not-named-the-same-as-the-action
created: 2013-03-07T18:33:55.0000000Z
authors:
- id: 23
  title: Damian Brady

---



<span class='intro'> <p>Returning a view that is named differently to the action confuses the MVC process and can make the code difficult to maintain.</p> </span>

<p>In cases where data is posted, if you don't do a redirect and the user hits the refresh/reload button in the browser, the data can be is submitted more than once. This can lead to duplicate data being stored in your database.</p><p>Redirecting after posted data has been processed is called the 
   <a href="http&#58;//en.wikipedia.org/wiki/Post/Redirect/Get">Post-Redirect-Get (or PRG) pattern</a>.</p>
   
<dl class="badImage"><dt><div class="greyBox"><pre>[HttpPost]
public ActionResult Create(CreateModel model)
&#123;
    // ... save to DB, then&#58;
    ViewBag.Message = &quot;Successfully created &quot; + model.Name;
    return View(&quot;Success&quot;);
&#125;

</pre></div></dt><dd>Figure&#58; Bad Example – Returning a different view is misleading and potentially dangerous</dd></dl><dl class="goodImage"><dt><div class="greyBox"><pre>[HttpPost]
public ActionResult Create(CreateModel model)
&#123;
    // ... save to DB, then&#58;
    return RedirectToAction(&quot;Success&quot;, new &#123; message = &quot;Successfully created &quot; + model.Name &#125;);
&#125;

public ActionResult Success(string message)
&#123;
    ViewBag.Message = message;
    return View();
&#125;

</pre></div></dt><dd>Figure&#58; Good Example – Using the PRG pattern to avoid duplicate data being posted</dd></dl>


