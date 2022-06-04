---
type: rule
archivedreason: 
title: Do you use icons on files' links to not to surprise users?
guid: 283e14e7-fe59-4017-9422-e9efc3eda6da
uri: use-icons-to-not-surprise-users
created: 2015-02-16T02:46:02.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Tiago Araujo
  url: https://ssw.com.au/people/tiago-araujo
related:
- do-you-use-icons-in-web-pages-to-enforce-the-text-meaning
- do-you-use-an-icon-so-a-password-prompt-should-never-be-a-surprise
- do-you-make-external-links-clear
- best-libraries-for-icons
redirects:
- do-you-use-icons-not-to-surprise-users-(aka-use-the-correct-image-for-files)
- do-you-use-icons-not-to-surprise-users-aka-use-the-correct-image-for-files

---

When a user clicks a hyperlink, they expect a webpage to open. If they click on a link that is actually a .DOC file, they might encounter the unexpected experience of having Microsoft Word open in the background.

<!--endintro-->

Don't surprise users! Use icons next to links to show different types of links/files.

| Link/file type           |      Examples (see option A)      |
| ------------- | ----------- |
| **PDF**                  | [This is a PDF file](Sample-PDF.pdf) |
| **DOC**                  | [This is a Word Document file](Sample-DOC.docx) |
| **XLS**                  | [This is an Excel Spreadsheet file](Sample-XLS.xlsx) |
| **PPT**                  | [This is a PowerPoint file](Sample-PPT.pptx) |
| **TXT**                  | [This is a text file](Sample-TXT.txt) |
| **AVI, MOV, MPG, etc.**  | [This is a video file](sample-VIDEO.mp4) |
| **WAV, WMA, MP3, etc.**  | [This is a music file](sample-AUDIO.mp3) |
| **ICS or VCS**           | [This is a calendar file](Sample-ICS.ics) |
| **ZIP**                  | [This is a zip file](Sample-ZIP.zip) |
| **YouTube**              | [This is a link to a YouTube video](https://www.youtube.com/watch?v=gp_F43lx6iM) |
| **Email (mailto:)**      | [This link will send an email](mailto:example@mail.com) |
| **Normal link**          | [This is a normal link](/rules) |
| **External link ([see rule](/do-you-make-external-links-clear))** | [This is an external link](https://www.microsoft.com/) |

::: bad  
![Figure: Bad example - Users would expect all these hyperlinks to work the same way](link-with-icons-bad.png)  
:::

::: good  
![Figure: Good example - The PDF icon indicates one of the links is not a webpage](link-with-icons-good.png)  
:::

### How to add icons to links using CSS

Use CSS to match the extension at the end of the &lt;a&gt; tag. Add some padding to give it some space before the text (where the icon will be).

**Option A: Using font icons, like FontAwesome (Recommended)**

Using icon fonts saves time and hassle during the development process. It replaces the need to create/buy images, and upload them to the server.  
They will also look good on any screen resolution or display.

✅ UI - Consistent icons   
✅ Fast to load (lightweight as no image)   
✅ Free $   
✅ Editing is easier  

To implement [use one of the different ways to set up Font Awesome](https://fontawesome.com/docs/web/#web-setup). Then find the icon unicode at [FontAwesome icons page](https://fontawesome.com/icons) and replace on the CSS "content" value.

```css
a[href$='.pdf']:before
    content: "\F08B ";
    font-family: FontAwesome;
    padding-right: 4px;
    display: inline-block;
}
```

**Option B: Using images**

Create or buy a collection of icons that match your website style. The benefit is the ability to have custom and multi-colored icons, that can look exactly like a software logo for example. But it's usually not worth the hassle. 

You will add each icon image to your server, and then add the path as background URL in the CSS file.

❌ UI - Hard to get all icons consistent   
❌ Paid $ (icon collection required if you want them to have a nice and consistent UI)  
❌ Maintenance of needing to upload to server

```css
a[href$='.pdf'] 
{ 
background: transparent url(/images/icon_pdf.gif) center left no-repeat; 
padding-left: 20 px; 
}
```
