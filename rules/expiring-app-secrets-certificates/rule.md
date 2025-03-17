---
type: rule
title: Do you keep track of expiring app registration secrets and certificates?
seoDescription: Keep track of expiring app registration secrets and certificates
  in Azure AD to avoid authentication issues.
uri: expiring-app-secrets-certificates
authors:
  - title: Chris Schultz
    url: https://ssw.com.au/people/chris-schultz
  - title: Brady Stroud
    url: https://ssw.com.au/people/brady-stroud/
created: 2023-05-12T00:55:28.532Z
guid: 429dbbef-ea36-4fc6-b358-924330966b4a
---

In Entra ID (formerly Azure AD), App Registrations are used to establish a trust relationship between your app and the Microsoft identity platform. This allows you to give your app access to various resources, such as Graph API.

App Registrations use secrets or certificates for authentication. It is important to keep track of the expiry date of these authentication methods, so you can update them before things break.

<!--endintro-->

### Use a PowerShell script to check expiry dates

An easy way to do this is to run a PowerShell script that checks the expiry date of all app registration secrets or certificates. This requires the Microsoft.Graph module; the cmdlets used are:

`Get-MgApplication `

`Get-MgApplicationPassword`

`et-MgApplicationKeyCredential`

There's an example of a working script here: https://github.com/demiliani/PowershellCloudScripts/blob/master/AzureADCheckSecretsToExpire.ps1

To extend the example above, you can run the script on a schedule using Task Scheduler or an Azure Automation Runbook, and send an email with [Send-MailMessage](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/send-mailmessage?view=powershell-7.3).

:::greybox

Note: To run this on a schedule, you should create an app registration to authenticate the script. The app registration will need the role **Cloud Application Administrator**.

:::

### Use a Logic App to check expiry dates

If you prefer working with Logic Apps, there's an example of how it can be done here: https://www.inthecloud247.com/get-notified-on-expiring-azure-app-registration-client-secrets/

You will also need an App Registration to authenticate your Logic App. Notifications can then be sent to email or a Teams channel.

![Figure: Example email, listing app registration secrets that are expiring soon](app-reg-email.png)
