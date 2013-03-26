---
type: rule
title: Do you use the URL as a navigation aid (aka redirect to the correct url if it is incorrect)?
uri: do-you-use-the-url-as-a-navigation-aid-aka-redirect-to-the-correct-url-if-it-is-incorrect
created: 2013-03-26T20:26:11.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 23
  title: Damian Brady

---



<span class='intro'> <p>MVC gives us great URLs, but you need to help users navigate via the URL.  If the user changes a URL, and the route parameters no longer match, you should correct them with a redirect.</p> </span>

<dl class="image"><dt><div class="greyBox"><pre>public ActionResult Edit(string employeename, int id)
&#123;
    var model = _repository.GetEmployee(id);

    // check for a parameter match and redirect if incorrect
    if (string.IsNullOrEmpty(employeename) || employeename != model.EmployeeName)
    &#123;
        return RedirectToAction(
            &quot;Edit&quot;, new &#123; employeename = model.EmployeeName, id &#125;);
    &#125;

    return View(model);
&#125;
</pre></div>
   </dt><dd>Figure&#58; Good example - the comment says it all</dd></dl>


