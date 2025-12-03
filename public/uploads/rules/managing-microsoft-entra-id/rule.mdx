---
type: rule
title: Do you follow best practices for managing Microsoft Entra ID?
seoDescription: Learn best practices for managing Microsoft Entra ID to enhance
  security and efficiency in your organization.
uri: managing-microsoft-entra-id
authors:
  - title: Rob Thomlinson
    url: https://www.ssw.com.au/people/rob-thomlinson/
related:
  - how-to-name-documents
created: 2025-01-03T10:58:08.000Z
guid: 096b7e93-242d-4383-8978-f86c6cf0f2f3
---
Effective management of Microsoft Entra ID (formerly Azure Active Directory) is crucial for maintaining the security and efficiency of your organisation's IT infrastructure. Neglecting best practices can lead to unauthorised access, data breaches, and operational disruptions. <!--endintro-->

## 1. Enforce Strong Authentication

* **Implement Multi-Factor Authentication (MFA):** Require MFA for all users, especially administrators, to add an extra layer of security
* **Adopt Passwordless Authentication:** Utilize methods like Windows Hello for Business or FIDO2 security keys to enhance security and user experience

To check if your users are still typing passwords, use the [Get-MgBetaAuditLogSignIn cmdlet](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.beta.reports/get-mgbetaauditlogsignin?view=graph-powershell-beta) - for example:

```powershell
Connect-MgGraph

Import-Module Microsoft.Graph.Beta.Reports

$startDate = (Get-Date).AddDays(-30).ToString("yyyy-MM-ddTHH:mm:ssZ")
$endDate   = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssZ")

$Output = @()

$signIns = Get-MgBetaAuditLogSignIn -Filter "createdDateTime ge $startDate and createdDateTime le $endDate" -All

foreach ($signIn in $signIns) {
    $authMethods = $signIn.AuthenticationDetails | ForEach-Object { $_.AuthenticationMethod -join "," }
    $authMethodsString = $authMethods -join "; "

    if ($signIn.Status.errorCode -eq 0 -and $authMethodsString -contains "Password" -and !($authMethodsString -contains "Passwordless")) {
        $Output += [PSCustomObject]@{
            UserDisplayName    = $signIn.UserDisplayName
            UserPrincipalName  = $signIn.UserPrincipalName
            CreatedDateTime    = $signIn.CreatedDateTime
            AppDisplayName     = $signIn.AppDisplayName
            AuthenticationMethod = $authMethodsString
        }
    }
}

$Output | Export-Csv -Path C:\temp\password-use.csv -NoTypeInformation
```

## 2. Apply the Principle of Least Privilege

* **Use Role-Based Access Control (RBAC):** Assign users the minimum permissions necessary for their roles to reduce the risk of unauthorized access
* **Implement Just-In-Time Access:** Utilize Privileged Identity Management (PIM) to grant temporary access to resources only when needed

## 3. Regularly Review and Audit Access

* **Conduct Access Reviews:** Periodically review user access to ensure that only authorized individuals have access to resources
* **Monitor Sign-In Activity:** Keep track of user sign-ins to detect unusual or suspicious activities promptly

## 4. Secure Application Registrations

* **Use Certificates Over Secrets:** Always use certificate credentials for app authentication instead of client secrets, as certificates are more secure
* **Limit API Permissions:** Assign the least privileged permissions necessary for applications to function

## 5. Enable Security Features

* **Activate Security Defaults:** Enable security defaults in Microsoft Entra ID to enforce a basic level of security across your organization
* **Implement Conditional Access Policies:** Define policies that grant or block access based on conditions like user location, device state, or risk level

## 6. Plan for Emergency Access

* **Create Break Glass Accounts:** Establish at least two emergency access accounts that are not protected by MFA to ensure access during critical situations
* **Monitor and Secure Emergency Accounts:** Regularly audit these accounts to ensure they are not misused and are only accessed during emergencies

## 7. Use Clear Access Group Naming Conventions

Clear and consistent naming conventions for access groups make management simpler and ensure clarity across the organization

### Why are naming conventions important?

Without clear naming conventions, it becomes difficult to understand the purpose or scope of access groups, leading to confusion and potential security risks.

#### Best practices

1. **Follow a Standard Structure:** Include key details in the group name, such as department, function, and access level

   * Example: `[Department]-[Resource]-[Level]`
   * `HR-Payroll-ReadOnly` or `IT-SharePoint-Admin`
2. **Use Prefixes for Type Indication:** Add a prefix to indicate the type of group

   * `DL-` for Distribution List, `SEC-` for Security Group, `O365-` for Office 365 Group 'Intune-' for Intune policies
3. **Avoid Ambiguity:** Ensure names are descriptive but concise. Avoid generic terms like "Admin" or "Users" that lack specific context
4. **Adopt Case Conventions:** Use consistent casing, such as PascalCase or lowercase, for easy readability. [Kebab-case is recommended](/how-to-name-documents).

#### Common naming conventions examples

| **Name**                                           | **Purpose**                                           |
| -------------------------------------------------- | ----------------------------------------------------- |
| SEC-IT-VPN-Access                                  | Provides VPN access for IT personnel.                 |
| SEC-Marketing-WebAnalytics                         | Grants access to web analytics tools.                 |
| SEC-Finance-ERP-ReadOnly                           | Read-only access to the ERP system.                   |
| O365-SharePoint-Accounts-private-library-ReadWrite | Read-write access to the Accounts SharePoint library. |
| DL-All-Company-Broadcast                           | Organization-wide communication group.                |
| Intune-User-AccountingSoftware                     | Intune user policy to install accounting software.    |
| Intune-Computer-ScreenTimeout                      | Intune computer screen timeout policy.                |

::: good
Figure: Good example - Access group naming conventions that improve clarity and reduce errors in assignment
:::

- - -

By adhering to these best practices, including clear naming conventions for access groups, you can strengthen your organization's security posture and streamline the management of Microsoft Entra ID.
