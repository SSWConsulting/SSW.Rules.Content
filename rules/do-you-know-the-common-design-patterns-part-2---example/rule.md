---
type: rule
title: Do you know the common Design Patterns? (Part 2 - Example)
uri: do-you-know-the-common-design-patterns-part-2---example
created: 2012-03-20T02:29:38.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 23
  title: Damian Brady
- id: 24
  title: Adam Stephensen
- id: 3
  title: Eric Phan

---



<span class='intro'> <div><span>“Only add complexity 
when you need flexibility” – Marcel de Vries</span></div> </span>

​<div><span>[eg. Bad example - code showing NOT using dependency 
injection]</span></div>
<div><span>[eg. Good example - code showing using dependency 
injection]</span></div>
<div><span>about overuse of patterns​</span></div>
<div><span>1.principles v.s. design patterns</span></div>
<table border="1" cellspacing="0" style="border-top-style&#58;solid;border-right-style&#58;solid;border-bottom-style&#58;solid;border-left-style&#58;solid;border-width&#58;initial;background-image&#58;initial;background-attachment&#58;initial;margin-top&#58;0px;margin-right&#58;0px;margin-bottom&#58;0px;margin-left&#58;0px;padding-top&#58;0px;padding-right&#58;0px;padding-bottom&#58;0px;padding-left&#58;0px;border-top-width&#58;1px;border-right-width&#58;0px;border-bottom-width&#58;0px;border-left-width&#58;1px;font-family&#58;'lucida grande', 'bitstream vera sans', 'trebuchet ms', verdana, tahoma, arial, sans-serif;font-size&#58;13px;line-height&#58;normal;text-align&#58;-webkit-auto;"><tbody><tr><td style="border-top-style&#58;solid;border-right-style&#58;solid;border-bottom-style&#58;solid;border-left-style&#58;solid;border-width&#58;initial;border-top-width&#58;0px;border-right-width&#58;1px;border-bottom-width&#58;1px;border-left-width&#58;0px;padding-top&#58;5px;padding-right&#58;5px;padding-bottom&#58;5px;padding-left&#58;5px;"><b>SRP</b></td>
<td style="border-top-style&#58;solid;border-right-style&#58;solid;border-bottom-style&#58;solid;border-left-style&#58;solid;border-width&#58;initial;border-top-width&#58;0px;border-right-width&#58;1px;border-bottom-width&#58;1px;border-left-width&#58;0px;padding-top&#58;5px;padding-right&#58;5px;padding-bottom&#58;5px;padding-left&#58;5px;"><a href="http&#58;//www.objectmentor.com/resources/articles/srp.pdf" style="background-image&#58;initial;background-attachment&#58;initial;background-color&#58;transparent;">The Single Responsibility Principle</a></td>
<td style="border-top-style&#58;solid;border-right-style&#58;solid;border-bottom-style&#58;solid;border-left-style&#58;solid;border-width&#58;initial;border-top-width&#58;0px;border-right-width&#58;1px;border-bottom-width&#58;1px;border-left-width&#58;0px;padding-top&#58;5px;padding-right&#58;5px;padding-bottom&#58;5px;padding-left&#58;5px;"><i>A class should have one, and only one, reason to change.</i></td></tr>
<tr><td style="border-top-style&#58;solid;border-right-style&#58;solid;border-bottom-style&#58;solid;border-left-style&#58;solid;border-width&#58;initial;border-top-width&#58;0px;border-right-width&#58;1px;border-bottom-width&#58;1px;border-left-width&#58;0px;padding-top&#58;5px;padding-right&#58;5px;padding-bottom&#58;5px;padding-left&#58;5px;"><b>OCP</b></td>
<td style="border-top-style&#58;solid;border-right-style&#58;solid;border-bottom-style&#58;solid;border-left-style&#58;solid;border-width&#58;initial;border-top-width&#58;0px;border-right-width&#58;1px;border-bottom-width&#58;1px;border-left-width&#58;0px;padding-top&#58;5px;padding-right&#58;5px;padding-bottom&#58;5px;padding-left&#58;5px;"><a href="http&#58;//www.objectmentor.com/resources/articles/ocp.pdf" style="background-image&#58;initial;background-attachment&#58;initial;background-color&#58;transparent;">The Open Closed Principle</a></td>
<td style="border-top-style&#58;solid;border-right-style&#58;solid;border-bottom-style&#58;solid;border-left-style&#58;solid;border-width&#58;initial;border-top-width&#58;0px;border-right-width&#58;1px;border-bottom-width&#58;1px;border-left-width&#58;0px;padding-top&#58;5px;padding-right&#58;5px;padding-bottom&#58;5px;padding-left&#58;5px;"><i>You should be able to extend a classes behavior, without modifying it.</i></td></tr>
<tr><td style="border-top-style&#58;solid;border-right-style&#58;solid;border-bottom-style&#58;solid;border-left-style&#58;solid;border-width&#58;initial;border-top-width&#58;0px;border-right-width&#58;1px;border-bottom-width&#58;1px;border-left-width&#58;0px;padding-top&#58;5px;padding-right&#58;5px;padding-bottom&#58;5px;padding-left&#58;5px;"><b>LSP</b></td>
<td style="border-top-style&#58;solid;border-right-style&#58;solid;border-bottom-style&#58;solid;border-left-style&#58;solid;border-width&#58;initial;border-top-width&#58;0px;border-right-width&#58;1px;border-bottom-width&#58;1px;border-left-width&#58;0px;padding-top&#58;5px;padding-right&#58;5px;padding-bottom&#58;5px;padding-left&#58;5px;"><a href="http&#58;//www.objectmentor.com/resources/articles/lsp.pdf" style="background-image&#58;initial;background-attachment&#58;initial;background-color&#58;transparent;">The Liskov Substitution Principle</a></td>
<td style="border-top-style&#58;solid;border-right-style&#58;solid;border-bottom-style&#58;solid;border-left-style&#58;solid;border-width&#58;initial;border-top-width&#58;0px;border-right-width&#58;1px;border-bottom-width&#58;1px;border-left-width&#58;0px;padding-top&#58;5px;padding-right&#58;5px;padding-bottom&#58;5px;padding-left&#58;5px;"><i>Derived classes must be substitutable for their base classes.</i></td></tr>
<tr><td style="border-top-style&#58;solid;border-right-style&#58;solid;border-bottom-style&#58;solid;border-left-style&#58;solid;border-width&#58;initial;border-top-width&#58;0px;border-right-width&#58;1px;border-bottom-width&#58;1px;border-left-width&#58;0px;padding-top&#58;5px;padding-right&#58;5px;padding-bottom&#58;5px;padding-left&#58;5px;"><b>DIP</b></td>
<td style="border-top-style&#58;solid;border-right-style&#58;solid;border-bottom-style&#58;solid;border-left-style&#58;solid;border-width&#58;initial;border-top-width&#58;0px;border-right-width&#58;1px;border-bottom-width&#58;1px;border-left-width&#58;0px;padding-top&#58;5px;padding-right&#58;5px;padding-bottom&#58;5px;padding-left&#58;5px;"><a href="http&#58;//www.objectmentor.com/resources/articles/dip.pdf" style="background-image&#58;initial;background-attachment&#58;initial;background-color&#58;transparent;">The Dependency Inversion Principle</a></td>
<td style="border-top-style&#58;solid;border-right-style&#58;solid;border-bottom-style&#58;solid;border-left-style&#58;solid;border-width&#58;initial;border-top-width&#58;0px;border-right-width&#58;1px;border-bottom-width&#58;1px;border-left-width&#58;0px;padding-top&#58;5px;padding-right&#58;5px;padding-bottom&#58;5px;padding-left&#58;5px;"><i>Depend on abstractions, not on concretions.</i></td></tr>
<tr><td style="border-top-style&#58;solid;border-right-style&#58;solid;border-bottom-style&#58;solid;border-left-style&#58;solid;border-width&#58;initial;border-top-width&#58;0px;border-right-width&#58;1px;border-bottom-width&#58;1px;border-left-width&#58;0px;padding-top&#58;5px;padding-right&#58;5px;padding-bottom&#58;5px;padding-left&#58;5px;"><b>ISP</b></td>
<td style="border-top-style&#58;solid;border-right-style&#58;solid;border-bottom-style&#58;solid;border-left-style&#58;solid;border-width&#58;initial;border-top-width&#58;0px;border-right-width&#58;1px;border-bottom-width&#58;1px;border-left-width&#58;0px;padding-top&#58;5px;padding-right&#58;5px;padding-bottom&#58;5px;padding-left&#58;5px;"><a href="http&#58;//www.objectmentor.com/resources/articles/isp.pdf" style="background-image&#58;initial;background-attachment&#58;initial;background-color&#58;transparent;">The Interface Segregation Principle</a></td>
<td style="border-top-style&#58;solid;border-right-style&#58;solid;border-bottom-style&#58;solid;border-left-style&#58;solid;border-width&#58;initial;border-top-width&#58;0px;border-right-width&#58;1px;border-bottom-width&#58;1px;border-left-width&#58;0px;padding-top&#58;5px;padding-right&#58;5px;padding-bottom&#58;5px;padding-left&#58;5px;"><i>Make fine grained interfaces that are client specific.</i></td></tr></tbody></table>
<div><span>Figure&#58; 5 principles for class design</span></div>
<div>[<a href="http&#58;//butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod">http&#58;//butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod</a></div>
<div>&lt;&lt;<a href="http&#58;//codebetter.com/davidhayden/2005/05/20/agile-software-development-principles-patterns-and-practices/">Agile Software Development, Principles, Patterns, and Practices</a>​<span></span>&gt;&gt;Robert.C.Martin&#58;</div>
<div><a href="http&#58;//butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod"></a>]</div>
<span></span><div></div>



