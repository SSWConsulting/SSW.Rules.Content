---
type: rule
title: Logon - Do you have a company-wide Word template?
uri: logon---do-you-have-a-company-wide-word-template
created: 2017-07-11T17:42:29.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 47
  title: Stanley Sidik

---



<span class='intro'> A company-wide template will be implemented, so users have automatic footers to save time and give better branding.​​<br>
<dl class="badImage"><dt><img src="/PublishingImages/word-template-bad.jpg" alt="word-template-bad.jpg" /></dt><dd>Figure&#58; Bad Example - creating an email/document does not have the company templates</dd></dl><dl class="goodImage"><dt> <img src="/PublishingImages/word-template-good.jpg" alt="word-template-good.jpg" /></dt><dd>Figure&#58; Good Example - creating an email/document with the company templates​<br></dd></dl> </span>

<p>How to have a company-wide Word template&#58;<br></p><ul><li>Modify your Normal.dotm file to have the headings and format that you want for Word document</li><li>Create standard employee email footer files e.g. JamesZhou.htm or JamesZho u.txt</li><li>Put the files on a network location - this is the place that will have the master copies&#160;<br>e.g. \\ssw\ant\standardsinternal\template\</li><li>Have a logon script which is setup through Group policy that will copy the file to the users' computer when they logon.<br></li></ul><div><p class="ssw15-rteElement-CodeArea">ECHO Copy Office Templates To Workstation &gt;&gt; %LogonLogFile%<br>call %ScriptFolder%\SSWLogonScript\BatchScript\SafeCopyNewerFile.bat &quot;\\fileserver\DataSSW\DataSSWEmployees\Templates\Normal.dot&quot; &quot;%APPDATA%\Microsoft\Templates\Normal.dot&quot; %LogonLogFile%<br>call %ScriptFolder%\SSWLogonScript\BatchScript\SafeCopyNewerFile.bat &quot;\\fileserver\DataSSW\DataSSWEmployees\Templates\Normal.dotm&quot; &quot;%APPDATA%\Microsoft\Templates\Normal.dotm&quot; %LogonLogFile%<br>call %ScriptFolder%\SSWLogonScript\BatchScript\SafeCopyNewerFile.bat &quot;\\fileserver\DataSSW\DataSSWEmployees\Templates\ProposalNormalTemplate.dotx&quot; &quot;%APPDATA%\Microsoft\Templates\ProposalNormalTemplate.dotx&quot; %LogonLogFile%<br>call %ScriptFolder%\SSWLogonScript\BatchScript\SafeCopyNewerFile.bat &quot;\\fileserver\DataSSW\DataSSWEmployees\Templates\NormalEmail.dot&quot; &quot;%APPDATA%\Microsoft\Templates\NormalEmail.dot&quot; %LogonLogFile%<br>call %ScriptFolder%\SSWLogonScript\BatchScript\SafeCopyNewerFile.bat &quot;\\fileserver\DataSSW\DataSSWEmployees\Templates\Microsoft_Normal.dotx&quot; &quot;%APPDATA%\Microsoft\Templates\Microsoft_Normal.dotx&quot; %LogonLogFile%<br>call %ScriptFolder%\SSWLogonScript\BatchScript\SafeCopyNewerFile.bat &quot;\\fileserver\DataSSW\DataSSWEmployees\Templates\Blank.potx&quot; &quot;%APPDATA%\Microsoft\Templates\Blank.potx&quot; %LogonLogFile%<br>xcopy /Y &quot;\\fileserver\DataSSW\DataSSWEmployees\Templates\NormalEmail.dotm&quot; &quot;%APPDATA%\Microsoft\Templates\&quot; &gt;&gt; %LogonLogFile%<br>xcopy /Y &quot;\\fileserver\DataSSW\DataSSWEmployees\Templates\NormalEmail.dotx&quot; &quot;%APPDATA%\Microsoft\QuickStyles\&quot; &gt;&gt; %LogonLogFile%<br>ECHO Templates Copied <br></p><dd class="ssw15-rteElement-FigureNormal">Figure&#58; This is a snippet of our login script<br>​ <br></dd><p><b>Note&#58;</b> We don't want people using .RTF emails so we include this message in SSW.rtf. Be aware that we don't want to use RTF because of&#160;<a href="https&#58;//www.ssw.com.au/ssw/Standards/BetterSoftwareSuggestions/Outlook.aspx#RemoveRTF">Remove RTF as an option or explain when it is a good choice</a>.<br></p><p>For more information on why we need to modify the Normal.dotm, you can access the website <a href="https&#58;//www.ssw.com.au/ssw/Redirect/Microsoft/MSOfficeNormalTemplate.htm">http&#58;//office.microsoft.com/en-us/word/HA100307561033.aspx</a>.<br></p><h3 class="ssw15-rteElement-H3">Related Rule <br></h3><ul><li><a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=73dea04c-b017-4c65-816e-aef8c84497be">Do you know what makes a great email signature? </a> <br><br></li></ul></div>


