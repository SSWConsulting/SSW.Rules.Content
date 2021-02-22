---
type: rule
archivedreason: 
title: Do you always rename staging Url on Azure?
guid: 92dd8fc9-110d-4ea6-8340-528f1b1d411e
uri: do-you-always-rename-staging-url-on-azure
created: 2015-03-08T23:23:53.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Stanley Sidik
  url: https://ssw.com.au/people/stanley-sidik
- title: Michael Demarco
  url: https://ssw.com.au/people/michael-demarco
- title: Shigemi Matsumoto
  url: https://ssw.com.au/people/shigemi-matsumoto
related: []
redirects: []

---


<p>​If you use the default Azure staging web site Url, it can be difficult to remember and a waste of time trying to lookup the name every time you access it. Follow this rule to increase your productivity and make it easier for everyone to access your staging site.</p>
<br><excerpt class='endintro'></excerpt><br>
<table width="100%" class="ssw15-rteTable-default" cellspacing="0"><tbody><tr><td class="ssw15-rteTable-default" style="width:100%;"><p>Default Azure Url:</p><ul><li><strong style="line-height:20px;background-color:initial;"><strong>sugarlearning<span style="color:#ff0066;">-staging</span>.azurewebsites.net</strong></strong><br></li></ul></td></tr></tbody></table><dd class="ssw15-rteElement-FigureBad">Figure: Bad e​​​​xample - Site using the default Url (hard to remember!!)</dd><table width="100%" class="ssw15-rteTable-default" cellspacing="0"><tbody><tr><td class="ssw15-rteTable-default" style="width:100%;"><p>Customized Url:</p><ul><li><strong style="line-height:20px;background-color:initial;"><font color="#ff0066">staging</font></strong><span style="line-height:20px;background-color:initial;">.</span><strong style="line-height:20px;background-color:initial;">sugarlearning.com</strong><br></li></ul></td></tr></tbody></table><dd class="ssw15-rteElement-FigureGood">Figure: ​Good ​example - Staging Url having production Url with "staging." prefix</dd><p class="ssw15-rteElement-P">​<br></p><p class="ssw15-rteElement-P">​​<strong>How to setup a custom Url</strong></p><p class="ssw15-rteElement-P"><span style="color:#555555;font-size:11px;font-weight:bold;">1. </span><span style="color:#555555;font-size:11px;font-weight:bold;">Add a CName to the default Url to your DNS server</span><span style="color:#555555;font-size:11px;font-weight:bold;"> </span><br></p><p class="ssw15-rteElement-FigureGood"><img alt="2015-03-10_17-13-55.png" src="2015-03-10_17-13-55.png" style="margin:5px;width:650px;" /> <span style="color:#555555;font-size:11px;font-weight:bold;line-height:20px;">Figure: ​ CName being added to DNS for the default Url</span></p><p class="ssw15-rteElement-FigureGood"><span style="color:#555555;font-size:11px;font-weight:bold;line-height:20px;">2. Instruc</span><span style="color:#555555;font-size:11px;font-weight:bold;line-height:20px;">t Azure to accept the custom Url </span><br></p><p class="ssw15-rteElement-FigureGood"> <img alt="custom domains (1).png" src="custom domains (1).png" style="margin:5px;width:650px;" /><span style="color:#555555;font-size:11px;font-weight:bold;line-height:20px;">Figure: ​ Azure being configured to accept the CName</span></p>


