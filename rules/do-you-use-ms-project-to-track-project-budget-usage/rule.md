---
type: rule
archivedreason: 
title: Do you use MS Project to track project budget usage?
guid: d7c9d502-42fd-4d64-ac5a-41ba7ff84efd
uri: do-you-use-ms-project-to-track-project-budget-usage
created: 2009-11-27T05:46:28.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Lei Xu
  url: https://ssw.com.au/people/lei-xu
related: []
redirects: []

---


As long as you have work items created and your developers keep them up to date, you can use MS Project to calculate project budget usage in real-time; this helps the project manager to determine the progress in term of $ which is what client really care about. <br>
Note&#58; To have this working properly, you need VSTS 2010 because it has better MS Project integration. <br>

<br><excerpt class='endintro'></excerpt><br>

  <strong>Calculate the total cost for your release&#58;</strong> <br>
Follow the steps below to save a baseline and track your project budget usage&#58;<br>
<ol>
    <li>Open MS Project and connect to your Team Project <img alt="" class="ms-rteCustom-ImageArea" src="/Standards/Management/RulesToBetterProjectManagement/PublishingImages/ChooseTeamProject_Small.jpg" /> <font class="ms-rteCustom-FigureNormal">Figure&#58; Click “Choose Team Project” and choose the project you want to track </font></li>
    <li>Query the work items from the team project <img alt="" src="/Standards/Management/RulesToBetterProjectManagement/PublishingImages/QueryTheWorkItem_Small.jpg" /><font class="ms-rteCustom-FigureNormal">Figure&#58; Click on “Get Work Items” and choose query to select the work items you want to track</font>Note&#58; normally you want to create queries for each of your Release, then you can quickly import them together. </li>
    <li>To Track progress, we will want to use “Team System Task Sheet” view, you can choose this from “View” menu. </li>
    <li>You will have your work items imported and they will be arranged with hierarchy, because we are trying to track the progress, we want to keep “Original Estimate”, “Remaining Work” and “Completed Work” together, so drag them after the Work Item Title. <img alt="" src="/Standards/Management/RulesToBetterProjectManagement/PublishingImages/ArrangeWorkItems_Small.jpg" /><font class="ms-rteCustom-FigureNormal">Figure&#58; Arrange your work items so we can easily track their progress</font> </li>
    <li>To have the cost calculated, we need to assign rate for each of the resources. Go to “View, Resource Sheet”, then you can assign rate for your resources&#58; <br>
    <img alt="" class="ms-rteCustom-ImageArea" src="/Standards/Management/RulesToBetterProjectManagement/PublishingImages/AssignResourceRates.jpg" /><font class="ms-rteCustom-FigureNormal">Figure&#58; Assign resources rates</font> </li>
    <li>When you switch back to “Team System Task Sheet”, you will want to add the following fields so we can see the cost status;<br>
    &#160;&#160;a.&#160; Baseline Cost<br>
    &#160;&#160;b. Remaining Cost<br>
    &#160;&#160;c. Actual Cost <br>
    You will notice the “Remaining Cost” column has been calculated based on the “Remaining Work” column and the Rate we entered for each task. <br>
    <img alt="" class="ms-rteCustom-ImageArea" src="/Standards/Management/RulesToBetterProjectManagement/PublishingImages/CostColumn_Small.jpg" /><font class="ms-rteCustom-FigureNormal">Figure&#58; Showing cost columns </font></li>
    <li>However, this will not giving you a total cost for your current release. You can do this by adding a summary task on the top so MS Project will calculate that for you.<br>
    Choose the 1st task in your project, right click and create a “New Task” <br>
    <img alt="" class="ms-rteCustom-ImageArea" src="/Standards/Management/RulesToBetterProjectManagement/PublishingImages/SummaryTask.jpg" /><font class="ms-rteCustom-FigureNormal">Figure&#58; Create a summary task at the top</font> Name the task as per your release name so you know what this plan is for; also you don’t want this task to be created in your TFS as a work item because it’s just a summary, set “Publish and Refresh” as “No”. <br>
    <img alt="" class="ms-rteCustom-ImageArea" src="/Standards/Management/RulesToBetterProjectManagement/PublishingImages/NoPublishAndRefresh.jpg" /><font class="ms-rteCustom-FigureNormal">Figure&#58; Don’t publish and refresh this summary task</font> To make this as a summary, you need to select all the rest tasks and indent them by clicking the little red forward arrow in the tool bar.<br>
    <img alt="" class="ms-rteCustom-ImageArea" src="/Standards/Management/RulesToBetterProjectManagement/PublishingImages/IndentTask_Small.jpg" /><font class="ms-rteCustom-FigureNormal">Figure&#58; Indent tasks</font> Now, your summary task is ready and it’s showing the total cost for your current release&#58; <img alt="" class="ms-rteCustom-ImageArea" src="/Standards/Management/RulesToBetterProjectManagement/PublishingImages/TotalCost_Small.jpg" /> <font class="ms-rteCustom-FigureNormal">Figure&#58; Total cost is calculated</font> </li>
</ol>
<p><strong>Baseline management&#58;</strong><br>
Baseline management is very important for every project managers as it helps you to determine the budget usage; the initial estimate of the project should be approved by the client, at this point it becomes your initial baseline. So before you set a baseline in your MS Project, make sure it’s approved by the client. </p>
<p>To set a baseline, choose “Tools, Tracking, Set Baseline” from the menu&#58; <img alt="" src="/Standards/Management/RulesToBetterProjectManagement/PublishingImages/SetBaseline_Small.jpg" /><font class="ms-rteCustom-FigureNormal">Figure&#58; Set Baseline …</font><img alt="" src="/Standards/Management/RulesToBetterProjectManagement/PublishingImages/ChooseBaseline.jpg" /><font class="ms-rteCustom-FigureNormal">Figure&#58; Choose “Baseline” and click ok</font></p>
<p>MS Project allows you to set multiple baselines; this is very handy because when the project is running, client will want to add/remove tasks from the project, then they will need to approve a new baseline. <br>
Once your baseline is set, you will be able to see the “Baseline Cost” column is showing $,<img alt="" class="ms-rteCustom-ImageArea" src="/Standards/Management/RulesToBetterProjectManagement/PublishingImages/BaselineCost_Small.jpg" /><font class="ms-rteCustom-FigureNormal">Figure&#58; Baseline Cost is showing $</font></p>
<p><strong>Track your project on the go</strong><br>
When your project is running, your developers will update the “Remaining Work” and “Completed Work” columns from TFS, they may not use MS Project so you will need to refresh your MS Project file to get these changes, and the $ will be calculated on the fly to give you up-to-date status.<br>
<img alt="" class="ms-rteCustom-ImageArea" src="/Standards/Management/RulesToBetterProjectManagement/PublishingImages/BudgetUsage_Small.jpg" /><font class="ms-rteCustom-FigureNormal">Figure&#58; Budget usage is calculated.</font> Note&#58; if the values are not calculated, it maybe your calculation mode is set to “manual”, then you need to hit F9 to force MS Project to calculate. Or you can change this setting in “Tools, Options, Calculation”. <br>
<img alt="" src="/Standards/Management/RulesToBetterProjectManagement/PublishingImages/CalculationMode_Small.jpg" /><font class="ms-rteCustom-FigureNormal">Figure&#58; set the calculation mode to “Automatic”</font>Also make sure “Actual costs are always calculated by Microsoft Office Project” is enabled. </p>



