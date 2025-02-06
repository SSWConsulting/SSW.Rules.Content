---
type: rule
archivedreason: 
seoDescription: Hover effects on text links are a great way to enhance user experience and make your website more interactive. 
title: Do you use underlines on links?
guid: b55df040-7424-48e4-b19b-14d4bcdcfbc7
uri: underlined-links
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
- do-you-use-underlines-only-on-links

---

Ensure your links are easily distinguishable from the background and surrounding text by **always making them underlined**. Users expect underlined texts to be a link; and links to be underlined.

<!--endintro-->

**Note:** Underlines are **not** necessary on obvious links, like **menu/breadcrumb items** or **buttons**. On the other hand, hover effect (see more below) should always exist.

::: greybox
For more information on this, please go to [SSW website](https://www.ssw.com.au).
:::
::: good  
Figure: Good example - The link is nice and clear  
:::

::: info
**Tip:** You can [use a different color on underlines](https://www.w3schools.com/cssref/css3_pr_text-decoration-color.asp) as a nice touch.
:::

## Never underline a text that isn't a link

Use bold or another styling if you need emphasis.

::: greybox
When you develop on SharePoint, you <u>do not</u> have a full copy of web.config in your Visual Studio project.
:::
::: bad  
Figure: Bad example - Never underline the text when it isn't a link  
:::

::: greybox
When you develop on SharePoint, you **do not** have a full copy of web.config in your Visual Studio project.
:::
::: good  
Figure: Good example - Using bold for emphasis  
:::

## Include a hovering effect

Rollovers are also important as they offer visual feedback to a user that this link that will take them somewhere. While there is a myriad of ways to do this; color change is recommended because it preserves text readability. Hover the good example above to see this working.

The basic CSS for changing the link color on hover is:

``` css
a:hover { 
    color: #cc4141;
}
```

### Avoid other effects on hover for text

Effects like bold, scaling, rotation, or background changes can distort text, making it harder for users to read and interact with links.

::: bad
![Figure: Bad example - Using bold on hovering may cause a text shift](bad-example-bold-hover.gif)
:::

**Note:** These effects may be used for buttons or other non-text content elements.

## Avoid replacing underlines with borders

The default implementation of underlines in CSS is:

``` css
text-decoration: underline;
```

Another way to add look-alike underlines is by adding `border-bottom: 1px;`, for example. In this case, you can even have a dotted underline. However, it's **not recommended** you use this method unless you are a designer and know what you are doing. It may create extra pixels in the interface, which can potentially cause other problems in your UI:

::: bad  
![Figure: Bad example - The different border size pushes the content down](border-problem-1.gif)  
:::

::: bad  
![Figure: Bad example - Borders going over the text area](border-problem-2.png)  
:::
