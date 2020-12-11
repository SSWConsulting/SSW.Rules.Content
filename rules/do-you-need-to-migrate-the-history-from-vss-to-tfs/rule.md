---
type: rule
archivedreason: 
title: Do you need to migrate the history from VSS to TFS?
guid: c4f91635-787a-4d8e-b5be-ffa8f9125e7f
uri: do-you-need-to-migrate-the-history-from-vss-to-tfs
created: 2011-11-18T03:52:46.0000000Z
authors:
- id: 22
  title: David Klein
- id: 5
  title: Justin King
- id: 17
  title: Ryan Tee
- id: 6
  title: Tristan Kurniawan
related: []

---

* Normally, you don't need to check the history very often. If you do need sometimes, then get it from VSS.
* Save much space for TFS. For example, we have a about 7G VSS history database, and we may only need a small bit of them every 3 months, so what's the point of coping about 7G file when we only need one line of code?


<!--endintro-->



But there are also some considerations that you may want to migrate the history:

* If the history of source changes will be checked very often, so you can check the old history with the recent together via TFS.
* You are going to decommission the old VSS completely. Say you don't want to keep the old VSS database, and then it will be necessary to keep the information somewhere.
* If the project is very active, then it will be worthy to migrate the history because your developers may need them every day.


If you are going to move the history, the links may help:

* [http://msdn2.microsoft.com/en-us/library/ms181247.aspx](http&#58;//www.ssw.com.au/ssw/redirect/msdn/MigratingToTFS.htm)
* [http://blogs.msdn.com/buckh/archive/2004/06/10/152609.aspx](http&#58;//www.ssw.com.au/ssw/redirect/MigratingToTFS.htm)
* [http://blogger.xs4all.nl/tty1/archive/2006/04/09/85962.aspx](http&#58;//www.ssw.com.au/ssw/redirect/MigratingToTFS2.htm)
