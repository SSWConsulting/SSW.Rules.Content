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



<span class='intro'> A companywide template will be implemented, so users have automatic footers to save time and give better branding.​​<br>
<dl class="badImage"><dt><img src="/PublishingImages/word-template-bad.jpg" alt="word-template-bad.jpg" /></dt><dd>Figure&#58; Bad Example - creating an email/document does not have the company templates</dd></dl><dl class="goodImage"><dt> <img src="/PublishingImages/word-template-good.jpg" alt="word-template-good.jpg" /></dt><dd>Figure&#58; Good Example - creating an email/document with the company templates​<br></dd></dl> </span>

<p>How to have a companywide Word template&#58;<br></p><ul><li>Modify your Normal.dotm file to have the headings and format that you want for Word document</li><li>Create standard employee email footer files e.g. JamesZhou.htm or JamesZhou.txt</li><li>Put the files on a network location - this is the place that will have the master copies&#160;<br>e.g. \\ssw\ant\standardsinternal\template\</li><li>Have a logon script which is setup through Group policy that will copy the file to the users' computer when they logon.<br></li></ul><div><p class="ssw15-rteElement-CodeArea">@ECHO OFF <br>ECHO This is in the default group policy - user section REM Copy template from network share <br>XCOPY /Y &quot;\\ant\ssw\StandardsInternal\Templates&quot; &quot;%APPDATA%\Microsoft\Templates\&quot; <br>ECHO. Templates Copied REM Copy user outlook template from network share <br>COPY &quot;\\ant\ssw\StandardsInternal\Templates\Outlook\SSW_%UserName%.htm&quot; &quot;%APPDATA%\Microsoft\Signatures\SSW.htm&quot; <br>COPY &quot;\\ant\ssw\StandardsInternal\Templates\Outlook\SSW_%UserName%.rtf&quot; &quot;%APPDATA%\Microsoft\Signatures\SSW.rtf&quot; <br>COPY &quot;\\ant\ssw\StandardsInternal\Templates\Outlook\SSW_%UserName%.txt&quot; &quot;%APPDATA%\Microsoft\Signatures\SSW.txt&quot; <br>ECHO. Outlook Template Updated ECHO. Write to log file <br>ECHO EXIT|%COMSPEC%/kPROMPT SSW Startup (\\cow\sysvol\sydney.ssw.com.au\Policies\&#123;31B2F340-016D-11D2-945F-00C04FB984F9&#125;\User\Scripts\Logon\sswlogon.cmd) Script Ran at $d $t &gt;&gt; C&#58;\SSWLogin.log &#58;EXIT</p><dd class="ssw15-rteElement-FigureNormal">Figure&#58; This is how our script looks like in microsoft word<br></dd><p><b><br></b></p><p><b>Note&#58;</b> We don't want people using .RTF emails so we include this message in SSW.rtf. Be aware that we don't want to use RTF because of&#160;<a href="https&#58;//www.ssw.com.au/ssw/Standards/BetterSoftwareSuggestions/Outlook.aspx#RemoveRTF">Remove RTF as an option or explain when it is a good choice</a>.<br></p><p>For more information on why we need to modify the Normal.dotm, you can access the website <a href="https&#58;//www.ssw.com.au/ssw/Redirect/Microsoft/MSOfficeNormalTemplate.htm">http&#58;//office.microsoft.com/en-us/word/HA100307561033.aspx</a>.<br></p><h3 class="ssw15-rteElement-H3">Related Rule <br></h3><ul><li><a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=73dea04c-b017-4c65-816e-aef8c84497be">Do you know what makes a great email signature? </a> <br></li></ul></div>


