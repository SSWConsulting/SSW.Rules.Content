---
type: rule
archivedreason: 
title: Do you store your secrets securely?
guid: 57dc15ba-605a-4a71-8b0e-d9f1551b9fc0
uri: store-your-secrets-securely
created: 2016-04-28T19:19:40.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Mehmet Ozdemir
  url: https://ssw.com.au/people/mehmet-ozdemir
- title: Brendan Richards
  url: https://ssw.com.au/people/brendan-richards
- title: Andrew Lean
  url: https://ssw.com.au/people/andrew-lean
related: []
redirects:
- do-you-store-your-secrets-securely

---


<p class="p1">Most systems will have variables that need to be stored securely; OpenId shared secret keys, connection strings and API tokens to name a few. </p><p class="p1">These secrets <strong>must not</strong> be stored in source control – it is insecure by nature, and basically means that it is sitting on everyone’s laptop, including the designers and that one manager guy who wrote hello world in 1996 and wants to look at the code.</p>
<br><excerpt class='endintro'></excerpt><br>
<p>​Instead, check in friendly development-only settings, ideally in Web.config or some JSON configuration, and have either your deployment system or your host (eg. Azure) fill in your secrets for you. They will encrypt and secure your secrets for you, and either do config transforms or supply environment variable overrides for them – a much nicer solution overall.​​</p><dl class="badImage"><dt>
      <img src="/PublishingImages/secrets-bad.png" alt="secrets-bad.png" style="width&#58;800px;" />
   </dt><dd>Figure&#58; Bad example -​ Secrets stored in code and saved in plain text, for anyone to read</dd></dl><dl class="goodImage"><dt><img src="/PublishingImages/secrets-good.png" alt="secrets-good.png" /></dt><dd>Figure&#58; Good example -​ Octopus Deploy can store the sensitive secrets and can transform them into the config files at deploy time</dd></dl>


