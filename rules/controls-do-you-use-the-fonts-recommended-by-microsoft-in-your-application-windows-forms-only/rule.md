---
type: rule
archivedreason: 
title: Controls - Do you use the fonts recommended by Microsoft in your application? (Windows Forms Only)
guid: 733e7da0-e5d7-4224-8362-5f6ca804f118
uri: controls-do-you-use-the-fonts-recommended-by-microsoft-in-your-application-windows-forms-only
created: 2012-11-27T09:16:16.0000000Z
authors: []
related: []
redirects:
- controls-do-you-use-the-fonts-recommended-by-microsoft-in-your-application-(windows-forms-only)

---

Some font are easier to read then others, at SSW we follow Microsoft's [Visual Design Guidelines](http://www.ssw.com.au/ssw/Redirect/Microsoft/MSDNInterfaceText.htm). This means we use Tahoma 8pt as our font of choice.

<!--endintro-->

At SSW, we use Code Auditor to ensure all fonts on our forms are set to Tahoma but we allow controls to use a different font. This is because certain information is better displayed in a different font. For example a Textbox to show code should use Courier instead of Tahoma.


::: bad  
![Figure: Bad Example - This form uses a non-standard font, and it is hard to read](../../assets/FontBadArialNarrow.gif)  
:::


::: good  
![Figure: Good Example - This form uses Tahoma, and it is easy to read](../../assets/FontGoodTahoma.gif)  
:::


::: good  
![Figure: Good Example - This form uses Tahoma, and the RichTextBox displays source code using Courier New](../../assets/FontCourierNew.gif)  
:::


| We have a program called [SSW Code Auditor](http://www.ssw.com.au/ssw/CodeAuditor/Rules.aspx#VBFont) to check for this rule. |
| --- |
