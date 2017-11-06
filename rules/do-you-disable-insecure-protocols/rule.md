---
type: rule
title: Do you disable insecure protocols?
uri: do-you-disable-insecure-protocols
created: 2017-11-02T22:51:47.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 71
  title: Steven Andrews

---



<span class='intro'> <div>​For better server security (especially regarding&#160;public facing servers​),&#160;certain security protocols and ciphers should be disabled.<br></div> </span>

<p>​​​Using a tool called &quot;IIS Crypto 2.0&quot; by <a href="https&#58;//www.nartac.com/Products/IISCrypto">Nartac</a>, these protocols can be easily disabled instead of having to manually edit the Registry Keys,.<br></p><ol><li>Download IIS Crypto 2.0 (<a href="https&#58;//www.nartac.com/Products/IISCrypto/Download">https&#58;//www.nartac.com/Products/IISCrypto/Download​</a>)<br></li><li>Run this on the se​rver you wish to lock down<br></li><li>Select the best practices button<img src="/PublishingImages/IIS%20Crypto%202.0.png" alt="IIS Crypto 2.0.png" style="margin&#58;5px;width&#58;808px;" /><dd class="ssw15-rteElement-FigureGood">​Figure&#58; Good exa​​mple – TLS should be enabled a​​n​d SSL should be disabled​</dd></li><li>Ensure that TLS 1.0 is also disabled and hit apply​<br></li><li>The server will need to be rebooted before the settings take affect<br></li></ol><p></p><p><br></p>


