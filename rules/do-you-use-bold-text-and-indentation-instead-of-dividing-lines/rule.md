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


<p>
                    Many applications have a lot of content on each form. If this is the case there
                    needs to be some way to separate certain sections. To achieve this separation Microsoft
                    (and therefore most developers) uses separating lines, but this UI is not perfect
                    because:
                </p><ul><li>It creates additional visual clutter</li><li>It is hard to maintain</li></ul>
<br><excerpt class='endintro'></excerpt><br>
<p> We recommend using bold instead of dividing lines because: </p><ol><li>Bold stands out</li><li>Indentation is more important</li><li>Developers are not good at keeping the lines aligned - you could create a .NET custom control to do this - but Microsoft do not provide one 
      <ul><li>The dividing lines create additional visual clutter (ever so slight)</li><li>Each line creates additional performance implications (ever so slight)</li></ul></li></ol><dl class="badImage"><dt> 
      <img border="0" alt="Internet options form of IE" src="../../assets/ToolsOptionforIE.gif" style="margin:5px;width:416px;" />
   </dt><dd> Figure: Bad Example - This is the Tools - Options from Internet Explorer and it groups each section in a groupbox - busy UI. </dd></dl><dl class="badImage"><dt> 
      <img border="0" alt="Options form of Outlook" src="../../assets/ToolsOptionforOutlook.gif" style="margin:5px;width:449px;" />
   </dt><dd> Figure: Bad Example - This is the Tools - Options from Outlook and it uses dividing lines for each section.</dd></dl><dl class="badImage"><dt> 
      <img border="0" alt="SSW Code AUditor - Email and Schedule" src="../../assets/BadDivider.gif" style="margin:5px;width:550px;" />
   </dt><dd> Figure: Bad Example - This is an old screen from Code Auditor - the dividing lines are not required. </dd></dl><dl class="goodImage"><dt> 
      <img border="0" alt="SSW Code Auditor - Email and Schedule" src="../../assets/GoodDivider.jpg" style="margin:5px;width:550px;" />
   </dt><dd> Figure: Good Example - This is the new screen from Code Auditor - the bold title and indenting are the best way to show the sections.</dd></dl>


