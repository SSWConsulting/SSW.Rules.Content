---
type: rule
archivedreason: 
title: Do you know when to use Power Automate vs internal workflow engine (Model Driven Apps)?
guid: 9a89cd74-7592-40dc-8c38-821dab93df6c
uri: do-you-know-when-to-use-power-automate-vs-internal-workflow-engine-model-driven-apps
created: 2020-10-27T22:32:26.0000000Z
authors:
- id: 32
  title: Mehmet Ozdemir
related: []

---

When creating workflows for Model-Driven Apps using Power Automate is now the suggested and for most scenarios the preferred workflow engine. Using Power Automate is simply a nicer experience compared to using the legacy workflow editor, with the ability to connect to over 300 connectors, visual editor, excellent expression editor that the built-in workflow editor simply can’t touch.

<!--endintro-->
<dl class="image">&lt;dt&gt;<img src="power-automate.png" alt="power-automate.png" style="width:750px;">&lt;/dt&gt;<dd>Figure: Using Power Automate is the preferred workflow engine</dd></dl>
There is one scenario where the built-in workflow engine is preferred and that is when a synchronous workflow is needed. A synchronous workflow means that all operations will wait until the workflow is completed. An example of this could be synchronous workflow being trigger on save of a record. You can be certain that when the user gets control back after saving the record that the workflow would have finished running. This is important in some instances, as with an asynchronous workflow (like Power Automate) the workflow will be triggered on save and the App will continue running as normal.
<dl class="image">&lt;dt&gt;<img src="builtin-workflow.png" alt="builtin-workflow.png" style="width:750px;">&lt;/dt&gt;<dd>Figure: Built-in workflow engine</dd></dl>
