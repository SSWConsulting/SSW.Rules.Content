---
type: rule
archivedreason: 
title: Messages - Do you know how to make message boxes user friendly? (1/3 Titles)
guid: 458076de-3da9-46a9-9b80-a811c76da68a
uri: messages---do-you-know-how-to-make-message-boxes-user-friendly-13-titles
created: 2012-11-27T04:33:49.0000000Z
authors: []
related: []

---


<p>Message boxes should have consistent and informative titles and descriptions, and icons should be used appropriately.</p>
<br><excerpt class='endintro'></excerpt><br>
​<h4>Title</h4>
<div>The title should contain the application name, so the user knows what application generated the warning/error. This is especially important when developing add-ins (e.g. Outlook add-ins or Smart Tags) as it can be difficult to know what caused the message box to pop up. <strong>Application.ProductName</strong> and <strong>Application.ProductVersion</strong> should be used to retrieve the data from AssemblyInfo. There is no need for the title to contain a brief description of the error because that information is readily available in the message box itself.</div>
<dl class="badImage"><dt><img alt="Bad Title Example" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/BadMsgTitle.jpg" /></dt>
<dd>Figure&#58; Bad Example - Title contains brief description of error, which is already contained in the message box</dd></dl>
<dl class="goodImage"><dt><img alt="Good Title Example" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/GoodMsgTitle.jpg" /></dt>
<dd>Figure&#58; Good Example - Title contains Product Name (&quot;SSW eXtreme Emails!&quot;) and Product Version (&quot;12.56&quot;)</dd></dl>
<div>We have a program called <a href="http&#58;//www.ssw.com.au/ssw/CodeAuditor/Rules.aspx#TitleCS">SSW Code Auditor</a> to check for this rule.</div>
<div><strong>Note</strong>&#58; The Version Number in the title should only contain the Major and the Minor version numbers (e.g. 11.28) and not the complete Major.Minor.Revision.Build Numbers (e.g. 11.28.92.1198)</div>



