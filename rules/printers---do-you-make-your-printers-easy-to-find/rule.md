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


<p>For PCs that are not in the domain, the printers won’t be automatically installed.<br></p>
<p>So&#160;you should&#160;add a DNS alias which maps \\printer to your print server.</p>

<br><excerpt class='endintro'></excerpt><br>
<dl class="image"><dt><img class="ms-rteCustom-ImageArea" alt="Add the printer via Connect" src="/PublishingImages/add-printer-via-connect.jpg" /></dt><dd>Figure&#58; \\printer takes to this window, were you can &quot;Add&quot;&#160;the printer via Connect</dd></dl><p class="ssw15-rteElement-GreyBox">Note&#58; It is better to automate mappings via GPO preferences. As a backup, you can allow users to manually map as above.</p>​<br>


