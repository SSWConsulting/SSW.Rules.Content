---
type: rule
archivedreason: 
title: Do you confirm there is no checked out data?
guid: 12122af0-1a73-42e8-aa52-6fcc520c5cc7
uri: do-you-confirm-there-is-no-checked-out-data
created: 2012-05-31T03:08:59.0000000Z
authors:
- id: 70
  title: Greg Harris
- id: 1
  title: Adam Cogan
- id: 9
  title: William Yin
related: []

---

One of the annoying things with SharePoint document libraries is that users often accidentally leave checked out files, that preventing others from modifying them.

Suggestion to Microsoft: send an email to the user to remind them they have outstanding checkouts potentially blocking other users.
<dl class="image">&lt;dt&gt; 
      <img src="sp-docs.jpg" alt="sp-docs.jpg" style="margin:0px;width:780px;height:120px;"> 
   &lt;/dt&gt;<dd>Figure: Here Greg Harris has not checked in a file </dd></dl>


**Upgrade warning:** The pages that are not checked-in, will not be migrated on a SharePoint upgrade. There is \*no\* warning either.

There are 2 ways to remind users of their "checked out files":

* **Solution A: Manage Content and Structure Report (No Code)**
* ** Solution B: Custom application report (Includes some coding work)
Eg. SSW.Dory
 **


<!--endintro-->

**Solution A. Manage Content and Structure Report (No Code)** 

1. Create CAML query in site content and structure

Go to "Site Settings | Manage Content and Structure | Content and Structure Reports", click "New":
<dl class="image">&lt;dt&gt; 
      <img class="ssw-rteStyle-ImageArea" alt="ContentAndStructureReportsNew.png" src="ContentAndStructureReportsNew.png"> 
   &lt;/dt&gt;<dd class="ssw-rteStyle-FigureNormal">Figure: Create a new report</dd></dl>
Fill the "CAML Query":
<where><isnotnull><fieldref name="CheckoutUser" lookupid="TRUE"></fieldref></isnotnull></where>

Fill the other fields like below:
<dl class="image">&lt;dt&gt; 
         <img class="ssw-rteStyle-ImageArea" alt="NewReportForm.png" src="NewReportForm.png"> 
      &lt;/dt&gt;<dd>Figure: Fill in form</dd></dl>
2. Run Checked Out report

 

Run the checkout report from "Site Settings | Manage Content and Structure | View: Checked out documents":
<dl class="image">&lt;dt&gt; 
         <img class="ssw-rteStyle-ImageArea" alt="CheckedOutDocuments.png" src="CheckedOutDocuments.png"> 
      &lt;/dt&gt;<dd>Figure: Checked Out Documents report link Make sure there are no files checked out, otherwise, go step 3</dd></dl>
3. Go chase after the users.

**Solution B. Custom application report (Includes some coding work)
** 


**TODO:** Move this tool to GitHub, find a better name than "SSW.SharePoint.CheckedOutFilesReport".  Also change from a farm solution to a solution that can be used on Office365 - now in SharePoint 2016 and SharePoint online called "Sharepoint Add-ins" 

<font color="#cc0000"> 
         <br></font>To make reminding users easier, this SharePoint Add-in has a custom page to show the "Checked out files". One button will send the notification email to all the naughty people. 



Even better, we have also improved the application with a scheduled task using SharePoint CSOM API to find checked out files and send these notification emails automatically every night.


<dl>&lt;dt&gt;
         <img class="ssw-rteStyle-ImageArea" alt="CheckedOutFilesApplicationReport.png" src="CheckedOutFilesApplicationReport.png">
      &lt;/dt&gt;<dd>Figure: One button reminds all users of their "Checked out Files"<br><br></dd></dl>

**Hi Sophie,** 

 

You have some pages checked out in SharePoint.


> 1. You should check in at least daily. Revise our SSW rule [<font color="#3a66cc">on Frequent SharePoint Check-ins</font>](/Pages/DoYouConfirmThereIsNoCheckedOutData.aspx).
> 2. If you are no longer editing these files, check them in! 
> 
> 3. Reply to this email with something like:
>     ‘Done - x files checked in’
> 
> 
> 
> 
> You currently have the following pages checked out:



> • <br>            <font color="#3a66cc"><a href="/Pages/DoYouConfirmThereIsNoCheckedOutData.aspx">http://<siteurl>/DesignandPresentation/RulesToBetterVideoRecording/Pages/Default.aspx</siteurl></a>  (parent folder)</font>
> • <br>            <font color="#3a66cc"><a href="/Pages/DoYouConfirmThereIsNoCheckedOutData.aspx">http://<siteurl>/DesignandPresentation/RulesToBetterVideoRecording/Pages/testing-rule.aspx</siteurl></a>  (parent folder)</font>



Tip: See all files you have checked out at [<font color="#3a66cc">http://<siteurl>/_layouts/<span>SSWReports/CheckedOutReport.aspx</span></siteurl></font>](/Pages/DoYouConfirmThereIsNoCheckedOutData.aspx)

<as per="" rule="" http://rules.ssw.com.au/itandnetworking/sharepoint/pages/doyouconfirmthereisnocheckedoutdata.aspx=""></as>


-- Powered by SSW.Dory
-- v16.1.7122.24300 Server: DESKTOP-C7SF4A3



 **Figure: An example of the reminder email that all users receive** **

**
