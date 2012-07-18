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
<span class="ssw-rteStyle-CodeArea">​ECHO OFF<font face="consolas" size="2"><br></font>ECHO ***********Importing new definitions*******************************<br>ECHO ON<br>witadmin importwitd /collection&#58;http&#58;//%1&#58;8080/tfs/%2 /p&#58;%3 /f&#58;&quot;..\CN.SAC.TfsProcessTemplate\WorkItem ​Tracking\TypeDefinitions\Requirement.xml&quot;<br>witadmin importwitd /collection&#58;http&#58;//%1&#58;8080/tfs/%2 /p&#58;%3 /f&#58;&quot;..\CN.SAC.TfsProcessTemplate\WorkItem Tracking\TypeDefinitions\Task.xml&quot;<br>witadmin importwitd /collection&#58;http&#58;//%1&#58;8080/tfs/%2 /p&#58;%3 /f&#58;&quot;..\CN.SAC.TfsProcessTemplate\WorkItem Tracking\TypeDefinitions\Issue.xml&quot;<br><br>​ECHO OFF​<br>ECHO ***********Importing new definitions*******************************<br>ECHO ON<br>witadmin importwitd /collection&#58;http&#58;//%1&#58;8080/tfs/%2 /p&#58;%3 /f&#58;&quot;..\CN.SAC.TfsProcessTemplate\WorkItem Tracking\TypeDefinitions\Requirement.xml&quot;<br>witadmin importwitd /collection&#58;http&#58;//%1&#58;8080/tfs/%2 /p&#58;%3 /f&#58;&quot;..\CN.SAC.TfsProcessTemplate\WorkItem Tracking\TypeDefinitions\Task.xml&quot;<br>witadmin importwitd /collection&#58;http&#58;//%1&#58;8080/tfs/%2 /p&#58;%3 /f&#58;&quot;..\CN.SAC.TfsProcessTemplate\WorkItem Tracking\TypeDefinitions\Issue.xml&quot;​​&#160;</span><span>Figure&#58; quick
deployment script for process template – UpdateProcessTemplate.batWith above script, you can execute the command like
below</span>UpdateProcessTemplate.bat &lt;serverAddress&gt;
&lt;collectionName&gt; &lt;projectName&gt;
​​


