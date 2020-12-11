---
type: rule
archivedreason: 
title: HTML - Do you use absolute paths for newsletter links and images?
guid: f7d0ff4a-2f23-44b2-83ef-b34c251c08a8
uri: html---do-you-use-absolute-paths-for-newsletter-links-and-images
created: 2018-06-07T21:48:16.0000000Z
authors:
- id: 16
  title: Tiago Araujo
related: []

---

Newsletters should always use  **absolute** references to all links and images within the HTML. Relative paths don't contain the server information so users see a broken link/image - the outside email application won't find the where the file is.

<!--endintro-->

&lt;a href="/ssw/Company/ContactUs.aspx "&gt;&lt;img src="/SSW/images/SSWLogo.png"&gt;&lt;/a&gt;


::: bad
Figure: Bad example - using relative paths for both link and image on a newsletter

:::


&lt;a href="<mark>https&#58;//ssw.com.au</mark>/ssw/Company/ContactUs.aspx "&gt;&lt;img src="<mark>https&#58;//ssw.com.au</mark>/SSW/images/SSWLogo.png"&gt;&lt;/a&gt;


::: good
Figure: Good example - using absolute paths for both link and image on a newsletter

:::
