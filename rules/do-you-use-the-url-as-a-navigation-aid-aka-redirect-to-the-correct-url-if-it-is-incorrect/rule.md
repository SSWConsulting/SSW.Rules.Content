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



<span class='intro'> <dl class="image"><iframe width="560" height="315" src="http&#58;//www.youtube.com/embed/1j3m4A9Tlhc" frameborder="0"></iframe> 
<dd>Figure&#58; Watch the URL working as a navigation aid</dd></dl><p>MVC gives us great URLs, but you need to help users navigate via the URL.  If the user changes a URL, and the route parameters no longer match, you should correct them with a redirect.</p> </span>

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
</pre></div></dt><dd><span class="ssw-rteStyle-FigureGood">Figure&#58; Good example - the comment says it all</span></dd></dl>

Wordpress and Stack Overflow&#160;have&#160;URL formats that&#160;do&#160;this very well&#58;<div><br></div><div><span class="ssw-rteStyle-CodeArea">http&#58;//tv.ssw.com/3102/business-value</span><span class="ssw-rteStyle-FigureGood">Good example&#58;&#160;If the &quot;business-value&quot; part of the URL changes, the page will redirect to the correct location.</span></div><div><br></div><div><span class="ssw-rteStyle-CodeArea">http&#58;//stackoverflow.com/questions/729921/settimeout-or-setinterval</span></div><div><span class="ssw-rteStyle-FigureGood">Figure&#58; Good example -&#160;If the &quot;settimeout-or-setinterval&quot; part of th eURL changes, the page will redirect to the correct location.</span></div>


