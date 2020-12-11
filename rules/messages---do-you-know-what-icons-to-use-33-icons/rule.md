---
type: rule
archivedreason: 
title: Messages - Do you know what icons to use? (3/3 Icons)
guid: 6d4001a7-aaee-40fe-a34b-ff049a1b6d94
uri: messages---do-you-know-what-icons-to-use-33-icons
created: 2012-11-27T04:37:34.0000000Z
authors: []
related: []

---


<h4>Icon</h4>
<div>Including an icon is important because not only does it give the user a visual indication of the type of message, but without it only the Default beep sound is used. The icon should reflect the type of information being presented:</div>
<br><excerpt class='endintro'></excerpt><br>
​<table class="clsSSWTable" border="0" cellspacing="0" cellpadding="3"><tbody><tr><th>Icon</th>
<th>Name</th>
<th>When to use</th></tr>
<tr><td><img alt="info" src="../../assets/Info.gif" width="32" height="32" /></td>
<td><strong>MessageBoxIcon.Information</strong></td>
<td>Non-error information, e.g. Database connection test completed successfully</td></tr>
<tr><td><img alt="Warning" src="../../assets/Warning.gif" width="31" height="31" /></td>
<td><strong>MessageBoxIcon.Warning</strong></td>
<td>A non-critical error, e.g. The input was invalid</td></tr>
<tr><td><img alt="error" src="../../assets/Error.gif" width="32" height="32" /></td>
<td><strong>MessageBoxIcon.Error</strong></td>
<td>Critical error in the program, e.g. Program file was not found</td></tr>
<tr valign="top"><td><img src="../../assets/Question.gif" width="32" height="32" alt="" /></td>
<td><strong>MessageBoxIcon.Question</strong></td>
<td><strong>NEVER</strong> use this.  <br>According to Microsoft, the Question mark is being phased out, as any of the other three: Error, Warning or Information can easily be reworded into a Question, and Question does not show the user the severity of the issue that has just occurred.<br>E.g.  If you want to ask the user whether they want to save a file before closing, you should use the Warning Icon. </td></tr></tbody></table>
<br><div>We have a program called <a href="http://www.ssw.com.au/ssw/CodeAuditor/Rules.aspx#TitleVB">SSW Code </a><span>Auditor</span>to check for this rule.</div>



