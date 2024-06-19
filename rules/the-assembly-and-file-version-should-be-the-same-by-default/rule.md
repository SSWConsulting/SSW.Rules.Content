---
seoDescription: Maintain consistency in version numbers by keeping Assembly and File versions same by default.
type: rule
title: Do you keep the assembly and file version the same by default?
uri: the-assembly-and-file-version-should-be-the-same-by-default
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T02:17:00.000Z
archivedreason: outdated
guid: 85981b84-a493-4e60-aeb7-de735b6c4afb
---

For the purpose of consistency, version numbers should be the same there are few exceptions. One exception is for backward compilation: if you have other .dll files depend on the assembly, changing Assembly Version will break these dependencies and then cause a crash in your application.

So you can keep the Assembly Version unchanged and increase the File Version when you release new build. It is easy to maintain the version numbers in VS.NET. For more information on versioning see [semantic versioning rule](/semantic-versioning).

<!--endintro-->

![Figure: Version numbers for assembly and file](versionnumbers.gif)
