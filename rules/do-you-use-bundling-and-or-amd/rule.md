---
type: rule
archivedreason: 
title: Do you use Bundling and/or AMD
guid: b51f62d0-83ea-4c94-b565-8e51552e846f
uri: do-you-use-bundling-and-or-amd
created: 2015-06-16T07:41:41.0000000Z
authors:
- title: Brendan Richards
  url: https://ssw.com.au/people/brendan-richards
- title: Duncan Hunter
  url: https://ssw.com.au/people/duncan-hunter
related:
- do-you-treat-javascript-like-a-real-language
- do-you-know-which-version-of-jquery-to-use
- do-you-use-hyperlinks-instead-of-javascript-to-open-pages
redirects: []

---


​​Minification and AMD are techniques&#160;to improve javascript performance. They can&#160;both can be used with vanilla JavaScript and with Typescript
<br><excerpt class='endintro'></excerpt><br>
<h3 class="ssw15-rteElement-H3">​​​AMD and&#160;RequireJs</h3><p>AMD is a client-side technology​​​ that&#160;allows you to break you Js code into small inter-dependent&#160;modules. The modules (and thier dependencies)&#160;required to render a particular page are determined at runtime and subsequently downloaded by Javascript. RequireJs is a popular AMD implementation.</p><dd class="ssw15-rteElement-FigureGood">Pro&#58; Only the js modules you need are downloaded</dd><dd class="ssw15-rteElement-FigureBad">Con&#58; Each module is downloaded in a separate http request</dd><h3 class="ssw15-rteElement-H3"><span style="font-weight&#58;normal;">​Bundling and Minification</span><br></h3><p>​This is a server side technique that combines and optimises client side files into single, optimised downloads.</p><p><span style="line-height&#58;1.6;">ASP</span><span style="line-height&#58;1.6;">.N</span><span style="line-height&#58;1.6;">et contains excellent server-side bundling support as outlined here&#58;&#160;</span><span style="line-height&#58;1.6;">​<a href="http&#58;//www.asp.net/mvc/overview/performance/bundling-and-minification">http&#58;//www.asp.net/mvc/overview/performance/bundling-and-minification​</a></span></p><p><span style="line-height&#58;1.6;">ASP.Net vnext &amp; VS 2015 also provides support for using&#160;task runners like Gulp or Grunt for bundling and minification.​</span></p><dd class="ssw15-rteElement-FigureGood">Pro&#58; Fewer Http requests and smaller files</dd><dd class="ssw15-rteElement-FigureBad">Con&#58; All client side modules are included in a single download​</dd>


