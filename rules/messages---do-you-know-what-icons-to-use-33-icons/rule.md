---
type: rule
archivedreason: 
title: Messages - Do you know what icons to use? (3/3 Icons)
guid: 6d4001a7-aaee-40fe-a34b-ff049a1b6d94
uri: messages---do-you-know-what-icons-to-use-33-icons
created: 2012-11-27T04:37:34.0000000Z
authors: []
related: []

---

#### Icon

Including an icon is important because not only does it give the user a visual indication of the type of message, but without it only the Default beep sound is used. The icon should reflect the type of information being presented:

<!--endintro-->


| Icon | Name | When to use |
| --- | --- | --- |
| ![](../../assets/Info.gif) |  **MessageBoxIcon.Information**  | Non-error information, e.g. Database connection test completed successfully |
| ![](../../assets/Warning.gif) |  **MessageBoxIcon.Warning**  | A non-critical error, e.g. The input was invalid |
| ![](../../assets/Error.gif) |  **MessageBoxIcon.Error**  | Critical error in the program, e.g. Program file was not found |
| ![](../../assets/Question.gif) |  **MessageBoxIcon.Question**  |  **NEVER** use this.  <br>According to Microsoft, the Question mark is being phased out, as any of the other three: Error, Warning or Information can easily be reworded into a Question, and Question does not show the user the severity of the issue that has just occurred.<br>E.g.  If you want to ask the user whether they want to save a file before closing, you should use the Warning Icon.  |



We have a program called [SSW Code](http://www.ssw.com.au/ssw/CodeAuditor/Rules.aspx#TitleVB)Auditorto check for this rule.
