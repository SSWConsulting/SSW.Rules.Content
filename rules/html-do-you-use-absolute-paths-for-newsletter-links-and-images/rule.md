---
type: rule
archivedreason: 
title: HTML - Do you use absolute paths for newsletter links and images?
guid: f7d0ff4a-2f23-44b2-83ef-b34c251c08a8
uri: html-do-you-use-absolute-paths-for-newsletter-links-and-images
created: 2018-06-07T21:48:16.0000000Z
authors:
- title: Tiago Araujo
  url: https://ssw.com.au/people/tiago-araujo
related: []
redirects:
- use-absolute-paths-on-newsletters

---

Newsletters should always use  **absolute** references to all links and images within the HTML. Relative paths don't contain the server information so users see a broken link/image - the outside email application won't find the where the file is.

<!--endintro-->



```
<a href="/ssw/Company/ContactUs.aspx "><img src="/SSW/images/SSWLogo.png"></a>
```




::: bad
Figure: Bad example - using relative paths for both link and image on a newsletter

:::



```
<a href="https://ssw.com.au/ssw/Company/ContactUs.aspx "><img src="https://ssw.com.au/SSW/images/SSWLogo.png"></a>
```




::: good
Figure: Good example - using absolute paths for both link and image on a newsletter

:::
