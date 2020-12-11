---
type: rule
archivedreason: 
title: Do you write unit tests to confirm bugfixes? (aka Red-Green-Refactor)
guid: 13fb161f-a1aa-458f-89a9-3e242a79ec1f
uri: do-you-write-unit-tests-to-confirm-bugfixes-aka-red-green-refactor
created: 2020-03-11T17:39:51.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

When you encounter a bug in your application you should never let the same bug happen again. The best way to do this is to write a unit test for the bug, see the test fail, then fix the bug and watch the test pass. This is also known as Red-Green-Refactor.




Tip: you can then reply to the bug report with "Done + Added a unit test so it can't happen again"



<!--endintro-->

See [how to send a good 'Done' email](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=d0a87319-837c-417d-9a16-3ffecb734a17).
