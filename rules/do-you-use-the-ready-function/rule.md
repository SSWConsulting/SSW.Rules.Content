---
type: rule
archivedreason: 
title: Do you use the .ready() function?
guid: 2a68ef85-90db-41a7-8042-b152668b9462
uri: do-you-use-the-ready-function
created: 2013-04-29T06:39:55.0000000Z
authors:
- title: Damian Brady
  url: https://ssw.com.au/people/damian-brady
related:
- do-you-know-which-version-of-jquery-to-use
redirects:
- do-you-use-the-ready()-function

---

Putting your initialization JavaScript code inside the `.ready()` function is not always required, but it's much safer to do so. 

<!--endintro-->

jQuery exposes a [.ready() event](https://api.jquery.com/ready) which fires when the Document Object Model (DOM) is fully loaded and ready to be manipulated.

You can attach a function to this event so you can be sure the page is ready for you to work on.

```js
$('#login').addClass('hidden');
```
::: bad
Figure: Bad example - If this jQuery is in the wrong place, the #login element may not exist!
:::

```js
$(function() {
    $('#login').addClass('hidden');
});
```
::: good
Figure: Good example - This code won't run until the DOM is fully loaded
:::
