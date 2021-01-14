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

For lightweight web projects such as Angular, often VS Code is more appropriate than Visual Studio. So make sure your code quality remains consistent with CssLint and TSLint.

<!--endintro-->

### Related Steps to Code Health: 


* [Do you use the Code Health Extensions in Visual Studio?](/do-you-use-the-code-health-extensions-in-visual-studio)
* [Do you run the Code Health checks in your VisualStudio.com Continuous Integration Build?](/do-you-run-the-code-health-checks-in-your-visualstudio-com-continuous-integration-build)


### Which Extensions to Use in VS Code


For web projects, we advocate the use of CSSLint for css files and TSLint for typescript files. ([Why you should be using TypeScript instead of JavaScript](/do-you-know-when-to-use-typescript-vs-javascript-and-coffeescript))
Linters for these can be easily added to VS Code via extensions.
Simply select the "Extensions" tab, search for "CSSLint" and "TSLint" and click "Install" on each respectively.


::: ok  
![Figure: Addition of CssLi nt and TSLint to VS Code Project](VSCode-Extensions.png)  
:::

If you prefer not to use the Extensions (which are currently a bit out of date). You can install them using npm as normal. 
CssLint ([Csslint npm guide](https://www.npmjs.com/package/csslint))
TSLint ([TSlint npm guide](https://www.npmjs.com/package/tslint))
