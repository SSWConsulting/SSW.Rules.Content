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



<span class='intro'> <div><span>a. &#160; &#160; &#160;You don’t want containers ????</span></div>
<div><div><a href="http&#58;//blogs.clariusconsulting.net/kzu/you-dont-need-an-ioc-or-servicelocator-for-everything/" rel="bookmark" title="You don’t need an IoC container or ServiceLocator for everything">You don’t need an IoC container or ServiceLocator for everything</a></div>
<div><p style="margin-bottom&#58;1em;padding-top&#58;0px;padding-bottom&#58;0px;border-top-width&#58;0px;border-right-width&#58;0px;border-bottom-width&#58;0px;border-left-width&#58;0px;border-style&#58;initial;border-color&#58;initial;font-size&#58;13px;font-family&#58;'segoe ui', calibri, 'helvetica neue', arial, verdana, sans-serif;vertical-align&#58;baseline;line-height&#58;19px;text-align&#58;-webkit-auto;">An IoC container WILL help if you have complex dependency graphs to instantiate (in your default constructor) or you have truly pluggable components (i.e. you want to allow a component to be picked up automatically at runtime from some binary if it’s in a folder, etc.).</p>
<p style="margin-bottom&#58;1em;padding-top&#58;0px;padding-bottom&#58;0px;border-top-width&#58;0px;border-right-width&#58;0px;border-bottom-width&#58;0px;border-left-width&#58;0px;border-style&#58;initial;border-color&#58;initial;font-size&#58;13px;font-family&#58;'segoe ui', calibri, 'helvetica neue', arial, verdana, sans-serif;vertical-align&#58;baseline;line-height&#58;19px;text-align&#58;-webkit-auto;">If you don’t, it’s perfectly fine to have a default constructor that is used at runtime and has a hardcoded instantiation of a dependency. It was never a requirement to make that thing configurable or dynamic. So don’t invent business requirements just ‘cause using an IoC container is fancier.&#160;​</p></div>
<span></span></div>
<div>[<a href="http&#58;//www.devtrends.co.uk/blog/how-not-to-do-dependency-injection-the-static-or-singleton-container">http&#58;//www.devtrends.co.uk/blog/how-not-to-do-dependency-injection-the-static-or-singleton-container</a>]</div>
<div>[<a href="http&#58;//stackoverflow.com/questions/871405/why-do-i-need-an-ioc-container-as-opposed-to-straightforward-di-code">http&#58;//stackoverflow.com/questions/871405/why-do-i-need-an-ioc-container-as-opposed-to-straightforward-di-code</a>]</div>
<div><br></div>
<span></span><div></div>
<div></div>
<div></div>
<div><span>b.&#160;&#160;&#160;&#160;&#160;&#160;You don’t want reflection ….. much better to use meth</span></div>
​ </span>




