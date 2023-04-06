---
type: rule
archivedreason: 
title: Do you include version numbers in your files?
guid: 121f7d57-3ad5-4291-a7dc-95badbe2711b
uri: include-version-numbers-in-your-file
created: 2016-03-22T05:59:17.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related:
- make-numbers-more-readable
- awesome-documentation
redirects:
- do-you-include-version-numbers-in-your-file

---

It is very important to have your Word, PowerPoint, PDFs and other documents up-to-date and having the version number on the RHS of the footer is the best way to show which version you are looking at.

Please read to understand how you increase the version number:

<!--endintro-->

Major **1.0** - Rarely change - only with major upgrades. E.g. Complete redesign

Minor **1.1** - New features / release (customer facing) E.g. Add/remove a heading or a section

Revision **1.11** - Emergency maintenance, spelling fixes

It is also good practice to include a version number in the name of the file. This helps us to navigate through the old and the new versions. It makes it easy if we decide to roll back any changes and use an older version.

::: greybox
codeauditor\file.pdf   
codeauditor\new\file.pdf   
codeauditor\file_latest.pdf    
:::
::: bad
Figure: Bad example - Files do not show any version information
:::

::: greybox
codeauditor\file_v1.pdf   
codeauditor\file_v2.pdf   
codeauditor\file_v3.pdf   
:::
::: good
Figure: Good example - Files show the version information  
:::
