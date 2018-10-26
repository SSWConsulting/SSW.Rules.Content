---
type: rule
title: Tools - Do you know what Angular Tools to install for an Angular project?
uri: tools---do-you-know-what-angular-tools-to-install-for-an-angular-project
created: 2016-12-20T14:01:27.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 24
  title: Adam Stephensen
- id: 44
  title: Duncan Hunter
- id: 72
  title: Gabriel George

---



<span class='intro'> <p>​It is suggested using&#160;<a href="http&#58;//cli.angular.io/">cli.angular.io</a>&#160;to start an&#160;Angular&#160;project, especially when learning as it is the easiest way to both get started and also follow best practices.​<br></p> </span>

<ol><li>Check&#160;that you are running at node 8.11+ (note&#58; some still use&#160;6.9+ as it works with Angular CLI). Check that you are running npm&#160;5+&#160;by running&#160;node&#160;in a terminal/console window. <br><br>Older versions produce errors, but newer versions are fine. If you have older versions please install the latest version from here&#160;<a href="https&#58;//nodejs.org/en/">https&#58;//nodejs.org/en</a><br><br>Check you have the right versions&#58;<p class="ssw15-rteElement-CodeArea">&#160;node -v<br>&#160;npm -v<br></p></li><li>Install git&#160;<a href="https&#58;//git-scm.com/">https&#58;//git-scm.com</a> Check you have git&#58;&#160;<p class="ssw15-rteElement-CodeArea" style="width&#58;751.438px;">git --version<br></p></li><li>Check you have the latest version of the Angular cli&#160;by running the below ng -v command in the terminal and checking the latest version on GitHub&#160;here&#160;<a href="https&#58;//github.com/angular/angular-cli">https&#58;//github.com/angular/angular-cli </a> <br> 
      <p class="ssw15-rteElement-CodeArea" style="width&#58;751.438px;">ng -v<br></p><dl class="image"><dt> <img src="/SiteAssets/angular-the-stuff-to-install/2017-07-04_12-54-27.jpg" alt="2017-07-04_12-54-27.jpg" style="width&#58;750px;" /> </dt><dd>Figure&#58; Current version to check on GitHub</dd></dl><p>If you are not running the latest version we recommend you run the below commands to update the cli. <br></p></li><p class="ssw15-rteElement-CodeArea" style="width&#58;751.438px;">npm uninstall -g @angular/ cli&#160;(not needed to run anymore as it is done automatically)<br>npm install -g&#160;@angular/ cli<br></p><li>Getting errors?<br>If you get node gyp errors, follow instructions here&#160;<a href="https&#58;//github.com/nodejs/node-gyp">https&#58;//github.com/nodejs/node-gyp</a> <br>If you get permission errors,&#160;follow instructions here&#160;<a href="https&#58;//docs.npmjs.com/getting-started/fixing-npm-permissions">https&#58;//docs.npmjs.com/getting-started/fixing-npm-permissions</a> <br><br></li><li>If you are new to Angular we recommend you use&#160;<b>VSCode</b>&#160;- <a href="http&#58;//code.visualstudio.com/">http&#58;//code.visualstudio.com</a>&#160; -&#160;versus&#160;<b>Visual Studio 2015/17</b>&#160;as the TypeScript support and project directory (without a Visual Studio Project) is easier.</li></ol>


