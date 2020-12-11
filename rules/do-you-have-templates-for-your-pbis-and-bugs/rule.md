---
type: rule
archivedreason: 
title: Do you have templates for your PBIs and Bugs?
guid: 6b0c6510-ccec-4f8c-9476-d934d12cf60c
uri: do-you-have-templates-for-your-pbis-and-bugs
created: 2019-07-26T05:34:05.0000000Z
authors:
- id: 78
  title: Matt Wicks
related: []

---


​Often bugs are hard to reproduce because they are inconsistently described, and people forget to say what they expected to see. To increase consistency of bug reporting - it's a great idea to add templates for work items in Azure DevOps. It guides people into the pit of success as it helps them fill in all the required info in a clear and concise manner – then you will never see unclear steps to repro a bug again. <br><br>
<br><excerpt class='endintro'></excerpt><br>
<p>​​Often bugs are hard to reproduce because they are inconsistently described, and people forget to say what they expected to see. To increase consistency of bug reporting - it’s a great idea to add templates for work items in Azure DevOps. It guides people into the pit of success as it helps them fill in all the required info in a clear and concise manner – then you will never see unclear steps to repro a bug again.<br> <br></p><p>
   <img src="templates for pbis and bugs - bad example.png" alt="templates for pbis and bugs - bad example.png" style="margin:5px;width:808px;" />​<br></p><dd class="ssw15-rteElement-FigureBad">Figure: Bad Example – This new bug template doesn’t make it obvious how the team likes their steps to repro</dd><p> <img src="templates for pbis and bugs - good example.png" alt="templates for pbis and bugs - good example.png" style="margin:5px;width:808px;" /><br></p><dd class="ssw15-rteElement-FigureGood">Figure: Good Example – This new bug template guides the user to fill in the steps to repro in an ordered list and even prompts them to fill in what they expected to happen (and what actually happened)</dd><p> <br>Setting this up is pretty easy.</p><ol><li>First you need to customise the template for a work item type <img src="templates for pbis and bugs - customise.png" alt="templates for pbis and bugs - customise.png" style="font-weight:bold;color:#444444;margin:5px;width:808px;" /><span style="font-weight:bold;color:#444444;">​</span><span style="font-weight:bold;color:#444444;">Fi</span><span style="font-weight:bold;color:#444444;">gure: Customising a bug work item</span></li><li>​Choose the form control to edit<br> 
      <dd class="ssw15-rteElement-FigureNormal">
         <img src="templates for pbis and bugs - customise form.png" alt="templates for pbis and bugs - customise form.png" style="margin:5px;width:808px;" />
         <br>Figure: Customising a bug work item form</dd></li><li>​​​​​Choose the form control to edit​ <img src="templates for pbis and bugs - customise default value.png" alt="templates for pbis and bugs - customise default value.png" style="margin:5px;width:808px;" />
      <dd class="ssw15-rteElement-FigureNormal">Figure: Set the default value for the Repro Steps field (tip: use HTML)</dd></li><li>Save Template​<br></li></ol>​ 
<p> <br>Sample Template:</p><p class="ssw15-rteElement-GreyBox"><ol><li>First I did this</li><li>Then I did this</li></ol><div><b>Expected Result</b></div><div>I expected it to save properly</div><div><b><br></b></div><div><b>Actual Result</b></div><div>I got an exception (tip: you can copy/paste screenshots)​<br></p>


