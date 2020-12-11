---
type: rule
archivedreason: 
title: Do you use icons not to surprise users (aka use the correct image for files)?
guid: 283e14e7-fe59-4017-9422-e9efc3eda6da
uri: do-you-use-icons-not-to-surprise-users-aka-use-the-correct-image-for-files
created: 2015-02-16T02:46:02.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 16
  title: Tiago Araujo
related:
- do-you-use-icons-to-enforce-the-text-meaning
- do-you-use-an-icon-so-a-password-prompt-should-never-be-a-surprise

---

When a user clicks on a hyperlink they expect to open an HTML file. If you click on a hyperlink (but it is actually a .doc file) you wait and wait while it takes forever to instantiate an instance of Microsoft Word in the background.

<!--endintro-->

Don't surprise users! Use the following icons:


| File Type | Example |
| --- | --- |
| PDF | 
![](../../assets/IconPdf.png) This is a PDF file<br> |
| JPG | 
![](../../assets/IconJpg.gif) This is an Image file |
| DOC or DOT | 
![](../../assets/IconDoc.png) This is a Word Document file |
| XLS | 
![](../../assets/IconXls.gif) This is an Excel Spreadsheet file |
| PPT | 
![](../../assets/IconPPT.png) This is a PowerPoint file |
| TXT | 
![](../../assets/IconTxt.gif) This is a Text file |
| AVI, MOV, MPG etc. | 
![](../../assets/IconMov.gif) This is a Video file |
| WAV, WMA, MP3 etc. | 
![](../../assets/IconMus.gif) This is a Music file |
| SNP | 
![](../../assets/IconSnp.gif) This is an Access Database snapshot file (discontinued and not recommended) |
| EPS | 
![](../../assets/IconEps.gif) This is an EPS file |
| ICS or VCS | 
![](../../assets/IconVCS.gif) This is a calendar file |
| EXE or ZIP | 
![](../../assets/Download.gif)This is an executable or zip file |
| Mailto: | 
![](../../assets/IconMailTo.gif) This will send an email |
| XML / RSS | 
![](../../assets/IconXML.gif) This will subscribe to RSS |
| ODF | 
![](../../assets/IconOFT.gif) This is an Outlook Item Template |
| Page | 
![](../../assets/ms_lock.gif) This is a link to password protected page |
| YouTube | 
![](youtube-icon_png.jpg)This is a link to a YouTube Video |

<dl class="image">&lt;dt&gt; <img alt="Image good link" src="../../assets/GoogleIcons.gif"> &lt;/dt&gt;<dd>Figure: FYI there are the same images used by Google at <a href="http://desktop.google.com/features.html">GoogleDesktopSideBar.htm</a>  <br> </dd></dl><dl class="badImage">&lt;dt&gt; <img alt="Image bad link" src="../../assets/IconImageBad.gif"> &lt;/dt&gt;<dd>Figure: Bad Example - The user would expect all these hyperlinks to work the same way<br> </dd></dl><dl class="goodImage">&lt;dt&gt; <img alt="Image good link" src="../../assets/IconImageGood.gif"> &lt;/dt&gt;<dd>Figure: Good Example - The pdf icon (before a hyperlink) indicates it is not a web page<br></dd></dl>
### How to add an icon before a link with CSS

Add the icon image to your server. Then use $= to make the match the extension of the >a< tag on your CSS. The padding is to give it some space before the text (where the icon will be).

a[href$='.pdf'] 
{ 
background: transparent url(/images/icon\_pdf.gif) center left no-repeat; 
padding-left: 20 px; 
}



We have the programs [SSW CodeAuditor](http://www.codeauditor.com/) and [SSW LinkAuditor](https://linkauditor.com.au/) to check for this rule.
