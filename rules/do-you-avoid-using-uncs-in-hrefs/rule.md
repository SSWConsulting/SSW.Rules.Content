---
type: rule
archivedreason: 
title: Do you avoid using UNCs in HREFs?
guid: 7e117f21-a259-489e-bddc-c63de9d95fbe
uri: do-you-avoid-using-uncs-in-hrefs
created: 2016-08-26T17:56:17.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- avoid-using-uncs-in-hrefs

---

Initially, errors of this nature would be picked up in the link checking utility. However, that is not the case because the link checker will not report any problems if you run it locally - which is the normal method. The reason it won't see the problems is because the link checking utility does not check hard coded links to local servers (e.g. http://localserver/ssw/Default.aspx). Therefore, it is testing a page that will exist internally, but the page will not exist when uploaded to the web (eg.[http://www.ssw.com.au/ssw/Default.aspx](https&#58;//www.ssw.com.au/ssw/Redirect/ssw/sswhome.htm)). 

<!--endintro-->


::: bad
Bad Example: &lt;a href="//ant/ssw/LookOut.htm"&gt;

:::


::: good
 **Good Example: &lt;a href="/ssw/LookOut.htm"&gt;** 

:::
