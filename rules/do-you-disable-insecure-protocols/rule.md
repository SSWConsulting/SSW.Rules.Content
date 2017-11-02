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



<span class='intro'> <div>For better security all our servers in our environment especially those that are public facing should have certain Security protocols and Cipers disabled.<br>​<br></div><div class="ssw15-rteElement-ContentBlock-SSW-Only">​SSW Internal<br></div><br> </span>

<p>​​​Using a tool called &quot;IIS Crypto 2.0&quot; by <a href="https&#58;//www.nartac.com/Products/IISCrypto">Nartac</a>, these protocols can be easily disabled instead of having to manually edit the Registry Keys,.<br>​​</p><p>1. Donwload IIS Crypto 2.0</p><p>2. Run this on the server you wish to lock down</p><p>3. Select the best practices button</p><p><img src="/PublishingImages/IIS%20Crypto%202.0.png" alt="IIS Crypto 2.0.png" style="margin&#58;5px;width&#58;808px;" /><br>​<br>4. Ensure that TLS 1.0 is also disabled and hit apply<br></p><p>5. The server will need to be rebooted before the settings take affect<br></p>


