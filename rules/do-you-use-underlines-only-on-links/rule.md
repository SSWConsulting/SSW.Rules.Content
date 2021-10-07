---
type: rule
archivedreason: 
title: Do you use underlines on links?
guid: b55df040-7424-48e4-b19b-14d4bcdcfbc7
uri: do-you-use-underlines-only-on-links
created: 2015-02-16T01:26:10.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Rebecca Liu
  url: https://ssw.com.au/people/rebecca-liu
- title: Tiago Araujo
  url: https://ssw.com.au/people/tiago-araujo
related: []
redirects:
- do-you-use-underlines-on-links

---

It's very important that your links stand out from the background as well as the surrounding text.

**Always make links underlined** - Users expect underlined texts to be a link; and links to be undelined. You can [use a different color on underlines](https://www.w3schools.com/cssref/css3_pr_text-decoration-color.asp) as a nice touch.

::: info
Note: This is **not** necessary on obvious links, like menus or buttons.
:::

**Never underline a text that isn't a link** - Use bold if you need emphasis.

#### Mouse hovering

Rollovers are also important as they offer visual feedback to a user that this link that will take them somewhere. While there is a myriad of ways to do this; you can't go wrong with a color change.

<!--endintro-->

::: greybox
When you develop on SharePoint, you <u>do not</u> have a full copy of web.config in your Visual Studio project.
:::
::: bad  
Figure: Bad example - Never underline the text when it isn't a link  
:::

::: greybox
For more information on this, please go to [SSW website](https://www.ssw.com.au/ssw/).
:::
::: good  
Figure: Good Example - The link is nice and clear  
:::

#### CSS - underlines or borders?

The default implementation of underlines in CSS is:

`text-decoration:underline;` 

Another way to add look-alike underlines is by adding border. In this case, you can even have a dotted underline. However, it's **not recommended** you use this method unless you are a designer and know what you are doing. It may create extra pixels in the interface, which can potentially cause other problems in your UI, for example:

::: bad  
![Figure: Bad example - the different border size pushes the content down](border-problem-1.gif)  
:::

::: bad  
![Figure: Bad example - borders going over the text area](border-problem-2.png)  
:::
