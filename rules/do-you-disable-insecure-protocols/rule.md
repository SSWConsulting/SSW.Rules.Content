---
type: rule
title: Do you disable insecure protocols?
uri: do-you-disable-insecure-protocols
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Steven Andrews
    url: https://ssw.com.au/people/steven-andrews
  - title: Kaique Biancatti (Kiki)
    url: https://www.ssw.com.au/people/kiki
    img: https://raw.githubusercontent.com/SSWConsulting/SSW.People.Profiles/main/Kaique-Biancatti/Images/Kaique-Biancatti-Profile.jpg
related: []
redirects: []
created: 2017-11-02T22:51:47.000Z
archivedreason: null
guid: ccc5ea3b-e835-4b8c-b5bc-d49d98bade9b
---

For better server security (especially regarding public facing servers), certain security protocols and ciphers should be disabled.

<!--endintro-->

Using a tool called "IIS Crypto 3.2" by [Nartac](https://www.nartac.com/Products/IISCrypto), these protocols can be easily disabled instead of having to manually edit the Registry Keys.

1. Download IIS Crypto 3.2 (https://www.nartac.com/Products/IISCrypto/Download)
2. Run this on the server you wish to lock down
3. Select the best practices button 
      
::: good  
![Figure: Good example – TLS should be enabled and SSL should be disabled](iis-crypto-3-2.png)  
:::

4. Ensure that TLS 1.0 and TLS 1.1 is also disabled | hit apply 
5. The server will need to be rebooted before the settings take effect
