---
type: rule
title: Quality - Do you know how to request a "test please"?
uri: quality---do-you-know-how-to-request-a-test-please
created: 2015-08-26T19:03:34.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 16
  title: Tiago Araujo

---



<span class='intro'> These are the steps you should take when request a &quot;test please&quot; &#58;<br>
 </span>

<ol><li>Find two free testers to send the email below</li><li>Stop working on the project until you receive either a &quot;pass&quot; or &quot;fail&quot; email</li><li>Create your &quot;test please&quot; following this template&#58;<div class="greyBox"><p> 
            <strong>Subject&#58; Test Please - Product Name v1.11</strong>​</p><p>Dear [XXX],</p><p>I am looking for bugs or approval to release this version.</p><p>I have done what I could for my code's health. E.g.</p><ul><li>Run SSW Code Auditor - it has [XXX] errors [If not 0, give reason]</li><li>Run SSW Link Auditor - it has [XXX] errors [If not 0, give reason]</li><li>Kept my eye on Application Insights</li></ul><p>Specific issues to look out for are&#58;</p><ul><li>[XXX]</li><li>[YYY]</li></ul><p>The latest version of [XXX] is at [WWW.URL.COM]</p><p>Keep in mind that a &quot;test please&quot; is an urgent task and that it should start within the hour.</p><p> 
            <strong>Note&#58;</strong></p><ul><li>Send suggestions/bugs one email at a time (with a new email subject) because it makes it easier to fix and reply &quot;done&quot;<ul><li>Please CC the project manager [xxx@yyy.com] and the client [xxx@yyy.com]</li></ul></li><li>Know the definition of a bug. Read <a href="http&#58;//www.ssw.com.au/ssw/Standards/Support/BugReportOrEnhancement.aspx">www.ssw.com.au/ssw/Standards/Support/BugReportOrEnhancement.aspx</a></li><li>Understand the importance of testing. Read the rule on <a href="/Management/RulesToSuccessfulProjects/Pages/InternalTestPlease.aspx" target="_blank">Do you conduct a &quot;test please&quot; internally and then with the client?</a></li><li>Use good subjects on your emails. Read <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=f4073e2a-b089-4a7f-8ee6-a7b1a48509e8" target="_blank">Do you realize the importance of a good email Subject?</a></li><li>Do not reply to this message until you can say &quot;Test Please Succeeded (as no Critical bugs). You are ready to deploy.&quot; or &quot;Test Please Failed (as per Critical bugs reported)&quot;</li></ul><p>Thanks, [XXX]</p></div></li><li> 
      <strong>What if you're doing a Windows Forms test?</strong>
      <p>Then you should also include this to the email&#58;</p><ul><li>The latest version of [XXX] has been uploaded to \\frog\SSW\Download\[Application_verX-XX_beta.exe</li><li>Test on a fresh VPC image of Windows</li><li>Install into a non-default directory</li><li>Check the installation folder for misplaced items</li><li>Test Unit Tests via &quot;Help - Run Unit Tests&quot;</li><li>(If Applicable)Test the &quot;Create&quot; and &quot;Reconcile&quot; buttons. Read <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=d384ebb3-3679-41cc-b05a-d439fa76cd35">Rules to Better .NET Projects</a></li><li>Test open and closing forms and saving values</li><li>Test most buttons and menus and links</li><li>Disable your network connection and test again (check for unhandled errors)</li><li>If your test fails, please rename the executable to [Application_verX-XX_failed.exe]</li></ul></li><li> 
      <strong>Note to </strong> <strong> developer&#58;&#160;</strong>If current version is better than the last version you can release (even with a test fail) as long&#58;<ul><li>The bugs reported in the test fail existed in the old version</li><li>Two people have tested it</li><li>The changes in this version are fairly important to get out</li><li>You get to work on the failures ASAP</li></ul></li><li>For clients on fixed price contracts, this email marks the start of the 30 day warranty period.</li><li>Use TFS to email the work items to the project manager and client&#58; <dl class="image"><dt> <img src="/PublishingImages/tfs-backlog-email.jpg" alt="tfs-backlog-email.jpg" style="width&#58;550px;" /> </dt><dd>Figure&#58; TFS makes it easy to export work items </dd></dl><dl class="image"><dt> <img src="/PublishingImages/tfs-backlog-email-2.jpg" alt="tfs-backlog-email-2.jpg" style="width&#58;550px;" />​ </dt><dd>Figure&#58; How the email is generated</dd></dl></li></ol>​


