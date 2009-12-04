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

  <strong>Calculate the total cost for your release&#58;<br>
</strong>Follow the steps below to save a baseline and track your project budget usage&#58;<br>
<ol>
    <li>Open MS Project and connect to your Team Project <img alt="" class="ms-rteCustom-ImageArea" src="/Standards/Management/RulesToBetterProjectManagement/PublishingImages/ChooseTeamProject_Small.jpg" /> <font class="ms-rteCustom-FigureNormal">Figure&#58; Click “Choose Team Project” and choose the project you want to track </font></li>
    <li>Query the work items from the team project <img alt="" class="ms-rteCustom-ImageArea" src="/Standards/Management/RulesToBetterProjectManagement/PublishingImages/QueryTheWorkItem_Small.jpg" /><font class="ms-rteCustom-FigureNormal">Figure&#58; To select the work items that you want to use you should click on “Get Work Items” and choose a query.</font>Note&#58; normally you want to create queries for each of your Releases, then you can quickly import them together. </li>
    <li>To Track progress, we will use the “Team System Task Sheet” view; this can be selected from the “View” menu. </li>
    <li>Your work items will be imported and arranged within a hierarchy. As we are trying to track the progress, we want to keep “Original Estimate”, “Remaining Work” and “Completed Work” together, so drag them after the Work Item Title.<img alt="" class="ms-rteCustom-ImageArea" src="/Standards/Management/RulesToBetterProjectManagement/PublishingImages/ArrangeWorkItems_Small.jpg" /><font class="ms-rteCustom-FigureNormal">Figure&#58; Arrange your work items so we can easily track their progress</font> </li>
    <li>In order to have the cost calculated, we need to assign a rate to each of the resources. This can be done by going to “View | Resource Sheet”<br>
    <img alt="" class="ms-rteCustom-ImageArea" src="/Standards/Management/RulesToBetterProjectManagement/PublishingImages/AssignResourceRates.jpg" /><font class="ms-rteCustom-FigureNormal">Figure&#58; Assign resource rates</font> </li>
    <li>When you switch back to “Team System Task Sheet”, you will want to add the following fields so we can see the cost status;<br>
    &#160;&#160;a.&#160; Baseline Cost<br>
    &#160;&#160;b. Remaining Cost<br>
    &#160;&#160;c. Actual Cost <br>
    You will notice the “Remaining Cost” column has been calculated based on the “Remaining Work” column and the Rate we entered for each task. <br>
    <img alt="" class="ms-rteCustom-ImageArea" src="/Standards/Management/RulesToBetterProjectManagement/PublishingImages/CostColumn_Small.jpg" /><font class="ms-rteCustom-FigureNormal">Figure&#58; Showing the cost columns </font></li>
    <li>In order for MS Project to calculate and display a total cost for your current release you will need to add a summary task at the top level of the project tasks.<br>
    Choose the 1st task in your project, right click and create a “New Task” <br>
    <img alt="" class="ms-rteCustom-ImageArea" src="/Standards/Management/RulesToBetterProjectManagement/PublishingImages/SummaryTask.jpg" /><font class="ms-rteCustom-FigureNormal">Figure&#58; Create a summary task at the top</font> Name the task as per your release name so you know what this plan is for; also you don’t want this task to be created in your TFS as a work item because it’s just a summary, set “Publish and Refresh” as “No”. <br>
    <img alt="" class="ms-rteCustom-ImageArea" src="/Standards/Management/RulesToBetterProjectManagement/PublishingImages/NoPublishAndRefresh.jpg" /><font class="ms-rteCustom-FigureNormal">Figure&#58; Don’t publish and refresh this summary task</font> In order to make this a summary item you need to select all the other tasks and indent them. To achieve this click the little red forward arrow in the toolbar.<br>
    <img alt="" class="ms-rteCustom-ImageArea" src="/Standards/Management/RulesToBetterProjectManagement/PublishingImages/IndentTask_Small.jpg" /><font class="ms-rteCustom-FigureNormal">Figure&#58; Indent tasks</font> Now, your summary task is ready and it’s showing the total cost for your current release&#58; <img alt="" class="ms-rteCustom-ImageArea" src="/Standards/Management/RulesToBetterProjectManagement/PublishingImages/TotalCost_Small.jpg" /> <font class="ms-rteCustom-FigureNormal">Figure&#58; Total cost is calculated</font> </li>
</ol>
<p><strong>Baseline management&#58;</strong><br>
Baseline management is very important for every project manager as it helps you to determine the budget usage; once the client approves your initial estimate for the project it will become your baseline. So before you set a baseline in your MS Project, make sure the client approves it. </p>
<p>To set a baseline, choose “Tools, Tracking, Set Baseline” from the menu&#58; <img alt="" class="ms-rteCustom-ImageArea" src="/Standards/Management/RulesToBetterProjectManagement/PublishingImages/SetBaseline_Small.jpg" /><font class="ms-rteCustom-FigureNormal">Figure&#58; Set Baseline …</font><img alt="" class="ms-rteCustom-ImageArea" src="/Standards/Management/RulesToBetterProjectManagement/PublishingImages/ChooseBaseline.jpg" /><font class="ms-rteCustom-FigureNormal">Figure&#58; Choose “Baseline” and click ok</font></p>
<p>A handy feature of MS Project is its ability to handle multiple baselines. Use a new baseline to seek approval from clients when they alter the project scope. <br>
Once your baseline is set, you will be able to see the “Baseline Cost” column is showing $,<img alt="" class="ms-rteCustom-ImageArea" src="/Standards/Management/RulesToBetterProjectManagement/PublishingImages/BaselineCost_Small.jpg" /><font class="ms-rteCustom-FigureNormal">Figure&#58; Baseline Cost is showing $</font></p>
<p><strong>Track your project on the go</strong><br>
When your project is running, your developers will update the “Remaining Work” and “Completed Work” columns from TFS, they may not use MS Project so you will need to refresh your MS Project file to get these changes, and the $ will be calculated on the fly to give you up-to-date status.<br>
To refresh your project file, simply click on the “Refresh” button in the toolbar. <img alt="" class="ms-rteCustom-ImageArea" src="/Standards/Management/RulesToBetterProjectManagement/PublishingImages/RefreshProject.jpg" /><font class="ms-rteCustom-FigureNormal">Figure&#58; Click the “Refresh” button to update your project file.</font><img alt="" class="ms-rteCustom-ImageArea" src="/Standards/Management/RulesToBetterProjectManagement/PublishingImages/BudgetUsage_Small.jpg" /><font class="ms-rteCustom-FigureNormal">Figure&#58; Budget usage is calculated.</font> Note&#58; If you find that the values are not calculating properly, it may be that the calculation mode is set incorrectly. If pressing F9 updates the values you should change the setting “Tools | Options | Calculation” from “Manual” to “Automatic”.<br>
<img alt="" class="ms-rteCustom-ImageArea" src="/Standards/Management/RulesToBetterProjectManagement/PublishingImages/CalculationMode_Small.jpg" /><font class="ms-rteCustom-FigureNormal">Figure&#58; set the calculation mode to “Automatic”</font>Also make sure “Actual costs are always calculated by Microsoft Office Project” is enabled. </p>



