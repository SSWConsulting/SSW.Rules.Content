---
type: rule
title: Do you confirm there is no checked out files?
uri: no-checked-out-files
authors:
  - title: Greg Harris
    url: https://ssw.com.au/people/greg-harris
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: William Yin
    url: https://ssw.com.au/people/william-yin
  - title: Jean Thirion
    url: https://ssw.com.au/people/jean-thirion
related: []
redirects:
- do-you-confirm-there-is-no-checked-out-data
created: 2012-05-31T03:08:59.000Z
archivedreason: null
guid: 12122af0-1a73-42e8-aa52-6fcc520c5cc7
---

One of the annoying things with SharePoint document and page libraries is that users often accidentally leave [checked out files](https://support.microsoft.com/en-us/office/check-out-check-in-or-discard-changes-to-files-in-a-sharepoint-library-7e2c12a9-a874-4393-9511-1378a700f6de), that prevents others from modifying them.


<!--endintro-->

::: greybox
**Suggestion to Microsoft:** send an email to the user to remind them they have outstanding checkouts potentially blocking other users.
:::

![Figure: Here Greg Harris has not checked in a file](sp-docs.jpg)  


There are 2 ways to remind users of their "checked out files":

* **Solution A:** Use Powershell scripts (see [PNP.github.io sample](https://www.sharepointdiary.com/2017/06/sharepoint-online-get-all-checked-out-files-using-powershell.html#:~:text=Navigate%20to%20the%20document%20library,get%20all%20checked%20out%20documents))
* **Solution B:** Custom application report (Includes some low-code work) E.g. [SSW.Dory](https://sswdory.com/)


### Solution A. Powershell scripts

1. Create a new PowerShell Script

```powershell
#Config Variables
$SiteURL = "https://crescent.sharepoint.com/sites/marketing"
$CSVFilePath = "C:\Temp\CheckedOutFiles.csv"
 
#Connect to PnP Online
Connect-PnPOnline -Url $SiteURL -Credentials (Get-Credential)
 
#Get all document libraries
$CheckedOutFiles = @()
$DocumentLibraries = Get-PnPList | Where-Object {$_.BaseType -eq "DocumentLibrary" -and $_.Hidden -eq $False}
 
#Iterate through document libraries
ForEach ($List in $DocumentLibraries)
{
    Write-host "Processing Library:"$List.Title -f Yellow
     
    #Get All Checked out Files of the library
    $FilesCheckedOut = Get-PnPListItem -List $List -PageSize 500 | Where {$_["CheckoutUser"] -ne $Null}
     
    #Collect data from each checked-out file
    ForEach ($File in $FilesCheckedOut) 
    {
        $CheckedOutFiles += [PSCustomObject][ordered]@{
            Library         = $List.Title
            FileName        = $File.FieldValues.FileLeafRef
            CheckedOutTo    = $File.FieldValues.CheckoutUser.LookupValue
            Location        = $File.FieldValues.FileRef
        }
    }
}
#Export Checked out Files data to CSV File
$CheckedOutFiles
$CheckedOutFiles | Export-Csv -Path $CSVFilePath -NoTypeInformation
```
To run the script against your entire tenant, see [PNP.github.io sample](https://www.sharepointdiary.com/2017/06/sharepoint-online-get-all-checked-out-files-using-powershell.html#:~:text=Navigate%20to%20the%20document%20library,get%20all%20checked%20out%20documents)

2. Run the PowerShell script

3. Go chase after the users.

### Solution B. Custom application report (Includes some low-code work)

Learn more: [SSW.Dory](https://sswdory.com/)

To make reminding users easier, we have created a [Power Automate](https://powerautomate.microsoft.com/en-au/) flow called SSW.Dory that will find checked out files and send out a notification email to all the naughty people automatically every day. 

::: email-template  

|          |     |
| -------- | --- |
| To:      | Dave |
| Subject: | SSW.Dory \| 🔷 SharePoint files need your attention |

::: email-content  

### Hi Dave,  

You currently have the following pages **checked out in SharePoint**:

- {{ LIST OF URLS }}

1. If you are no longer editing these files, **check them in!**   
  Note: You should check in at least daily, as per rule [SSW.Rules | Do you confirm there is no checked out data?](/do-you-confirm-there-is-no-checked-out-data).
2. Reply to this email with something like:
  
  > ‘Done - x files checked in’

**Note:** See all files you have checked out at {{ LINK TO CHECKED OUT LIST }}

*-- Powered by Power Automate, Job: SSW.Dory*

:::   
:::

**Figure: An example of the reminder email that all users receive**
