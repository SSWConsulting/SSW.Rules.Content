---
seoDescription: Ensure a consistent reading experience by using Microsoft-recommended Tahoma font on Windows Forms, while allowing controls to use alternative fonts for specific information.
type: rule
archivedreason: Deprecated
title: Controls - Do you use the fonts recommended by Microsoft in your application? (Windows Forms Only)
guid: 733e7da0-e5d7-4224-8362-5f6ca804f118
uri: controls-do-you-use-the-fonts-recommended-by-microsoft-in-your-application-windows-forms-only
created: 2012-11-27T09:16:16.0000000Z
authors: []
related: []
redirects:
  - controls-do-you-use-the-fonts-recommended-by-microsoft-in-your-application-(windows-forms-only)
---

Some font are easier to read then others, at SSW we follow Microsoft's Visual Design Guidelines. This means we use Tahoma 8pt as our font of choice.

<!--endintro-->

Ensure all fonts on your forms are set to Tahoma but we allow controls to use a different font. This is because certain information is better displayed in a different font. For example a Textbox to show code should use Courier instead of Tahoma.

::: bad  
![Figure: Bad example - This form uses a non-standard font, and it is hard to read](/FontBadArialNarrow.gif)  
:::

::: good  
![Figure: Good example - This form uses Tahoma, and it is easy to read](/FontGoodTahoma.gif)  
:::

::: good  
![Figure: Good example - This form uses Tahoma, and the RichTextBox displays source code using Courier New](/FontCourierNew.gif)  
:::
