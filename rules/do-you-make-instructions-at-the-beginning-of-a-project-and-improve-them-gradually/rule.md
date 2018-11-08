---
type: rule
title: Do you make instructions at the beginning of a project and improve them gradually?
uri: do-you-make-instructions-at-the-beginning-of-a-project-and-improve-them-gradually
created: 2009-05-13T06:12:34.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 17
  title: Ryan Tee
- id: 24
  title: Adam Stephensen

---



<span class='intro'> ​​​​​Instructions are&#160;very important when maintaining a project. With this document, people new to it can take over it quickly.<br> </span>

<p><br></p><p>​There are 4&#160;Levels of this documentation in a project.<br>​<br><span style="color&#58;#000000;font-family&#58;&quot;open sans&quot;, sans-serif;font-size&#58;1.2rem;">Level 1 - Lots of documentation step by step​​</span><br></p><p class="ssw15-rteElement-Tip">Add a document as a solution item and name it '_Instru​​ctions.docx'&#160;</p><p class="ssw15-rteElement-Reference">​​Tip&#58; Microsoft Word documents are preferred over .txt files because images and formatting are important<br></p><p>You can also break up this document into 4 smaller documents</p><ul><li>_Business.docx - Explaining the business purpose of the app</li><li>_Instructions_Compile.docx - Contains instructions on how to get the project to compile<br></li><li>_Instructions_Deployment.docx - Describes the deployment process</li><li>_Technologies.docx - Explaining the technical overview e.g. Broad architecture decisions, 3rd party utilities, patterns followed etc</li></ul><p>Here's a suggestion of what these documents could contain.&#160;<br></p><ol><li>Project structure 
      <p>All parts that composes the project and how they work with each other.</p></li><li>Third party components 
      <p>Any software, tools and DLL files that this project uses. (e.g., NHibernate, ComponentArt,&#160;KendoUI)<br></p></li><li>Database configuration</li><li>Other configuration information</li><li>Deployment information and&#160;procedures 
      <br></li><li>Other things to take care of</li></ol><dl class="badImage"><dt>
      <img src="/PublishingImages/BadNetProject.JPG" alt="A project with an instructions" />
   </dt><dd>Bad example - A project without an instructions. </dd></dl><dl class="goodImage"><dt>
      <img alt="Good Solutions Have Instructions" src="/PublishingImages/ProjectDocumentation.jpg" />
   </dt><dd>Good example - A project with instruction </dd></dl><p class="ssw15-rteElement-Tip">Level&#160; 1a&#58;</p><p class="ssw15-rteElement-Tip">VSTS with Markdown<br>Add a readme.md to your solution (Use&#160;<a href="https&#58;//docs.microsoft.com/en-us/azure/devops/project/wiki/markdown-guidance?view=vsts" target="_blank">this​</a>&#160;as a guidance for markdown)​<br></p><h2>Level 2&#58; Can you get latest and compile with a Docx</h2><p>When a new developer starts on a project you want them to get up and running as soon as possible.</p><p>Problems to check for&#58;</p><ul><li>Windows 8 not supported</li><li>Many things to build</li><li>Lots of dependencies</li></ul><p>It is essential to have documentation that describes what is required to configure a developer workstation.<br></p><dl class="image"><dd>You are at Level 2 when you have the static word documents with the step to compile. The _instructions_compile.docx contains the steps required to be able to get latest and compile</dd></dl><h2>Level 3&#58; Can you get latest and compile with the database</h2><dl class="image"><dt>
      <img alt="Good Solutions Have Instructions - level 2" src="/PublishingImages/instructions-level2.jpg" />
   </dt><dd>Figure&#58; Level 2 Documentation includes database build scripts. We use 
      <a target="_blank" href="http&#58;//sqldeploy.com/">SSW SQL Deploy</a>&#160;to make keeping all databases on the same version simple. Check out 
      <a target="_blank" href="http&#58;//tv.ssw.com/969/adam-stephensen-sql-deploy-demo">how to use SQL Deploy here </a></dd></dl><h2>Level 4&#58; Can you get latest and compile with a PowerShell script</h2><p>A perfect solution would need no static documentation. Perfect code would be so self-explanatory that it did not need comments. The same rule applies with instructions on how to get the solution compiling&#58; the best answer would be for the solution to contain scripts that automate&#160;the setup.</p><div style="margin&#58;0px 0px 0px 40px;border&#58;none;padding&#58;0px;"><h2>Example of Level 3&#58; PowerShell Documentation<br></h2><p>
      <strong>Recommendation&#58;</strong> All manual workstation setup steps should be scripted with powerShell (as per the below example)</p><p>
      <strong>Recommendation&#58;</strong> You should be able to get latest and compile within 1 minute. Also, a developer machine should not HAVE to be on the domain (to support external consultants)<br></p><div class="ssw-rteStyle-GreyBox">PS C&#58;\Code\Northwind&gt;<strong> .\Setup-Environment.ps1</strong><br><br>Problem&#58; Azure environment variable run state directory is not configured (_CSRUN_STATE_DIRECTORY).<br>&#160;<br>Problem&#58; Azure Storage Service is not running. Launch the development fabric by starting the solution.<br>&#160;<br>WARNING&#58; Abandoning remainder of script due to critical failures.<br>&#160;<br>To try and automatically resolve the problems found, re-run the script with a -Fix flag.<br></div><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good example - you see the problems in the devs environment<br></dd><div class="ssw-rteStyle-GreyBox">
      <br>PS C&#58;\Code\Northwind&gt; .\Setup-Environment.ps1 -fix<br><br>Problem&#58; Azure environment variable run state directory is not configured (_CSRUN_STATE_DIRECTORY).<br><br>Fixed&#58; _CSRUN_STATE_DIRECTORY user variable set<br>&#160;<br>Problem&#58; Azure Storage Service is not running. Launch the development fabric by starting the solution.<br><br>WARNING&#58; No automated fix availab ​​le for 'Azure Storage Service is running'<br>&#160;<br>WARNING&#58; Abandoning remainder of script due to critical failures.<br></div><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good example - when running with -fix this script&#160;tries to automatically fix the problem 
      <br></dd><div class="ssw-rteStyle-GreyBox">
      <br>
      <br>PS C&#58;\Code\Northwind&gt; .\Setup-Environment.ps1 -fix<br><br>Problem&#58; Azure Storage Service is not running. Launch the development fabric by starting the solution.<br>WARNING&#58; No automated fix available for 'Azure Storage Service is running'<br><br>WARNING&#58; Abandoning remainder of script due to critical failures.<br><br><br></div><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good example -&#160; Note that on the 2nd run, issues resolved by the 1st run are not re-reported 
      <br></dd></div><h2>Further Reading</h2><p>To see other documentation Rules, have a look at 
   <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=951ffbf9-4066-42f3-a9b7-e0d8603e728b">Do you review the documentation? </a></p>


