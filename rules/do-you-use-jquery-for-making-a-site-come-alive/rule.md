---
type: rule
archivedreason: 
title: Do you use jQuery for making a site come alive?
guid: 27612f09-8114-4b19-b7c3-66f172c94a15
uri: do-you-use-jquery-for-making-a-site-come-alive
created: 2009-08-25T00:13:02.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

To please customers every business knows they need to keep their services and offerings fresh and up-to-date. The same is true for websites. In order to attract new traffic, we should make the website vivid.   
<!--endintro-->

::: bad  
![Figure: Bad example – there is no response when mouse is over the image](OldFashionSite.jpg)  
:::

::: good  
![Figure: Good example – apply the different style when mouse is over](NewFashionSite.jpg)  
:::


``` jquery
$("p").hover(function () {
            $(this).css({ "background-color":"yellow", "font-weight":"bolder" }); },
            function () { 
                var cssObj = { "background-color": "#ddd", 
                "font-weight": "", 
                color: "rgb(0,40,244)"
            }
            $(this).css(cssObj);
        });
```
**Figure: Mouse hover code sample**
