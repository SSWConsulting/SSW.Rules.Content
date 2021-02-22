---
type: rule
archivedreason: 
title: Do you tell your designers to only use classes?
guid: 516aac5a-c691-4e58-af66-a87f8105e44a
uri: do-you-tell-your-designers-to-only-use-classes
created: 2013-04-10T21:08:06.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

In Sitefinity you can alter the appearance and content areas on your webpage using "Layouts". These layouts are basically just Divs with sizes applied.

<!--endintro-->

![Figure: You have the ability to assign a Class to a Div only. No other customisations can be made](sitefinity-class-only.jpg)  

Additionally, Sitefinity will hard code the widths of the layout and there is no way to stop it.
 The hack work around is to manually remove the widths via JQuery:


::: greybox

$(".sf\_colsOut").css("width", "");

:::
