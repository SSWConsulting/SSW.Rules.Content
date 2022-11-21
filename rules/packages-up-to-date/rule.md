---
type: rule
archivedreason: 
title: Do you keep your npm and yarn packages up to date?
guid: 1cf8a8d6-8140-42bb-8f5f-d8416a1f9dd7
uri: packages-up-to-date
created: 2020-09-30T00:17:47.0000000Z
authors:
- title: Sebastien Boissiere
  url: https://www.ssw.com.au/people/seb
- title: Adam Cogan
  url: https://www.ssw.com.au/people/adam-cogan
- title: Christian Morford-Waite
  url: https://www.ssw.com.au/people/christian-morford-waite
- title: Chris Clement
  url: https://www.ssw.com.au/people/chris-clement
related:
- the-best-package-manager-for-react
- monitor-packages-for-vulnerability
redirects:
- do-you-keep-your-npm-packages-up-to-date

---

Npm packages often get new releases (adding new functionalities, fixing bugs or vulnerabilities). It is important to keep the packages updated as much as possible during the development of your application. The best way to do that is to update all the packages every time you add a new package to your application, and include the `npm outdated` and `npm audit` reports in the Sprint Review. These commands are also available with yarn with `yarn outdated` and `yarn audit`.

<!--endintro-->

`npm outdated` returns an overview of your packages: the version, the wanted version (the maximum version of the package that satisfies the semver range specified in package.json) and the latest version of the package.

![Figure: Use 'npm outdated'](npm_outdated.png) 

-  **Red** indicates the package version is below the wanted version.
-  **Yellow** indicates the package version is at the wanted version but below the latest version.

`npm audit` returns an audit on your packages for vulnerabilities. It also provides information on how to resolve them.

![Figure: Use 'npm audit' to discover vulnerabilities in your application](npm_audit.png)

To add a new package, use `npm install package-name` or `yarn add package-name`.

To update your packages, use `npm update package-name` or `yarn upgrade package-name`. Yarn also has a useful tool called `yarn upgrade-interactive` that allows you to see which packages are outdated, and upgrade them all at once.

![Figure: Using yarn upgrade-interactive](upgrade-interactive.png)

**Note:** Use `yarn upgrade-interactive --latest` to see outdated packages with breaking changes.
