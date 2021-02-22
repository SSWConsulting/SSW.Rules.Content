---
type: rule
archivedreason: 
title: Do you use the Code Health Extensions in VS Code?
guid: ba1170f1-3d1a-4af1-b35e-b0c82b5b6ac2
uri: do-you-use-the-code-health-extensions-in-vs-code
created: 2017-03-09T22:12:04.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Danijel Malik
  url: https://ssw.com.au/people/danijel-malik
related: []
redirects: []

---


For lightweight web projects such as Angular, often VS Code is more appropriate than Visual Studio. So make sure your code quality remains consistent with CssLint and TSLint.<br>
<br><excerpt class='endintro'></excerpt><br>
<h3 class="ssw15-rteElement-H3">Related Steps to Code Health: <br></h3><ul><li> 
      <a href=/do-you-use-the-code-health-extensions-in-visual-studio>Do you use the Code Health Extensions in Visual ​Studio?</a><br></li><li> 
      <a href=/do-you-run-the-code-health-checks-in-your-visualstudio-com-continuous-integration-build>Do you run the Code Health checks in your VisualStudio.com Continuous Integration Bu<span style="font-family:calibri;font-size:11pt;">ild? </span></a> <br></li></ul><h3 class="ssw15-rteElement-H3">Which Extensions to Use in VS Code<br></h3><p>For web projects, we advocate the use of CSSLint for css files and TSLint for typescript files. (<a href=/do-you-know-when-to-use-typescript-vs-javascript-and-coffeescript>Why you should be using TypeScript instead of JavaScript </a>)<br>Linters for these can be easily added to VS Code via extensions.​<br>Simply select the "Extensions" tab, search for "CSSLint" and "TSLint" and click "Install" on each respectively.</p><dl class="image"><dt><img src="VSCode-Extensions.png" alt="VSCode-Extensions.png" style="width:650px;" />  </dt><dd>Figure: Addition of CssLi nt and TSLint to VS Code Project</dd></dl><p>If you prefer not to use the Extensions (which are currently a bit out of date). You can install them using npm as normal. <br>CssLint (<a href="https://www.npmjs.com/package/csslint">Csslint npm guide</a>)<br>TSLint (<a href="https://www.npmjs.com/package/tslint">TSlint npm guide </a>)<br><br></p>


