---
type: rule
archivedreason: 
title: Do you use the testing stage, in the file name?
guid: bc50d07e-bbc9-4bc2-ac7c-4a9b91bf8e0f
uri: use-the-testing-stage-in-the-file-name
created: 2018-04-23T21:52:42.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-use-the-testing-stage-in-the-file-name

---

When moving through the different stages of testing i.e. from internal testing, through to UAT, you should suffix the application name with the appropriate stage:

<!--endintro-->


| **Stage**  | **Testing Description**  | **Naming Convention**  |
| --- | --- | --- |
| Alpha | Developer testing with project team | Northwind\_v2-3\_alpha.exe |
| Beta | Internal “Test Please" testing with non-project working colleagues | Northwind\_v2-3\_beta.exe |
| Production e.g. | When moving onto production, this naming convention is dropped | Northwind\_v2-3.exe |
