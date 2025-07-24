---
seoDescription: This rule is outdated as Visual SourceSafe (VSS) is deprecated. Modern source control systems like Git are now industry standards. Updated guidance focuses on best practices for excluding files in Git repositories.
type: rule
archivedreason: Obsolete - Visual SourceSafe (VSS) has been deprecated. Use Git or other modern source control systems. See https://www.ssw.com.au/rules/do-you-know-how-to-use-git-effectively/
title: Do you know what files not to put into VSS?
guid: e0a8cd75-8f41-433f-8dd7-4acc88926d9c
uri: do-you-know-what-files-not-to-put-into-vss
created: 2009-05-06T09:39:03.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Ryan Tee
    url: https://ssw.com.au/people/ryan-tee
    noimage: true
related: []
redirects: []
---

The following files should NOT be included in source safe as they are user specific files:

* \*.scc;\*.vspscc - Source Safe Files
* \*.pdb - Debug Files
* \*.user - User settings for Visual Studio .NET IDE

<!--endintro-->
