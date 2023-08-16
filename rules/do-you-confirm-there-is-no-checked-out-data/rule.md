---
type: rule
title: Do you confirm there is no checked out data?
uri: do-you-confirm-there-is-no-checked-out-data
authors:
  - title: Greg Harris
    url: https://ssw.com.au/people/greg-harris
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: William Yin
    url: https://ssw.com.au/people/william-yin
related: []
redirects: []
created: 2012-05-31T03:08:59.000Z
archivedreason: null
guid: 12122af0-1a73-42e8-aa52-6fcc520c5cc7
---

One of the annoying things with SharePoint document libraries is that users often accidentally leave [checked out files](https://support.microsoft.com/en-us/office/check-out-check-in-or-discard-changes-to-files-in-a-sharepoint-library-7e2c12a9-a874-4393-9511-1378a700f6de), that prevents others from modifying them.

<!--endintro-->

::: greybox
**Suggestion to Microsoft:** send an email to the user to remind them they have outstanding checkouts potentially blocking other users.
:::

![Figure: Here Greg Harris has not checked in a file](sp-docs.jpg)  

**Upgrade warning:** The pages that are not checked-in, will not be migrated on a SharePoint upgrade. There is \*no\* warning either.

There are 2 ways to remind users of their "checked out files":

* **Solution A: Manage Content and Structure Report (No Code)**
* **Solution B: Custom application report (Includes some low-code work) E.g. SSW.Dory**

### Solution A. Manage Content and Structure Report (No Code)

1. Create CAML query in site content and structure

    Go to **Site Settings | Manage Content and Structure | Content and Structure Reports**, click "New":

    ![Figure: Create a new report](ContentAndStructureReportsNew.png)  

    Fill the "CAML Query":
    ```caml
    <Where>
      <IsNotNull>
        <FieldRef Name="CheckoutUser" LookupId="TRUE"/>
      </IsNotNull>
    </Where>
    ```

    Fill the other fields like below:
    ![Figure: Fill in form](NewReportForm.png)  

2. Run Checked Out report

    Run the checkout report from **Site Settings | Manage Content and Structure | View: Checked out documents**:

    ![Figure: Checked Out Documents report link Make sure there are no files checked out, otherwise, go step 3](CheckedOutDocuments.png)  

3. Go chase after the users.

### Solution B. Custom application report (Includes some low-code work)

::: todo
**TODO:** Move this tool to GitHub, find a better name than "SSW.SharePoint.CheckedOutFilesReport". Also change from a farm solution to a solution that can be used on Office365 - now in SharePoint 2016 and SharePoint online called "Sharepoint Add-ins" 
:::

To make reminding users easier, this SharePoint Add-in has a custom page to show the "Checked out files". One button will send the notification email to all the naughty people. 

Even better, we have also improved the application with a scheduled task using SharePoint CSOM API to find checked out files and send these notification emails automatically every night.

![Figure: One button reminds all users of their "Checked out Files"](CheckedOutFilesApplicationReport.png)

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
