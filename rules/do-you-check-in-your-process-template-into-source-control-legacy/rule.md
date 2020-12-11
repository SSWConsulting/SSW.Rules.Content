---
type: rule
archivedreason: 
title: Do you Check-in your process template into source control? (legacy)
guid: 2c2ef28f-d706-4153-8107-791037a14190
uri: do-you-check-in-your-process-template-into-source-control-legacy
created: 2012-07-18T07:16:38.0000000Z
authors:
- id: 10
  title: Lei Xu
- id: 78
  title: Matt Wicks
related:
- do-you-control-the-drop-down-list-value-for-assigned-to-field
- do-you-have-a-witadmin-script-to-import-work-item-definitions
- do-you-start-from-a-built-in-process-template
- do-you-use-global-list

---

For Azure DevOps Server (and old TFS servers)
Note: If using Azure DevOps (cloud) then you have no method of tracking changes to the Process Template

The customized process template is a very important asset for your team, you should use Source Control to store the work-in-progress template so you can track the changes and avoid mistakes.
<dl class="image">&lt;dt&gt;<img src="CheckInTemplateIntoSourceControl.png" alt="CheckInTemplateIntoSourceControl.png">&lt;/dt&gt;<dd>Figure: customized process template in source control </dd> </dl>
<!--endintro-->

You should also keep a version history log in ProcessTemplate.xml so you can track the deployed version easily.
<dl class="image">&lt;dt&gt;<img src="KeepHistoryForTemplate.png" alt="keep history">
   &lt;/dt&gt;<dd>Figure: ProcessTemplate.xml with version history log<br></dd></dl>
