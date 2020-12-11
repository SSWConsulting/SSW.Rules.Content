---
type: rule
archivedreason: 
title: Do you use the Authorize attribute to secure actions or controllers?
guid: 31714273-ddd8-4d9a-8173-4601244dd866
uri: do-you-use-the-authorize-attribute-to-secure-actions-or-controllers
created: 2013-03-07T18:44:09.0000000Z
authors:
- id: 23
  title: Damian Brady
related: []

---

ASP.NET MVC provides the [AuthorizeAttribute](https&#58;//msdn.microsoft.com/en-us/library/system.web.mvc.authorizeattribute.aspx) which ensures there is a logged in user before it will execute an action. You can also provide parameters to restrict actions or controllers to only be accessible to certain roles or users. This is a better solution than checking whether a logged-in user exists in code as the authorisation itself doesn’t need to be repeated.

<!--endintro-->
<dl class="badImage">&lt;dt&gt;<br><br>::: greybox<br><pre>public ActionResult Delete(string tagName)
&#123;
    if (!Request.RequestContext.HttpContext.User.IsInRole(&quot;CanDeleteTags&quot;))
    &#123;
        return new System.Web.Mvc.HttpUnauthorizedResult();
    &#125;
    // delete view
    return View();
&#125;
</pre><br>:::<br><br>&lt;/dt&gt;<dd>Figure&#58; Bad Example – Checking for an appropriate role in code leads to repetition </dd></dl><dl class="goodImage">&lt;dt&gt;<br><br>::: greybox<br><pre>[Authorize(Roles = &quot;CanDeleteTags&quot;)]
public ActionResult Delete(string tagName)
&#123;
    // ...delete tag
    return View();
&#125;
</pre><br>:::<br><br>&lt;/dt&gt;<dd>Figure&#58; Good Example – Using the Authorize attribute to check for appropriate roles</dd></dl>
