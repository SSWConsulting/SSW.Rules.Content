---
type: rule
title: Do you have Password Writeback enabled?
uri: do-you-have-password-writeback-enabled
created: 2018-11-13T04:10:57.0000000Z
authors:
- id: 73
  title: Kaique Biancatti

---



<span class='intro'> Do you have Password Writeback enabled in your Azure AD Connect?<br> </span>

<p>If you want to let your users reset their own, on-premises passwords directly from the cloud, you need to have Password Writeback enabled in Azure AD Connect!</p><p>You can read more about Password Writeback from the Microsoft Documentation&#58; <a href="https&#58;//docs.microsoft.com/en-us/azure/active-directory/authentication/howto-sspr-writeback">https&#58;//docs.microsoft.com/en-us/azure/active-directory/authentication/howto-sspr-writeback</a> <br></p><p>When setting up Azure AD Connect, you need to set the &quot;Password Writeback&quot; option&#58;</p><p><img src="/PublishingImages/enablepasswordwriteback.png" alt="enablepasswordwriteback.png" style="margin&#58;5px;" />&#160;</p><dd class="ssw15-rteElement-FigureGood">Good Example&#58; Setting up Password Writeback in Azure AD Connect</dd><dt><br></dt>


