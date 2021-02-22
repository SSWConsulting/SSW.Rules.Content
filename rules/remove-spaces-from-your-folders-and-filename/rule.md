---
type: rule
archivedreason: 
title: Do you remove spaces from your folders and filename?
guid: 77003d23-7544-4bbe-92b9-48eae917d4a0
uri: remove-spaces-from-your-folders-and-filename
created: 2018-04-23T21:58:29.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-remove-spaces-from-your-folders-and-filename

---

It is not a good idea to have spaces in a folder or file name as they don't translate to URLs very well and can even cause technical problems.

Instead of using spaces, you should have the first letter of each word in UPPERCASE and the rest of the word in lowercase. Alternatively, you can choose to use underscores. This alternative method to spacing makes file names more readable when published on the web.

<!--endintro-->

Note that this rule should apply to any file or folder that is on the web. This includes TFS Team Project names and SharePoint Pages.



```
extremeemailsversion1.2.doc
Extreme Emails version 1.2.doc
```




::: bad
Figure - Bad Examples: filenames have spaces or dots 

:::



```
Extreme_Emails_v1_2.doc
ExtremeEmails_v1_2.doc
```




::: good
Figure – Good Examples: file names do not have spaces  
:::



```
<a href="http://sharepoint.ssw.com.au/Training/UTSNET/Pages/UTS%20NET%20Short%20Course.aspx">UTS Short Course</a>
<a href="file://fileserver/Shared%20Documents/Ignite%20Brisbane%20Talk.docx">Ignite Talk</a>
```




::: bad
Figure – Bad Examples: file names have been published with spaces so the URLs look ugly and are hard to read  
:::



```
<a href="http://sharepoint.ssw.com.au/Training/UTSNET/Pages/UTSNETShortCourse.aspx">UTS Short Course</a>
<a href="file://fileserver/SharedDocuments/Ignite_Brisbane_Talk.docx">Ignite Talk</a>
```




::: good
Figure – Good Examples: file names have no spaces so are much easier to read

:::
