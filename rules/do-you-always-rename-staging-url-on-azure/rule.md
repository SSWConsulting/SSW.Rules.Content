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


<p><span style="line-height&#58;20px;">Do you feel pain testing your code on Azure staging site? </span><span style="line-height&#58;20px;">I did because the Url wasn't easy to remember. </span><span style="line-height&#58;20px;">Follow this rule to increase your productivity.</span>&#160;</p><p>&#160;</p>
<br><excerpt class='endintro'></excerpt><br>
<table width="100%" class="ssw15-rteTable-default" cellspacing="0"><tbody><tr><td class="ssw15-rteTable-default" style="width&#58;100%;"><p>Default Azure Url&#160;naming with staged publishing&#58;</p><ul><li><span style="line-height&#58;20px;">Production web site&#58; <strong>sugarlearning.com</strong> (or sugarlearning.azurewebsites.net)</span></li><li><span style="line-height&#58;20px;">Staging web site&#58; <strong><strong>sugarlearning<span style="color&#58;#ff0066;">-staging</span>.azurewebsites.net</strong></strong></span></li></ul></td></tr></tbody></table><dd class="ssw15-rteElement-FigureBad">Bad e​​​​xample&#58; Site using the default Url (hard to remember!!)</dd><table width="100%" class="ssw15-rteTable-default" cellspacing="0"><tbody><tr><td class="ssw15-rteTable-default" style="width&#58;100%;"><p>Add a CName to resolve default Url like this&#58;</p><ul><li><span style="line-height&#58;20px;">Production web site&#58; <strong>sugarlearning.com</strong> (or sugarlearning.azurewebsites.net)</span></li><li><span style="line-height&#58;20px;">Staging web site&#58; <strong><font color="#ff0066">staging</font></strong>.<strong>sugarlearning.com </strong>(or&#160;sugarlearning-staging.azurewebsites.net)</span></li></ul></td></tr></tbody></table><dd class="ssw15-rteElement-FigureGood">​Good&#160;​example&#58; Staging Url having production Url with &quot;staging.&quot; prefix</dd>


