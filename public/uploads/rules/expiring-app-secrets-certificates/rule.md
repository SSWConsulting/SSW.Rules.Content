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

An easy way to do this is to run a PowerShell script that checks the expiry date of all app registration secrets or certificates. This requires the Microsoft Graph PowerShell module, as the older AzureAD module is deprecated. The key cmdlets used is **Get-MgApplication**.

Here’s a script using the Microsoft Graph module. It will:
- Get a list of app registrations with expiring secrets/certs within a specified date range
- Email the list to a specified address, as well as any owners of the app registration

```
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

$LimitExpirationDays = 14 #secret expiration date filter - how many days in the future
$LimitExpirationDaysPast = -14 #secret expiration date filter - how many days in the past

$ownersEmail = @()

# Install Microsoft Graph module (if not installed)
if (-not (Get-Module -ListAvailable -Name Microsoft.Graph)) {
    Write-Host "Installing Microsoft Graph..."
    Install-Module Microsoft.Graph -Scope AllUSers -Force
}

Connect-MgGraph

#Retrieving the list of secrets that expires in the above days
$SecretsToExpire = Get-MgApplication -All | ForEach-Object {
    $app = $_
    $owners = ""
    Get-MgApplicationOwner -ApplicationId $app.Id | ForEach-Object {
        $owner = Get-MgUser -UserId $_.Id -ErrorAction SilentlyContinue | Select -ExpandProperty DisplayName
        if ($null -ne $owner) {
            $owners = $owners+$owner+", "
        }
    }
    @(
        $app.PasswordCredentials
        $app.KeyCredentials
    ) | Where-Object {
        $_.EndDateTime -lt (Get-Date).AddDays($LimitExpirationDays) -and $_.EndDateTime -gt (Get-Date).AddDays($LimitExpirationDaysPast)
    } | ForEach-Object {
        $id = "Not set"
        if($_.CustomKeyIdentifier) {
            $id = [System.Text.Encoding]::UTF8.GetString($_.CustomKeyIdentifier)
        }
        [PSCustomObject] @{
            App = $app.DisplayName
            ObjectID = $app.ObjectId
            AppId = $app.AppId
            Type = $_.GetType().name
            KeyIdentifier = $id
            EndDate = $_.EndDateTime
            Owners = $owners
        }
        Get-MgApplicationOwner -ApplicationId $app.Id | ForEach-Object {
            $ownerEmail = Get-MgUser -UserId $_.Id | Select -ExpandProperty mail
            $ownersEmail += $ownerEmail
        }
    }
}
 
#Gridview list
#$SecretsToExpire | Out-GridView

#Printing the list of secrets that are near to expire
if($SecretsToExpire.Count -EQ 0) {
    Write-Output "No secrets found that will expire in this range"
}
else {
    Write-Output "Secrets that will expire in this range:" $SecretsToExpire.Count
    Write-Output $SecretsToExpire
}


$emailBody = @"
    <div>
        <p>Here is a list of expiring app registration secrets & certificates. Please renew them before they expire!</p>
    </div>
"@
$emailBody += '<pre>{0}</pre>' -f ($SecretsToExpire | Format-Table -AutoSize -Property App,EndDate,Owners | Out-String)
$emailBody += @"
    <div style='font-family:Calibri'>
    <p>Thanks!</p>
    </div>
"@

$ccRecipients = foreach ($email in ($ownersEmail -split ' ' | Select -Unique)) {
    @{ emailAddress = @{ address = $email } }
}

$emailParams = @{
    message = @{
        subject = "Entra ID - Expiring app registration secrets"
        body = @{
            contentType = "HTML"
            content = $emailBody
        }
        toRecipients = @(
            @{
                emailAddress = @{
                    address = "SysAdmins@northwind.com"
                }
            }
        )
#        ccRecipients = $ccRecipients
    }
}

Write-Output $ccRecipients

Send-MgUserMail -UserId "noreply@northwind.com" -BodyParameter $emailParams

```

:::greybox

Note: To run this on a schedule, you should create an app registration to authenticate the script. The app registration will at least need **Application.Read.All** rights to be able to run this.

:::

### Use a Logic App to check expiry dates

If you prefer working with Logic Apps, there's an example of how it can be done here: https://www.inthecloud247.com/get-notified-on-expiring-azure-app-registration-client-secrets/

You will also need an App Registration to authenticate your Logic App. Notifications can then be sent to email or a Teams channel.

![Figure: Example email, listing app registration secrets that are expiring soon](app-reg-email.png)
