---
type: rule
archivedreason: 
title: Do you make instructions at the beginning of a project and improve them gradually?
guid: 3f837d99-dd94-4f21-8b07-7348151fb89d
uri: do-you-make-instructions-at-the-beginning-of-a-project-and-improve-them-gradually
created: 2009-05-13T06:12:34.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ryan Tee
  url: https://ssw.com.au/people/ryan-tee
- title: Adam Stephensen
  url: https://ssw.com.au/people/adam-stephensen
related: []
redirects: []

---


Developers are better at coding then creating documentation. However project instructions are very important to enable developers to get up and running quickly.<br>
<br><excerpt class='endintro'></excerpt><br>
<p>In the prior rule:  
   <a href=/do-you-review-the-documentation>Do you review the documentation? we learnt of the 6 documents</a><br></p><p>​There are 4 levels of project documentation. Documentation can start simple but ends up having a lot of manual steps. The best projects have simple documentation but more done automatically (level 4).​​​</p><h3 class="ssw15-rteElement-H3">Level 1 - Lots of documentation step by step​​​​​<br></h3><p class="ssw15-rteElement-Tip">Add a document as a solution item and name it '_Instru​​ctions.docx' </p><p class="ssw15-rteElement-Reference">​​Tip: Microsoft Word documents are preferred over .txt files because images and formatting are important<br></p><p>You can also break up this document into 4 smaller documents</p><ul><li>_Business.docx - Explaining the business purpose of the app</li><li>_Instructions_Compile.docx - Contains instructions on how to get the project to compile<br></li><li>_Instructions_Deployment.docx - Describes the deployment process</li><li>_Technologies.docx - Explaining the technical overview e.g. Broad architecture decisions, 3rd party utilities, patterns followed etc</li></ul><p>Here's a suggestion of what these documents could contain. <br></p><ol><li>Project structure 
      <p>All parts that composes the project and how they work with each other.</p></li><li>Third party components 
      <p>Any software, tools and DLL files that this project uses. (e.g., NHibernate, ComponentArt, KendoUI)<br></p></li><li>Database configuration</li><li>Other configuration information</li><li>Deployment information and procedures 
      <br></li><li>Other things to take care of</li></ol><dl class="badImage"><dt>
      <img src="BadNetProject.JPG" alt="A project with an instructions" />
   </dt><dd>Bad example - A project without an instruction. </dd></dl><dl class="goodImage"><dt>
      <img alt="Good Solutions Have Instructions" src="ProjectDocumentation.jpg" />
   </dt><dd>Good example - A project with instructions​<br></dd></dl><p class="ssw15-rteElement-Tip">Add a readme.md to your solution (Use <a href="https://docs.microsoft.com/en-us/azure/devops/project/wiki/markdown-guidance?view=vsts">this​</a>  as a guidance for markdown)​​<br></p><h3 class="ssw15-rteElement-H3">​​​Level #2: Lots of documentation (and the *exact* steps to Get Latest and compile)<br></h3><p>When a new developer starts on a project you want them to get up and running as soon as possible.</p><p class="ssw15-rteElement-GreyBox">If you were at Level 2 you might have a document that says:<br>Dear Northwind Developer<br>     This documentation describes what is required to configure a developer PC.​<br><br>Problems to check for:<br><span class="ssw15-rteStyle-IndentText">​</span>​Windows 8 not supported<br>​<span class="ssw15-rteStyle-IndentText">​</span>Many things to build<br>​​<span class="ssw15-rteStyle-IndentText">​</span>Lots of dependencies​​<br></p><p></p><dl class="image"><dd>You are at Level 2 when you have some static Word documents with the steps​ to compile. The _instructions_compile.docx contains the steps required to be able to get latest and compile.<br></dd></dl><h3 class="ssw15-rteElement-H3">Level #3: Lots of documentation (and the exact steps to Get Latest and compile with the *database*)<br></h3><dl class="image"><dt>
      <img alt="Good Solutions Have Instructions - level 2" src="instructions-level2.jpg" />
   </dt><dd>Figure: Level 2 Documentation includes database build scripts. We use 
      <a target="_blank" href="http://sqldeploy.com/">SSW SQL Deploy</a> to make keeping all databases on the same version simple. Check out 
      <a target="_blank" href="http://tv.ssw.com/969/adam-stephensen-sql-deploy-demo">how to use SQL Deploy here </a></dd></dl><h3 class="ssw15-rteElement-H3">Level #4: Less documentation (and Get Latest and compile with a PowerShell script)​<br></h3><p>A perfect solution would need no static documentation. Perfect code would be so self-explanatory that it did not need comments. The same rule applies with instructions on how to get the solution compiling: the best answer would be for the solution to contain scripts that automate the setup.<br></p><p>
   <span style="font-weight:bold;">Example of Level </span>
   <span style="font-weight:bold;">6</span><span style="font-weight:bold;">: PowerShell Documentation</span></p><div style="margin:0px 0px 0px 40px;border:none;padding:0px;"><p>
      <strong>Recommendation:</strong> All manual workstation setup steps should be scripted with powerShell (as per the below example)</p><p>
      <strong>Recommendation:</strong> You should be able to get latest and compile within 1 minute. Also, a developer machine should not HAVE to be on the domain (to support external consultants)<br></p><div class="ssw-rteStyle-GreyBox">PS C:\Code\Northwind&gt;<strong> .\Setup-Environment.ps1</strong><br><br>Problem: Azure environment variable run state directory is not configured (_CSRUN_STATE_DIRECTORY).<br> <br>Problem: Azure Storage Service is not running. Launch the development fabric by starting the solution.<br> <br>WARNING: Abandoning remainder of script due to critical failures.<br> <br>To try and automatically resolve the problems found, re-run the script with a -Fix flag.<br></div><dd class="ssw15-rteElement-FigureGood">Figure: Good example - you see the problems in the devs environment<br></dd><div class="ssw-rteStyle-GreyBox">
      <br>PS C:\Code\Northwind&gt; .\Setup-Environment.ps1 -fix<br><br>Problem: Azure environment variable run state directory is not configured (_CSRUN_STATE_DIRECTORY).<br><br>Fixed: _CSRUN_STATE_DIRECTORY user variable set<br> <br>Problem: Azure Storage Service is not running. Launch the development fabric by starting the solution.<br><br>WARNING: No automated fix availab ​​le for 'Azure Storage Service is running'<br> <br>WARNING: Abandoning remainder of script due to critical failures.<br></div><dd class="ssw15-rteElement-FigureGood">Figure: Good example - when running with -fix this script tries to automatically fix the problem 
      <br></dd><div class="ssw-rteStyle-GreyBox">
      <br>
      <br>PS C:\Code\Northwind&gt; .\Setup-Environment.ps1 -fix<br><br>Problem: Azure Storage Service is not running. Launch the development fabric by starting the solution.<br>WARNING: No automated fix available for 'Azure Storage Service is running'<br><br>WARNING: Abandoning remainder of script due to critical failures.<br><br><br></div><dd class="ssw15-rteElement-FigureGood">Figure: Good example -  Note that on the 2nd run, issues resolved by the 1st run are not re-reported 
      <br></dd></div><h2>Further Reading</h2><p>To see other documentation Rules, have a look at 
   <a href=/do-you-review-the-documentation>Do you review the documentation? </a>
   <br><br></p>


