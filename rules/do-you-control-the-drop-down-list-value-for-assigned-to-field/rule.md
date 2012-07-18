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


<p class="MsoListParagraph">The default WIT doesn’t control the valid drop down
items in Assigned To filed, this will introduce unnecessary items to be shown
in the list which will make your users confused, e.g. TFSBUILD, tfsBuildService
should never be used to assign a job.<br><img src="/TFS/RulesToBetterTFSCustomization/PublishingImages/UnnecessaryValue.png" alt="UnnecessaryValue.png" style="margin&#58;5px;" /><br><br>&#160;Figure&#58; Bad Example – shown unnecessary values<br>&#160;You can add the following XML in the Assigned To filed definition to control
the valid values​&#160;</p>
<br><excerpt class='endintro'></excerpt><br>
​&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;
<span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;">&lt;</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;background-color&#58;white;">FIELD</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;"> </span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;red;background-color&#58;white;">name</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;">=</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">&quot;</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;">Assigned To</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">&quot;</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;"> </span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;red;background-color&#58;white;">refname</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;">=</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">&quot;</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;">System.AssignedTo</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">&quot;</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;"> </span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;red;background-color&#58;white;">type</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;">=</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">&quot;</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;">String</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">&quot;</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;"> </span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;red;background-color&#58;white;">reportable</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;">=</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">&quot;</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;">dimension</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">&quot;</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;"> </span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;red;background-color&#58;white;">syncnamechanges</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;">=</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">&quot;</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;">true</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">&quot;</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;">&gt;</span>

<p class="MsoNormal"><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;">&#160;&#160;&#160;&#160;&#160;&#160;&#160;
&lt;</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;background-color&#58;white;">ALLOWEXISTINGVALUE</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;"> /&gt;</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;"></span></p>

<p class="MsoNormal"><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;">&#160;&#160;&#160;&#160;&#160;&#160;&#160;
&lt;</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;background-color&#58;white;">REQUIRED</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;">
/&gt;</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;"></span></p>

<p class="MsoNormal"><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;">&#160;&#160;&#160;&#160;&#160;&#160;&#160;
&lt;</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;background-color&#58;white;">ALLOWEXISTINGVALUE</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;"> /&gt;</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;"></span></p>

<p class="MsoNormal"><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;">&#160;&#160;&#160;&#160;&#160;&#160;&#160;
&lt;</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;background-color&#58;white;">VALIDUSER</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;">
/&gt;</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;"></span></p>

<p class="MsoNormal"><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;">&#160;&#160;&#160;&#160;&#160;&#160;&#160;
&lt;</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;background-color&#58;white;">ALLOWEDVALUES</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;"> </span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;red;background-color&#58;white;">expanditems</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;">=</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">&quot;</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;">true</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">&quot;</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;"> </span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;red;background-color&#58;white;">filteritems</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;">=</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">&quot;</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;">excludegroups</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">&quot;</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;">&gt;</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;"></span></p>

<p class="MsoNormal"><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;">&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;
&lt;</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;background-color&#58;white;">LISTITEM</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;"> </span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;red;background-color&#58;white;">value</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;">=</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">&quot;</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;">Active</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">&quot;</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;"> /&gt;</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;"></span></p>

<p class="MsoNormal"><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;">&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;
&lt;</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;background-color&#58;white;">LISTITEM</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;"> </span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;red;background-color&#58;white;">value</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;">=</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">&quot;</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;">[project]\xxxxDepNamexxxxGroup</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">&quot;</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;"> /&gt;</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;"></span></p>

<p class="MsoNormal"><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;">&#160;&#160;&#160;&#160;&#160;&#160;&#160;
&lt;/</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;background-color&#58;white;">ALLOWEDVALUES</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;">&gt;</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;"></span></p>

<p class="MsoNormal"><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;">&#160;&#160;&#160;&#160;&#160;
&lt;/</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;background-color&#58;white;">FIELD</span><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;blue;background-color&#58;white;">&gt;</span></p>

<p class="MsoNormal">&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;
Figure&#58; Use ALLOWEDVALUES to control the values in Assigned to field </p>

<p class="MsoNormal">&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;
</p>

<p class="MsoNormal">&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;
[Good Example screen]</p>



