---
type: rule
title: Do you have templates for your PBIs and Bugs?
uri: do-you-have-templates-for-your-pbis-and-bugs
created: 2019-07-26T05:34:05.0000000Z
authors:
- id: 78
  title: Matt Wicks

---



<span class='intro'> ​Often bugs are hard to reproduce because they are inconsistently described, and people forget to say what they expected to see. To increase consistency of bug reporting - it's a great idea to add templates for work items in Azure DevOps. It guides people into the pit of success as it helps them fill in all the required info in a clear and concise manner – then you will never see unclear steps to repro a bug again.&#160;<br><br> </span>

<p>​​Often bugs are hard to reproduce because they are inconsistently described, and people forget to say what they expected to see. To increase consistency of bug reporting - it’s a great idea to add templates for work items in Azure DevOps. It guides people into the pit of success as it helps them fill in all the required info in a clear and concise manner – then you will never see unclear steps to repro a bug again.<br>&#160;<br></p><p>
   <img src="templates%20for%20pbis%20and%20bugs%20-%20bad%20example.png" alt="templates for pbis and bugs - bad example.png" style="margin&#58;5px;width&#58;808px;" />​<br></p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad Example – This new bug template doesn’t make it obvious how the team likes their steps to repro</dd><p>&#160;<img src="templates%20for%20pbis%20and%20bugs%20-%20good%20example.png" alt="templates for pbis and bugs - good example.png" style="margin&#58;5px;width&#58;808px;" /><br></p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good Example – This new bug template guides the user to fill in the steps to repro in an ordered list and even prompts them to fill in what they expected to happen (and what actually happened)</dd><p>&#160;<br>Setting this up is pretty easy.</p><ol><li>First you need to customise the template for a work item type&#160;<img src="templates%20for%20pbis%20and%20bugs%20-%20customise.png" alt="templates for pbis and bugs - customise.png" style="font-weight&#58;bold;color&#58;#444444;margin&#58;5px;width&#58;808px;" /><span style="font-weight&#58;bold;color&#58;#444444;">​</span><span style="font-weight&#58;bold;color&#58;#444444;">Fi</span><span style="font-weight&#58;bold;color&#58;#444444;">gure&#58; Customising a bug work item</span></li><li>​Choose the form control to edit<br> 
      <dd class="ssw15-rteElement-FigureNormal">
         <img src="templates%20for%20pbis%20and%20bugs%20-%20customise%20form.png" alt="templates for pbis and bugs - customise form.png" style="margin&#58;5px;width&#58;808px;" />
         <br>Figure&#58; Customising a bug work item form</dd></li><li>​​​​​Choose the form control to edit​&#160;<img src="templates%20for%20pbis%20and%20bugs%20-%20customise%20default%20value.png" alt="templates for pbis and bugs - customise default value.png" style="margin&#58;5px;width&#58;808px;" />
      <dd class="ssw15-rteElement-FigureNormal">Figure&#58; Set the default value for the Repro Steps field (tip&#58; use HTML)</dd></li><li>Save Template​<br></li></ol>​ 
<p>&#160;<br>Sample Template&#58;</p><p class="ssw15-rteElement-GreyBox">&lt;ol&gt;&lt;li&gt;First I did this&lt;/li&gt;&lt;li&gt;Then I did this&lt;/li&gt;&lt;/ol&gt;&lt;div&gt;&lt;b&gt;Expected Result&lt;/b&gt;&lt;/div&gt;&lt;div&gt;I expected it to save properly&lt;/div&gt;&lt;div&gt;&lt;b&gt;&lt;br&gt;&lt;/b&gt;&lt;/div&gt;&lt;div&gt;&lt;b&gt;Actual Result&lt;/b&gt;&lt;/div&gt;&lt;div&gt;I got an exception (tip&#58; you can copy/paste screenshots)​<br></p>


