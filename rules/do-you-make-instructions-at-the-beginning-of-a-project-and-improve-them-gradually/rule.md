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



<span class='intro'> Instructions are&#160;very important when maintaining a project. With this document, people new to it can take over it quickly. This document should be created at the beginning of a project and make sure it's updated gradually. ​​ </span>

<p>We recommend that you add a document as a solution item and name it '_Instructions.docx'. <br></p>
<p>You can also break up this document into 4 smaller documents</p>
<ul><li>_Business.docx - Explaining the business purpose of the app</li>
<li>_Instructions_Compile.docx - Contains instructions on how to get the project to compile</li>
<li>_Instructions_Deployment.docx - Describes the deployment process</li>
<li>_Technologies.docx - Explaining the technical overview e.g. Broad 
architecture decisions, 3rd party utilities, patterns followed etc</li></ul>
<p>Here's a suggestion of what these documents could contain. They are not compulsory but may be necessary for running the project. </p>
<ol><li>Project structure <p>All parts that composes the project and how they work with each other.</p></li>
<li>Third party components <p>Any software, tools and DLL files that this project uses. (e.g., NHibernate, ComponentArt)</p></li>
<li>Database configuration </li>
<li>Other configuration information</li>
<li>FTP information and Deployment procedure </li>
<li>Other things to take care of </li></ol>
<dl class="badImage"><dt><img border="0" src="/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/BadNetProject.JPG" alt="A project with an instructions" style="border-width&#58;0px;border-style&#58;solid;border-color&#58;-moz-use-text-color;" /> </dt>
<dd>Bad example - A project without an instructions. </dd></dl>
<dl class="goodImage"><dt><img alt="Good Solutions Have Instructions" src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/ProjectDocumentation.jpg" /></dt>
<dd>Good example - A project with instruction. </dd></dl>

<p>When a new developer starts on a project you want them to get up and running as soon as possible.</p>
<p>Problems to check for&#58;</p>
<ul>
<li> Windows 8 not supported</li>
<li>Many things to build</li>
<li>Lots of dependencies</li>
</ul>
<p>It is essential to have documentation that describes what is required to configure a developer workstation.</p>
<p>There are 3 Levels of this documentation in a project.</p>
<h2>Level 1&#58; Can you get latest and compile with a Docx </h2>
<dl class="image"><dt><img alt="Good Solutions Have Instructions - Level 1" src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/instructions-level1.jpg" /></dt>
<dd>Figure&#58; Level 1 documentation is static word documents. The _instructions_compile.docx contains the steps required to be able to get latest and compile</dd></dl>

<h2>Level 2&#58; Can you get latest and compile with the database </h2>
<dl class="image"><dt><img alt="Good Solutions Have Instructions - level 2" src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/instructions-level2.jpg" /></dt>
<dd>Figure&#58; Level 2 Documentation includes database build scripts. We use [SSW SQL Deploy] (link to SQL Deploy page) to make keeping all databases on the same version simple. Check out how to use [SQL Deploy here] (link to sql deploy video on ssw.tv)</dd></dl>

<h2>Level 3&#58; Can you get latest and compile  with a Powershell script</h2>

<p>A perfect solution would need no static documentation. Perfect code would be so self-explanatory that it did not need comments. The same rule applies with instructions on how to get the solution compiling&#58; the best answer would be for the solution to contain scripts that automates the setup.</p>
<h2>Example of Level 3&#58; Powershell Documentation</h2>

<p><strong>Recommendation&#58;</strong> All manual work station setup steps should be scripted with powershell (as per the below example)</p>
<p><strong>Recommendation&#58;</strong> You should be able to get latest and compile within 1 minute. Also, a developer machine should not HAVE to be on the domain (to support external consultants)</p>
<div class="ssw-rteStyle-GreyBox">PS C&#58;\Code\Northwind&gt;<strong> .\Setup-Environment.ps1</strong><br><br>Problem&#58; Azure environment variable run state directory is not configured (_CSRUN_STATE_DIRECTORY).<br>&#160;<br>Problem&#58; Azure Storage Service is not running. Launch the development fabric by starting the solution.<br>&#160;<br>WARNING&#58; Abandoning remainder of script due to critical failures.<br>&#160;<br>To try and automatically resolve the problems found, re-run the script with a -Fix flag.<br></div>
<span class="ssw-rteStyle-FigureNormal">Figure&#58; You see the problems in the devs environment</span>
<div class="ssw-rteStyle-GreyBox"><br>PS C&#58;\Code\Northwind&gt; .\Setup-Environment.ps1 -fix<br><br>Problem&#58; Azure environment variable run state directory is not configured (_CSRUN_STATE_DIRECTORY).<br><br>Fixed&#58; _CSRUN_STATE_DIRECTORY user variable set<br>&#160;<br>Problem&#58; Azure Storage Service is not running. Launch the development fabric by starting the solution.<br><br>WARNING&#58; No automated fix available for 'Azure Storage Service is running'<br>&#160;<br>WARNING&#58; Abandoning remainder of script due to critical failures.<br></div>
<span class="ssw-rteStyle-FigureNormal">Figure&#58; The script tries to automatically fix the problem<br></span>
<div class="ssw-rteStyle-GreyBox"><br><br>PS C&#58;\Code\Northwind&gt; .\Setup-Environment.ps1 -fix<br><br>Problem&#58; Azure Storage Service is not running. Launch the development fabric by starting the solution.<br>WARNING&#58; No automated fix available for 'Azure Storage Service is running'<br><br>WARNING&#58; Abandoning remainder of script due to critical failures.<br><br><br></div>
<span class="ssw-rteStyle-FigureNormal">Figure&#58; Note that on the 2nd run, issues resolved by the 1st run are not re-reported</span>

<h2>Further Reading</h2>
<p>To see other documentation Rules, have a look at <a href="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/Pages/DoYouReviewTheDocumentation.aspx">Do you review the documentation? </a></p>


