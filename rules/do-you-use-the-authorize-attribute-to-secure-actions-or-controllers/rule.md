---
type: rule
archivedreason: 
title: Do you use AuthorizeAttribute to secure actions or controllers?
guid: 31714273-ddd8-4d9a-8173-4601244dd866
uri: do-you-use-the-authorize-attribute-to-secure-actions-or-controllers
created: 2013-03-07T18:44:09.0000000Z
authors:
- title: Damian Brady
  url: https://ssw.com.au/people/damian-brady
related: []
redirects: []

---

ASP.NET MVC provides the [AuthorizeAttribute](https://msdn.microsoft.com/en-us/library/system.web.mvc.authorizeattribute.aspx) which ensures there is a logged in user before it will execute an action. You can also provide parameters to restrict actions or controllers to only be accessible to certain roles or users. This is a better solution than checking whether a logged-in user exists in code as the authorisation itself doesn’t need to be repeated.

<!--endintro-->

::: greybox

``` cs
public ActionResult Delete(string tagName)
{
    if (!Request.RequestContext.HttpContext.User.IsInRole("CanDeleteTags"))
    {
        return new System.Web.Mvc.HttpUnauthorizedResult();
    }
    // delete view
    return View();
}
```
::: bad
Figure: Bad Example – Checking for an appropriate role in code leads to repetition 
:::

``` cs
[Authorize(Roles = "CanDeleteTags")]
public ActionResult Delete(string tagName)
{
    // ...delete tag
    return View();
}
```
::: good
Figure: Good Example – Using the AuthorizeAttribute to check for appropriate roles
:::
