---
type: rule
title: Do you use Anti Forgery Tokens on any page that takes a POST?
uri: do-you-use-anti-forgery-tokens-on-any-page-that-takes-a-post
authors:
  - title: Damian Brady
    url: https://ssw.com.au/people/damian-brady
related: []
redirects: []
created: 2013-03-08T14:57:32.000Z
archivedreason: null
guid: 4d370343-7442-4305-b1ee-1d175f4184f4
---

To prevent cross-site request forgery (XSRF), you should use Html.AntiForgeryToken. On the action which takes the post request, place the ValidateAntiForgeryToken attribute to enable the request to validate.  Doing this ensures that the post is a direct response to the page that was given to this user so only verified posts will be processed.

<!--endintro-->

```cs
@using (Html.BeginForm()) {
    @Html.ValidationSummary(true)

    <div class="editor-label">
        @Html.LabelFor(model => model.Name)
    </div>
    <div class="editor-field">
        @Html.EditorFor(model => model.Name)
        @Html.ValidationMessageFor(model => model.Name)
    </div>

    <p>
        <input type="submit" value="Create" />
    </p>
 }
```
::: bad
Figure: Bad example – The page is potentially vulnerable to XSRF attacks. Any post will be accepted by the server
:::

```cs
View:

@using (Html.BeginForm()) {
    @Html.AntiForgeryToken()
    @Html.ValidationSummary(true)

    <div class="editor-label">
        @Html.LabelFor(model => model.Name)
    </div>
    <div class="editor-field">
        @Html.EditorFor(model => model.Name)
        @Html.ValidationMessageFor(model => model.Name)
    </div>

    <p>
        
            <input type="submit" value="Create"/>
    </p>
}

Controller:

[ValidateAntiForgeryToken]
public ActionResult Create(CreateModel model)
{
    // save data
}
```
::: good
Figure: Good example – The page is no longer vulnerable to XSRF attacks
:::
