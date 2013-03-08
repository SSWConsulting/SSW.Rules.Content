---
type: rule
title: Do you use Anti Forgery Tokens on any page that takes a POST?
uri: do-you-use-anti-forgery-tokens-on-any-page-that-takes-a-post
created: 2013-03-08T14:57:32.0000000Z
authors:
- id: 23
  title: Damian Brady

---



<span class='intro'> <p>To prevent cross-site request forgery (XSRF), you should use Html.AntiForgeryToken. On the action which takes the post request, place the ValidateAntiForgeryToken attribute to enable the request to validate.  Doing this ensures that the post is a direct response to the page that was given to this user so only verified posts will be processed.</p> </span>

<dl class="badImage"><dt><div class="greyBox"><pre>@using (Html.BeginForm()) &#123;
    @Html.ValidationSummary(true)

    &lt;div class=&quot;editor-label&quot;&gt;
        @Html.LabelFor(model =&gt; model.Name)
    &lt;/div&gt;
    &lt;div class=&quot;editor-field&quot;&gt;
        @Html.EditorFor(model =&gt; model.Name)
        @Html.ValidationMessageFor(model =&gt; model.Name)
    &lt;/div&gt;

    &lt;p&gt;
        &lt;input type=&quot;submit&quot; value=&quot;Create&quot; /&gt;
    &lt;/p&gt;
 &#125;
      </pre></div></dt><dd>Figure&#58; Bad Example – The page is potentially vulnerable to XSRF attacks. Any post will be accepted by the server</dd></dl><dl class="goodImage"><dt><div class="greyBox"><pre>            <em>View&#58;</em>

@using (Html.BeginForm()) &#123;
    @Html.AntiForgeryToken()
    @Html.ValidationSummary(true)

    &lt;div class=&quot;editor-label&quot;&gt;
        @Html.LabelFor(model =&gt; model.Name)
    &lt;/div&gt;
    &lt;div class=&quot;editor-field&quot;&gt;
        @Html.EditorFor(model =&gt; model.Name)
        @Html.ValidationMessageFor(model =&gt; model.Name)
    &lt;/div&gt;

    &lt;p&gt;
        
            &lt;input type=&quot;submit&quot; value=&quot;Create&quot;/&gt;
    &lt;/p&gt;
&#125;

<em>Controller&#58;</em>

[ValidateAntiForgeryToken]
public ActionResult Create(CreateModel model)
&#123;
    // save data
&#125;

      </pre></div></dt><dd>Figure&#58; Good Example – The page is no longer vulnerable to XSRF attacks</dd></dl>


