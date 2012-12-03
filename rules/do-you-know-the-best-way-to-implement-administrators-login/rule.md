---
type: rule
archivedreason: 
title: Do you know the best way to implement administrators' login
guid: d1076fdd-3d24-4bb9-8188-ea8b1d9cf316
uri: do-you-know-the-best-way-to-implement-administrators-login
created: 2012-12-03T02:57:12.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---


When administrators need different credentials to login to a SharePoint site, there are different ways to implement it.
<br><excerpt class='endintro'></excerpt><br>
<p>​1. Obvious &quot;Login&quot; link&#58;</p>
<p><img class="ssw-rteStyle-ImageArea" alt="LoginLink.png" src="/SoftwareDevelopment/RulesToBetterSharePoint/PublishingImages/LoginLink.png" style="margin&#58;5px;" /><br></p>
<span class="ssw-rteStyle-FigureBad">Bad example&#58; 'login' link</span> <p>2. Use little dot for a hidden link&#58;</p>
<p><img class="ssw-rteStyle-ImageArea" alt="HiddenDotLink.png" src="/SoftwareDevelopment/RulesToBetterSharePoint/PublishingImages/HiddenDotLink.png" style="margin&#58;5px;" /><br><span class="ssw-rteStyle-FigureBad">Bad example&#58; little dot for a hidden link</span></p>
<p>3. Use /admin/ to let administrators to login&#160;(And WordPress is almost perfect how they use /wp-admin/)&#58;</p>
<p><img class="ssw-rteStyle-ImageArea" alt="AdminURL.png" src="/SoftwareDevelopment/RulesToBetterSharePoint/PublishingImages/AdminURL.png" style="margin&#58;5px;" /><br><span class="ssw-rteStyle-FigureGood">Good example&#58; Use /admin/ URL for administrators</span></p>


