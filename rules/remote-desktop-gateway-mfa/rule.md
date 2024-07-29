---
type: rule
tips: ""
title: Security - Do you protect your Remote Desktop connections with Multi
  Factor Authentication (MFA)?
seoDescription: Protecting your Remote Desktop connections is crucial in today's
  cybersecurity landscape. One effective way to enhance security is by using
  Azure MFA (Multi-Factor Authentication) in conjunction with the Azure MFA NPS
  (Network Policy Server) extension. This setup ensures that even if an attacker
  obtains a user's credentials, they still need a second form of authentication
  to gain access, significantly reducing the risk of unauthorized access.
uri: remote-desktop-gateway-mfa
authors:
  - title: Kiki Biancatti
    url: https://ssw.com.au/people/kaique-biancatti
    img: https://raw.githubusercontent.com/SSWConsulting/SSW.People.Profiles/main/Kaique-Biancatti/Images/Kaique-Biancatti-Profile.jpg
created: 2024-07-28T23:54:43.601Z
guid: bc8ab9ff-4cae-457b-852e-b61660a79801
---
Protecting your Remote Desktop connections is crucial in today's cybersecurity landscape. One effective way to enhance security is by using Azure MFA (Multi-Factor Authentication) in conjunction with the Azure MFA NPS (Network Policy Server) extension. This setup ensures that even if an attacker obtains a user's credentials, they still need a second form of authentication to gain access, significantly reducing the risk of unauthorized access.

`youtube: https://www.youtube.com/embed/qV9wddunpCY?si=RR0P8UBJ0wnYSXqn`
**Video: Identity Architecture: MFA with RADIUS | Microsoft Entra ID (8 min)**

##### Why Use Azure MFA to Protect Servers?

* Enhanced Security: By adding an additional layer of authentication, you mitigate the risk of credential theft.
* Compliance: Many regulatory frameworks require multi-factor authentication to protect sensitive data.

<!--endintro-->

You can follow along [Microsoft's documentation](https://learn.microsoft.com/en-us/entra/identity/authentication/howto-mfa-nps-extension) to implement this at your company and follow the summary below, if you already fill the prerequisites:

1. ##### Enable the NPS role on a domain-joined server

There needs to be a new server for RADIUS authentication in your environment, solely for MFA prompts. Generally, you don't want MFA for all your RADIUS authentication, so you'll need to create a new one, as it's not possible to have a single server with non-MFA and MFA in it. Once the extension is installed, it's going to analyza every request.

2. ##### Register users for MFA

If users are already registered for MFA in your tenant, then this will work. If not, you need to register them for MFA and ensure it works before proceeding.

3. ##### Install the Azure MFA NPS Extension

This entails running the .exe from Microsoft and running a PowerShell script to connect it to your Azure tenant.

4. ##### Configure your NPS extension

You can configure advanced options at this stage and what happens with users that are not enrolled for MFA.

5. ##### Troubleshoot

If necessary, Microsoft provides scripts and tools to check if your extension is working correctly.
You should expect an MFA prompt on your phone every time you connect to a server if this setup was successful.

Finally, implementing Azure MFA for your Remote Desktop connections significantly enhances your security posture. By following the steps above, you can ensure that your remote access solutions are protected against unauthorized access, providing peace of mind and compliance with industry standards.
