---
type: rule
archivedreason: 
title: Do you remove spaces from your folders and filename?
guid: 77003d23-7544-4bbe-92b9-48eae917d4a0
uri: do-you-remove-spaces-from-your-folders-and-filename
created: 2018-04-23T21:58:29.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

It is not a good idea to have spaces in a folder or file name as they don't translate to URLs very well and can even cause technical problems.

Instead of using spaces, you should have the first letter of each word in UPPERCASE and the rest of the word in lowercase. Alternatively, you can choose to use underscores. This alternative method to spacing makes file names more readable when published on the web.

<!--endintro-->

Note that this rule should apply to any file or folder that is on the web. This includes TFS Team Project names and SharePoint Pages.

extremeemailsversion1.2.doc
Extreme Emails version 1.2.doc


::: bad
Figure - Bad Examples: filenames have spaces or dots 

:::


Extreme\_Emails\_v1\_2.doc
ExtremeEmails\_v1\_2.doc


::: good
Figure – Good Examples: file names do not have spaces
:::


&lt;a href="http://sharepoint.ssw.com.au/Training/UTSNET/Pages/UTS%20NET%20Short%20Course.aspx"&gt;UTS Short Course&lt;/a&gt;
&lt;a href="file://fileserver/Shared%20Documents/Ignite%20Brisbane%20Talk.docx"&gt;Ignite Talk&lt;/a&gt;


::: bad
Figure – Bad Examples: file names have been published with spaces so the URLs look ugly and are hard to read
:::


&lt;a href="http://sharepoint.ssw.com.au/Training/UTSNET/Pages/UTSNETShortCourse.aspx"&gt;UTS Short Course&lt;/a&gt;
&lt;a href="file://fileserver/SharedDocuments/Ignite\_Brisbane\_Talk.docx"&gt;Ignite Talk&lt;/a&gt;


::: good
Figure – Good Examples: file names have no spaces so are much easier to read

:::
