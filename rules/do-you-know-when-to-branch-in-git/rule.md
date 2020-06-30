---
type: rule
title: Do you know when to branch in git?
uri: do-you-know-when-to-branch-in-git
created: 2016-01-19T22:38:55.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 3
  title: Eric Phan
- id: 46
  title: Danijel Malik
- id: 68
  title: Edgar Rocha
- id: 72
  title: Gabriel George

---



<span class='intro'> <dl class="image"><dt>​ <img src="finishing-a-feature-with-world-class-flow.jpg" alt="" />  </dt><dd>Note&#58; This rule applies&#160;to git. For branching advice in TFVC, see&#160;<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=cd330379-4568-45fa-bd68-7229044697b7">Do you know when to branch in TFVC?</a></dd></dl><p>The best way to handle continuous development and deployment is following <a href="https&#58;//guides.github.com/introduction/flow/">GitHub Flow</a>. The basic idea is to always deploy from <strong> master</strong>, and to create a feature branch for every feature. When the feature is complete, it is merged back to master via a pull request, which provides a trigger for other developers to build.</p><p>Using this strategy, <strong> master </strong>is always production-ready and deployable.</p> </span>

<div class="ms-rtestate-read ms-rte-embedcode ms-rte-embedil ms-rtestate-notify"> 
   <iframe width="853" height="480" src="https&#58;//www.youtube.com/embed/9bP4-ly2qtQ?rel=0" frameborder="0"></iframe>&#160;</div><div></div><dl class="badImage"><dt>
      <img src="commit-master-bad.jpg" alt="commit-master-bad.jpg" />
   </dt><dd>Figure&#58; Bad example - Committing to master</dd></dl><dl class="goodImage"><dt>
      <img src="commit-branch-good.jpg" alt="commit-branch-good.jpg" />
   </dt><dd> Figure&#58; Good example - Committing to a new branch<br></dd></dl><dl class="image"><dt>
      <img src="github-flow.jpg" alt="github-flow.jpg" />
   </dt><dd>Figure&#58; Great diagram from 
      <a href="https&#58;//guides.github.com/pdfs/githubflow-online.pdf">GitHub</a>&#160;</dd></dl><h3>The process</h3><h3 class="ssw15-rteElement-H3">#assumption​<br></h3><p>
   <b>Set up build system to deploy from the master branch </b></p><p>Your build systems should always deploy from master, and should automatically deploy on every commit to master.<br>Since master is always being deployed, it must always be in a deployable state.</p><h3>1) Create a branch</h3><p> 
   <b>a) Create a &quot;feature branch&quot; for every&#160;PBI</b></p><p>When starting a PBI from the task board, create a branch from 
   <b> master</b> with a&#160;descriptive name for that feature.</p><dl class="badImage"><dt> 
      <img alt="git branch start-stuff" src="BadBranchName.png" data-pin-nopin="true" /> 
   </dt><dd>Figure&#58; Bad example - Branch name is not descriptive</dd></dl><dl class="goodImage"><dt> 
      <img alt="git branch create-basic-web-application" src="GoodBranchName.png" data-pin-nopin="true" /> 
   </dt><dd> Figure&#58; Good Example - Branch name describes the intent of the change</dd></dl><p> 
   <strong>It is critical that this branch always comes off master, not another feature branch. Master is the only branch that is mandated to be in a deployable state, so any other option is unsafe.</strong></p><p>Obviously, we're creating a lot of branches and merging a lot under this strategy - and that's ok. &#160;Be sure to keep your PBIs small (as per&#160;<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=2e446681-6eff-4cec-b955-e530edc4cdc8">do you break large tasks into smaller tasks</a>), and you will not have much merge pain.</p><p>The benefit of creating feature branches is to reduce the number of conflicts and churn of unfinished code during development of a feature. &#160;It allows features to be developed independently of each other and reduces the amount of expensive &quot;pull latest from the server, and rebuild everything&quot; operations, as well as greatly limiting the impact of commits with unfinished code.</p><p class="ssw15-rteElement-P"> 
   <b>b) Code away and complete the PBI</b><br></p><p class="ssw15-rteElement-P"> 
   <b>c) Create a commit - it will contain your changed files on your local PC&#160;</b></p><p>While working, commit frequently to this branch with nice, descriptive messages. For example, &quot;Added a field to hold the product category to our timesheet read model&quot; and &quot;added a column to the timesheet summary UI for the product category&quot;.</p><dl class="badImage"><dt> 
      <img alt="git commit -m &quot;Started report change&quot;" src="BadCommitMessage.png" data-pin-nopin="true" /> 
   </dt><dd>Figure&#58; Bad Example - Commit message does not describe what was changed</dd></dl><dl class="goodImage"><dt> 
      <img alt="GoodCommitMessage.png" src="GoodCommitMessage.png" data-pin-nopin="true" /> 
   </dt><dd>Figure&#58; Good Example - Commit message describes exactly what was changed.&#160;<br></dd></dl><p class="ssw15-rteElement-P"> 
   <b>d) Push your changes to your remote Feature Branch </b></p><h3>2) Open a pull request (to merge from your current branch to the master)<br></h3><p>When the change is complete, or when you want feedback on anything, open a pull request to merge the branch back to 
   <strong> master</strong>. The pull request is more than just a request to merge, it is a request to have someone review the code and architecture, and to discuss any issues. &#160;Resolve these issues with more commits in the branch before continuing.</p><p>Tip&#58; A best practice is to have another developer review your work and then approve.<br></p><p class="ssw15-rteElement-GreyBox">It is easy to chalk this step up as busy-work, but it is one of the most valuable parts of the strategy<br></p><h3 class="ssw15-rteElement-H3">#assumption<br></h3><p>Deploy the changes to a staging environment. &#160;This allows the features to be tested before being merged to 
   <strong>master</strong>.</p><p class="ssw15-rteElement-InfoBox">Some prefer to move this step&#160;to after the merge, especially when using a release management tool like VSTS Release or Octopus Deploy (see 
   <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=e2608875-5b0b-4215-bee8-8ffd966dc972">Do you use the best deployment tool</a>). &#160;If you decide to go this route, remember that 
   <strong>master</strong> should remain deployable and production ready at all times and that all branches come from 
   <b> master</b>. &#160;If skipping this step,&#160;ensure that you have CI on your feature&#160;branch to ensure that your branch compiles and passes all tests before merging. 
   <br></p><h3>3) Merge and Deploy (to master)<br></h3><p>Once everyone is happy and everything is tested, complete the pull request, which will merge back to 
   <strong> master</strong>. Ensure you are not using the &quot;Fast Forward&quot; merge option (git), or details about the branch will be lost - it will appear as though all work was done in 
   <strong>master</strong>. Being able to see the feature branches in the git log is very useful.&#160;</p><dl class="goodImage"><dt> 
      <img alt="GoodGitHistory.png" src="GoodGitHistory.png" /> 
   </dt><dd>Figure&#58; Good Example - Each change is well described, small&#160;and in its own feature branch.</dd></dl><p class="ssw15-rteElement-P">
    After you completed the pull request, make sure you also delete the branch
    that you made the pull request of. Deleting your completed branch will not just help yourself in the long run, but also everyone else. Having too many branches especially a stale one will confuse developers on what &quot;may&quot; be in progress, moreover it would cause so much pain to the future developer when they have to do a clean-up and the branch author has left.<br>
</p><dl class="badImage">
    <img src="bad-figure-stale-branches2.png" alt="bad-figure-stale-branches2.png" style="margin&#58;5px;width&#58;808px;" />
    <br>
    <p></p><dd class="ssw15-rteElement-FigureBad">
        Figure&#58; Bad Example - Lots of stale branches that could cause confusion or potentially take a long time to resolve conflicts when merging​<br>
    </dd></dl><p class="ssw15-rteElement-P">
    Otherwise, you can do it before you complete the pull request by ticking
    delete branch option.<br>
</p><dl class="goodImage">

    <img src="delete%20branch%20in%20devops.png" alt="delete branch in devops.png" style="margin&#58;5px;" />&#160;
    <p></p><dd class="ssw15-rteElement-FigureGood">
        ​​Figure&#58; Good Example - Automatically delete the branch after the pull
        request completion in Azure Devops<br>
    </dd></dl><dl class="goodImage">
    ​​​​​<img src="github%20settings.png" alt="github settings.png" style="margin&#58;5px;width&#58;808px;" />
    <dd class="ssw15-rteElement-FigureGood">
        ​​Figure&#58; Good Example - Set the whole project to auto-delete branch after
        merging in GitHub<br>
    </dd></dl>​
<p class="ssw15-rteElement-GreyBox">Once merged, 
   <b> master</b> should immediately and automatically be deployed (in a perfect world,&#160;to production).</p>


