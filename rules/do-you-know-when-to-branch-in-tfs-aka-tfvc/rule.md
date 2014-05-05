---
type: rule
archivedreason: 
title: Do you know when to branch in TFS (aka TFVC)?
guid: aeeec9fa-6d78-4682-838d-091a3347ca28
uri: do-you-know-when-to-branch-in-tfs-aka-tfvc
created: 2013-12-06T17:54:34.0000000Z
authors:
- id: 24
  title: Adam Stephensen
related: []

---


<p>One of the most controversial issues we discuss is when to create branches.</p><p>Many smart people like creating braches e.g. 
   <a href="http&#58;//blog.hinshelwood.com/archive/2010/04/14/guidance-a-branching-strategy-for-scrum-teams.aspx"> 
      <span class="s2">http&#58;//blog.hinshelwood.com/archive/2010/04/14/guidance-a-branching-strategy-for-scrum-teams.aspx</span></a>.</p><p class="p2">As outlined by Martin Fowler in his article on <a href="http&#58;//martinfowler.com/bliki/FeatureBranch.html">Feature Branches</a>&#160;however, there are a number of issues related to merging that lead us to try and minimise the number of branches that we work with.</p>
<br><excerpt class='endintro'></excerpt><br>
<h3>Why we don’t like branching</h3>
<ol><li>Merging is painful, complex and is a time consuming task that does not add value.</li><li>Often regressions are introduced as merges are missed and not merged back to trunk</li><li>The longer branches are, the more people that have worked on them... the more unpleasant the merge is going to be.<br> Amount of pain = size of the change * the amount of work on the trunk in that period</li><li>The more you need to create a branch, the harder it is going to be to merge it back into the trunk!</li><li>Branching impedes refactoring.<br> If a am working on a branch and perform sweeping renaming, and a developer working on another branch does the same – merging is nearly impossible.<br> This is 
      <strong>very</strong> likely to happen on code bases that require tidying when you have developers who believe in improving code as they go (see the 
      <a href="http&#58;//www.ssw.com.au/ssw/standards/Rules/RulestoBetterCode.aspx#BoyscoutRule">Boy Scout Rule</a>)</li></ol><h3>When we *DO* branch</h3><ul><li>For a disposable, investigatory spike</li><li>Every time we release​</li></ul><dl class="badImage"><dt>
      <img src="/ALM/RulesToBetterBranchingAndBuilds/PublishingImages/branch-bad.jpg" alt="" />
   </dt><dd>Figure&#58; Bad Example – Creating a branch per feature leads to lots of merging (Image from<a href="http&#58;//paulhammant.com/blog/branch_by_abstraction.html"><span class="s2">http&#58;//paulhammant.com/blog/branch_by_abstraction.html</span></a>)</dd></dl><dl class="badImage"><dt>
      <img src="/ALM/RulesToBetterBranchingAndBuilds/PublishingImages/branch-bad-2.jpg" alt="" />
   </dt><dd>Figure&#58; Bad Example – Creating a branch per sprint has everyone working on the same code but requires at least one merge every sprint</dd></dl><dl class="goodImage"><dt>
      <img src="/ALM/RulesToBetterBranchingAndBuilds/PublishingImages/branch-good.jpg" alt="" />
   </dt><dd>Figure&#58; Good Example&#58; Release Branching - always develop on the trunk, but create a new branch each time you release.&#160;<br>This means th​at all developers are continually integrating all their code, branching is rare, but you always have access to your released version in case bug fixes or small mods are required.<br>(Image from&#160;<a href="http&#58;//paulhammant.com/blog/branch_by_abstraction.html"><span class="s2">http&#58;//paulhammant.com/blog/branch_by_abstraction.html</span></a>)</dd></dl><p>Further reading&#58;</p><ul><li>
      <a href="http&#58;//continuousdelivery.com/2011/05/make-large-scale-changes-incrementally-with-branch-by-abstraction/">http&#58;//continuousdelivery.com/2011/05/make-large-scale-changes-incrementally-with-branch-by-abstraction/</a></li><li>
      <a href="http&#58;//paulhammant.com/blog/branch_by_abstraction.html">http&#58;//paulhammant.com/blog/branch_by_abstraction.html</a></li><li>
      <a href="http&#58;//martinfowler.com/bliki/FeatureBranch.html">http&#58;//martinfowler.com/bliki/FeatureBranch.html</a></li><li>
      <a href="http&#58;//martinfowler.com/bliki/SemanticConflict.html">http&#58;//martinfowler.com/bliki/SemanticConflict.html</a></li></ul>


