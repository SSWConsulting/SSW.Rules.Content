---
type: rule
title: Do you use Bundling and/or AMD
uri: do-you-use-bundling-andor-amd
created: 2015-06-16T07:41:41.0000000Z
authors:
- id: 34
  title: Brendan Richards
- id: 44
  title: Duncan Hunter

---



<span class='intro'> ​Minification and AMD are techniques&#160;to improve javascript performance. They can&#160;both can be used with both vanilla JavaScript and with Typescript </span>

<h3 class="ssw15-rteElement-H3">​​​AMD and&#160;RequireJs</h3><p>AMD is a client-side technology​​​ that&#160;allows you to break you Js code into small inter-dependent&#160;modules. The modules (and thier dependencies)&#160;required to render a particular page are determined at runtime and subsequently downloaded by Javascript. RequireJs is a popular AMD implementation.</p><dd class="ssw15-rteElement-FigureGood">Pro&#58; Only the js modules you need are downloaded</dd><dd class="ssw15-rteElement-FigureBad">Con&#58; Each module is downloaded in a separate http request</dd><h3 class="ssw15-rteElement-H3"><span style="font-weight&#58;normal;">​Bundling and Minification</span><br></h3><p>​This is a server side technique that combines and optimises client side files into single, optimised downloads.</p><p><span style="line-height&#58;1.6;">ASP</span><span style="line-height&#58;1.6;">.N</span><span style="line-height&#58;1.6;">et contains excellent server-side bundling support as outlined here&#58;&#160;</span><span style="line-height&#58;1.6;">​<a href="http&#58;//www.asp.net/mvc/overview/performance/bundling-and-minification">http&#58;//www.asp.net/mvc/overview/performance/bundling-and-minification​</a></span></p><p><span style="line-height&#58;1.6;">ASP.Net vnext &amp; VS 2015 also provides support for using node/npm based bundling and&#160;minification tools.</span></p><dd class="ssw15-rteElement-FigureGood">Pro&#58; Fewer Http requests and smaller files</dd><dd class="ssw15-rteElement-FigureBad">Con&#58; All client side modules are included in a single download​</dd>


