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

Users expect underlined texts to be a hyperlink. You should visually differentiate links by underlining them. Of course, this is  **not** necessary on menus, obvious links, or buttons. Never underline a text that isn't a link - Use bold or italics if you need emphasis.

<!--endintro-->


::: bad  
![Figure: Never underline the text when it isn't a link (even        Scott Guthrie agrees!)](../../assets/Websites\_UnderlineNoHyperlink.gif)  
:::

The default implementation of underlines in CSS is " **text-decoration:underline;** ".

Another way to add look-alike underlines is by adding " **border-bottom: 1px solid #000;** ". In this case, you can even have a dotted underline. However, it's not recommended you use this method unless you are a designer and know what you are doing. It creates extra pixels in the interface, which can potentially cause other problems in your UI, for example:


::: bad  
![Figure: Bad example - the different border size pushes the content down](border-problem-1.gif)  
:::


::: bad  
![Figure: Bad example - borders going over the text area](border-problem-2.png)  
:::
