---
type: rule
archivedreason: 
title: Do you use icons not to surprise users (aka use the correct image for files)?
guid: 283e14e7-fe59-4017-9422-e9efc3eda6da
uri: do-you-use-icons-not-to-surprise-users-aka-use-the-correct-image-for-files
created: 2015-02-16T02:46:02.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Tiago Araujo
  url: https://ssw.com.au/people/tiago-araujo
related:
- do-you-use-icons-in-web-pages-to-enforce-the-text-meaning
- do-you-use-an-icon-so-a-password-prompt-should-never-be-a-surprise
redirects:
- do-you-use-icons-not-to-surprise-users-(aka-use-the-correct-image-for-files)

---


<p>When a user clicks on a hyperlink they expect to open an HTML​ file. If you click on a hyperlink (but it is actually a .doc file) you wait and wait while it takes forever to instantiate an instance of Microsoft Word in the background. <br></p>
<br><excerpt class='endintro'></excerpt><br>
<p>Don't surprise users! Use the following icons:</p> 
<table cellspacing="0" cellpadding="3" class="normal" style="width:100%;"><tbody><tr><th scope="col">File Type</th><th scope="col">Example</th></tr><tr><td>PDF</td><td> 
            <img alt="Icon PDF" src="../../assets/IconPdf.png" style="margin:5px;" /> This is a PDF file<br></td></tr><tr><td>JPG</td><td> 
            <img alt="Icon JPG" src="../../assets/IconJpg.gif" style="margin:5px;" /> This is an Image file</td></tr><tr><td>DOC or DOT</td><td> 
            <img alt="Icon DOC" src="../../assets/IconDoc.png" style="margin:5px;" /> This is a Word Document file</td></tr><tr><td>XLS</td><td> 
            <img alt="Icon XLS" src="../../assets/IconXls.gif" style="margin:5px;" /> This is an Excel Spreadsheet file</td></tr><tr><td>PPT</td><td> 
            <img alt="Icon PPT" src="../../assets/IconPPT.png" style="margin:5px;" /> This is a PowerPoint file</td></tr><tr><td>TXT</td><td> 
            <img alt="Icon TXT" src="../../assets/IconTxt.gif" style="margin:5px;" /> This is a Text file</td></tr><tr><td>AVI, MOV, MPG etc.</td><td> 
            <img alt="Icon MOV" src="../../assets/IconMov.gif" style="margin:5px;" /> This is a Video file</td></tr><tr><td>WAV, WMA, MP3 etc.</td><td> 
            <img alt="Icon MP3" src="../../assets/IconMus.gif" data-pin-nopin="true" style="margin:5px;" /> This is a Music file</td></tr><tr><td>SNP</td><td> 
            <img alt="Icon SNP" src="../../assets/IconSnp.gif" style="margin:5px;" /> This is an Access Database snapshot file (discontinued and not recommended)</td></tr><tr><td>EPS</td><td> 
            <img alt="Icon EPS" src="../../assets/IconEps.gif" style="margin:5px;" /> This is an EPS file</td></tr><tr><td>ICS or VCS</td><td> 
            <img alt="Icon VCS" src="../../assets/IconVCS.gif" style="margin:5px;" /> This is a calendar file</td></tr><tr><td>EXE or ZIP</td><td> 
            <img alt="Download" src="../../assets/Download.gif" style="margin:5px;" />This is an executable or zip file</td></tr><tr><td>Mailto:</td><td> 
            <img alt="Icon MailTo" src="../../assets/IconMailTo.gif" style="margin:5px;" /> This will send an email</td></tr><tr><td>XML / RSS</td><td> 
            <img alt="Icon XML" src="../../assets/IconXML.gif" style="margin:5px;" /> This will subscribe to RSS</td></tr><tr><td>ODF</td><td> 
            <img alt="Icon ODF" src="../../assets/IconOFT.gif" /> This is an Outlook Item Template</td></tr><tr><td>Page</td><td> 
            <img src="../../assets/ms_lock.gif" alt="" /> This is a link to password protected page</td></tr><tr><td rowspan="1">YouTube</td><td rowspan="1">​<img src="youtube-icon_png.jpg" alt="" style="margin:5px;" />This is a link to a YouTube Video</td></tr></tbody></table><dl class="image"><dt> <img alt="Image good link" src="../../assets/GoogleIcons.gif" /> </dt><dd>Figure: FYI there are the same images used by Google at <a href="http://desktop.google.com/features.html">GoogleDesktopSideBar.htm</a>  <br> </dd></dl><dl class="badImage"><dt> <img alt="Image bad link" src="../../assets/IconImageBad.gif" /> </dt><dd>Figure: Bad Example - The user would expect all these hyperlinks to work the same way<br> </dd></dl><dl class="goodImage"><dt> <img alt="Image good link" src="../../assets/IconImageGood.gif" /> </dt><dd>Figure: Good Example - The pdf icon (before a hyperlink) indicates it is not a web page<br></dd></dl><h3>How to add an icon before a link with CSS</h3><p>Add the icon image to your server. Then use $= to make the match the extension of the &gt;a&lt; tag on your CSS. The padding is to give it some space before the text (where the icon will be).</p><p class="ssw15-rteElement-CodeArea">a[href$='.pdf'] <br>{ <br>background: transparent url(/images/icon_pdf.gif) center left no-repeat; <br>padding-left: 20 px; <br>}</p><div> 
   <br> 
   <p class="ssw15-rteElement-YellowBorderBox">We have the programs <a href="http://www.codeauditor.com/" target="_blank">SSW CodeAuditor</a> and <a href="https://linkauditor.com.au/" target="_blank">SSW LinkAuditor</a> to check for this rule.<br></p></div>


