---
type: rule
archivedreason: 
title: Do you use subdomains instead of virtual directories?
guid: 768ddd4e-85d9-4433-aca8-f164381d515b
uri: do-you-use-subdomains-instead-of-virtual-directories
created: 2013-10-14T07:53:27.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

Using subdomains over directories has 2 benefits:

<!--endintro-->

1. it is easier to host different sections of your website on different platforms, and
2. in different geographic locations


::: greybox
http://www.myservice.com/ **ssw** /
http://www.myservice.com/ **northwind** /  
:::


::: bad
Figure: Bad Example - Virtual directories used to distinguish organizations


:::


::: greybox
http:// **ssw** .myservice.com/
http:// **northwind** .myservice.com/

:::


::: good
Figure: Good Example - Subdomains used to distinguish organizations  
:::
