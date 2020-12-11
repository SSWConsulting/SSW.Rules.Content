---
type: rule
archivedreason: 
title: Do you control the drop down list value for Assigned To field?
guid: d8c9078f-2f20-4c87-8647-094081b8ce92
uri: do-you-control-the-drop-down-list-value-for-assigned-to-field
created: 2012-07-18T07:44:27.0000000Z
authors:
- id: 10
  title: Lei Xu
related:
- do-you-check-in-your-process-template-into-source-control-legacy
- do-you-have-a-witadmin-script-to-import-work-item-definitions
- do-you-start-from-a-built-in-process-template
- do-you-use-global-list

---

The default WIT doesn’t control the valid drop down items in Assigned To filed, this will introduce unnecessary items to be shown in the list which will make your users confused, e.g. TFSBUILD, tfsBuildService should never be used to assign a job.

[[badExample]]
| ![shown unnecessary values](UnnecessaryValue.png)
<!--endintro-->
 You can add the following XML in the Assigned To filed definition to control the valid values:

<FIELD name="Assigned To" refname="System.AssignedTo" type="String" reportable="dimension" syncnamechanges="true">
<ALLOWEXISTINGVALUE />
  <REQUIRED />
  <ALLOWEXISTINGVALUE />
  <VALIDUSER />
  <ALLOWEDVALUES expanditems="true" filteritems="excludegroups">
        <LISTITEM value="Active" />
        <LISTITEM value="[project]\xxxxDepNamexxxxGroup" />
ALLOWEDVALUES>
FIELD> 

Figure: Use ALLOWEDVALUES to control the values in Assigned to field


[[goodExample]]
| ![shown necessary values](ShowNecessaryUser.png)
