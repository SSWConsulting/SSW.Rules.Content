---
type: rule
archivedreason: 
title: Do you underline links (and include a rollover)?
guid: aaef4269-0a29-4752-b3eb-a6920b9bd373
uri: do-you-underline-links-and-include-a-rollover
created: 2015-02-16T01:30:13.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Duncan Hunter
  url: https://ssw.com.au/people/duncan-hunter
- title: Tiago Araujo
  url: https://ssw.com.au/people/tiago-araujo
related: []
redirects:
- do-you-underline-links-(and-include-a-rollover)

---

Always make links perfectly clear.

<!--endintro-->

It's very important that your links stand out from the background as well as the surrounding text. A solid underline and a contrasting color is the usually the best choice, but the exact method is not important as long as the end result stands out. A link should not only be discoverable upon accidental hovering.

Rollovers are important as they offer visual feedback to a user that this link that will take them somewhere. While there is a myriad of ways to do this; you can't go wrong with an underline or border-bottom.


::: greybox
For more information on this, please [go to SSW website](https://www.ssw.com.au/).

:::
Bad Example: The link is hard to recognize


::: greybox
For more information on this, please [go to SSW website](https://www.ssw.com.au/). 

:::
Good Example: This link is obvious


![](link-hover.jpg)




::: good
Good Example: Obvious rollover. You can test it by hovering the links on the example above

:::

Example CSS for rollover:



```
a:hover { 
    color: #cc4141;
    cursor: pointer;
}
```


Figure: Example CSS for rollover effect
