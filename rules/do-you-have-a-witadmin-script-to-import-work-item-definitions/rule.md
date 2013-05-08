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


​You will need to update your work item types
very frequently once the customization process is started, make sure you have a
script like below in your solution, this will help you to upload your
process template quickly with one click, which make your development more
efficient.
<br><excerpt class='endintro'></excerpt><br>
<span class="ssw-rteStyle-CodeArea">​ECHO OFF<br>ECHO ***********Importing new definitions*******************************<br>ECHO ON<br>witadmin importwitd /collection&#58;http&#58;//%1&#58;8080/tfs/%2 /p&#58;%3 /f&#58;&quot;..\CN.SAC.TfsProcessTemplate\WorkItem ​Tracking\TypeDefinitions\Requirement.xml&quot;<br>witadmin importwitd /collection&#58;http&#58;//%1&#58;8080/tfs/%2 /p&#58;%3 /f&#58;&quot;..\CN.SAC.TfsProcessTemplate\WorkItem Tracking\TypeDefinitions\Task.xml&quot;<br>witadmin importwitd /collection&#58;http&#58;//%1&#58;8080/tfs/%2 /p&#58;%3 /f&#58;&quot;..\CN.SAC.TfsProcessTemplate\WorkItem Tracking\TypeDefinitions\Issue.xml&quot;<br><br>​ECHO OFF​<br>ECHO ***********Importing new definitions*******************************<br>ECHO ON<br>witadmin importwitd /collection&#58;http&#58;//%1&#58;8080/tfs/%2 /p&#58;%3 /f&#58;&quot;..\CN.SAC.TfsProcessTemplate\WorkItem Tracking\TypeDefinitions\Requirement.xml&quot;<br>witadmin importwitd /collection&#58;http&#58;//%1&#58;8080/tfs/%2 /p&#58;%3 /f&#58;&quot;..\CN.SAC.TfsProcessTemplate\WorkItem Tracking\TypeDefinitions\Task.xml&quot;<br>witadmin importwitd /collection&#58;http&#58;//%1&#58;8080/tfs/%2 /p&#58;%3 /f&#58;&quot;..\CN.SAC.TfsProcessTemplate\WorkItem Tracking\TypeDefinitions\Issue.xml&quot;​​&#160;​</span><span class="ssw-rteStyle-FigureNormal">Figure&#58; quick
deployment script for process template – Upd​ateProcessTemplate.bat</span>
With above script, you can execute the command like
below
<span class="ssw-rteStyle-Tip">UpdateProcessTemplate.bat &lt;serverAddress&gt;
&lt;collectionName&gt; &lt;projectName&gt;
​​​</span>So, just one command, all of your customized work item types will be updated on the server. <br><br>


