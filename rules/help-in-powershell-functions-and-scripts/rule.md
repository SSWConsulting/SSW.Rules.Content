---
type: rule
title: Do you use Comment-Based Help in PowerShell functions and scripts?
uri: help-in-powershell-functions-and-scripts
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Kaique Biancatti
    url: https://ssw.com.au/people/kaique-biancatti
related: []
redirects:
  - do-you-use-comment-based-help-in-powershell-functions-and-scripts
created: 2020-03-24T21:36:14.000Z
archivedreason: null
guid: 542db12e-4a45-4ae6-b649-0136d39b27f6
---

In PowerShell, you can use Comment-Based Help snippets to better define what your function or script is doing, its examples, inputs, and outputs.

When you are building functions in PowerShell, you can use Comment-Based Help snippets at the beginning of the function body, at the end of the function body or before the Function keyword. 

If you do this, the Get-Help cmdlet will show the information contained in the code for your function (making it super easy for anyone to use and understand it!).

<!--endintro-->

You can use it like this (beginning of the Function body):

```powershell
function Get-Function
{
  <#
    .<help keyword>
    <help content>
  #>

  # function logic
}
```
::: good
Figure: Good example - Using Comment-Based Help for Functions
:::

Or like this (before the function keyword):

```powershell
<#
  .<help keyword>
  <help content>
#>
function Get-Function { }
```
::: good
Figure: Good example - Using Comment-Based Help for Function  
:::

You can do the same with scripts, with a little difference - you need to place the snippet at the beginning or end of the script file:


```powershell
#Accept input parameters
param(
    [switch]$FullAccess,
    [switch]$SendAs,
    [switch]$SendOnBehalf,
    [switch]$UserMailboxOnly,
    [switch]$AdminsOnly,
    [string]$MBNamesFile,
    [string]$UserName,
    [string]$Password,
    [switch]$MFA
)
```
::: bad
Figure: Bad example - Script not using any Comment-Based Help snippet
:::

```powershell
<#
.SYNOPSIS
Gets THE IP addresses in a file and checks if they are on blacklists across the web.

.DESCRIPTION
Gets THE IP addresses in a file and checks if they are on blacklists across the web. If they are, add them to the final blacklist file that will be used by the firewall.

.EXAMPLE
PS C:\> Check-Blacklist -File "FileWithNewIPs" -BaseFile "BaseBlacklistFile" -Logfile "LogfileLocation"
Checks the newly-generated blacklist file to see if any IPs are blacklisted, if yes, adds them to the final blacklist file.

.NOTES
Created by Kiki Biancatti for SSW.

#>
Param(
[Parameter(Position = 0, Mandatory = $true)]
[string] $File,
[Parameter(Position = 1, Mandatory = $true)]
[string] $BaseFile,
[Parameter(Position = 2, Mandatory = $true)]
[string] $LogFile
) ...
```
::: good
Figure: Good example - Using Comment-Based Help at the beginning of a script file
:::

You can check some good PowerShell examples in [SSW's GitHub](https://github.com/SSWConsulting):
* [github.com/SSWConsulting/SSWSysAdmins.ITPurchaseRequestForm](https://github.com/SSWConsulting/SSWSysAdmins.ITPurchaseRequestForm)
* [github.com/SSWConsulting/SSWSysAdmins.BlacklistChecker](https://github.com/SSWConsulting/SSWSysAdmins.BlacklistChecker)
* [github.com/SSWConsulting/SSWSysAdmins.LeavingStandard](https://github.com/SSWConsulting/SSWSysAdmins.LeavingStandard)
