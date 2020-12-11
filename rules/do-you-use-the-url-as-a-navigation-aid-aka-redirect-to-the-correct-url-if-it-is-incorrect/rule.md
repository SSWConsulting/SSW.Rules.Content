---
type: rule
archivedreason: 
title: Do you use the URL as a navigation aid (aka redirect to the correct url if it is incorrect)?
guid: 7f894c9f-4c5f-4460-a5f0-cfe8e0fa5805
uri: do-you-use-the-url-as-a-navigation-aid-aka-redirect-to-the-correct-url-if-it-is-incorrect
created: 2013-03-26T20:26:11.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 23
  title: Damian Brady
related: []

---

<dl class="image"><br>`youtube: http&#58;//www.youtube.com/embed/1j3m4A9Tlhc`<br> 
<dd>Figure&#58; Watch the URL working as a navigation aid</dd></dl>
MVC gives us great URLs, but you need to help users navigate via the URL.  If the user changes a URL, and the route parameters no longer match, you should correct them with a redirect.

<!--endintro-->
<dl class="image">&lt;dt&gt;<br><br>::: greybox<br><pre>public ActionResult Edit(string employeename, int id)
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
</pre><br>:::<br><br>&lt;/dt&gt;<dd><span class="ssw-rteStyle-FigureGood">Figure&#58; Good example - the comment says it all</span></dd></dl>  Wordpress and Stack Overflow have URL formats that do this very well:



http://tv.ssw.com/3102/business-valueGood example: If the "business-value" part of the URL changes, the page will redirect to the correct location.




http://stackoverflow.com/questions/729921/settimeout-or-setinterval

Figure: Good example - If the "settimeout-or-setinterval" part of th eURL changes, the page will redirect to the correct location.
