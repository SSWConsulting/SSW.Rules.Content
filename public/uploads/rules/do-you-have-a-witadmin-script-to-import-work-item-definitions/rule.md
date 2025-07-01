---
seoDescription: Do you need to frequently update your work item types? This script helps you quickly upload customized process templates with one click, making development more efficient.
type: rule
archivedreason:
title: Do you have a WitAdmin script to import work item definitions?
guid: a3674fce-a018-47e0-ac55-e8e21043af58
uri: do-you-have-a-witadmin-script-to-import-work-item-definitions
created: 2012-07-18T07:34:00.0000000Z
authors:
  - title: Lei Xu
    url: https://ssw.com.au/people/lei-xu
related: []
redirects: []
---

You will need to update your work item types very frequently once the customization process is started, make sure you have a script like below in your solution, this will help you to upload your process template quickly with one click, which make your development more efficient.

<!--endintro-->

```bash
ECHO OFF
ECHO \*\*\*\*\*\*\*\*\*\*\*Importing new definitions\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
ECHO ON
witadmin importwitd /collection:http://%1:8080/tfs/%2 /p:%3 /f:"..\CN.SAC.TfsProcessTemplate\WorkItem Tracking\TypeDefinitions\Requirement.xml"
witadmin importwitd /collection:http://%1:8080/tfs/%2 /p:%3 /f:"..\CN.SAC.TfsProcessTemplate\WorkItem Tracking\TypeDefinitions\Task.xml"
witadmin importwitd /collection:http://%1:8080/tfs/%2 /p:%3 /f:"..\CN.SAC.TfsProcessTemplate\WorkItem Tracking\TypeDefinitions\Issue.xml"

ECHO OFF
ECHO \*\*\*\*\*\*\*\*\*\*\*Importing new definitions\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
ECHO ON
witadmin importwitd /collection:http://%1:8080/tfs/%2 /p:%3 /f:"..\CN.SAC.TfsProcessTemplate\WorkItem Tracking\TypeDefinitions\Requirement.xml"
witadmin importwitd /collection:http://%1:8080/tfs/%2 /p:%3 /f:"..\CN.SAC.TfsProcessTemplate\WorkItem Tracking\TypeDefinitions\Task.xml"
witadmin importwitd /collection:http://%1:8080/tfs/%2 /p:%3 /f:"..\CN.SAC.TfsProcessTemplate\WorkItem Tracking\TypeDefinitions\Issue.xml" Figure: quick
deployment script for process template – UpdateProcessTemplate.bat With above script, you can execute the command like below UpdateProcessTemplate.bat <serverAddress>
<collectionName> <projectName>
```

So, just one command, all of your customized work item types will be updated on the server.
