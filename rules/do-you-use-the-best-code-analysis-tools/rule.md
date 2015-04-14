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



<span class='intro'> ​​Whenever you are writing code, you should always make sure it conforms to&#160;your team's&#160;standards.&#160;The more pain a developer has when trying to check in, the better, because&#160;there will be less left up to testers to find.​<div><br>&#160;</div><div>​​<span style="line-height&#58;20.79px;">No matter how good a coder you are, you will always miss some of them some of the time, so it's a really good idea to have a tool that automatically scans your code and reports on what you need to change in order to improve it.</span>​<br></div><div><br>&#160;</div><p>Visual Studio has a great Code Analysis tool to help you look for problems in your code. Combine this with Jetbrain's ReSharper and your code will be smell free.​</p><p>The levels of protection are&#58;</p>
 </span>

<div><p class="ssw15-rteElement-GreyBox">​​​<img alt="CricketHelmet.jpg" src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/CricketHelmet.jpg" style="margin&#58;5px;width&#58;594px;" /><br></p></div><div><dd class="ssw15-rteElement-FigureNormal">Figure&#58; You wouldn't play cricket without protective gear and you shouldn't code without protective tools​<br></dd></div><div><h3 class="ssw15-rteElement-H3">Level 1</h3><p>Get ReSharper to green on each file you touch.&#160;<span style="line-height&#58;1.6;">You want the files you work on to be left better than when you started. See&#160;</span><a href="http&#58;//www.ssw.com.au/ssw/standards/rules/RulestoBetterCode.aspx#BoyscoutRule" style="line-height&#58;1.6;">Do you follow the boyscout rule?</a>&#160;</p><p><strong style="line-height&#58;1.6;">Tip</strong><span style="line-height&#58;1.6;">&#58; You can run through a file and tidy it very quickly if you know two great keyboard shortcuts&#58;</span></p><ul><li>Alt + [Page Down/Page Up] &#58; Next/Previous Resharper Error / Warning</li><li>Alt + Enter&#58; Smart refactoring suggestions</li></ul><img class="ms-rteCustom-ImageArea" alt="Image 01" src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/image001.png" style="margin&#58;5px;width&#58;600px;" /><br><span class="ssw-rteStyle-FigureNormal">​Figure&#58; ReSharper will show Orange when it detects that there is code that could be improved</span><img class="ms-rteCustom-ImageArea" alt="image002.png" src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/image002.png" style="margin&#58;5px;width&#58;600px;" /><span class="ssw-rteStyle-FigureNormal">​Figure&#58; ReSharper will show green when all code is tidy</span><h3 class="ssw15-rteElement-H3">Level 2</h3><p>Is to use <a href="http&#58;//www.ssw.com.au/ssw/CodeAuditor/Default.aspx"><span style="text-decoration&#58;underline;"><font color="#0066cc">Code Auditor.</font></span></a></p><p><img class="ms-rteCustom-ImageArea" alt="stylecop.png" src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/SiteAssets/Pages/DoYouDoCodeAnalysis/CodeAuditor.png" style="margin&#58;5px;width&#58;632px;" />&#160;<strong style="line-height&#58;1.6;font-size&#58;12px;">Figure&#58;&#160;Code Auditor shows a lot of warnings in this test project</strong></p><p><strong>Note&#58;</strong> Document any rules you've turned off.</p><h3 class="ssw15-rteElement-H3">Level 3</h3><p>Is to use <a href="http&#58;//www.ssw.com.au/ssw/LinkAuditor/">Link Auditor</a>.</p><p><strong>Note&#58;</strong> Document any rules you've turned off.</p><h3 class="ssw15-rteElement-H3">Level 4</h3><p>Is to use&#160; <img title="You are now leaving SSW" src="/Style%20Library/SSW/CoreImages/external.gif" alt="" /> StyleCop&#160;to check that your code has consistent style and formatting.</p><img class="ms-rteCustom-ImageArea" alt="stylecop.png" src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/StyleCopInVS2010.png" style="margin&#58;5px;width&#58;650px;" /> <span class="ssw-rteStyle-FigureNormal">Figure&#58;&#160;StyleCop&#160;shows a lot of warnings in this test project</span><h3 class="ssw15-rteElement-H3">Level 5</h3><p>Run Code Analysis (was FxCop) with the default settings</p><img class="ms-rteCustom-ImageArea" alt="runcodeanalysisvs11.png" src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/CodeAnalysisVS11.png" style="margin&#58;5px;" /><span class="ssw-rteStyle-FigureNormal">Figure&#58;&#160;Run&#160;Code Analysis&#160;in VS2015</span></div><p>&#160;</p><img class="ms-rteCustom-ImageArea" alt="Code Analysis" src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/codeanalysis.png" />
<span class="ssw-rteStyle-FigureNormal">Figure&#58; The&#160;Code Analysis results indicate there are 17 items that need fixing</span>
<h3 class="ssw15-rteElement-H3">Level 6</h3>
<p>Ratchet up your Code Analysis Rules until you get to 'Microsoft All Rules'</p>
<img class="ms-rteCustom-ImageArea" alt="image003.png" src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/image003.png" />
<span class="ssw-rteStyle-FigureNormal">Figure&#58; Start with the Minimum Recommended Rules, and then ratched up.</span>
<h3 class="ssw15-rteElement-H3">Level 7</h3>
<p>Is to document any rules you've turned off.</p>
<p>All of these rules allow you to disable rules that you're not concerned about.&#160; There's nothing wrong with&#160;disabling rules you don't want checked, but you should make it clear to developers why those rules were removed.</p>
<p>Create an <strong>_InstructionsCodeAnalysis.doc </strong>document in your solution with the rules that have been turned off and why.</p>
<div class="ssw-rteStyle-YellowBorderBox">More Information&#58;&#160;<a href="/SoftwareDevelopment/RulesToBetterDotNETProjects/Pages/DoYouMakeInstructions.aspx">Do you make instructions at the beginning of a project and improve them gradually?​​</a></div>
<img class="ms-rteCustom-ImageArea" alt="stylecop_removed_rules.png" src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/StyleCopRemovedRules.png" />
<span class="ssw-rteStyle-FigureNormal">Figure&#58; The document _InstructionsCodeAnalysis.doc shows that there were 3 StyleCop rules disabled.</span>
<div class="ssw-rteStyle-GreyBox"><p>Suggestion to MS&#58; Allow developers to put a comment against any disabled rule when you turn&#160;it off</p>
TODO - Damian&#58; Add image</div>
<div><p class="ssw15-rteElement-P">​​​​<br></p></div>


