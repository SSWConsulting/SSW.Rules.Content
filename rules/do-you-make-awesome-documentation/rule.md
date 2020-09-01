---
type: rule
archivedreason: 
title: Do you make awesome documentation?
guid: d9a17cdf-0f7c-43dc-91a1-7b8fcc29467d
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
- id: 97
  title: Matt Goldman
related:
- reference-do-you-use-the-correct-symbols-when-documenting-instructions
- reference-do-you-use-the-right-order-of-instructions
- do-you-highlight-actions-correctly-in-your-document
- do-you-make-numbers-more-readable
- do-you-include-version-numbers-in-your-file
- do-you-refer-to-the-reader-and-author-consistently-throughout-your-document
- tiny-do-you-use-active-phrases-no-zombies-please

---



<p>​​​There are a few&#160;styles of documentation&#58;<br></p>
<br><excerpt class='endintro'></excerpt><br>
<h3 class="ssw15-rteElement-H3">Bad Example – Old School</h3><dl class="badImage"><dt> 
      <img src="/PublishingImages/old-documentation.png" alt="old-documentation.png" /> 
   </dt><dd>Figure&#58; The dinosaur’s method of documentation [5 options, recommended option highlighted]</dd></dl><p>The old school way is document first – lots of planning, and lots of heavy documentation created upfront before even a single line of code is written.</p><p>This is the method most familiar to teams who are comfortable with Waterfall and have possibly never heard of Agile. Documentation can normally be characterized by&#58;<br></p><ul><li>Heavy, long documents</li><li>Sequence Diagrams</li><li>UML</li></ul>This is a well-established way to do documentation, but it has several problems&#58;<br>
<ul><li>Gets out of date quickly</li><li>High maintenance overhead</li><li>Needs a business analyst</li></ul><dl class="badImage"><dt>
      <img alt="enterprisearchitect1" src="/PublishingImages/enterprisearchitect1.jpg" />
   </dt><dd>Figure&#58; Documentation can take the form of Sequence Diagrams</dd></dl><dl class="badImage"><dt>
      <img alt="enterprisearchitectusecases.png" src="/PublishingImages/EnterpriseArchitectUseCases.jpg" />
   </dt><dd>Figure&#58; Bad example - Use Case Diagrams are even worse!</dd></dl><p class="ssw15-rteElement-P"> ​There may be exceptions – some situations benefit from this kind of documentation; for example, it may be necessary to support a business case – although a well-defined spec is a better document to support a business case.</p><div><p class="ssw15-rteElement-GreyBox">
      <b>More info&#58; </b><a>https&#58;//rules.ssw.com.au/rules-to-better-specification-reviews​​</a><br></p>
   <b>Tip&#58;</b>&#160;Documentation should be as minimal as possible. If your circumstances require this style of documentation, start by limiting it to just enough to cover your first couple of Sprints. And recognize that by going down this path you make a commitment to keeping it up-to-date.</div><div>
   <br>
   <h3 class="ssw15-rteElement-H3">G​​ood example – The 7 Important Documents</h3><div class="ssw15-rteElement-ContentBlock-SSW-Only">
      <b>TODO David B&#58; </b>Add&#160;Figure&#58; Cool developers use the important 7 documents [can maybe use all 5 pics and organize them nicely into a collage]</div></div><div>
   <br>
   <p class="ssw15-rteElement-P">This style of documentation is used by modern teams who are Agile only.​<br></p></div><div><p class="ssw15-rteElement-P">There are 7 crucial documents for your project&#58;<br></p><p class="ssw15-rteElement-P"><br></p><p class="ssw15-rteElement-P"><b>In the repository (for developers)&#58;</b></p> 
   <p class="ssw15-rteElement-P">
      <b>&#160; &#160; 1. README.md</b> – Explains the overview of the project and provides links to the rest of the documentation.</p><p class="ssw15-rteElement-P">
      <strong>&#160; &#160; 2. docs\Instructions-Compile.md </strong>– Instructions on how to build and run the project (AKA the F5 experience).</p><p class="ssw15-rteElement-P">
      <strong>&#160; &#160; 3. docs\Instructions-Deployment.md</strong> – Explains how to deploy the solution, including any additional processes (e.g. DevOps)</p><p class="ssw15-rteElement-P">Keeping these documents in the repository means that you ensure that any documentation the developers need to work on or run the code is where they need it - with the code.</p><p class="ssw15-rteElement-P">It also means that when a developer makes a change to the code that needs an update to the documentation, the documentation changes can be checked in with along the code in the same commit.<br></p><p class="ssw15-rteElement-P"><br></p><p class="ssw15-rteElement-P"><b>In the Wiki (for developers and other stakeholders)&#58;</b></p><p class="ssw15-rteElement-GreyBox">
      <b>Note&#58;</b> When using a GitHub Wiki, it’s a separate repository. When using an Azure DevOps Wiki, it’s in the same repository.</p><p class="ssw15-rteElement-P">
      <b>&#160; &#160; 4. Wiki\Business</b> – explains the purpose of the application, including the problem, goals, and statement of intent.</p><p class="ssw15-rteElement-P">
      <b>&#160; &#160; 5.&#160;Wiki\Technologies-and-Architecture</b> – Provides a technical overview of the solution, including any 3rd party libraries or utilities, patterns followed (e.g. 
      <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=b3a8b0b0-6439-4d24-9b9c-9561bc749d0c">https&#58;//rules.ssw.com.au/rules-to-better-clean-architecture​</a>), architecture decisions, etc. This document should cover software architecture and cloud architecture (or on-premises if you’re a dinosaur &#128049;‍&#128009;), and should *always* have a system architecture diagram (see&#58; 
      <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=7b588070-e0d2-46f4-811e-87b15a8c190d">https&#58;//rules.ssw.com.au/have-an-architecture-diagram</a>)</p><p class="ssw15-rteElement-P">
      <b>&#160; &#160; 6.&#160;Wiki\Definition-of-Done</b> - Ensures that your team&#160;<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=6449ae79-ba88-447e-aa48-36173029a2af">maintains a high level of quality with a Definition of Done​&#160;</a></p><p class="ssw15-rteElement-P">
      <b>&#160; &#160; 7.​&#160;Wiki\Definition-of-Ready </b>– Ensures that all your PBIs are well defined to an agreed standard before adding them to a sprint (see&#58; 
      <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=e01abde1-9a3e-4e4c-84a8-50e98e9c44d0">https&#58;//rules.ssw.com.au/have-a-definition-of-ready</a>)<br></p><p class="ssw15-rteElement-P"><br></p><p class="ssw15-rteElement-P">Documents to be read or edited by the Product Owner (or other members of the Scrum team) are better kept out of the code repository, in the Wiki. The advantages of this approach are&#58;</p><ul><li>Updating the Wiki does not trigger the CI/CD pipeline</li><li>The writing experience in the Wiki is more friendly for non-developers (no need to clone the repo and submit a pull request; especially annoying for a minor change)</li></ul>
   <b>Tip&#58;</b> All of your documents (in your Wiki and your repository) should be written in Markdown (see&#58; 
   <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=a7b84edd-3378-423c-b8b7-a8590b454f85">https&#58;//rules.ssw.com.au/using-markdown-to-store-your-content</a>)</div><div><dl class="badImage"><dt> 
         <img src="/SiteAssets/do-you-review-the-documentation/documentation__level2__bad-example-gh.png" alt="documentation__level2__bad-example-gh.png" style="width&#58;750px;" /> 
         <br> 
      </dt><dd>Bad example - Github project without any documentation or instruction<br></dd></dl><dl class="badImage"><dt>
         <img src="/PublishingImages/azuredevops-bad.png" alt="azuredevops-bad.png" style="width&#58;750px;" />
      </dt><dd>​Bad example - Azure DevOps project without any documentation or instruction<span style="color&#58;#444444;">​</span></dd></dl><dl class="image"><dt>
         <img src="/SiteAssets/do-you-review-the-documentation/documentation__level2__good-example-1-gh.png" alt="documentation__level2__good-example-1-gh.png" style="width&#58;750px;" />
      </dt><dd>Better example - Github&#160;project with ​README instructions on how to compile and run the project (but still has a TODO)</dd></dl><dl class="goodImage"><dt> 
         <img src="/PublishingImages/azuredevops-good.png" alt="azuredevops-good.png" style="width&#58;750px;" /> 
      </dt><dd>Good example - Azure DevOps project&#160;with ​README instructions&#160;on how to compile&#160;and run the&#160;project<span style="color&#58;#444444;">​</span></dd></dl><dl class="goodImage"><dt> 
         <img src="/SiteAssets/do-you-review-the-documentation/documentation__level2__good-example-2-gh.png" alt="documentation__level2__good-example-2-gh.png" style="width&#58;750px;" />
      </dt><dd>Good example - Github&#160;project with Wiki instructions for product owners, stakeholders, or public consumption&#160;<span style="color&#58;#444444;">(Source&#58; </span><span style="color&#58;#444444;"><a href="https&#58;//github.com/christoment/Northwind/wiki">https&#58;//github.com/christoment/Northwind/wiki​</a></span><span style="color&#58;#444444;">)</span></dd></dl><dl class="goodImage"><dt>
         <img src="/PublishingImages/azuredevops-wiki-good.png" alt="azuredevops-wiki-good.png" style="width&#58;750px;" />
      </dt><dd>Good example -&#160;Azure DevOps&#160;project with Wiki instructions for product owners, stakeholders, or public consumption<br></dd></dl><p class="ssw15-rteElement-P"> 
      <b>Tip&#58;</b> Use your documentation for onboarding developers</p></div><dl class="badImage"><dt> 
      <img src="/PublishingImages/sit-dev-bad.png" alt="sit-dev-bad.png" style="width&#58;750px;" /> 
   </dt><dd>Bad Example -&#160;No documentation, go and sit with another developer<br></dd></dl><dl class="goodImage"><dt> 
      <img src="/SiteAssets/do-you-review-the-documentation/documentation__level2__onboarding-pbi-3.png" alt="documentation__level2__onboarding-pbi-3.png" style="width&#58;750px;" /> 
   </dt><dd>Good example -&#160;​Developer onboarding can be self-guided by good documentation, and offers a structure for feedback and improvement if the developer hits any issues</dd></dl><p> 
   <b>Tip&#58; </b>Keep your documentation as minimal as possible - automate the F5 experience and deployment process (documents 2 and 3) using PowerShell scripts. Then your documents can just say &quot;​run these scripts&quot;</p><h3 class="ssw15-rteElement-H3">Level 3+&#58; The rest of the jigsaw​​<br></h3><div class="greyBox"><p> 
      <b>Scrum Tip&#58; Update your Acceptance Criteria</b> - If you use a policy that requires commits to be linked to PBIs, then you understand that the PBI is now the documentation. If requirements change (based on a conversation with the&#160;Product Owner of course) then the PBI should be updated.</p><p>When updating the Acceptance Criteria, 
      <s>strike through</s> the altered Acceptance Criteria, and add the new ones. Get the PO to confirm your understanding. 
      <br></p><p>E.g.<br><s>Enter search text, click ‘Google’, and see the results populate below.</s><br>[Updated]<br>Enter search text and automatically see the results populate below.</p><p>This should be added to the 
      <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=6449ae79-ba88-447e-aa48-36173029a2af">Definition of Done</a>.<br></p></div><div class="greyBox" style="margin-top&#58;20px;"> 
   <img class="ms-rteCustom-ImageArea" alt="Technical Debt" src="/PublishingImages/Debt.jpg" style="float&#58;right;" />
   <p>
      <strong>What's &quot;Technical Debt&quot;?</strong></p><p>During a project, when you add functionality, you have a choice&#58;</p><p>One way&#160;is quick but messy - it will make further changes harder in the future (i.e. quick and dirty).</p><p>The other way is cleaner – it will make changes easier to do in the future&#160;but will take longer to put in place.<br></p><p>'Technical Debt' is a metaphor to help us think about this problem. In this metaphor (often mentioned during Scrum software projects), doing things the quick and dirty way gives us a 'technical debt', which will have to be fixed later. Like financial debt, the technical debt incurs interest payments - in the form of the extra effort that we must&#160;do in future development.</p><p>We can choose to continue paying the interest, or we can pay the debt in full by redoing the piece of work in a cleaner way.</p><p>The same principle is true with documentation. Using the 'old school' method will leave you with a build-up of documentation that you will need to keep up to date as the project evolves.</p><p>Warning&#58; if you want to follow Scrum and have zero technical debt, then you must​ throw away all documentation at the end of each sprint. If you do want to keep it, make sure you add it to your&#160;<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=6449ae79-ba88-447e-aa48-36173029a2af">definition of done </a>to keep it updated.​<br></p></div>​<br>


