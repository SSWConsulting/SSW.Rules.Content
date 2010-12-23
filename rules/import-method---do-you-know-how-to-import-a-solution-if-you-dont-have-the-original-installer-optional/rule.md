---
type: rule
archivedreason: 
title: Import Method - Do you know how to import a solution if you don’t have the original installer? (optional)
guid: 1bc2b15b-4c78-4692-a6f0-384c37794b57
uri: import-method---do-you-know-how-to-import-a-solution-if-you-dont-have-the-original-installer-optional
created: 2010-12-23T03:10:35.0000000Z
authors: []
related: []

---


You should have at this point, either&#58;<br>
<br>
1. Installer packages from 3rd Party Vendors for installing their custom solution or,<br>
2. WSP packages from 3rd party, or built from your own source code, or extracted using the Export Method (not recommended)<br>
<br>
You can add the WSP package solutions&#160;to the new server by&#58;
<ol>
    <li>Open up <b>cmd</b> with Administrator privileges</li>
    <li>Enter your <b>C&#58;\SharePointCustomizations </b>folder<br>
    <span class="ms-rteCustom-CodeArea">cd C&#58;\SharePointCustomizations</span> </li>
    <li>Use <b>stsadm</b> to import the solution to your new server<br>
    <span class="ms-rteCustom-CodeArea">Stsadm –o AddSolution –filename NameOfSolution.wsp</span> </li>
    <li>Make sure there are no errors when the command runs</li>
</ol>

<br><excerpt class='endintro'></excerpt><br>



