---
seoDescription: Control assigned to field values in TFS by adding allowedvalues and valid user options in XML definition.
type: rule
archivedreason:
title: Do you control the drop down list value for Assigned To field?
guid: d8c9078f-2f20-4c87-8647-094081b8ce92
uri: do-you-control-the-drop-down-list-value-for-assigned-to-field
created: 2012-07-18T07:44:27.0000000Z
authors:
  - title: Lei Xu
    url: https://ssw.com.au/people/lei-xu
related:
  - do-you-check-in-your-process-template-into-source-control
  - do-you-have-a-witadmin-script-to-import-work-item-definitions
  - do-you-start-from-a-built-in-process-template
  - do-you-use-global-list
redirects: []
---

The default WIT doesn’t control the valid drop down items in Assigned To filed, this will introduce unnecessary items to be shown in the list which will make your users confused, e.g. TFSBUILD, tfsBuildService should never be used to assign a job.
![](UnnecessaryValue.png)
Figure: Bad Example – shown unnecessary values

<!--endintro-->

You can add the following XML in the Assigned To filed definition to control the valid values:

&lt;FIELD name="Assigned To" refname="System.AssignedTo" type="String" reportable="dimension" syncnamechanges="true"&gt;
&lt;ALLOWEXISTINGVALUE /&gt;
&lt;REQUIRED /&gt;
&lt;ALLOWEXISTINGVALUE /&gt;
&lt;VALIDUSER /&gt;
&lt;ALLOWEDVALUES expanditems="true" filteritems="excludegroups"&gt;
&lt;LISTITEM value="Active" /&gt;
&lt;LISTITEM value="[project]\xxxxDepNamexxxxGroup" /&gt;
&lt;/ALLOWEDVALUES&gt;
&lt;/FIELD&gt;

Figure: Use ALLOWEDVALUES to control the values in Assigned to field

![](ShowNecessaryUser.png)
Figure: Good Example – shown necessary values
