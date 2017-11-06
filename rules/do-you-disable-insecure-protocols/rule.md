---
type: rule
archivedreason: 
title: Do you disable insecure protocols?
guid: ccc5ea3b-e835-4b8c-b5bc-d49d98bade9b
uri: do-you-disable-insecure-protocols
created: 2017-11-02T22:51:47.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Steven Andrews
  url: https://ssw.com.au/people/steven-andrews
related: []
redirects: []

---


<div>​For better server security (especially regarding&#160;public facing servers​),&#160;certain security protocols and ciphers should be disabled.<br></div>
<br><excerpt class='endintro'></excerpt><br>
<p>​​​Using a tool called &quot;IIS Crypto 2.0&quot; by <a href="https&#58;//www.nartac.com/Products/IISCrypto">Nartac</a>, these protocols can be easily disabled instead of having to manually edit the Registry Keys,.<br></p><ol><li>Download IIS Crypto 2.0 (<a href="https&#58;//www.nartac.com/Products/IISCrypto/Download">https&#58;//www.nartac.com/Products/IISCrypto/Download​</a>)<br></li><li>Run this on the se​rver you wish to lock down<br></li><li>Select the best practices button<img src="/PublishingImages/IIS%20Crypto%202.0.png" alt="IIS Crypto 2.0.png" style="margin&#58;5px;width&#58;808px;" /><dd class="ssw15-rteElement-FigureGood">​Figure&#58; Good exa​​mple – TLS should be enabled a​​n​d SSL should be disabled​</dd></li><li>Ensure that TLS 1.0 is also disabled and hit apply​<br></li><li>The server will need to be rebooted before the settings take affect<br></li></ol><p></p><p><br></p>


