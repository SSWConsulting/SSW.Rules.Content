---
type: rule
archivedreason: 
title: Do you use display classes to responsively hide/show content?
guid: 516a0486-d6d5-4ca2-9171-356115874c60
uri: do-you-use-hidden-visible-classes-when-resizing-to-hide-show-content
created: 2014-06-18T05:16:40.0000000Z
authors:
- title: Ben Cull
  url: https://ssw.com.au/people/ben-cull
related: []
redirects: []

---

When designing responsive websites, it's important to consider what content is appropriate for each screen size. Desktops might have large navigation areas and extra content in a sidebar, whereas the phone might focus on other content.

<!--endintro-->

By default, Bootstrap will wrap the columns and make them full width on phones. If you want to hide content rather than let it wrap you can use the `.d-none` class or one of the `.d-{sm,md,lg,xl}-none` classes for any responsive screen variation.

More information on [Display property - Quickly and responsively toggle the display value of components and more with our display utilities](https://getbootstrap.com/docs/4.0/utilities/display/#how-it-works).

::: bad  
![Figure: Bad Example - The mobile view on the right has a large unneccessary title](RulesBootstrap - hidden.png)  
:::

Remove the title by adding the .hidden-xs class.

``` html
<h1 class="d-xl-none">ASP.NET</h1>
```

::: good  
![Figure: Good example - The mobile view is now leaner and cleaner thanks to Bootstrap display classes](RulesBootstrap - hidden2.png)  
:::
