---
type: rule
archivedreason: 
title: Do you know the minimum builds to create for your project?
guid: 1314cede-0e06-4fd7-8668-e75ed103fcdb
uri: do-you-know-the-minimum-builds-to-create-for-your-project
created: 2011-11-18T03:52:49.0000000Z
authors:
- id: 22
  title: David Klein
- id: 6
  title: Tristan Kurniawan
- id: 17
  title: Ryan Tee
- id: 5
  title: Justin King
- id: 23
  title: Damian Brady
related: []

---


<p>When creating projects one of the only ways that you have of proving that it works and is a viable solution is to build it. This is easy when you only have one developer and that developer will be the only one using a solution. But what if you have 2 developers? How do you prove that one developer's code works with the other? The answer is build servers. These build servers take specific code away to another computer and build it there.</p>
<p>You should always have two builds on your team project. These should be setup and tested using an empty solution before you write any code at all.</p>
<br><excerpt class='endintro'></excerpt><br>
<img class="ms-rteCustom-ImageArea" src="/TFS/RulesToBetterVersionControlwithTFS(AKASourceControl)/PublishingImages/Builds.jpg" alt="" />&#160;<font class="ms-rteCustom-FigureNormal" size="+0">Figure&#58; Two builds named in the format [TeamProject].[AreaPath]_[Branch].|CI|Nightly] for every branch.</font> These builds should use the same XAML build workflow; however you may set them up to run a different set of tests depending on the time it takes to run a full build. 
<br>
<ul><li></li><li>
      <strong>CI</strong> - This should run all Unit Tests and all of the automated UI tests. It is run after a successful developer check-in.<br><strong>Note&#58;</strong> This build should take no more than 10 minutes to run.<br></li><li>
      <strong>Nightly</strong> - The Nightly build should run all of the Unit Tests, all of the Automated UI tests and all of the Load and Performance tests. The nightly build is time consuming and will run but once a night. Packaging of your Product for testing the next day may be done at this stage as well.<br><strong>Note&#58;</strong> This build can take as long as it needs to - of course more than 24 hours is too long.</li></ul><p><strong>Important&#58; </strong>Gate Builds are bad! Some people believe in having a build that stops developers checking in code unless the build succeeds. See our rule on <a href="/Management/RulesToBetterScrumUsingTFS/Pages/Gated-Checkins-Mask-Dysfunction.aspx">Do You Know That Gated Checkins Mask Dysfunction?</a></p> 
<img class="ms-rteCustom-ImageArea" src="/TFS/RulesToBetterVersionControlwithTFS(AKASourceControl)/PublishingImages/ControlTestAndData.jpg" alt="" /> 
<font class="ms-rteCustom-FigureNormal" size="+0">Figure&#58; You can control what tests are run and what data is collected while they are running.</font> Note&#58; We do not run all the tests every time because of the time consuming nature of running some tests, but ALL tests should be run overnight. 
<br>Note&#58; If you had a really large project with thousands of tests including long running Load tests you may need to add a Weekly build to the mix. 
<br>
<img class="ms-rteCustom-ImageArea" src="/TFS/RulesToBetterVersionControlwithTFS(AKASourceControl)/PublishingImages/BuildStatus01.jpg" alt="" />&#160;<font class="ms-rteCustom-FigureBad" size="+0">Figure&#58; Bad example, you can't tell what these builds do if they are in a larger list </font>
<img class="ms-rteCustom-ImageArea" src="/TFS/RulesToBetterVersionControlwithTFS(AKASourceControl)/PublishingImages/BuildStatus02.jpg" alt="" />
<font class="ms-rteCustom-FigureGood" size="+0">Figure&#58; Good example, you know exactly what project, branch and type of build these are for. </font>


