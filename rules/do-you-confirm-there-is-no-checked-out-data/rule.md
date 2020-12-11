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


<p>​<br></p><p class="p1">One of the annoying things with SharePoint document libraries is that users often accidentally leave checked out files, that preventing others from modifying them.​​<br></p><p class="p1">Suggestion to Microsoft: send an email to the user to remind them they have outstanding checkouts potentially blocking other users.</p><dl class="image"><dt> 
      <img src="sp-docs.jpg" alt="sp-docs.jpg" style="margin:0px;width:780px;height:120px;" /> 
   </dt><dd>Figure: Here Greg Harris has not checked in a file </dd></dl><p></p><p> 
   <b>Upgrade warning:</b> The pages that are not checked-in, will not be migrated on a SharePoint upgrade. There is *no* warning either.​</p><p>There are 2 ways to remind users of their "checked out files":​<br></p><ul><li>
      <strong>Solution A: Manage Content and Structure Report (No Code)​</strong></li><li>
      <strong><strong>Solution B: Custom application report (Includes some coding work)​<br>Eg. SSW.Dory​​<br></strong></strong></li></ul>
<br><excerpt class='endintro'></excerpt><br>
​ 
<div>
   <strong>Solution A. Manage Content and Structure Report (No Code)</strong></div><div>1. Create CAML query in site content and structure</div><div>Go to "Site Settings | Manage Content and Structure | Content and Structure Reports", click "New":</div><dl class="image"><dt> 
      <img class="ssw-rteStyle-ImageArea" alt="ContentAndStructureReportsNew.png" src="ContentAndStructureReportsNew.png" /> 
   </dt><dd class="ssw-rteStyle-FigureNormal">Figure: Create a new report</dd></dl><div>
   <span>Fill the</span><span> "CAML Query":</span> 
   <div class="ssw-rteStyle-CodeArea"><Where><IsNotNull><FieldRef Name="CheckoutUser" LookupId="TRUE"/></IsNotNull></Where></div><p>Fill the other fields like below:</p><dl class="image"><dt> 
         <img class="ssw-rteStyle-ImageArea" alt="NewReportForm.png" src="NewReportForm.png" /> 
      </dt><dd>Figure: Fill in form</dd></dl><div>2. Run Checked Out report</div><div> </div><div>Run the checkout report from "Site Settings | Manage Content and Structure | View: Checked out documents":</div><dl class="image"><dt> 
         <img class="ssw-rteStyle-ImageArea" alt="CheckedOutDocuments.png" src="CheckedOutDocuments.png" /> 
      </dt><dd>Figure: Checked Out Documents report link Make sure there are no files checked out, otherwise, go step 3</dd></dl><div>3. Go chase after the users.</div>​ 
   <div>
      <strong>Solution B. Custom application report (Includes some coding work)<br></strong><span style="color:#cc0000;"><br></span></div><div>
      <span style="color:#cc0000;"> 
         <b>TODO: </b>Move this tool to GitHub, find a better name than "SSW.SharePoint.CheckedOutFilesReport". </span> 
      <span style="color:#cc0000;"> Also</span><span style="color:#cc0000;"> change from a farm solution to a solution that can be used on Office365 - now in SharePoint 2016 and SharePoint online called "Sharepoint Add-ins" </span></div><div>
      <font color="#cc0000"> 
         <br></font>To make reminding users easier, this SharePoint Add-in ha​s a custom page to show the "Checked out files". One button will send the notification email to all the naughty people. <br><br></div><div>Even better, we have also improved the application with a scheduled task using SharePoint CSOM API to find checked out files and send these notification emails automatically​ every night.<br>​<br></div><dl><dt>
         <img class="ssw-rteStyle-ImageArea" alt="CheckedOutFilesApplicationReport.png" src="CheckedOutFilesApplicationReport.png" />
      </dt><dd>Figure: One button reminds all users of their "Checked out Files"<br><br></dd></dl><div class="ssw-rteStyle-GreyBox" style="width:862px;height:344px;"><div>
         <strong>Hi Sophie, </strong></div><div>
         <strong></strong> </div><div>You have some pages checked out in SharePoint.</div><blockquote dir="ltr" style="margin-right:0px;"><div>1. You should check in at least daily. Revise our SSW rule <a href="/Pages/DoYouConfirmThereIsNoCheckedOutData.aspx"><font color="#3a66cc">on Frequent SharePoint Check-ins</font></a>.<br>2. If you are no longer editing these files, check them in! </div><div>3. Reply to this email with something like:<br>    ‘Done - x files checked in’</div><div><span style="font-size:inherit;"><br></span></div><div><span style="font-size:inherit;">You currently have the following pages checked out:</span><br></div></blockquote><blockquote dir="ltr"><div>• 
            <font color="#3a66cc"><a href="/Pages/DoYouConfirmThereIsNoCheckedOutData.aspx">http://<siteurl>/DesignandPresentation/RulesToBetterVideoRecording/Pages/Default.aspx</a>  (parent folder)</font><br>• 
            <font color="#3a66cc"><a href="/Pages/DoYouConfirmThereIsNoCheckedOutData.aspx">http://<siteurl>/DesignandPresentation/RulesToBetterVideoRecording/Pages/testing-rule.aspx</a>  (parent folder)</font></div></blockquote><div>
         <br>Tip: See all files you have checked out at <a href="/Pages/DoYouConfirmThereIsNoCheckedOutData.aspx"><font color="#3a66cc">http://<siteurl>/_layouts/<span>SSWReports/CheckedOutReport.aspx</span></font></a></div><div><span style="font-size:inherit;"><As per rule http://rules.ssw.com.au/ITAndNetworking/SharePoint/Pages/DoYouConfirmThereIsNoCheckedOutData.aspx></span><br></div><p><br><span style="font-size:inherit;">-- Powered by SSW.Dory<br></span><span style="font-size:inherit;">-- </span><span style="font-size:inherit;">v16.1.7122.24300 Server: DESKTOP-C7SF4A3</span></p><p><br><br></p></div><dd class="ssw15-rteElement-FigureNormal"> Figure: An example of the reminder email that all users receive </dd><dd class="ssw15-rteElement-FigureNormal">
      <br><br></dd></div>


