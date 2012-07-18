---
type: rule
archivedreason: 
title: Do you have a WitAdmin script to import work item definitions?
guid: a3674fce-a018-47e0-ac55-e8e21043af58
uri: do-you-have-a-witadmin-script-to-import-work-item-definitions
created: 2012-07-18T07:34:00.0000000Z
authors:
- id: 10
  title: Lei Xu
related: []

---


<p class="MsoListParagraph">You will need to update your work item type
frequently once the customization process is started, make sure you have a
script like below ready in your solution, this will help you to upload your
process template quickly with one click, it will make your development more
efficient.&#160;</p>
<br><excerpt class='endintro'></excerpt><br>
<span class="ssw-rteStyle-CodeArea">​<span style="font-family&#58;consolas;font-size&#58;13.333333969116211px;">ECHO OFF​<br></span><p class="MsoNormal" style="margin-left&#58;36pt;font-size&#58;12.222222328186035px;"><span style="font-size&#58;10pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">ECHO ***********Importing new definitions*******************************</span></p>
<p class="MsoNormal" style="margin-left&#58;36pt;font-size&#58;12.222222328186035px;"><span style="font-size&#58;10pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">ECHO ON</span></p>
<p class="MsoNormal" style="margin-left&#58;36pt;font-size&#58;12.222222328186035px;"><span style="font-size&#58;10pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">witadmin importwitd /collection&#58;http&#58;//%1&#58;8080/tfs/%2 /p&#58;%3 /f&#58;&quot;..\CN.SAC.TfsProcessTemplate\WorkItem Tracking\TypeDefinitions\Requirement.xml&quot;</span></p>
<p class="MsoNormal" style="margin-left&#58;36pt;font-size&#58;12.222222328186035px;"><span style="font-size&#58;10pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">witadmin importwitd /collection&#58;http&#58;//%1&#58;8080/tfs/%2 /p&#58;%3 /f&#58;&quot;..\CN.SAC.TfsProcessTemplate\WorkItem Tracking\TypeDefinitions\Task.xml&quot;</span></p>
<p class="MsoListParagraph" style="font-size&#58;12.222222328186035px;"><span></span><span style="font-size&#58;10pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">witadmin importwitd /collection&#58;http&#58;//%1&#58;8080/tfs/%2 /p&#58;%3 /f&#58;&quot;..\CN.SAC.TfsProcessTemplate\WorkItem Tracking\TypeDefinitions\Issue.xml&quot;<br><br></span><p class="MsoNormal" style="margin-left&#58;36pt;font-size&#58;12.222222328186035px;"><span style="line-height&#58;17.77777862548828px;">​</span><span style="line-height&#58;17.77777862548828px;font-family&#58;consolas;font-size&#58;13.333333969116211px;">ECHO OFF​<br></span><span style="line-height&#58;17.77777862548828px;"></span><span style="line-height&#58;17.77777862548828px;"></span></p>
<p class="MsoNormal" style="margin-left&#58;36pt;font-size&#58;12.222222328186035px;"><span style="font-size&#58;10pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">ECHO ***********Importing new definitions*******************************</span></p>
<p class="MsoNormal" style="margin-left&#58;36pt;font-size&#58;12.222222328186035px;"><span style="font-size&#58;10pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">ECHO ON</span></p>
<span style="line-height&#58;17.77777862548828px;"></span><p class="MsoNormal" style="margin-left&#58;36pt;font-size&#58;12.222222328186035px;"><span style="font-size&#58;10pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">witadmin importwitd /collection&#58;http&#58;//%1&#58;8080/tfs/%2 /p&#58;%3 /f&#58;&quot;..\CN.SAC.TfsProcessTemplate\WorkItem Tracking\TypeDefinitions\Requirement.xml&quot;</span></p>
<p class="MsoNormal" style="margin-left&#58;36pt;font-size&#58;12.222222328186035px;"><span style="font-size&#58;10pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">witadmin importwitd /collection&#58;http&#58;//%1&#58;8080/tfs/%2 /p&#58;%3 /f&#58;&quot;..\CN.SAC.TfsProcessTemplate\WorkItem Tracking\TypeDefinitions\Task.xml&quot;</span></p>
<p class="MsoListParagraph" style="font-size&#58;12.222222328186035px;"><span style="font-size&#58;10pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">witadmin importwitd /collection&#58;http&#58;//%1&#58;8080/tfs/%2 /p&#58;%3 /f&#58;&quot;..\CN.SAC.TfsProcessTemplate\WorkItem Tracking\TypeDefinitions\Issue.xml&quot;​​</span></p></p></span>

<br>

<p class="MsoListParagraph"><b>Figure&#58; quick deployment script for process
template – UpdateProcessTemplate.bat</b></p>

<p class="MsoListParagraph">&#160;</p>

<p class="MsoListParagraph">With above script, you can execute the command like
below</p>

<p class="MsoListParagraph"><b>UpdateProcessTemplate.bat &lt;serverAddress&gt;
&lt;collectionName&gt; &lt;projectName&gt;​</b></p>
​


