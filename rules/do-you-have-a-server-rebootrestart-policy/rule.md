---
type: rule
title: Do you have a server reboot/restart policy?
uri: do-you-have-a-server-rebootrestart-policy
created: 2017-06-30T19:21:55.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 47
  title: Stanley Sidik
- id: 71
  title: Steven Andrews

---



<span class='intro'> <p>If your servers are down or have to go down during business hours you should notify the users at least 15 minutes beforehand so you will not get 101 people all asking you if the computer is down.<br></p><p>For short outages (under 15 minutes) that only affect only a few people (under 5 people), or are outside of business hours, then IM is the best method.&#160;If you use 
   <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=3a474efa-ca72-4320-af36-b0e6af355684">Teams or Skype</a>&#160;a quick&#160;message will do.&#160;</p><p>
   <b>Note&#58; </b>If they are not online on Teams or Skype, then they can't complain that they were not warned. 
   <br></p><p>For extended or planned outages, or if you have a larger number of users (50+), 
   <b>email</b> is the suggested method.​​<br></p> </span>

<h3 class="ssw15-rteElement-H3">Email</h3><p>If you send an email it is a good idea to tell the user a way to monitor the network themselves. Eg. Software solutions like SCOM or WhatsUp Gold. 
   <br></p><p>Include a &quot;<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=5c16d531-007d-49ef-8acc-b26596e13e84">To&#160;myself</a>&quot;. It gives visibility to others who are interested in what needs to be done to fix the problem and makes<br>it easier to remember to send the 'done' email. E.g. &quot;done - CRM is alive again&quot;.&#160;</p><p>Example&#58; 
   <br></p><dl class="greyBox"><dt style="padding-right&#58;0px;padding-left&#58;0px;margin-top&#58;0px;margin-bottom&#58;0px;margin-left&#58;10px;font-size&#58;1em;"> 
      <strong>To&#58;&#160;</strong>SSWALL</dt><dt style="padding-right&#58;0px;padding-left&#58;0px;margin-top&#58;0px;margin-bottom&#58;0px;margin-left&#58;10px;font-size&#58;1em;"> 
      <br> 
   </dt><dt style="padding-right&#58;0px;padding-left&#58;0px;margin-top&#58;0px;margin-bottom&#58;0px;margin-left&#58;10px;font-size&#58;1em;">Hi All, 
      <br>
      <br>Here&#160;is the summary of the outage plan&#58;<br style="font-size&#58;1em;"><br style="font-size&#58;1em;">
      <table style="margin-top&#58;0px;margin-bottom&#58;0px;font-size&#58;1em;"><tbody><tr><td>
                  <strong>Planned/Unplanned&#58;</strong></td><td>Planned</td></tr><tr><td>
                  <strong>Change Description&#58;</strong></td><td>Install Windows Updates and Restart Server<br></td></tr><tr><td>
                  <strong>Risk (see table below)&#58;</strong></td><td>LOW RISK (LOW Probability and MEDIUM Impact)</td></tr><tr><td>
                  <strong>Reason For Change&#58;</strong></td><td>Windows 2016&#160;Windows Updates<br></td></tr><tr><td>
                  <strong>Uptime over last month&#58;</strong></td><td>91.361%</td></tr><tr><td></td><td> 
                  <br> 
               </td></tr><tr><td>
                  <strong>Planned Outage (mins)&#58;</strong></td><td>150</td></tr><tr><td>
                  <strong>Planned Start Time&#58;</strong></td><td>26 October 9&#58;00 PM</td></tr><tr><td>
                  <strong>Planned Finish Time&#58;</strong></td><td>26 October 11&#58;30 PM<br></td></tr><tr><td></td><td></td></tr><tr><td>
                  <strong>Affected Services&#58;</strong></td><td>\\Windows&#160;Server 2016<br></td></tr><tr><td></td><td>http&#58;//sharepoint.ssw.com.au<br style="font-size&#58;1em;">http&#58;//intranet.ssw.com.au<br style="font-size&#58;1em;">http&#58;//projects.ssw.com.au</td></tr><tr><td></td><td>
                  <br>
               </td></tr></tbody></table>
      <br>
      <strong>Risk Lookup Table by Probability and Impact&#58;</strong><br style="font-size&#58;1em;">
      <table border="0" cellspacing="0" cellpadding="0" style="margin-top&#58;0px;margin-bottom&#58;0px;font-size&#58;1em;"><tbody><tr><td width="554" colspan="6" valign="top" style="padding&#58;0cm 5.4pt;width&#58;415.35pt;border&#58;1pt solid black;background&#58;#eeece1;"> 
                  <strong style="font-size&#58;1em;">Risk</strong></td></tr><tr style="font-size&#58;1em;"><td width="182" colspan="2" rowspan="2" valign="top" style="padding&#58;0cm 5.4pt;width&#58;136.2pt;border-right&#58;1pt solid black;border-bottom&#58;1pt solid black;border-left&#58;1pt solid black;border-top&#58;none;"><p align="center" style="margin-top&#58;7px;margin-bottom&#58;7px;text-align&#58;center;">
                     <strong></strong></p></td><td width="372" colspan="4" style="padding&#58;0cm 5.4pt;width&#58;279.15pt;border-top&#58;none;border-left&#58;none;border-bottom&#58;1pt solid black;border-right&#58;1pt solid black;"><p align="center" style="margin-top&#58;7px;margin-bottom&#58;7px;text-align&#58;center;">
                     <strong>Probability</strong></p></td></tr><tr style="font-size&#58;1em;"><td width="91" valign="top" style="padding&#58;0cm 5.4pt;width&#58;68.1pt;border-top&#58;none;border-left&#58;none;border-bottom&#58;1pt solid black;border-right&#58;1pt solid black;"><p style="margin-top&#58;7px;margin-bottom&#58;7px;">
                     <strong>Low</strong></p></td><td width="99" valign="top" style="padding&#58;0cm 5.4pt;width&#58;74.2pt;border-top&#58;none;border-left&#58;none;border-bottom&#58;1pt solid black;border-right&#58;1pt solid black;"><p style="margin-top&#58;7px;margin-bottom&#58;7px;">
                     <strong>Medium</strong></p></td><td width="91" valign="top" style="padding&#58;0cm 5.4pt;width&#58;68.1pt;border-top&#58;none;border-left&#58;none;border-bottom&#58;1pt solid black;border-right&#58;1pt solid black;"><p style="margin-top&#58;7px;margin-bottom&#58;7px;">
                     <strong>High</strong></p></td><td width="92" valign="top" style="padding&#58;0cm 5.4pt;width&#58;68.75pt;border-top&#58;none;border-left&#58;none;border-bottom&#58;1pt solid black;border-right&#58;1pt solid black;"><p style="margin-top&#58;7px;margin-bottom&#58;7px;">
                     <strong>Unknown</strong></p></td></tr><tr style="font-size&#58;1em;"><td width="91" rowspan="4" style="padding&#58;0cm 5.4pt;width&#58;68.1pt;border-right&#58;1pt solid black;border-bottom&#58;1pt solid black;border-left&#58;1pt solid black;border-top&#58;none;"><p align="center" style="margin-top&#58;7px;margin-bottom&#58;7px;text-align&#58;center;">
                     <strong>Impact</strong></p></td><td width="91" valign="top" style="padding&#58;0cm 5.4pt;width&#58;68.1pt;border-top&#58;none;border-left&#58;none;border-bottom&#58;1pt solid black;border-right&#58;1pt solid black;"><p style="margin-top&#58;7px;margin-bottom&#58;7px;">
                     <strong>Low</strong></p></td><td width="91" valign="top" style="padding&#58;0cm 5.4pt;width&#58;68.1pt;border-top&#58;none;border-left&#58;none;border-bottom&#58;1pt solid black;border-right&#58;1pt solid black;"><p style="margin-top&#58;7px;margin-bottom&#58;7px;">Low risk<br></p></td><td width="99" valign="top" style="padding&#58;0cm 5.4pt;width&#58;74.2pt;border-top&#58;none;border-left&#58;none;border-bottom&#58;1pt solid black;border-right&#58;1pt solid black;"><p style="margin-top&#58;7px;margin-bottom&#58;7px;">Low Risk<br></p></td><td width="91" valign="top" style="padding&#58;0cm 5.4pt;width&#58;68.1pt;border-top&#58;none;border-left&#58;none;border-bottom&#58;1pt solid black;border-right&#58;1pt solid black;"><p style="margin-top&#58;7px;margin-bottom&#58;7px;">Low Risk</p></td><td width="91" valign="top" style="padding&#58;0cm 5.4pt;width&#58;68.75pt;border-top&#58;none;border-left&#58;none;border-bottom&#58;1pt solid black;border-right&#58;1pt solid black;"><p style="margin-top&#58;7px;margin-bottom&#58;7px;">Medium Risk<br></p></td></tr><tr style="font-size&#58;1em;"><td width="91" valign="top" style="padding&#58;0cm 5.4pt;width&#58;68.1pt;border-top&#58;none;border-left&#58;none;border-bottom&#58;1pt solid black;border-right&#58;1pt solid black;"><p style="margin-top&#58;7px;margin-bottom&#58;7px;">
                     <strong>Medium</strong></p></td><td width="91" valign="top" style="padding&#58;0cm 5.4pt;width&#58;68.1pt;border-top&#58;none;border-left&#58;none;border-bottom&#58;1pt solid black;border-right&#58;1pt solid black;background&#58;yellow;"><p style="margin-top&#58;7px;margin-bottom&#58;7px;">Low Risk 
                     <br></p></td><td width="99" valign="top" style="padding&#58;0cm 5.4pt;width&#58;74.2pt;border-top&#58;none;border-left&#58;none;border-bottom&#58;1pt solid black;border-right&#58;1pt solid black;"><p style="margin-top&#58;7px;margin-bottom&#58;7px;">Medium Risk<br></p></td><td width="91" valign="top" style="padding&#58;0cm 5.4pt;width&#58;68.1pt;border-top&#58;none;border-left&#58;none;border-bottom&#58;1pt solid black;border-right&#58;1pt solid black;"><p style="margin-top&#58;7px;margin-bottom&#58;7px;">Medium Risk</p></td><td width="91" valign="top" style="padding&#58;0cm 5.4pt;width&#58;68.75pt;border-top&#58;none;border-left&#58;none;border-bottom&#58;1pt solid black;border-right&#58;1pt solid black;"><p style="margin-top&#58;7px;margin-bottom&#58;7px;">High Risk</p></td></tr><tr style="font-size&#58;1em;"><td width="91" valign="top" style="padding&#58;0cm 5.4pt;width&#58;68.1pt;border-top&#58;none;border-left&#58;none;border-bottom&#58;1pt solid black;border-right&#58;1pt solid black;"><p style="margin-top&#58;7px;margin-bottom&#58;7px;">
                     <strong>High</strong></p></td><td width="91" valign="top" style="padding&#58;0cm 5.4pt;width&#58;68.1pt;border-top&#58;none;border-left&#58;none;border-bottom&#58;1pt solid black;border-right&#58;1pt solid black;">Medium Risk</td><td width="99" valign="top" style="padding&#58;0cm 5.4pt;width&#58;74.2pt;border-top&#58;none;border-left&#58;none;border-bottom&#58;1pt solid black;border-right&#58;1pt solid black;"><p style="margin-top&#58;7px;margin-bottom&#58;7px;">High Risk</p></td><td width="91" valign="top" style="padding&#58;0cm 5.4pt;width&#58;68.1pt;border-top&#58;none;border-left&#58;none;border-bottom&#58;1pt solid black;border-right&#58;1pt solid black;"><p style="margin-top&#58;7px;margin-bottom&#58;7px;">High Risk</p></td><td width="91" valign="top" style="padding&#58;0cm 5.4pt;width&#58;68.75pt;border-top&#58;none;border-left&#58;none;border-bottom&#58;1pt solid black;border-right&#58;1pt solid black;"><p style="margin-top&#58;7px;margin-bottom&#58;7px;">High Risk</p></td></tr><tr style="font-size&#58;1em;height&#58;24.75pt;"><td width="91" valign="top" style="padding&#58;0cm 5.4pt;width&#58;68.1pt;border-top&#58;none;border-left&#58;none;border-bottom&#58;1pt solid black;border-right&#58;1pt solid black;height&#58;24.75pt;"><p style="margin-top&#58;7px;margin-bottom&#58;7px;">
                     <strong>Unknown</strong></p></td><td width="91" valign="top" style="padding&#58;0cm 5.4pt;width&#58;68.1pt;border-top&#58;none;border-left&#58;none;border-bottom&#58;1pt solid black;border-right&#58;1pt solid black;height&#58;24.75pt;">Medium Risk
                  <p style="margin-top&#58;7px;margin-bottom&#58;7px;">
                     <span style="font-size&#58;1em;color&#58;#1f497d;"></span></p></td><td width="91" valign="top" style="padding&#58;0cm 5.4pt;width&#58;74.2pt;border-top&#58;none;border-left&#58;none;border-bottom&#58;1pt solid black;border-right&#58;1pt solid black;height&#58;24.75pt;"><p style="margin-top&#58;7px;margin-bottom&#58;7px;">High Risk<br></p></td><td width="91" valign="top" style="padding&#58;0cm 5.4pt;width&#58;68.1pt;border-top&#58;none;border-left&#58;none;border-bottom&#58;1pt solid black;border-right&#58;1pt solid black;height&#58;24.75pt;"><p style="margin-top&#58;7px;margin-bottom&#58;7px;">High Risk<br></p></td><td width="91" valign="top" style="padding&#58;0cm 5.4pt;width&#58;68.75pt;border-top&#58;none;border-left&#58;none;border-bottom&#58;1pt solid black;border-right&#58;1pt solid black;height&#58;24.75pt;"><p style="margin-top&#58;7px;margin-bottom&#58;7px;">High Risk 
                     <br></p></td></tr></tbody></table></dt><dt style="padding-right&#58;0px;padding-left&#58;0px;margin-top&#58;0px;margin-bottom&#58;0px;margin-left&#58;10px;"> 
      <b>Figure&#58; Clearly showing the potential risks<br><br></b></dt><dt style="padding-right&#58;0px;padding-left&#58;0px;margin-top&#58;0px;margin-bottom&#58;0px;margin-left&#58;10px;"><p class="ssw15-rteElement-P">
         <b> Note&#58; </b>The following servers will be affected<br></p>
      <img src="/PublishingImages/rule-outage-1.jpg" alt="rule-outage-1.jpg" style="margin&#58;0px;" /> 
      <br>
      <a href="http&#58;//wug.ssw.com.au/"> http&#58;//wug.ssw.com.au/</a><br><br><img src="/PublishingImages/rule-outage-2.jpg" alt="rule-outage-2.jpg" style="width&#58;750px;" /> 
      <br></dt><dt style="padding-right&#58;0px;padding-left&#58;0px;margin-top&#58;0px;margin-bottom&#58;0px;margin-left&#58;10px;"> 
      <br>
   </dt><dt style="padding-right&#58;0px;padding-left&#58;0px;margin-top&#58;0px;margin-bottom&#58;0px;margin-left&#58;10px;"> 
      <b>To myself,</b></dt><dt style="padding-right&#58;0px;padding-left&#58;0px;margin-top&#58;0px;margin-bottom&#58;0px;margin-left&#58;10px;"> 
      <b> 
         <br></b>To show others who are interested in what needs to be done to fix the problem&#58;<br><b>Detailed Change Plan&#58; </b><br>1) Lockout&#160;users via IIS<br>2) Backup server<br>3) Install Windows Updates&#160;<br>4) Reboot server<br>5) Follow&#160;test&#160;plan<br>6) Based on&#160;result&#160;of&#160;test&#160;plan, follow backout plan if&#160;procedure&#160;failed<br>7) Procedure completed</dt><dt style="padding-right&#58;0px;padding-left&#58;0px;margin-top&#58;0px;margin-bottom&#58;0px;margin-left&#58;10px;"> 
      <br>
      <b>Test Plan&#58; </b><br>1) Check Event log for errors<br>2) Check each affected service is running<br>3) Call test users to start “Test Please” on the affect services&#160;<br>4) Get result of user “Test Please” by email by 11&#58;15 PM</dt><dt style="padding-right&#58;0px;padding-left&#58;0px;margin-top&#58;0px;margin-bottom&#58;0px;margin-left&#58;10px;"> 
      <br>
      <b>Backout Plan&#58; </b><br>1) Restore server from backup<br></dt><dt style="padding-right&#58;0px;padding-left&#58;0px;margin-top&#58;0px;margin-bottom&#58;0px;margin-left&#58;10px;"> 
      <br>
      <b>Note&#58; </b>&lt;This is as per rule&#160;<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=e3a456b4-3513-4dbe-a958-0176c1dfa85d">What is your server reboot/restart policy?</a> &gt;<br></dt><dt style="padding-right&#58;0px;padding-left&#58;0px;margin-top&#58;0px;margin-bottom&#58;0px;margin-left&#58;10px;"> 
      <br>
   </dt></dl><p>Immediately before the scheduled downtime, check for logged in users, file access, and database connections.</p><h3 class="ssw15-rteElement-H3">Users</h3><p>Open 'Windows Task Manager' (Run &gt; taskmgr) and select the 'Users' tab. Check with users if they have active connections, then have them log off.<br></p><dl class="image"><dt> 
      <img src="/PublishingImages/rule-outage-3.png" alt="rule-outage-3.png" /> 
   </dt><dd>Figure&#58; Connected users can be viewed in Task Manager</dd></dl><h3 class="ssw15-rteElement-H3">Files</h3><p>Open 'Computer Management' (Run &gt; compmgmt.msc), then 'System Tools &gt; Shared Folders'. Check 'Session' and 'Open Files' for user connections.</p><dl class="image"><dt> 
      <img src="/PublishingImages/rule-outage-4.png" alt="rule-outage-4.png" /> 
   </dt><dd>Figure&#58; Computer Management 'Open Files' View</dd></dl><h3 class="ssw15-rteElement-H3">Database</h3><p>Open SQL Server Management Studio on the server. Connect to the local SQL Server. Expand 'Management' and double-click 'Activity Manager'.<br></p><dl class="image"><dt> 
      <img src="/PublishingImages/rule-outage-5.gif" alt="rule-outage-5.gif" style="width&#58;800px;" /> 
   </dt><dd>Figure&#58; SQL Management Studio 'Active Connections' View</dd></dl><p>Once these have been checked for active users, and users have logged off, maintenance can be carried out.</p><p>
   <strong>Restarts should only be performed during the following time periods</strong></p><ol><li>Between 7am and 7&#58;05am</li><li>Between 1pm and 1&#58;05pm<br></li><li>Between 7pm and 7&#58;05pm 
      <br></li></ol><p>If a scheduled shutdown is required, use the PsShutdown utility from&#160;<a href="https&#58;//www.ssw.com.au/ssw/Redirect/Microsoft/Technet.htm">Microsoft's Sys&#160;Internals</a>&#160;page.</p><p>
   <strong>Always reply 'Done' when you finish the task. </strong>​</p>


