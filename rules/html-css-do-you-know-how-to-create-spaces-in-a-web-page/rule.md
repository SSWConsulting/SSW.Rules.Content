---
type: rule
archivedreason: 
title: HTML/CSS - Do you know how to create spaces in a web page?
guid: 4586408c-b6a1-40ab-81c4-55dc91d631b1
uri: html-css-do-you-know-how-to-create-spaces-in-a-web-page
created: 2012-07-02T14:19:41.0000000Z
authors:
- title: Tiago Araujo
  url: https://ssw.com.au/people/tiago-araujo
related: []
redirects: []

---

There are many scenarios where you need some extra space in a web page. No matter which one you are at, CSS is the answer.

<!--endintro-->

Sometimes the first thing that comes to the developer mind is to use the "break line" tag (&lt;br /&gt;) or the [ASCII character code](https://en.wikipedia.org/wiki/ASCII) for "space" (&#160;) to create these extra spaces. It's wrong. CSS is the way to go. You can use both "margin" or "padding" CSS properties to get the result you want.


``` html
<ul>
  <li>&#160;&#160;&#160;List item</li>
</ul>

```
::: bad
Figure: Bad Example - Using the "space" ASCII character to create a padding on that list
:::

``` html
<ul>
  <li>List item</li>
</ul>
<br />
<br />
<br />
```
::: bad
Figure: Bad Example - Using the &lt;br /&gt; tag to create a space at the bottom of that list
:::

``` css
ul {margin-bottom:15px;}
  ul li {padding-left:10px;}  
```
::: good
Figure: Good Example - Using CSS to add a margin at the bottom of the list a the padding on the left side of each list item
:::

**Tip:** You might be not familiar with editing a CSS file... In this case, contact a designer, they will be more than happy to help you.
