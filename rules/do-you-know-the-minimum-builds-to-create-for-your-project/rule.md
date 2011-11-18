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


This field should not be null (Remove me when you edit this field).
<br><excerpt class='endintro'></excerpt><br>

  <img alt="" class="ms-rteCustom-ImageArea" src="/TFS/RulesToBetterVersionControlwithTFS(AKASourceControl)/PublishingImages/Builds.jpg" />&#160;<font class="ms-rteCustom-FigureNormal" size="+0">Figure&#58; Three builds named in the format [TeamProject].[AreaPath]_[Branch].[Gate|CI|Nightly] for every branch.</font> These builds should use the same XAML build workflow; however you may set them up to run a different set of tests depending on the time it takes to run a full build. <br>
<ul>
    <li><strong>Gate</strong> - Only needs to run the smallest set of tests, but should run most if not all of the Unit Test. This is run before developers are allowed to check-in </li>
    <li><strong>CI</strong> - This should run all Unit Tests and all of the automated UI tests. It is run after a developer check-in. </li>
    <li><strong>Nightly</strong> - The Nightly build should run all of the Unit Tests, all of the Automated UI tests and all of the Load and Performance tests. The nightly build is time consuming and will run but once a night. Packaging of your Product for testing the next day may be done at this stage as well.</li>
</ul>
<img alt="" class="ms-rteCustom-ImageArea" src="/TFS/RulesToBetterVersionControlwithTFS(AKASourceControl)/PublishingImages/ControlTestAndData.jpg" /> <font class="ms-rteCustom-FigureNormal" size="+0">Figure&#58; You can control what tests are run and what data is collected while they are running.</font> Note&#58; We do not run all the tests every time because of the time consuming nature of running some tests, but ALL tests should be run overnight. <br>
Note&#58; If you had a really large project with thousands of tests including long running Load tests you may need to add a Weekly build to the mix. <br>
<img alt="" class="ms-rteCustom-ImageArea" src="/TFS/RulesToBetterVersionControlwithTFS(AKASourceControl)/PublishingImages/BuildStatus01.jpg" />&#160;<font class="ms-rteCustom-FigureBad" size="+0">Figure&#58; Bad example, you can't tell what these builds do if they are in a larger list </font><img alt="" class="ms-rteCustom-ImageArea" src="/TFS/RulesToBetterVersionControlwithTFS(AKASourceControl)/PublishingImages/BuildStatus02.jpg" /><font class="ms-rteCustom-FigureGood" size="+0">Figure&#58; Good example, you know exactly what project, branch and type of build these are for. </font>



