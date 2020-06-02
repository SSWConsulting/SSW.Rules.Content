

---
uri: do-you-avoid-making-changes-to-individual-css-styles-using-jquery
title: Do you avoid making changes to individual CSS styles using jQuery?
created: YYYY-07-DD 18:13:03
authors:
  - id: 16
    title: Tiago Araujo
---




<span class='intro'> <p>We all know that jQuery is very powerful and can do a lot of stuff, including style changes. However, this practice is bad.</p> </span>

<p>Instead of changing the appearance of elements with jQuery, you should use CSS classes. This way you can keep all your CSS in your CSS files, specify different appearances for different classes.</p>

<p>It's OK to use jQuery to add or remove classes and apply your CSS. For this we can use .addClass() and .removeClass() methods.</p>


