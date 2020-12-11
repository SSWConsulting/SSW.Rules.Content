---
type: rule
archivedreason: 
title: Do you avoid limiting source control to just code?
guid: 7a55595d-281d-43b9-b76a-97557f0e9fe6
uri: do-you-avoid-limiting-source-control-to-just-code
created: 2011-11-18T03:52:55.0000000Z
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

You can spend valuable developer time on every part of a project. The bulk of time is normally spent on coding up .cs, .vb, .resx and .aspx files. However, you could potentially have the following happen if you do not include other files in source control:* lose work
* lose old versions of work
* have work overwritten


<!--endintro-->

In particular, you should make it as easy as possible to see who changed what and who deleted what and allow a simple rollback to previous versions of non-code files. Files you should put in source control include:* XSL files
* Word documents
* Excel Spreadsheets
* Visio Diagrams
* HTML files
* Image files, Flash animations and psd files  (yes this takes room in your source control database - but we still want to be able to revert to an old version easily)


Things you don't store are:* Video files eg. avi
* Installers eg. .msi
