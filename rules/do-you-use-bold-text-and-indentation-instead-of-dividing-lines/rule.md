---
seoDescription: Use bold text and indentation instead of dividing lines to separate sections, enhancing visual clarity and reducing clutter for a better user experience.
type: rule
archivedreason:
title: Do you use bold text and indentation, instead of dividing lines?
guid: b6c9c134-bcc4-475a-a8fc-af1c42922d52
uri: do-you-use-bold-text-and-indentation-instead-of-dividing-lines
created: 2014-12-01T04:06:48.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []
---

Many applications have a lot of content on each form. If this is the case there needs to be some way to separate certain sections. To achieve this separation Microsoft (and therefore most developers) uses separating lines, but this UI is not perfect because:

* It creates additional visual clutter
* It is hard to maintain

<!--endintro-->

We recommend using bold instead of dividing lines because:

1. Bold stands out
2. Indentation is more important
3. Developers are not good at keeping the lines aligned - you could create a .NET custom control to do this - but Microsoft do not provide one
   * The dividing lines create additional visual clutter (ever so slight)
   * Each line creates additional performance implications (ever so slight)

::: bad  
![Figure: Bad Example - This is the Tools - Options from Internet Explorer and it groups each section in a groupbox - busy UI.](/ToolsOptionforIE.gif)  
:::

::: bad  
![Figure: Bad Example - This is the Tools - Options from Outlook and it uses dividing lines for each section.](/ToolsOptionforOutlook.gif)  
:::

::: bad  
![Figure: Bad Example - This is an old screen from Code Auditor - the dividing lines are not required.](/Bad-Divider.gif)  
:::

::: good  
![Figure: Good Example - This is the new screen from Code Auditor - the bold title and indenting are the best way to show the sections.](/GoodDivider.jpg)  
:::
