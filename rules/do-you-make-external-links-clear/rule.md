---
type: rule
title: Do you visually indicate when a link is external?
uri: do-you-make-external-links-clear
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Tiago Araujo
    url: https://ssw.com.au/people/tiago-araujo
related:
  - external-links-open-on-a-new-tab
redirects: []
created: 2015-02-16T02:21:22.000Z
archivedreason: null
guid: d178549e-bdef-4636-8dc7-b3514b360bd0
---

When creating links, you should follow a few basic rules:

<!--endintro-->

- If your link is an **internal** link, then it should keep the default behaviour, navigating within the same tab
- If the link is **external**, it should:
  - [Open in a new tab](/external-links-open-on-a-new-tab)
  - Be visually clear to the user that it will lead them away from the current site, that way it is not a surprise.
      
::: greybox
[Google](https://www.ssw.com.au/ssw/Redirect/Web/Google.htm) is by far the best but try other search engines as well.
:::
::: bad
Figure: Bad example - Without visual indication
:::

::: greybox
[Google](https://google.com) is by far the best but try other search engines as well.
:::
::: good
Figure: Good example - With visual indication
:::

### How to add the external link indicator?

It should be inserted by CSS as following: 
      
```css
a[href*=&quot;//&quot;]&#58;not([href*=&quot;mysite.com&quot;]):after {
content&#58; url(https://www.ssw.com.au/ssw/images/external.gif);     
padding-left: 4px;
}
```
**Figure: Icon can be added via CSS using a simple declaration**
