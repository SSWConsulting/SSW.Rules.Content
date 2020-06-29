---
type: rule
title: Do you use icons not to surprise users (aka use the correct image for files)?
uri: do-you-use-icons-not-to-surprise-users-aka-use-the-correct-image-for-files
created: 2015-02-16T02:46:02.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 16
  title: Tiago Araujo

---



<span class='intro'> <p>When a user clicks on a hyperlink they expect to open an HTML​ file. If you click on a hyperlink (but it is actually a .doc file) you wait and wait while it takes forever to instantiate an instance of Microsoft Word in the background. <br></p> </span>

<p>Don't surprise users! Use the following icons&#58;</p> 
<table cellspacing="0" cellpadding="3" class="normal" style="width&#58;100%;"><tbody><tr><th scope="col">File Type</th><th scope="col">Example</th></tr><tr><td>PDF</td><td> 
            <img alt="Icon PDF" src="http&#58;//www.ssw.com.au/ssw/Images/IconPdf.png" style="margin&#58;5px;" /> This is a PDF file<br></td></tr><tr><td>JPG</td><td> 
            <img alt="Icon JPG" src="http&#58;//www.ssw.com.au/ssw/Images/IconJpg.gif" style="margin&#58;5px;" /> This is an Image file</td></tr><tr><td>DOC or DOT</td><td> 
            <img alt="Icon DOC" src="http&#58;//www.ssw.com.au/ssw/Images/IconDoc.png" style="margin&#58;5px;" /> This is a Word Document file</td></tr><tr><td>XLS</td><td> 
            <img alt="Icon XLS" src="http&#58;//www.ssw.com.au/ssw/Images/IconXls.gif" style="margin&#58;5px;" /> This is an Excel Spreadsheet file</td></tr><tr><td>PPT</td><td> 
            <img alt="Icon PPT" src="http&#58;//www.ssw.com.au/ssw/Images/IconPPT.png" style="margin&#58;5px;" /> This is a PowerPoint file</td></tr><tr><td>TXT</td><td> 
            <img alt="Icon TXT" src="http&#58;//www.ssw.com.au/ssw/Images/IconTxt.gif" style="margin&#58;5px;" /> This is a Text file</td></tr><tr><td>AVI, MOV, MPG etc.</td><td> 
            <img alt="Icon MOV" src="http&#58;//www.ssw.com.au/ssw/Images/IconMov.gif" style="margin&#58;5px;" /> This is a Video file</td></tr><tr><td>WAV, WMA,&#160;MP3 etc.</td><td> 
            <img alt="Icon MP3" src="http&#58;//www.ssw.com.au/ssw/Images/IconMus.gif" data-pin-nopin="true" style="margin&#58;5px;" /> This is a Music file</td></tr><tr><td>SNP</td><td> 
            <img alt="Icon SNP" src="http&#58;//www.ssw.com.au/ssw/Images/IconSnp.gif" style="margin&#58;5px;" /> This is an Access Database snapshot file (discontinued and not recommended)</td></tr><tr><td>EPS</td><td> 
            <img alt="Icon EPS" src="http&#58;//www.ssw.com.au/ssw/Images/IconEps.gif" style="margin&#58;5px;" /> This is an EPS file</td></tr><tr><td>ICS or VCS</td><td> 
            <img alt="Icon VCS" src="http&#58;//www.ssw.com.au/ssw/Images/IconVCS.gif" style="margin&#58;5px;" /> This is a calendar file</td></tr><tr><td>EXE or ZIP</td><td> 
            <img alt="Download" src="http&#58;//www.ssw.com.au/ssw/Images/Download.gif" style="margin&#58;5px;" />This is an executable or zip file</td></tr><tr><td>Mailto&#58;</td><td> 
            <img alt="Icon MailTo" src="http&#58;//www.ssw.com.au/ssw/Images/IconMailTo.gif" style="margin&#58;5px;" /> This will send an email</td></tr><tr><td>XML / RSS</td><td> 
            <img alt="Icon XML" src="http&#58;//www.ssw.com.au/ssw/Images/IconXML.gif" style="margin&#58;5px;" /> This will subscribe to RSS</td></tr><tr><td>ODF</td><td> 
            <img alt="Icon ODF" src="http&#58;//www.ssw.com.au/ssw/Images/IconOFT.gif" /> This is an Outlook Item Template</td></tr><tr><td>Page</td><td> 
            <img src="http&#58;//www.ssw.com.au/SSW/Standards/Rules/Images/ms_lock.gif" alt="" /> This is a link to password protected page</td></tr><tr><td rowspan="1">YouTube</td><td rowspan="1">​<img src="_t/youtube-icon_png.jpg" alt="" style="margin&#58;5px;" />This is a link to a YouTube Video</td></tr></tbody></table><dl class="image"><dt> <img alt="Image good link" src="http&#58;//www.ssw.com.au/SSW/Standards/Rules/Images/GoogleIcons.gif" /> </dt><dd>Figure&#58; FYI there are the same images used by Google at <a href="http&#58;//desktop.google.com/features.html">GoogleDesktopSideBar.htm</a> &#160;<br> </dd></dl><dl class="badImage"><dt> <img alt="Image bad link" src="http&#58;//www.ssw.com.au/SSW/Standards/Rules/Images/IconImageBad.gif" /> </dt><dd>Figure&#58; Bad Example - The user would expect all these hyperlinks to work the same way<br> </dd></dl><dl class="goodImage"><dt> <img alt="Image good link" src="http&#58;//www.ssw.com.au/SSW/Standards/Rules/Images/IconImageGood.gif" /> </dt><dd>Figure&#58; Good Example - The pdf icon (before a hyperlink) indicates it is not a web page<br></dd></dl><h3>How to add an icon before a link with CSS</h3><p>Add the icon image to your server. Then use $= to make the match the extension of the &gt;a&lt; tag on your CSS. The padding is to give it some space before the text (where the icon will be).</p><p class="ssw15-rteElement-CodeArea">a[href$='.pdf'] <br>&#123; <br>background&#58; transparent url(/images/icon_pdf.gif) center left no-repeat; <br>padding-left&#58; 20 px; <br>&#125;</p><div> 
   <br> 
   <p class="ssw15-rteElement-YellowBorderBox">We have the&#160;programs&#160;<a href="http&#58;//www.codeauditor.com/" target="_blank">SSW CodeAuditor</a>&#160;and <a href="https&#58;//linkauditor.com.au/" target="_blank">SSW LinkAuditor</a>&#160;to check for this rule.<br></p></div>


