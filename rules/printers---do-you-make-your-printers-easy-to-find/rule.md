---
type: rule
archivedreason: 
title: Printers - Do you make your Printers easy to find?
guid: 44c288e4-76da-4293-b738-a2bd1319dc44
uri: printers---do-you-make-your-printers-easy-to-find
created: 2012-03-05T15:41:28.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

For PCs that are not in the domain, the printers won’t be automatically installed.

So you should add a DNS alias which maps \\printer to your print server.

<!--endintro-->
<dl class="image">&lt;dt&gt;<img class="ms-rteCustom-ImageArea" alt="Add the printer via Connect" src="add-printer-via-connect.jpg">&lt;/dt&gt;<dd>Figure: \\printer takes to this window, were you can "Add" the printer via Connect</dd></dl>

::: greybox
Note: It is better to automate mappings via GPO preferences. As a backup, you can allow users to manually map as above.
:::
