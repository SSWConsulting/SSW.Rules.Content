---
type: rule
title: Do you always rename staging Url on Azure?
uri: do-you-always-rename-staging-url-on-azure
created: 2015-03-08T23:23:53.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 47
  title: Stanley Sidik
- id: 43
  title: Michael Demarco
- id: 42
  title: Shigemi Matsumoto

---



<span class='intro'> <p>​If you use the default Azure staging web site Url, it can be difficult to remember and&#160;a waste of time trying to lookup the name every time you access it.&#160;Follow this rule to increase&#160;your productivity and make it easier for everyone to access&#160;your staging&#160;site.</p> </span>

<table width="100%" class="ssw15-rteTable-default" cellspacing="0"><tbody><tr><td class="ssw15-rteTable-default" style="width&#58;100%;"><p>Default Azure Url&#58;</p><ul><li><strong style="line-height&#58;20px;background-color&#58;initial;"><strong>sugarlearning<span style="color&#58;#ff0066;">-staging</span>.azurewebsites.net</strong></strong><br></li></ul></td></tr></tbody></table><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad e​​​​xample -&#160;Site using the default Url (hard to remember!!)</dd><table width="100%" class="ssw15-rteTable-default" cellspacing="0"><tbody><tr><td class="ssw15-rteTable-default" style="width&#58;100%;"><p>Customized Url&#58;</p><ul><li><strong style="line-height&#58;20px;background-color&#58;initial;"><font color="#ff0066">staging</font></strong><span style="line-height&#58;20px;background-color&#58;initial;">.</span><strong style="line-height&#58;20px;background-color&#58;initial;">sugarlearning.com</strong><br></li></ul></td></tr></tbody></table><dd class="ssw15-rteElement-FigureGood">Figure&#58; ​Good&#160;​example - Staging Url having production Url with &quot;staging.&quot; prefix</dd><p class="ssw15-rteElement-P">​<br></p><p class="ssw15-rteElement-P">​​<strong>How to setup a custom Url</strong></p><p class="ssw15-rteElement-P"><span style="color&#58;#555555;font-size&#58;11px;font-weight&#58;bold;">1. </span><span style="color&#58;#555555;font-size&#58;11px;font-weight&#58;bold;">Add a CName to the default Url to your DNS server</span><span style="color&#58;#555555;font-size&#58;11px;font-weight&#58;bold;">&#160;</span><br></p><p class="ssw15-rteElement-FigureGood"><img alt="2015-03-10_17-13-55.png" src="/PublishingImages/2015-03-10_17-13-55.png" style="margin&#58;5px;width&#58;650px;" />&#160;<span style="color&#58;#555555;font-size&#58;11px;font-weight&#58;bold;line-height&#58;20px;">Figure&#58; ​&#160;CName being added to DNS&#160;for the default Url</span></p><p class="ssw15-rteElement-FigureGood"><span style="color&#58;#555555;font-size&#58;11px;font-weight&#58;bold;line-height&#58;20px;">2. Instruc</span><span style="color&#58;#555555;font-size&#58;11px;font-weight&#58;bold;line-height&#58;20px;">t Azure to accept the custom Url&#160;</span><br></p><p class="ssw15-rteElement-FigureGood">&#160;<img alt="custom domains (1).png" src="/PublishingImages/custom%20domains%20(1).png" style="margin&#58;5px;width&#58;650px;" /><span style="color&#58;#555555;font-size&#58;11px;font-weight&#58;bold;line-height&#58;20px;">Figure&#58; ​&#160;Azure being configured&#160;to accept the CName</span></p>


