---
seoDescription: Easily find and connect to printers from outside the domain with a simple DNS alias setup.
type: rule
archivedreason:
title: Printers - Do you make your Printers easy to find?
guid: 44c288e4-76da-4293-b738-a2bd1319dc44
uri: printers-do-you-make-your-printers-easy-to-find
created: 2012-03-05T15:41:28.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []
---

For PCs that are not in the domain, the printers won’t be automatically installed.

So you should add a DNS alias which maps \\printer to your print server.

<!--endintro-->

![Figure: \printer takes to this window, were you can "Add" the printer via Connect](add-printer-via-connect.jpg)

::: greybox
Note: It is better to automate mappings via GPO preferences. As a backup, you can allow users to manually map as above.  
:::
