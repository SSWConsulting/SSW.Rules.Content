---
type: rule
title: Do you use the Authorize attribute to secure actions or controllers?
uri: do-you-use-the-authorize-attribute-to-secure-actions-or-controllers
created: 2013-03-07T18:44:09.0000000Z
authors:
- id: 23
  title: Damian Brady

---



<span class='intro'> <p>ASP.NET MVC provides the <a href="http&#58;//www.google.com.au/url?sa=t&amp;source=web&amp;cd=1&amp;ved=0CBQQFjAA&amp;url=http&#58;//msdn.microsoft.com/en-us/library/system.web.mvc.authorizeattribute.aspx&amp;ei=1ZBrTN2_LMjIcbOgpVU&amp;usg=AFQjCNEHsdmOFBGQVLASZUrcBHMvch4x-g" target="_blank">AuthorizeAttribute</a> which ensures there is a logged in user before it will execute an action. You can also provide parameters to restrict actions or controllers to only be accessible to certain roles or users. This is a better solution than checking whether a logged in user exists in code as the authorisation itself doesn’t need to be repeated.</p> </span>

<dl class="badImage"><dt><div class="greyBox"><pre>public ActionResult Delete(string tagName)
&#123;
    if (!Request.RequestContext.HttpContext.User.IsInRole(&quot;CanDeleteTags&quot;))
    &#123;
        return new System.Web.Mvc.HttpUnauthorizedResult();
    &#125;
    // delete view
    return View();
&#125;
</pre></div></dt><dd>Figure&#58; Bad Example – Checking for an appropriate role in code leads to repetition </dd></dl><dl class="goodImage"><dt><div class="greyBox"><pre>[Authorize(Roles = &quot;CanDeleteTags&quot;)]
public ActionResult Delete(string tagName)
&#123;
    // ...delete tag
    return View();
&#125;
</pre></div></dt><dd>Figure&#58; Good Example – Using the Authorize attribute to check for appropriate roles</dd></dl>


