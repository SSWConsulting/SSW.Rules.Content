---
type: rule
title: Do you confirm there is no checked out data?
uri: do-you-confirm-there-is-no-checked-out-data
created: 2012-05-31T03:08:59.0000000Z
authors:
- id: 70
  title: Greg Harris
- id: 1
  title: Adam Cogan
- id: 9
  title: William Yin

---



<span class='intro'> <p>​<br></p><p class="p1">One of the annoying things with SharePoint document libraries is that users often accidentally leave checked out files, that preventing others from modifying them.​​<br></p><p class="p1">Suggestion to Microsoft&#58; send an email to the user to remind them they have outstanding checkouts potentially blocking other users.</p><dl class="image"><dt> 
      <img src="sp-docs.jpg" alt="sp-docs.jpg" style="margin&#58;0px;width&#58;780px;height&#58;120px;" /> 
   </dt><dd>Figure&#58; Here Greg Harris has not checked in a file </dd></dl><p></p><p> 
   <b>Upgrade warning&#58;</b> The pages that are not checked-in, will not be migrated on a SharePoint upgrade. There is *no* warning either.​</p><p>There are 2 ways to remind users of their &quot;checked out files&quot;&#58;​<br></p><ul><li>
      <strong>Solution A&#58; Manage Content and Structure Report (No Code)​</strong></li><li>
      <strong><strong>Solution B&#58; Custom application report (Includes some coding work)​<br>Eg.&#160;SSW.Dory​​<br></strong></strong></li></ul> </span>

​ 
<div>
   <strong>Solution A. Manage Content and Structure Report (No Code)</strong></div><div>1. Create CAML query in site content and structure</div><div>Go to &quot;Site Settings | Manage Content and Structure | Content and Structure Reports&quot;, click &quot;New&quot;&#58;</div><dl class="image"><dt> 
      <img class="ssw-rteStyle-ImageArea" alt="ContentAndStructureReportsNew.png" src="ContentAndStructureReportsNew.png" /> 
   </dt><dd class="ssw-rteStyle-FigureNormal">Figure&#58; Create a new report</dd></dl><div>
   <span>Fill the</span><span>&#160;&quot;CAML Query&quot;&#58;</span> 
   <div class="ssw-rteStyle-CodeArea">&lt;Where&gt;&lt;IsNotNull&gt;&lt;FieldRef Name=&quot;CheckoutUser&quot; LookupId=&quot;TRUE&quot;/&gt;&lt;/IsNotNull&gt;&lt;/Where&gt;</div><p>Fill the other fields like below&#58;</p><dl class="image"><dt> 
         <img class="ssw-rteStyle-ImageArea" alt="NewReportForm.png" src="NewReportForm.png" /> 
      </dt><dd>Figure&#58; Fill in form</dd></dl><div>2. Run Checked Out report</div><div>&#160;</div><div>Run the checkout report from &quot;Site Settings | Manage Content and Structure | View&#58; Checked out documents&quot;&#58;</div><dl class="image"><dt> 
         <img class="ssw-rteStyle-ImageArea" alt="CheckedOutDocuments.png" src="CheckedOutDocuments.png" /> 
      </dt><dd>Figure&#58; Checked Out Documents report link Make sure there are no files checked out, otherwise, go step 3</dd></dl><div>3. Go chase after the users.</div>​ 
   <div>
      <strong>Solution B. Custom application report (Includes some coding work)<br></strong><span style="color&#58;#cc0000;"><br></span></div><div>
      <span style="color&#58;#cc0000;"> 
         <b>TODO&#58; </b>Move this tool to GitHub, find a better name than &quot;SSW.SharePoint.CheckedOutFilesReport&quot;. </span> 
      <span style="color&#58;#cc0000;"> Also</span><span style="color&#58;#cc0000;"> change from a farm solution to a solution that can be used on Office365 - now in SharePoint 2016 and SharePoint online called &quot;Sharepoint Add-ins&quot;&#160;</span></div><div>
      <font color="#cc0000"> 
         <br></font>To make reminding users&#160;easier, this SharePoint Add-in&#160;ha​s&#160;a custom page to show the &quot;Checked out files&quot;. One button will&#160;send the notification email to all the naughty people. <br><br></div><div>Even better, we have also improved the application with&#160;a scheduled task using SharePoint CSOM API to find checked out files and send these notification emails automatically​ every night.<br>​<br></div><dl><dt>
         <img class="ssw-rteStyle-ImageArea" alt="CheckedOutFilesApplicationReport.png" src="CheckedOutFilesApplicationReport.png" />
      </dt><dd>Figure&#58; One button reminds all users of their&#160;&quot;Checked out Files&quot;<br><br></dd></dl><div class="ssw-rteStyle-GreyBox" style="width&#58;862px;height&#58;344px;"><div>
         <strong>Hi Sophie, </strong></div><div>
         <strong></strong>&#160;</div><div>You have some pages checked out in SharePoint.</div><blockquote dir="ltr" style="margin-right&#58;0px;"><div>1. You should check in at least daily. Revise our SSW rule <a href="/Pages/DoYouConfirmThereIsNoCheckedOutData.aspx"><font color="#3a66cc">on Frequent SharePoint Check-ins</font></a>.<br>2. If you are no longer editing these files, check them in! </div><div>3.&#160;Reply to this email with something like&#58;<br>&#160; &#160; ‘Done - x files checked in’</div><div><span style="font-size&#58;inherit;"><br></span></div><div><span style="font-size&#58;inherit;">You currently have the following pages checked out&#58;</span><br></div></blockquote><blockquote dir="ltr"><div>• 
            <font color="#3a66cc"><a href="/Pages/DoYouConfirmThereIsNoCheckedOutData.aspx">http&#58;//&lt;siteurl&gt;/DesignandPresentation/RulesToBetterVideoRecording/Pages/Default.aspx</a>&#160;&#160;(parent folder)</font><br>• 
            <font color="#3a66cc"><a href="/Pages/DoYouConfirmThereIsNoCheckedOutData.aspx">http&#58;//&lt;siteurl&gt;/DesignandPresentation/RulesToBetterVideoRecording/Pages/testing-rule.aspx</a>&#160;&#160;(parent folder)</font></div></blockquote><div>
         <br>Tip&#58; See all files you have checked&#160;out at&#160;<a href="/Pages/DoYouConfirmThereIsNoCheckedOutData.aspx"><font color="#3a66cc">http&#58;//&lt;siteurl&gt;/_layouts/<span>SSWReports/CheckedOutReport.aspx</span></font></a></div><div><span style="font-size&#58;inherit;">&lt;As per rule http&#58;//rules.ssw.com.au/ITAndNetworking/SharePoint/Pages/DoYouConfirmThereIsNoCheckedOutData.aspx&gt;</span><br></div><p><br><span style="font-size&#58;inherit;">-- Powered by SSW.Dory<br></span><span style="font-size&#58;inherit;">-- </span><span style="font-size&#58;inherit;">v16.1.7122.24300 Server&#58; DESKTOP-C7SF4A3</span></p><p><br><br></p></div><dd class="ssw15-rteElement-FigureNormal">&#160;Figure&#58; An example of the reminder email that all users receive </dd><dd class="ssw15-rteElement-FigureNormal">
      <br><br></dd></div>


