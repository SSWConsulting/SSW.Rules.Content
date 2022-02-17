---
type: rule
title: Do you change link sharing default behaviour?
uri: change-link-sharing-default-behaviour
authors:
  - title: Warwick Leahy
    url: warwick-leahy
  - title: Jean Thirion
    url: jean-thirion
created: 2022-02-07T00:14:18.003Z
guid: 086a184c-b63f-4726-9eb7-bfd6fef3432a
---
If you are checking your sites permissions regularly you will probably notice a lot of unique permissions being applied.



![Figure: Some items may have unique permissions](uniquepermissions.png)



The default "Copy Link" setting in SharePoint is usually set to "People from your organization can view this document".  This creates a unique sharing link each time it is used, giving people access to the file even if they didn't already.

Consequence in SharePoint is that unique permissions are applied to the individual items breaking permission inheritance.  Links should instead be created with the "People with existing access" setting.



<!--endintro-->



To fix the issue you need to change the default sharing method.  There are 2 ways to do this - manually via the GUI or programmatically via PNP.PowerShell.



## Method 1 - Manually via SharePoint Admin GUI

1. In the SharePoint Admin site select the SharePoint site and click Sharing

   ![Figure: Select Sharing](defaultsharinglinktype1.png)


2. Untick same as organization-level setting | Select People with existing access | Click Save

   ![Figure: Select people with existing access](defaultsharinglinktype2.png)



3. Repeat for each site



## Method 2 - Programmatically via PNP.PowerShell



1. Run the following script to change this default for all sites associated to your SharePoint Hub-Site - This could be extended to include all sites in your tenant if required.



```
#Variables
$AdminCenterURL = "https://sswcom-northwind.sharepoint.com"
$HubSiteURL = "https://sswcom.northwind.com"

 
#Connect to PnP Online
Connect-PnPOnline -Url $AdminCenterURL -Interactive
 
#Get the children of the main HubSite
$Hub = Get-PnPHubSiteChild -Identity $HubSiteURL


foreach ($Url in $Hub)
{
    #Remove the "Same as organization-level" setting. Can be set to anything Internal, None or Direct.  
    Set-PnPTenantSite -Url $Url -DefaultSharingLinkType Internal

    #Set the Default Link type to be Existing Access
    Set-PnPTenantSite -Url $Url -DefaultLinkToExistingAccess $true
    
}
```