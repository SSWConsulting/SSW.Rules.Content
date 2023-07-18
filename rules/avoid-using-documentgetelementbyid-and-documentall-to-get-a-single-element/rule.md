---
type: rule
title: Do you avoid using document.getElementById(id) and document.all(id) to
  get a single element, instead use selector $(#id)?
uri: avoid-using-documentgetelementbyid-and-documentall-to-get-a-single-element
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-avoid-using-document-getelementbyidid-and-document-allid-to-get-a-single-element-instead-use-selector-id
  - do-you-avoid-using-document-getelementbyid(id)-and-document-all(id)-to-get-a-single-element-instead-use-selector-(id)
created: 2016-11-17T15:17:08.000Z
archivedreason: null
guid: 9ddcb98a-a721-4191-af87-3109043184f8
---

`$(#id)` is a selector of jQuery. It gets the single element with the given id.

[jQuery](https://jquery.com/) is a fast and concise JavaScript Library that simplifies how you traverse HTML documents, handle events, perform animations, and add Ajax interactions to your web pages. jQuery is designed to change the way that you write JavaScript.

<!--endintro-->

With jQuery, you can write less code but do more work.

```html
<h1 id="Head1">Hello</h1> 
<script type="text/javascript" language="javascript">
    document.all("Head1").style.color="red"; 
</script>
```
::: bad
Figure - Bad Code  
:::

```html
<h1 id="Head1">Hello</h1> 
<script type="text/javascript" language="javascript">
    document.getElementById("Head1").style.color="red"; 
</script>
```
::: bad
Figure: Bad Code  
:::

```html
<h1 id="Head1">Hello</h1> 
<script type="text/javascript" language="javascript">
    $("#Head1").css("color","red"); 
</script>
```
::: good
Figure: Good Code - Using $("#Head1")
:::
