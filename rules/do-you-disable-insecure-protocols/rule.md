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

For better server security (especially regarding public facing servers), certain security protocols and ciphers should be disabled.


<!--endintro-->

Using a tool called "IIS Crypto 2.0" by     [Nartac](https://www.nartac.com/Products/IISCrypto), these protocols can be easily disabled instead of having to manually edit the Registry Keys.

1. Download IIS Crypto 2.0 (https://www.nartac.com/Products/IISCrypto/Download)
2. Run this on the server you wish to lock down
3. Select the best practices button <br>      <dl class="goodImage"><br><br>::: good  <br>![Figure: Good example – TLS should be enabled and SSL should be disabled](IIS Crypto 2.0.png)  <br>:::<br></dl>
4. Ensure that TLS 1.0 is also disabled and hit apply <br>
5. The server will need to be rebooted before the settings take effect
