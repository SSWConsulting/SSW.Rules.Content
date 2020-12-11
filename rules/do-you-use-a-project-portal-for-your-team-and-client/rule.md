---
type: rule
archivedreason: 
title: Do you use a Project Portal for your team and client?
guid: 073dcd99-1259-4bda-8eb7-1b371750083c
uri: do-you-use-a-project-portal-for-your-team-and-client
created: 2016-06-05T21:21:17.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 3
  title: Eric Phan
related: []

---

When a new developer joins a project, there is often a sea of information that they need to learn right away to be productive. This includes things like:

1. Who the <br>         [Product Owner](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=a91de77d-a8dd-40be-b61a-bd6305e7183f) is and who the <br>         [Scrum Master](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=c38e68bd-763b-4e19-b3ab-6083115ac1f2) is
2. Where the backlog is
3. Where the automated builds are
4. Where the staging and production environments are
5. How to set up the development environment for the project


Make it easy for the new developer by putting all this information in a central location like the Visual Studio dashboard.
<dl class="image">&lt;dt&gt;
      <img src="plaindashboard.png" alt="plaindashboard.png" style="width:800px;"> 
   &lt;/dt&gt;  </dl><dl class="badImage">&lt;dt&gt;
      <img src="2016-06-06_8-00-55.png" alt="2016-06-06_8-00-55.png" style="width:800px;">
      <br>
   &lt;/dt&gt;<dd>Figure: Bad Example - Don't stick with the default dashboard, it's almost useless</dd></dl><dl class="goodImage">&lt;dt&gt; 
      <img src="2016-06-06_9-15-14.png" alt="2016-06-06_9-15-14.png" style="width:800px;">
   &lt;/dt&gt;<dd>Figure: Good Example - This dashboard contains all the information a new team member would need to get started<br></dd></dl> 

<!--endintro-->

The dashboard should contain:

1. Who the [Product Owner](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=a91de77d-a8dd-40be-b61a-bd6305e7183f) is and who the [Scrum Master](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=c38e68bd-763b-4e19-b3ab-6083115ac1f2) is
2. The [Definition of Ready](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=e01abde1-9a3e-4e4c-84a8-50e98e9c44d0) and the [Definition of Done](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=6449ae79-ba88-447e-aa48-36173029a2af)
3. When the [daily standups](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=731a3f5d-a266-4944-876c-a45afa82832f) occur and when the next sprint review is scheduled
4. The current sprint backlog
5. Show the current build status
6. Show links to:
    * Staging environment
    * Production environment
    * Any other external service used by the project e.g. Octopus Deploy, Application Insights, RayGun, Elmah, Slack


Your solution should also contain the standard [\_Instructions.docx](/Pages/DoYouMakeInstructions.aspx) to your solution file for additional details on getting the project up and running in Visual Studio.

For particularly large and complex projects you can use an induction tool like [SugarLearning](https://www.sugarlearning.com/) to create a course for getting up to speed with the project.
<dl class="image">&lt;dt&gt;<img src="2016-06-06_7-18-43.png" alt="2016-06-06_7-18-43.png" style="width:800px;"><br>&lt;/dt&gt;</dl>
