---
type: rule
archivedreason: 
title: Logon - Do you have a company-wide Word template?
guid: a58e2456-e070-4ddb-9ed8-996eab71ef90
uri: have-a-companywide-word-template
created: 2017-07-11T17:42:29.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Stanley Sidik
  url: https://ssw.com.au/people/stanley-sidik
- title: Kaique Biancatti
  url: https://ssw.com.au/people/kaique-biancatti
related:
- do-you-know-if-you-are-using-the-template
- great-email-signatures
redirects:
- logon-do-you-have-a-company-wide-word-template

---


A company-wide template will be implemented, so users have automatic footers to save time and give better branding.​​<br>
<dl class="badImage"><dt><img src="word-template-bad.jpg" alt="word-template-bad.jpg" /></dt><dd>Figure: Bad Example - creating an email/document does not have the company templates</dd></dl><dl class="goodImage"><dt> <img src="word-template-good.jpg" alt="word-template-good.jpg" /></dt><dd>Figure: Good Example - creating an email/document with the company templates​<br></dd></dl>
<br><excerpt class='endintro'></excerpt><br>
<p>How to have a company-wide Word template:<br></p><ul><li>Modify your Normal.dotm file to have the headings and format that you want for Word document</li><li>Create standard employee email footer files e.g. JamesZhou.htm or JamesZhou.txt</li><li>Put the files on a network location - this is the place that will have the master copies <br></li><li>​Have a logon script which is set up through Group policy that will copy the file to the users' computer when they logon.<br>e.g. a PowerShell login script like <a href="https://github.com/SSWConsulting/SSWSysAdmins.LoginScript">https://github.com/SSWConsulting/SSWSysAdmins.LoginScript</a><br></li></ul><div><p class="ssw15-rteElement-CodeArea">ECHO Copy Office Templates To Workstation &gt;&gt; %LogonLogFile%<br>call %ScriptFolder%\SSWLogonScript\BatchScript\SafeCopyNewerFile.bat "\\fileserver\DataSSW\DataSSWEmployees\Templates\Normal.dot" "%APPDATA%\Microsoft\Templates\Normal.dot" %LogonLogFile%<br>call %ScriptFolder%\SSWLogonScript\BatchScript\SafeCopyNewerFile.bat "\\fileserver\DataSSW\DataSSWEmployees\Templates\Normal.dotm" "%APPDATA%\Microsoft\Templates\Normal.dotm" %LogonLogFile%<br>call %ScriptFolder%\SSWLogonScript\BatchScript\SafeCopyNewerFile.bat "\\fileserver\DataSSW\DataSSWEmployees\Templates\ProposalNormalTemplate.dotx" "%APPDATA%\Microsoft\Templates\ProposalNormalTemplate.dotx" %LogonLogFile%<br>call %ScriptFolder%\SSWLogonScript\BatchScript\SafeCopyNewerFile.bat "\\fileserver\DataSSW\DataSSWEmployees\Templates\NormalEmail.dot" "%APPDATA%\Microsoft\Templates\NormalEmail.dot" %LogonLogFile%<br>call %ScriptFolder%\SSWLogonScript\BatchScript\SafeCopyNewerFile.bat "\\fileserver\DataSSW\DataSSWEmployees\Templates\Microsoft_Normal.dotx" "%APPDATA%\Microsoft\Templates\Microsoft_Normal.dotx" %LogonLogFile%<br>call %ScriptFolder%\SSWLogonScript\BatchScript\SafeCopyNewerFile.bat "\\fileserver\DataSSW\DataSSWEmployees\Templates\Blank.potx" "%APPDATA%\Microsoft\Templates\Blank.potx" %LogonLogFile%<br>xcopy /Y "\\fileserver\DataSSW\DataSSWEmployees\Templates\NormalEmail.dotm" "%APPDATA%\Microsoft\Templates\" &gt;&gt; %LogonLogFile%<br>xcopy /Y "\\fileserver\DataSSW\DataSSWEmployees\Templates\NormalEmail.dotx" "%APPDATA%\Microsoft\QuickStyles\" &gt;&gt; %LogonLogFile%<br>ECHO Templates Copied <br></p><dd class="ssw15-rteElement-FigureBad">Figure: Bad Example - This is a snippet of an old login script</dd><p class="ssw15-rteElement-YellowBorderBox">​ You can automatically have your SSW Word doc template on sign-in via a script. See https://github.com/SSWConsulting/SSWSysAdmins.LoginScript</p></div><dd class="ssw15-rteElement-FigureGood">Good Example - New Login script on Github</dd><dt><br></dt><div><p><b>Note #1:</b> We don't want people using .RTF emails so we include this message in SSW.rtf. Be aware that we don't want to use RTF because of <a href="https://www.ssw.com.au/ssw/Standards/BetterSoftwareSuggestions/Outlook.aspx#RemoveRTF">Remove RTF as an option or explain when it is a good choice</a>.<br></p><p><b>Note #2: </b>If you use a Mac computer, a login script will not work. In order to use a Word template, you must open the template on Word locally, hit "Save as Template", and then upload that document to Teams.​<br></p></div>


