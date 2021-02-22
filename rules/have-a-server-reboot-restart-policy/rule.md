---
type: rule
archivedreason: 
title: Do you have a server reboot/restart policy?
guid: eb97dfa8-5bb8-4e19-932a-76d6f2f655fd
uri: have-a-server-reboot-restart-policy
created: 2017-06-30T19:21:55.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Stanley Sidik
  url: https://ssw.com.au/people/stanley-sidik
- title: Steven Andrews
  url: https://ssw.com.au/people/steven-andrews
related: []
redirects:
- do-you-have-a-server-reboot-restart-policy

---


<p>​For unplanned outages see: <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=d3f1bdc6-5ea1-495b-8c0d-98504963b563">https://rules.ssw.com.au/unplanned-outage-process​</a><br></p><p>​​​If your servers are down or have to go down during business hours you should notify the users at least 15 minutes beforehand so you will not get 101 people all asking you if the computer is down.</p><p>For short outages (under 15 minutes) that only affect only a few people (under 5 people), or are outside of business hours, then IM is the best method. If you use 
   <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=3a474efa-ca72-4320-af36-b0e6af355684">Teams or Skype</a> a quick message will do. </p><p>
   <b>Note: </b>If they are not online on Teams or Skype, then they can't complain that they were not warned. 
   <br></p><p>For extended or planned outages, or if you have a larger number of users (50+), 
   <b>email</b> is the suggested method.​​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<h3 class="ssw15-rteElement-H3">Email</h3><p>If you send an email it is a good idea to tell the user a way to monitor the network themselves. Eg. Software solutions like SCOM or WhatsUp Gold. 
   <br></p><p>Include a "<a href=/dones-do-you-send-yourself-emails>To myself</a>". It gives visibility to others who are interested in what needs to be done to fix the problem and makes<br>it easier to remember to send the 'done' email. E.g. "done - CRM is alive again". </p><p>Example: 
   <br></p><dl class="greyBox"><dt style="padding-right:0px;padding-left:0px;margin-top:0px;margin-bottom:0px;margin-left:10px;font-size:1em;">
      <strong>To: </strong>SSWALL</dt><dt style="padding-right:0px;padding-left:0px;margin-top:0px;margin-bottom:0px;margin-left:10px;font-size:1em;">
      <br>
   </dt><dt style="padding-right:0px;padding-left:0px;margin-top:0px;margin-bottom:0px;margin-left:10px;font-size:1em;">Hi All, 
      <br> 
      <br>Here is the summary of the outage plan:<br style="font-size:1em;"><br style="font-size:1em;"> 
      <table style="margin-top:0px;margin-bottom:0px;font-size:1em;"><tbody><tr><td> 
                  <strong>Planned/Unplanned:</strong></td><td>Planned</td></tr><tr><td> 
                  <strong>Change Description:</strong></td><td>Install Windows Updates and Restart Server<br></td></tr><tr><td> 
                  <strong>Risk (see table below):</strong></td><td>LOW RISK (LOW Probability and MEDIUM Impact)</td></tr><tr><td> 
                  <strong>Reason For Change:</strong></td><td>Windows 2016 Windows Updates<br></td></tr><tr><td> 
                  <strong>Uptime over last month:</strong></td><td>91.361%</td></tr><tr><td></td><td>
                  <br>
               </td></tr><tr><td> 
                  <strong>Planned Outage (mins):</strong></td><td>150</td></tr><tr><td> 
                  <strong>Planned Start Time:</strong></td><td>26 October 9:00 PM</td></tr><tr><td> 
                  <strong>Planned Finish Time:</strong></td><td>26 October 11:30 PM<br></td></tr><tr><td></td><td></td></tr><tr><td> 
                  <strong>Affected Services:</strong></td><td>\\Windows Server 2016<br></td></tr><tr><td></td><td>http://sharepoint.ssw.com.au<br style="font-size:1em;">http://intranet.ssw.com.au<br style="font-size:1em;">http://projects.ssw.com.au</td></tr><tr><td></td><td> 
                  <br> 
               </td></tr></tbody></table> 
      <br> 
      <strong>Risk Lookup Table by Probability and Impact:</strong><br style="font-size:1em;"> 
      <table border="0" cellspacing="0" cellpadding="0" style="margin-top:0px;margin-bottom:0px;font-size:1em;"><tbody><tr><td width="554" colspan="6" valign="top" style="padding:0cm 5.4pt;width:415.35pt;border:1pt solid black;background:#eeece1;">
                  <strong style="font-size:1em;">Risk</strong></td></tr><tr style="font-size:1em;"><td width="182" colspan="2" rowspan="2" valign="top" style="padding:0cm 5.4pt;width:136.2pt;border-right:1pt solid black;border-bottom:1pt solid black;border-left:1pt solid black;border-top:none;"><p align="center" style="margin-top:7px;margin-bottom:7px;text-align:center;"> 
                     <strong></strong></p></td><td width="372" colspan="4" style="padding:0cm 5.4pt;width:279.15pt;border-top:none;border-left:none;border-bottom:1pt solid black;border-right:1pt solid black;"><p align="center" style="margin-top:7px;margin-bottom:7px;text-align:center;"> 
                     <strong>Probability</strong></p></td></tr><tr style="font-size:1em;"><td width="91" valign="top" style="padding:0cm 5.4pt;width:68.1pt;border-top:none;border-left:none;border-bottom:1pt solid black;border-right:1pt solid black;"><p style="margin-top:7px;margin-bottom:7px;"> 
                     <strong>Low</strong></p></td><td width="99" valign="top" style="padding:0cm 5.4pt;width:74.2pt;border-top:none;border-left:none;border-bottom:1pt solid black;border-right:1pt solid black;"><p style="margin-top:7px;margin-bottom:7px;"> 
                     <strong>Medium</strong></p></td><td width="91" valign="top" style="padding:0cm 5.4pt;width:68.1pt;border-top:none;border-left:none;border-bottom:1pt solid black;border-right:1pt solid black;"><p style="margin-top:7px;margin-bottom:7px;"> 
                     <strong>High</strong></p></td><td width="92" valign="top" style="padding:0cm 5.4pt;width:68.75pt;border-top:none;border-left:none;border-bottom:1pt solid black;border-right:1pt solid black;"><p style="margin-top:7px;margin-bottom:7px;"> 
                     <strong>Unknown</strong></p></td></tr><tr style="font-size:1em;"><td width="91" rowspan="4" style="padding:0cm 5.4pt;width:68.1pt;border-right:1pt solid black;border-bottom:1pt solid black;border-left:1pt solid black;border-top:none;"><p align="center" style="margin-top:7px;margin-bottom:7px;text-align:center;"> 
                     <strong>Impact</strong></p></td><td width="91" valign="top" style="padding:0cm 5.4pt;width:68.1pt;border-top:none;border-left:none;border-bottom:1pt solid black;border-right:1pt solid black;"><p style="margin-top:7px;margin-bottom:7px;"> 
                     <strong>Low</strong></p></td><td width="91" valign="top" style="padding:0cm 5.4pt;width:68.1pt;border-top:none;border-left:none;border-bottom:1pt solid black;border-right:1pt solid black;"><p style="margin-top:7px;margin-bottom:7px;">Low risk<br></p></td><td width="99" valign="top" style="padding:0cm 5.4pt;width:74.2pt;border-top:none;border-left:none;border-bottom:1pt solid black;border-right:1pt solid black;"><p style="margin-top:7px;margin-bottom:7px;">Low Risk<br></p></td><td width="91" valign="top" style="padding:0cm 5.4pt;width:68.1pt;border-top:none;border-left:none;border-bottom:1pt solid black;border-right:1pt solid black;"><p style="margin-top:7px;margin-bottom:7px;">Low Risk</p></td><td width="91" valign="top" style="padding:0cm 5.4pt;width:68.75pt;border-top:none;border-left:none;border-bottom:1pt solid black;border-right:1pt solid black;"><p style="margin-top:7px;margin-bottom:7px;">Medium Risk<br></p></td></tr><tr style="font-size:1em;"><td width="91" valign="top" style="padding:0cm 5.4pt;width:68.1pt;border-top:none;border-left:none;border-bottom:1pt solid black;border-right:1pt solid black;"><p style="margin-top:7px;margin-bottom:7px;"> 
                     <strong>Medium</strong></p></td><td width="91" valign="top" style="padding:0cm 5.4pt;width:68.1pt;border-top:none;border-left:none;border-bottom:1pt solid black;border-right:1pt solid black;background:yellow;"><p style="margin-top:7px;margin-bottom:7px;">Low Risk 
                     <br></p></td><td width="99" valign="top" style="padding:0cm 5.4pt;width:74.2pt;border-top:none;border-left:none;border-bottom:1pt solid black;border-right:1pt solid black;"><p style="margin-top:7px;margin-bottom:7px;">Medium Risk<br></p></td><td width="91" valign="top" style="padding:0cm 5.4pt;width:68.1pt;border-top:none;border-left:none;border-bottom:1pt solid black;border-right:1pt solid black;"><p style="margin-top:7px;margin-bottom:7px;">Medium Risk</p></td><td width="91" valign="top" style="padding:0cm 5.4pt;width:68.75pt;border-top:none;border-left:none;border-bottom:1pt solid black;border-right:1pt solid black;"><p style="margin-top:7px;margin-bottom:7px;">High Risk</p></td></tr><tr style="font-size:1em;"><td width="91" valign="top" style="padding:0cm 5.4pt;width:68.1pt;border-top:none;border-left:none;border-bottom:1pt solid black;border-right:1pt solid black;"><p style="margin-top:7px;margin-bottom:7px;"> 
                     <strong>High</strong></p></td><td width="91" valign="top" style="padding:0cm 5.4pt;width:68.1pt;border-top:none;border-left:none;border-bottom:1pt solid black;border-right:1pt solid black;">Medium Risk</td><td width="99" valign="top" style="padding:0cm 5.4pt;width:74.2pt;border-top:none;border-left:none;border-bottom:1pt solid black;border-right:1pt solid black;"><p style="margin-top:7px;margin-bottom:7px;">High Risk</p></td><td width="91" valign="top" style="padding:0cm 5.4pt;width:68.1pt;border-top:none;border-left:none;border-bottom:1pt solid black;border-right:1pt solid black;"><p style="margin-top:7px;margin-bottom:7px;">High Risk</p></td><td width="91" valign="top" style="padding:0cm 5.4pt;width:68.75pt;border-top:none;border-left:none;border-bottom:1pt solid black;border-right:1pt solid black;"><p style="margin-top:7px;margin-bottom:7px;">High Risk</p></td></tr><tr style="font-size:1em;height:24.75pt;"><td width="91" valign="top" style="padding:0cm 5.4pt;width:68.1pt;border-top:none;border-left:none;border-bottom:1pt solid black;border-right:1pt solid black;height:24.75pt;"><p style="margin-top:7px;margin-bottom:7px;"> 
                     <strong>Unknown</strong></p></td><td width="91" valign="top" style="padding:0cm 5.4pt;width:68.1pt;border-top:none;border-left:none;border-bottom:1pt solid black;border-right:1pt solid black;height:24.75pt;">Medium Risk 
                  <p style="margin-top:7px;margin-bottom:7px;"> 
                     <span style="font-size:1em;color:#1f497d;"></span></p></td><td width="91" valign="top" style="padding:0cm 5.4pt;width:74.2pt;border-top:none;border-left:none;border-bottom:1pt solid black;border-right:1pt solid black;height:24.75pt;"><p style="margin-top:7px;margin-bottom:7px;">High Risk<br></p></td><td width="91" valign="top" style="padding:0cm 5.4pt;width:68.1pt;border-top:none;border-left:none;border-bottom:1pt solid black;border-right:1pt solid black;height:24.75pt;"><p style="margin-top:7px;margin-bottom:7px;">High Risk<br></p></td><td width="91" valign="top" style="padding:0cm 5.4pt;width:68.75pt;border-top:none;border-left:none;border-bottom:1pt solid black;border-right:1pt solid black;height:24.75pt;"><p style="margin-top:7px;margin-bottom:7px;">High Risk 
                     <br></p></td></tr></tbody></table></dt><dt style="padding-right:0px;padding-left:0px;margin-top:0px;margin-bottom:0px;margin-left:10px;">
      <b>Figure: Clearly showing the potential risks<br><br></b></dt><dt style="padding-right:0px;padding-left:0px;margin-top:0px;margin-bottom:0px;margin-left:10px;"><p class="ssw15-rteElement-P"> 
         <b> Note: </b>The following servers will be affected<br></p> 
      <img src="rule-outage-1.jpg" alt="rule-outage-1.jpg" style="margin:0px;width:100%;height:auto;" />  
      <br> 
      <a href="http://wug.ssw.com.au/"> http://wug.ssw.com.au/</a><br><br><img src="rule-outage-2.jpg" alt="rule-outage-2.jpg" style="width:100%;height:auto;" /><br></dt><dt style="padding-right:0px;padding-left:0px;margin-top:0px;margin-bottom:0px;margin-left:10px;">
      <br> 
   </dt><dt style="padding-right:0px;padding-left:0px;margin-top:0px;margin-bottom:0px;margin-left:10px;">
      <b>To myself,</b></dt><dt style="padding-right:0px;padding-left:0px;margin-top:0px;margin-bottom:0px;margin-left:10px;">
      <b><br></b>To show others who are interested in what needs to be done to fix the problem:<br><b>Detailed Change Plan:	</b><br>1)	Lockout users via IIS<br>2)	Backup server<br>3) Install Windows Updates <br>4) Reboot server<br>5) Follow test plan<br>6) Based on result of test plan, follow backout plan if procedure failed<br>7) Procedure completed</dt><dt style="padding-right:0px;padding-left:0px;margin-top:0px;margin-bottom:0px;margin-left:10px;">
      <br> 
      <b>Test Plan:	</b><br>1)	Check Event log for errors<br>2)	Check each affected service is running<br>3)	Call test users to start “Test Please” on the affect services <br>4)	Get result of user “Test Please” by email by 11:15 PM</dt><dt style="padding-right:0px;padding-left:0px;margin-top:0px;margin-bottom:0px;margin-left:10px;">
      <br> 
      <b>Backout Plan:	</b><br>1)	Restore server from backup<br></dt><dt style="padding-right:0px;padding-left:0px;margin-top:0px;margin-bottom:0px;margin-left:10px;">
      <br> 
      <b>Note:	</b>&lt;This is as per rule <a href=/have-a-server-reboot-restart-policy>What is your server reboot/restart policy?</a> &gt;<br></dt><dt style="padding-right:0px;padding-left:0px;margin-top:0px;margin-bottom:0px;margin-left:10px;">
      <br> 
   </dt></dl><p>Immediately before the scheduled downtime, check for logged in users, file access, and database connections.</p><h3 class="ssw15-rteElement-H3">Users</h3><p>Open 'Windows Task Manager' (Run &gt; taskmgr) and select the 'Users' tab. Check with users if they have active connections, then have them log off.<br></p><dl class="image"><dt>
      <img src="rule-outage-3.png" alt="rule-outage-3.png" style="width:100%;height:auto;" />
   </dt><dd>Figure: Connected users can be viewed in Task Manager</dd></dl><h3 class="ssw15-rteElement-H3">Files</h3><p>Open 'Computer Management' (Run &gt; compmgmt.msc), then 'System Tools &gt; Shared Folders'. Check 'Session' and 'Open Files' for user connections.</p><dl class="image"><dt>
      <img src="rule-outage-4.png" alt="rule-outage-4.png" style="width:100%;height:auto;" />
   </dt><dd>Figure: Computer Management 'Open Files' View</dd></dl><h3 class="ssw15-rteElement-H3">Database</h3><p>Open SQL Server Management Studio on the server. Connect to the local SQL Server. Expand 'Management' and double-click 'Activity Manager'.<br></p><dl class="image"><dt>
      <img src="rule-outage-5.gif" alt="rule-outage-5.gif" style="width:100%;height:auto;" />
   </dt><dd>Figure: SQL Management Studio 'Active Connections' View</dd></dl><p>Once these have been checked for active users, and users have logged off, maintenance can be carried out.</p><p> 
   <strong>Restarts should only be performed during the following time periods</strong></p><ol><li>Between 7am and 7:05am</li><li>Between 1pm and 1:05pm<br></li><li>Between 7pm and 7:05pm 
      <br></li></ol><p>If a scheduled shutdown is required, use the PsShutdown utility from <a href="https://www.ssw.com.au/ssw/Redirect/Microsoft/Technet.htm">Microsoft's Sys Internals</a> page.</p><p> 
   <strong>Always reply 'Done' when you finish the task. </strong>​</p>


