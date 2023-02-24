---
type: rule
archivedreason: 
title: Do you confirm there is no checked out data?
guid: 12122af0-1a73-42e8-aa52-6fcc520c5cc7
uri: do-you-confirm-there-is-no-checked-out-data
created: 2012-05-31T03:08:59.0000000Z
authors:
- title: Greg Harris
  url: https://ssw.com.au/people/greg-harris
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: William Yin
  url: https://ssw.com.au/people/william-yin
related: []
redirects: []

---

One of the annoying things with SharePoint document libraries is that users often accidentally leave checked out files, that preventing others from modifying them.

<!--endintro-->

::: greybox
**Suggestion to Microsoft:** send an email to the user to remind them they have outstanding checkouts potentially blocking other users.
:::

![Figure: Here Greg Harris has not checked in a file](sp-docs.jpg)  

**Upgrade warning:** The pages that are not checked-in, will not be migrated on a SharePoint upgrade. There is \*no\* warning either.

There are 2 ways to remind users of their "checked out files":

* **Solution A: Manage Content and Structure Report (No Code)**
* **Solution B: Custom application report (Includes some coding work) E.g. SSW.Dory**

### Solution A. Manage Content and Structure Report (No Code)

1. Create CAML query in site content and structure

Go to "Site Settings | Manage Content and Structure | Content and Structure Reports", click "New":

![Figure: Create a new report](ContentAndStructureReportsNew.png)  

Fill the "CAML Query":
&lt;Where&gt;&lt;IsNotNull&gt;&lt;FieldRef Name="CheckoutUser" LookupId="TRUE"/&gt;&lt;/IsNotNull&gt;&lt;/Where&gt;

Fill the other fields like below:

![Figure: Fill in form](NewReportForm.png)  

2. Run Checked Out report

Run the checkout report from "Site Settings | Manage Content and Structure | View: Checked out documents":

![Figure: Checked Out Documents report link Make sure there are no files checked out, otherwise, go step 3](CheckedOutDocuments.png)  

3. Go chase after the users.

### Solution B. Custom application report (Includes some coding work)

::: todo
**TODO:** Move this tool to GitHub, find a better name than "SSW.SharePoint.CheckedOutFilesReport". Also change from a farm solution to a solution that can be used on Office365 - now in SharePoint 2016 and SharePoint online called "Sharepoint Add-ins" 
:::

To make reminding users easier, this SharePoint Add-in has a custom page to show the "Checked out files". One button will send the notification email to all the naughty people. 

Even better, we have also improved the application with a scheduled task using SharePoint CSOM API to find checked out files and send these notification emails automatically every night.


![Figure: One button reminds all users of their "Checked out Files"](CheckedOutFilesApplicationReport.png)

```
::: email-template  
|          |     |
| -------- | --- |
| To:      | Dave |
| Subject: | You have some pages checked out in SharePoint |  
::: email-content  

### Hi Dave,  

You have some pages checked out in SharePoint.

1. You should check in at least daily. Revise the SSW rule [on Frequent SharePoint Check-ins](/do-you-confirm-there-is-no-checked-out-data).
2. If you are no longer editing these files, check them in! 
3. Reply to this email with something like:
  
  >     ‘Done - x files checked in’

You currently have the following pages checked out:

- {{ LIST OF URLS }}

**Note:** See all files you have checked out at {{ LINK TO CHECKED OUT LIST }}

&lt;As per rule https://www.ssw.com.au/rules/do-you-confirm-there-is-no-checked-out-data&gt;


-- Powered by SSW.Dory
-- v16.1.7122.24300 Server: DESKTOP-C7SF4A3

:::  
:::  
**Figure: An example of the reminder email that all users receive**
