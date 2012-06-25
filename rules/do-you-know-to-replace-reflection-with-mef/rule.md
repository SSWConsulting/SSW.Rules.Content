---
type: rule
title: Do you know to replace reflection with MEF?
uri: do-you-know-to-replace-reflection-with-mef
created: 2012-03-21T01:47:46.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 23
  title: Damian Brady

---



<span class='intro'> <p>Reflection code is often used to implement a &quot;plugin&quot; architecture where components are loaded at runtime rather than referenced directly in the code. This is done instead of statically referencing classes to make the solution more flexible.</p>
 </span>

<p>The Managed Extensibility Framework (MEF) is an Inversion of Control (IoC)&#160;framework build on Reflection that simplifies and standardises this plugin methodology.</p>
<p><a title="You don’t need an IoC container or ServiceLocator for everything" href="http&#58;//blogs.clariusconsulting.net/kzu/you-dont-need-an-ioc-or-servicelocator-for-everything/" rel="bookmark">You don't need an IoC container or ServiceLocator for everything</a>, but an IoC container WILL help if you have complex dependency graphs to instantiate (in your default constructor) or you have truly pluggable components.&#160; For example, if you want to allow a component to be picked up automatically at runtime from some&#160;assembly if it’s in a folder.</p>
<p>Any existing Reflection code should be examined to see whether&#58; </p>
<ol>
<li>It needs reflection at all - can the component be directly referenced? OR</li>
<li>Can the pure reflection code be simplified with MEF?</li>
</ol>
<p>[TODO - Damian&#58;&#160;Bad example - using reflection]</p>
<p>[TODO - Damian Good Example - using MEF]</p>


