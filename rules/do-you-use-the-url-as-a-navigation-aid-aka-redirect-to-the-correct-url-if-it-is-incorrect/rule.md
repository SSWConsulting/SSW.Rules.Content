---
type: rule
title: Do you use the URL as a navigation aid (aka redirect if URL is incorrect)?
uri: do-you-use-the-url-as-a-navigation-aid-aka-redirect-to-the-correct-url-if-it-is-incorrect
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Damian Brady
    url: https://ssw.com.au/people/damian-brady
related: []
redirects:
  - do-you-use-the-url-as-a-navigation-aid-(aka-redirect-to-the-correct-url-if-it-is-incorrect)
created: 2013-03-26T20:26:11.000Z
archivedreason: null
guid: 7f894c9f-4c5f-4460-a5f0-cfe8e0fa5805
---

`youtube: http://www.youtube.com/embed/1j3m4A9Tlhc`

**Figure: Watch the URL working as a navigation aid**

MVC gives us great URLs, but you need to help users navigate via the URL. If the user changes a URL, and the route parameters no longer match, you should correct them with a redirect.

<!--endintro-->

```cs
public ActionResult Edit(string employeename, int id)
{
    var model = _repository.GetEmployee(id);

    // check for a parameter match and redirect if incorrect
    if (string.IsNullOrEmpty(employeename) || employeename != model.EmployeeName)
    {
        return RedirectToAction(
            "Edit", new { employeename = model.EmployeeName, id });
    }

    return View(model);
}
```
::: good
Figure: Good example - The comment says it all  Wordpress and Stack Overflow have URL formats that do this very well
:::

::: greybox
http://stackoverflow.com/questions/729921/settimeout-or-setinterval
:::

::: good
Figure: Good example - If the "settimeout-or-setinterval" part of th eURL changes, the page will redirect to the correct location
:::
