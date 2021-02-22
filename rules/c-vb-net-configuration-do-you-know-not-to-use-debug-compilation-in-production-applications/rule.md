---
type: rule
archivedreason: 
title: C#/VB.NET Configuration - Do you know not to use debug compilation in production applications?
guid: b50ed5b1-e954-4b6c-bc92-f159228150dc
uri: c-vb-net-configuration-do-you-know-not-to-use-debug-compilation-in-production-applications
created: 2013-01-11T18:25:53.0000000Z
authors: []
related: []
redirects: []

---


<p>​Debug compilation considerably increases memory footprint since debug symbols are required to be loaded. </p>
<p>Additionally it will hit the performance because that will include the optional debug and trace statements in the output IL code.</p>

<br><excerpt class='endintro'></excerpt><br>
<p>In debug mode the compiler emits debug symbols for all variables and compiles the code as is. In release mode some optimizations are included:</p><ul><li>unused variables do not get compiled at all</li><li>some loop variables are taken out of the loop by the compiler if they are proven to be invariants</li><li>code written under #debug directive is not included etc.</li></ul><p>The rest is up to the JIT.</p><p>As per: 
   <a target="_blank" href="http://stackoverflow.com/questions/2446027/c-sharp-debug-vs-release-performance">C# debug vs release performance</a>.</p><dl class="badImage"><dt>
      <img src="debug-bad.jpg" alt="" />
   </dt><dd>Figure: Bad Example</dd></dl><dl class="goodImage"><dt>
      <img src="debug-good.jpg" alt="" />
   </dt><dd>Figure: Good Example</dd></dl>
<p class="ssw15-rteElement-YellowBorderBox"><span style="font-size:12px;line-height:19px;">We have a program called </span><a href="http://www.ssw.com.au/ssw/CodeAuditor" style="font-size:12px;line-height:19px;">SSW Code Auditor</a><span style="font-size:12px;line-height:19px;"> to check for this rule.​</span>​</p>


