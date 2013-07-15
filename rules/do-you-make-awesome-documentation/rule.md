---
type: rule
title: Do you make awesome documentation?
uri: do-you-make-awesome-documentation
created: 2012-03-16T08:01:26.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 23
  title: Damian Brady
- id: 3
  title: Eric Phan
- id: 4
  title: Ulysses Maclaren
- id: 24
  title: Adam Stephensen

---



<span class='intro'> 
<p>There are 2 styles of documentation&#58;</p> </span>

<h3>Style #1&#58; Old School&#58;</h3><table class="ssw-rteTable-default" cellspacing="0" style="width&#58;80%;font-size&#58;1em;"><tbody><tr class="ssw-rteTableEvenRow-default"><th class="ssw-rteTableFirstCol-default">​<img class="ms-rteCustom-ImageArea" alt="IwS2" src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/iwS2.jpg" style="margin-right&#58;10px;" /></th><td class="ssw-rteTableOddCol-default"><p>​This style of team does a lot of upfront documentation and planning, is very comfortable with Waterfall, and has rarely even heard of Agile &#58;)</p></td></tr></tbody></table><ul><li>Heavy, long documents</li><li>Sequence Diagrams​</li><li>UML</li></ul><p>This is a well established way to do documentation but the issue with it is that it gets out of date.</p><dl class="image"><dt> 
      <img alt="enterprisearchitect1" src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/enterprisearchitect1.jpg" /> 
   </dt><dd>Figure&#58; Documentation can take the form of Sequence Diagrams</dd></dl><dl class="image"><dt> 
      <img alt="enterprisearchitectusecases.png" src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/EnterpriseArchitectUseCases.jpg" /> 
   </dt><dd>Figure&#58; ...or Use Case Diagrams </dd></dl><p>Exception&#58; Keep this limited to just enough documentation to cover a couple of sprints, and be committed to keeping it updated. The tool of choice if you're going down this road is Enterprise Architect (an excellent application built by Australians).</p><h3>Style #2&#58; New School&#58;</h3><table class="ssw-rteTable-default" cellspacing="0" style="width&#58;80%;font-size&#58;1em;"><tbody><tr class="ssw-rteTableEvenRow-default"><th class="ssw-rteTableFirstCol-default">​<img alt="Mark Zuckerberg" src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/68843503-mark-zuckerberg.jpg" style="margin-right&#58;10px;" /></th><td class="ssw-rteTableLastCol-default">​This style of team are all under 30 and have never heard of FoxPro or Access</td></tr></tbody></table><ul><li>4 small docs (a couple of pages max + in the order you would read them)&#58; </li><li>Business.docx - Explaining the business purpose of the app</li><li>_Instructions_Compile.docx - Contains instructions on 
      <a href="/SoftwareDevelopment/RulesToBetterDotNETProjects/Pages/DoYouMakeInstructions.aspx">how to get the project to compile (aka the F5 experience)</a></li><li>_Instructions_Deployment.docx - Describes the deployment process</li><li>Technologies.docx - Explaining the technical overview e.g. Broad architecture decisions, 3rd party utilities, patterns followed etc.</li><li>Unit Tests</li><li>Code and Work Items (Via the magic of Annotation) </li></ul><dl class="image"><dt> 
      <img alt="ProjectDocumentation.jpg" src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/ProjectDocumentation.jpg" />
   </dt><dd>Figure&#58;&#160;4 small docs explain most of what you need to know very briefly.</dd></dl><dl class="image"><dt> 
      <img alt="UnitTestExplorer.png" src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/UnitTestExplorer.png" /> 
   </dt><dd>Figure&#58; Nice Unit Tests explain what the code is supposed to be doing.</dd></dl><dl class="image"><dt> 
      <img alt="vs11debug.png" src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/VS11Debug.png" /> 
   </dt><dd>Figure&#58; Most young developers are happy with good old stepping through code with F11. The good thing is there are no diagrams that become out of date (which they always do after the first couple of sprints) giving you nasty Technical Debt.</dd></dl><dl class="image"><dt> 
      <img alt="tfspreviewbacklog.png" src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/TFSPreviewBacklog.jpg" /> 
   </dt><dd>Figure&#58; Don't forget that you have the completed requirements which get done and archived and can now serve as free documentation&#160;e.g. User Stories (aka PBIs)</dd><dl class="image"><dt> 
         <img alt="Annotation and Comment" src="http&#58;//www.ssw.com.au/ssw/standards/rules/Images/AnnotationAndComment.jpg" /> 
      </dt><dd>Figure&#58; Annotations marry up the code with the PBIs, showing who, what, why and when for each piece of code</dd></dl><div class="scrum-GreyBox"><p>If you subscribe to this work item check in policy, then you understand that the PBI is now the documentation. If requirements change during the course of the PBI (based on a conversation with Product Owner of course) then the PBI should be updated.</p><p>When updating the acceptance criteria, 
         <s>strike through</s> the altered acceptance criteria and add the new ones. Get the PO to confirm your understanding.</p><p>E.g.<br><s>Enter search text, click ‘Google’, and see the results populate below.</s><br>[Updated]<br> Enter search text and automatically see the results populate below.</p><p>This should be added to the 
         <a href="/Management/RulesToSuccessfulProjects/Pages/DoYouGoBeyondDoneAndFollowADoneCriteria.aspx">definition of done</a>.</p></div><div class="greyBox" style="margin-top&#58;20px;">
      <img class="ms-rteCustom-ImageArea" alt="Technical Debt" src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/Debt.jpg" style="float&#58;right;" /> 
      <p> 
         <strong>What's &quot;Technical Debt&quot;?</strong></p><p>During a project, when you add functionality, you have a choice&#58; </p><p>One way&#160;is quick but messy - it will make further changes harder in the future (i.e. quick and dirty). </p><p>The other way is cleaner – it will make changes easier to do in the future, but will take longer to put in place.</p><p>'Technical Debt' is a metaphor to help us think about this problem. In this metaphor (often mentioned during Scrum software projects), doing things the quick and dirty way gives us a 'technical debt', which will have to be fixed later. Like a financial debt, the technical debt incurs interest payments - in the form of the extra effort that we have to do in future development. </p><p>We can choose to continue paying the interest, or we can pay the debt up front by redoing the piece of work in the cleaner way.</p><p>The same principle is true with documentation. Using the 'old school' method will leave you with a build up of documentation that you will need to keep up-to-date as the project evolves.</p><p>Warning&#58; if you want to follow Scrum and have zero technical debt, then you have to throw away all documentation at the end of each sprint. If you do want to keep it, make sure you add it to your 
         <a href="/Management/RulesToSuccessfulProjects/Pages/DoYouGoBeyondDoneAndFollowADoneCriteria.aspx">definition of done </a>to keep it updated.</p></div></dl>


