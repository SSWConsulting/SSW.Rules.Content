---
type: rule
archivedreason: 
title: Do you keep your npm packages up to date?
guid: 1cf8a8d6-8140-42bb-8f5f-d8416a1f9dd7
uri: do-you-keep-your-npm-packages-up-to-date
created: 2020-09-30T00:17:47.0000000Z
authors: []
related: []
redirects: []

---


<p>​Npm packages often get new releases (adding new functionalities, fixing bugs or vulnerabilities). It is important to keep the packages updated as much as possible during the development of your application. The best way to do that is to update all the packages every time you add a new package to your application, and include the 'npm outdated' and 'npm audit' reports in the Sprint Review. These&#160;commands are also&#160;available with yarn with 'yarn outdated' and 'yarn audit'.<br></p><ul><li>'npm outdated' returns an overview of your packages&#58; the version, the wanted version (the maximum version of the package that satisfies the semver range specified in package.json) and the latest version of the package.&#160;<br></li></ul><blockquote><div><img src="/SiteAssets/do-you-keep-your-npm-packages-up-to-date/npm_outdated.png" alt="npm_outdated.png" style="margin&#58;5px;" />&#160;<br></div><dd class="ssw15-rteElement-FigureNormal">​Figure&#58; Use 'npm outdated'<br></dd><p class="ssw15-rteElement-P">- <strong>Red </strong>indicates the package version is below the wanted version.</p><p class="ssw15-rteElement-P">- <strong>Yellow </strong>indicates the package version is at the wanted version but&#160;below the latest version.​<br></p></blockquote><div><br></div><ul><li>'npm audit' returns an audit on your packages for&#160;vulnerabilities. It also provides information on how to resolve them.<br></li></ul><blockquote><p><img src="/SiteAssets/do-you-keep-your-npm-packages-up-to-date/npm_audit.png" alt="npm_audit.png" style="margin&#58;5px;" />&#160;</p></blockquote><dd class="ssw15-rteElement-FigureNormal">Figure&#58; Use 'npm audit' to discover&#160;vulnerabilities in&#160;your application​​​<br></dd><dd class="ssw15-rteElement-FigureNormal"><br></dd><p><br></p><p><br></p>
<br><excerpt class='endintro'></excerpt><br>



