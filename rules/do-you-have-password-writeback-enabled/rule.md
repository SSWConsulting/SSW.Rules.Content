---
type: rule
archivedreason: 
title: Do you have Password Writeback enabled?
guid: 7b11d493-7025-4f67-94a7-592ad109b1c3
uri: do-you-have-password-writeback-enabled
created: 2018-11-13T04:10:57.0000000Z
authors:
- title: Kaique Biancatti
  url: https://ssw.com.au/people/kaique-biancatti
related: []
redirects: []

---


Do you have Password Writeback enabled in your Azure AD Connect?<br>
<br><excerpt class='endintro'></excerpt><br>
<p>If you want to let your users reset their own, on-premises passwords directly from the cloud, you need to have Password Writeback enabled in Azure AD Connect!</p><p>You can read more about Password Writeback from the Microsoft Documentation: <a href="https://docs.microsoft.com/en-us/azure/active-directory/authentication/howto-sspr-writeback">https://docs.microsoft.com/en-us/azure/active-directory/authentication/howto-sspr-writeback</a> <br></p><p>When setting up Azure AD Connect, you need to set the "Password Writeback" option:</p><p><img src="enablepasswordwriteback.png" alt="enablepasswordwriteback.png" style="margin:5px;" /> </p><dd class="ssw15-rteElement-FigureGood">Good Example: Setting up Password Writeback in Azure AD Connect</dd><dt><br></dt>


