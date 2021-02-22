---
type: rule
archivedreason: 
title: Do you avoid making changes to individual CSS styles using jQuery?
guid: 2adca90a-3482-44f5-a3d4-06391521cf0a
uri: do-you-avoid-making-changes-to-individual-css-styles-using-jquery
created: 2012-07-24T18:13:03.0000000Z
authors:
- title: Tiago Araujo
  url: https://ssw.com.au/people/tiago-araujo
related: []
redirects: []

---

We all know that jQuery is very powerful and can do a lot of stuff, including style changes. However, this practice is bad.

<!--endintro-->

Instead of changing the appearance of elements with jQuery, you should use CSS classes. This way you can keep all your CSS in your CSS files, specify different appearances for different classes.

It's OK to use jQuery to add or remove classes and apply your CSS. For this we can use .addClass() and .removeClass() methods.
