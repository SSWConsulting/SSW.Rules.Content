---
type: rule
title: Do you use the best Code Analysis tools?
uri: do-you-use-the-best-code-analysis-tools
created: 2012-03-16T08:43:44.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 23
  title: Damian Brady
- id: 3
  title: Eric Phan

---



<span class='intro'> <p></p><p>Whenever you are writing code, you should always make sure it conforms to&#160;your team's&#160;standards. If everyone is following the same set of rules; someone else’s code will look more familiar and more like your code - ultimately easier to work with.</p><p>No matter how good a coder you are, you will always miss things from time to time, so it's a really good idea to have a tool that automatically scans your code and reports on what you need to change in order to improve it.</p>
<p>Visual Studio has a great Code Analysis tool to help you look for problems in your code. Combine this with Jetbrains' ReSharper and your code will be smell free.</p><p>The levels of protection are&#58;</p> </span>

<dl class="image"><dt> 
      <img alt="CricketHelmet.jpg" src="CricketHelmet.jpg" /> 
      <br> 
   </dt><dd>Figure&#58; You wouldn't play cricket without protective gear and you shouldn't code without protective tools </dd></dl><h3>Level 1</h3><p>Get ReSharper to green on each file you touch. You want the files you work on to be left better than when you started. See 
   <a href="http&#58;//www.ssw.com.au/ssw/standards/rules/RulestoBetterCode.aspx#BoyscoutRule">Do you follow the boyscout rule?</a></p><p> 
   <strong>Tip&#58;</strong> You can run through a file and tidy it very quickly if you know two great keyboard shortcuts&#58;</p><ul><li>Alt + [Page Down/Page Up] &#58; Next/Previous Resharper Error / Warning</li><li>Alt + Enter&#58; Smart refactoring suggestions</li></ul><dl class="image"><dt> 
      <img alt="Image 01" src="48bc81_image001.png" style="width&#58;750px;" /> 
   </dt><dd> Figure&#58; ReSharper will show Orange when it detects that there is code that could be improved</dd></dl><dl class="image"><dt> 
      <img alt="image002.png" src="image002.png" style="width&#58;750px;" /> 
   </dt><dd> Figure&#58; ReSharper will show green when all code is tidy</dd></dl><h3>Level 2</h3><p>Is to use 
   <a href="http&#58;//www.ssw.com.au/ssw/CodeAuditor/Default.aspx">Code Auditor.</a></p><dl class="image"><dt> 
      <img class="ms-rteCustom-ImageArea" alt="stylecop.png" src="CodeAuditor.png" style="width&#58;750px;" /> 
   </dt><dd>Figure&#58; Code Auditor shows a lot of warnings in this test project</dd></dl><p> 
   <strong>Note&#58;</strong> Document any rules you've turned off.</p><h3>Level 3</h3><p>Is to use 
   <a href="http&#58;//www.ssw.com.au/ssw/LinkAuditor/">Link Auditor</a>.</p><p> 
   <strong>Note&#58;</strong> Document any rules you've turned off.</p><h3 class="ssw15-rteElement-H3">Level 4</h3><p>Is to use StyleCop&#160;to check that your code has consistent style and formatting.</p><dl class="image"><dt> 
      <img alt="stylecop.png" src="StyleCopInVS2010.png" style="width&#58;750px;" /> 
   </dt><dd>Figure&#58;&#160;StyleCop&#160;shows a lot of warnings in this test project</dd></dl><h3>Level 5</h3><p>Run Code Analysis (was FxCop) with the default settings or ReSharper with Code Analysis turned on</p><dl class="image"><dt> 
      <img alt="runcodeanalysisvs11.png" src="CodeAnalysisVS11.png" /> 
   </dt><dd>Figure&#58;&#160;Run&#160;Code Analysis&#160;in Visual Studio<br></dd></dl><dl class="image"><dt> 
      <img alt="Code Analysis" src="codeanalysis.png" /> 
   </dt><dd>Figure&#58; The&#160;Code Analysis results indicate there are 17 items that need fixing</dd></dl><h3>Level 6</h3><p>Ratchet up your Code Analysis Rules until you get to 'Microsoft All Rules'</p><dl class="image"><dt> 
      <img alt="image003.png" src="image003.png" /> 
   </dt><dd>Figure&#58; Start with the Minimum Recommended Rules, and then ratched up.</dd></dl><h3>Level 7</h3><p>Is to document any rules you've turned off.</p><p>All of these rules allow you to disable rules that you're not concerned about.&#160; There's nothing wrong with&#160;disabling rules you don't want checked, but you should make it clear to developers why those rules were removed.</p><p>Create a 
   <b>GlobalSuppressions.cs</b> file in your project with the rules that have been turned off and why.<br></p><dl class="image"><dt><img src="suppressions-file.png" alt="suppressions-file.png" style="width&#58;750px;" /></dt><dd>Figure&#58; The suppressions file tells Code Analysis which rules it should disable for specific code blocks</dd></dl>
<p class="ssw15-rteElement-GreyBox">
   <b>More Information&#58;</b>&#160;<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=d6d34c31-ac6a-49a4-876a-f9d30e1ab78a">Do you make instructions at the beginning of a project and improve them gradually?</a>&#160;and 
   <a href="https&#58;//docs.microsoft.com/en-us/visualstudio/code-quality/in-source-suppression-overview">https&#58;//docs.microsoft.com/en-us/visualstudio/code-quality/in-source-suppression-overview</a><br></p>&#160;
<h3 class="ssw15-rteElement-H3">Level 8</h3><div>The gold standard is to use 
   <a href="https&#58;//www.sonarqube.org/" target="_blank">SonarQube</a>, which gives you the code analysis that the previous levels give you as wells as the ability to analyze technical debt and to see which code changes had the most impact to technical debt</div><dl class="image"><dt> 
      <img src="2016-06-08_12-59-38.png" alt="2016-06-08_12-59-38.png" style="width&#58;750px;" /> 
   </dt><dd> Figure&#58;&#160; SonarQube workflow with Visual Studio and Azure DevOps​<br></dd></dl><dl class="image"><dt> 
      <img src="2016-06-08_12-59-53.png" alt="2016-06-08_12-59-53.png" />  
   </dt><dd> Figure&#58; SonarQube gives you the changes in code analysis results between each check-in<br><br><br></dd></dl>


