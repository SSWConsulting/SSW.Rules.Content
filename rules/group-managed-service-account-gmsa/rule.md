---
seoDescription: Microsoft's Group Managed Service Accounts (gMSAs) provide a secure and practical identity solution for services, automating password management and eliminating expired passwords.
type: rule
title: Do you use gMSAs (Group Managed Service Accounts)?
uri: group-managed-service-account-gmsa
authors:
  - title: Kiki Biancatti
    url: https://ssw.com.au/people/kaique-biancatti
    img: https://raw.githubusercontent.com/SSWConsulting/SSW.People.Profiles/main/Kaique-Biancatti/Images/Kaique-Biancatti-Profile.jpg
created: 2022-07-14T02:32:14.150Z
guid: 3a0225ad-a27f-4f72-b978-ab2580a82342
---

gMSA (Group Managed Service Accounts) are a secure and practical identity solution from Microsoft where services can be configured to use the gMSA principal and password management is handled by Windows - you don't need to worry about expired passwords anymore.

<!--endintro-->

gMSAs are the superior option when it comes to security and flexibility. It should always be used, when possible, instead of user accounts, MSAs, security principals, service accounts (with manually managed passwords) and any other on-premises identity types.

### The benefits of gMSAs

1. **Multiple servers -** Services and tasks can be set and run across multiple servers, a necessity given the modern state of organizations today
2. **Automated password management -** Passwords are automatically generated, rotated and handled by the OS
3. **Passwords are handled by the OS** - When applications require a password, they query Active Directory. No human knows the password to that, making it much harder to be compromised
4. **You can delegate management to other administrators** - Having the flexibility to delegate management can be incredibly helpful for ensuring there isn't just a single admin responsible for your service account security

### There are some requirements and difficulties for using these kinds of accounts

- **Support** - The application/service must support gMSAs
- **AD domain and forest functional level** - Windows Server 2012 or newer
- **KDC** - Domain controller with Microsoft Key Distribution Service (KdsSvc) enabled
- **PowerShell** - To create and manage service AD accounts, you need to install the Active Directory module for Windows PowerShell
- **Supported Windows versions** - Windows Server 2012/Windows 8 or newer
- **Services set up without gMSAs** - Rebuilding or changing the service account in applications that already set up and running (e.g. Data Protection Manager, Azure AD Sync) might break these applications, so a full re-install might be necessary to use gMSAs instead of a simple user change

## Set up gMSAs

### Create the Key Distribution Service (KDS) Key

A one-time operation must be performed to create a KDS root key. Do the following:

1. Login to your DC (Domain Controller) | run the PowerShell command:\
   `Add-KdsRootKey –EffectiveImmediately`
2. Ensure the key has been created succesfully by running the following PowerShell:\
   `Get-KdsRootKey`

### Create a gMSA

1. Login to your DC | run the PowerShell command:

   1. _`New-ADServiceAccount [-Name] <string> -DNSHostName <string> [-KerberosEncryptionType <ADKerberosEncryptionType>] [-ManagedPasswordIntervalInDays <Nullable[Int32]>] [-PrincipalsAllowedToRetrieveManagedPassword <ADPrincipal[]>] [-SamAccountName <string>] [-ServicePrincipalNames <string[]>]`_

Here's how you should fill out each of the bracketed parameters:

1. **Name:** The name of your account
2. **DNS Host Name:** The DNS hostname of the service
3. **Kerberos Encryption Type:** The encryption type supported by the host servers
4. **Managed Password Internal In Days:** How often you want the password to be changed (by default this is 30 days -- remember, the change is handled by Windows)

   \* note: This cannot be changed after the gMSA is created. To change the interval, you'll need to create a new gMSA and set a new interval.

5. **Principals Allowed To Retrieve Managed Password:** These can be the accounts of member hosts, or if there is a security group that member hosts are a part of, you would enter them here.
6. **Sam Account Name:** This is the NetBIOS name for the service if it's different from the account name.
7. **Service Principal Names:** This is a list of the Service Principal Names (SPNs) for the service)

The final command could look like this:

`New-ADServiceAccount -name gMSAAccount1 -DNSHostName gMSAAccount1.sydney.ssw.com.au -PrincipalsAllowedToRetrieveManagedPassword gMSAAccount1GroupWithComputerAccountsIn –verbose`

### Install a gMSA on the target server or workstation

1. Login to the target server | run the PowerShell command to install the Active Directory PowerShell module:\
   `Add-WindowsFeature RSAT-AD-PowerShell`
2. Run the PowerShell command to install the gMSA on the server:\
   `Install-ADServiceAccount -Identity gMSAAccount1`
3. Check if the gMSA is isntalled correctly:\
   `Test-ADServiceAccount gMSAAccount1`

If the command returns **True**, everything is configured correctly.

You can read more about gMSAs here: <https://docs.microsoft.com/en-us/windows-server/security/group-managed-service-accounts/group-managed-service-accounts-overview>
