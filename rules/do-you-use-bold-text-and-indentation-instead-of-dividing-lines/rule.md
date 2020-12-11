---
type: rule
archivedreason: 
title: Do you use bold text and indentation, instead of dividing lines?
guid: b6c9c134-bcc4-475a-a8fc-af1c42922d52
uri: do-you-use-bold-text-and-indentation-instead-of-dividing-lines
created: 2014-12-01T04:06:48.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

Many applications have a lot of content on each form. If this is the case there                     needs to be some way to separate certain sections. To achieve this separation Microsoft                     (and therefore most developers) uses separating lines, but this UI is not perfect                     because:

* It creates additional visual clutter
* It is hard to maintain


<!--endintro-->

We recommend using bold instead of dividing lines because:

1. Bold stands out
2. Indentation is more important
3. Developers are not good at keeping the lines aligned - you could create a .NET custom control to do this - but Microsoft do not provide one
    * The dividing lines create additional visual clutter (ever so slight)
    * Each line creates additional performance implications (ever so slight)

<dl class="badImage">&lt;dt&gt; 
      <img border="0" alt="Internet options form of IE" src="../../assets/ToolsOptionforIE.gif" style="margin:5px;width:416px;">
   &lt;/dt&gt;<dd> Figure: Bad Example - This is the Tools - Options from Internet Explorer and it groups each section in a groupbox - busy UI. </dd></dl><dl class="badImage">&lt;dt&gt; 
      <img border="0" alt="Options form of Outlook" src="../../assets/ToolsOptionforOutlook.gif" style="margin:5px;width:449px;">
   &lt;/dt&gt;<dd> Figure: Bad Example - This is the Tools - Options from Outlook and it uses dividing lines for each section.</dd></dl><dl class="badImage">&lt;dt&gt; 
      <img border="0" alt="SSW Code AUditor - Email and Schedule" src="../../assets/BadDivider.gif" style="margin:5px;width:550px;">
   &lt;/dt&gt;<dd> Figure: Bad Example - This is an old screen from Code Auditor - the dividing lines are not required. </dd></dl><dl class="goodImage">&lt;dt&gt; 
      <img border="0" alt="SSW Code Auditor - Email and Schedule" src="../../assets/GoodDivider.jpg" style="margin:5px;width:550px;">
   &lt;/dt&gt;<dd> Figure: Good Example - This is the new screen from Code Auditor - the bold title and indenting are the best way to show the sections.</dd></dl>
