---
type: rule
title: Do you store your secrets securely?
uri: do-you-store-your-secrets-securely
created: 2016-04-28T19:19:40.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 32
  title: Mehmet Ozdemir
- id: 34
  title: Brendan Richards
- id: 63
  title: Andrew Lean

---



<span class='intro'> <p class="p1">Most systems will have variables that need to be stored securely; OpenId shared secret keys, connection strings, and API tokens to name a few. <br></p><p class="p1">These secrets <strong>must not</strong> be stored in source control in plain text – it is insecure by nature, and basically means that it is sitting.<br></p> </span>

<p>There are many options for managing secrets in a secure way&#58;</p><h3>Bad Practices<br></h3><div class="greyBox"><h3>Store production&#160;passwords in source control protected with the 
      <a href="https&#58;//msdn.microsoft.com/en-us/library/zhhddkxy.aspx">ASP.NET IIS Registration Tool </a></h3><p class="ssw15-rteElement-P">Pros&#58; 
      <br></p><ul><li>Minimal change to existing process – no need for 
         <a href="https&#58;//msdn.microsoft.com/en-us/library/ms995355.aspx">DPAPI </a>or a dedicated Release&#160;Management (RM)&#160;tool.<br></li><li>Simple and easy to understand<br></li></ul><p>Cons&#58;</p><ul><li>Need to manually give the app pool identity ability to read the default RSA key container.<br></li><li>Difficult to manage production and non-production config settings<br></li><li>Developers can easily decrypt and access the production password.<br></li><li>Manual transmission of the password from the key store to the encrypted config file.<br></li></ul></div><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad practice -&#160;Overall rating&#58;&#160;2/10<br></dd>&#160; ​ 
<div class="greyBox"><h3 class="ssw15-rteElement-H3">Use Windows Identity instead of username/ password.</h3><p class="ssw15-rteElement-P">Pros&#58;<br></p><ul><li>Minimal change to existing process – no need for DPAPI or a dedicated RM tool.</li><li>Simple and easy to understand</li></ul><p class="ssw15-rteElement-P">Cons&#58;<br> </p><ul><li>Difficult to manage production and non-production config settings</li><li>Not generally applicable to all secured resources.&#160;</li><li>Can hit firewall snags with Kerberos and AD ports</li><li>Vulnerable to DOS attacks related to password lockout policies<br></li><li>Has key-person reliance on network admin</li></ul></div><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad practice -&#160;Overall rating&#58; 4/10</dd>&#160; 
<div class="greyBox"><h3 class="ssw15-rteElement-H3">
      <a href="https&#58;//docs.microsoft.com/en-us/aspnet/identity/overview/features-api/best-practices-for-deploying-passwords-and-other-sensitive-data-to-aspnet-and-azure">Use External Configuration Files</a><br></h3><p class="ssw15-rteElement-P">Pros&#58;</p><ul><li>Simple to understand and implement<br></li></ul><p class="ssw15-rteElement-P">Cons&#58; 
      <br></p><ul><li>Makes setting up projects the first time very hard.</li><li>Easy to accidentally check the external config file into source control.</li><li>Still need DPAPI to protect the external config file.</li><li>No clear way to manage the DevOps process for external config files.</li></ul></div><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad practice -&#160; Overall rating&#58; 1/10</dd><div> 
   <br> 
   <h3 class="ssw15-rteElement-H3">Good Practices</h3> ​ 
   <div class="greyBox"><h3 class="ssw15-rteElement-H3">Use Octopus/ VSTS RM secret management, with passwords sourced from KeePass<br></h3><p class="ssw15-rteElement-P">Pros&#58; 
         <br></p><ul><li>Scalable and secure.<br></li><li>General industry best practice - great for organizations of most sizes below large corporate.<br></li></ul><p class="ssw15-rteElement-P">Cons&#58; 
         <br></p><ul><li>Password reset process is still manual<br></li><li>DPAPI still needed.<br></li></ul></div><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good practice -&#160;Overall rating&#58; 8/10</dd></div><div> 
   <br> 
   <div class="greyBox"><h3 class="ssw15-rteElement-H3">Use Enterprise Secret Management Tool – LastPass/ Hashicorp Vault/ etc..</h3><p class="ssw15-rteElement-P">Pros&#58; 
         <br></p><ul><li>Enterprise grade – supports cryptographically strong passwords, auditing of secret access and dynamic secrets<br></li><li>Supports hierarchy of secrets<br></li><li>API interface for interfacing with other tools.<br></li><li>Password transmission can be done without a human in the chain.<br></li></ul><p class="ssw15-rteElement-P">Cons&#58; 
         <br></p><ul><li>More complex to install and administer<br></li><li>DPAPI still needed for config files at rest<br></li></ul></div><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good practice -&#160; Overall rating&#58; 8/10<br></dd><div class="greyBox"><h3 class="ssw15-rteElement-H3">​​Use Azure KeyVault</h3><p class="ssw15-rteElement-P"> See the SSW Rewards mobile app repository for how SSW is using this in a production application&#58; <a href="https&#58;//github.com/SSWConsulting/SSW.Rewards">https&#58;//github.com/SSWConsulting/SSW.Rewards</a> </p><p class="ssw15-rteElement-P"> Pros&#58; </p><ul><li>​Best solution for cloud (Azure) solutions</li><li>Enterprise grade</li><li>Uses industry standard best encryption</li><li>Dynamically cycles secrets</li><li>Access granted&#160;based on Azure AD permissions - no need to 'securely' share passwords with colleagues</li><li>Can be used to inject secrets in your CI/CD&#160;pipelines for non-cloud solutions</li></ul><p></p><p class="ssw15-rteElement-P"> Cons&#58; </p><ul><li>Price is per transaction - can become&#160;​costly if used in high volume and not managed thoroughly (see SSW's William Liebenberg on Azure SpendOps&#58; <a href="https&#58;//azuregems.io/spendops-with-azure-cosmos-db/">https&#58;//azuregems.io/spendops-with-azure-cosmos-db/</a>​<br></li></ul><p></p></div>​ 
   <dd class="ssw15-rteElement-FigureGood">​​Figure&#58; Good Practice - Overall rating 9/10<br></dd></div>​<br>


