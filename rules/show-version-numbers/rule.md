---
type: rule
archivedreason: 
title: Do you have version numbers in documents and design files?
guid: 121f7d57-3ad5-4291-a7dc-95badbe2711b
uri: show-version-numbers
created: 2016-03-22T05:59:17.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Tiago Araujo
  url: https://ssw.com.au/people/tiago-araujo
related:
- make-numbers-more-readable
- awesome-documentation
- how-to-name-documents
redirects:
- do-you-include-version-numbers-in-your-file
- include-version-numbers-in-your-file

---

It is very important to have your Word, PowerPoint, PDFs, and design documents up-to-date. You should also make it easy for anyone to identify which version they are looking at. The most effective way to achieve this is by **placing the version number on the right-hand side of the footer**.

<!--endintro-->

::: good
![Figure: Good example - Version number on the RHS of a design document](scrum-image-version-number.png)
:::

See [how you increase the version number](/semantic-versioning):

* Major **1.0** - Rarely change - only with major upgrades. E.g. Complete redesign
* Minor **1.1** - New features / release (customer facing) E.g. Add/remove a heading or a section
* Revision **1.11** - Emergency maintenance, spelling fixes

### Add major version numbers in internal file names

For internal use, it is also good practice to include the major version number in the name of the files. This helps navigating through the old and the new versions, and makes it easy to roll back any changes and use an older version. For public files you should **not** include version numbers.

::: info
**Warning:** This should only be changed on **major versions** and only on **internal documents**.
:::

::: greybox
codeauditor\file.pdf
codeauditor\new\file.pdf
codeauditor\file_latest.pdf
:::
::: bad
Figure: Bad example - Internal file names do not show any version information
:::

::: greybox
codeauditor\file_v1.pdf
codeauditor\file_v2.pdf
codeauditor\file_v3.pdf
:::
::: good
Figure: Good example - Internal file names show the version information  
:::
