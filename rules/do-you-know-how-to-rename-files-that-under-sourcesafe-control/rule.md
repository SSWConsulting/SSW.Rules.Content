---
type: rule
archivedreason: 
title: Do you know how to rename files that under SourceSafe control?
guid: 5097d3f0-e86d-4cbe-9f89-1b3d22d2b38c
uri: do-you-know-how-to-rename-files-that-under-sourcesafe-control
created: 2009-05-06T08:46:37.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ryan Tee
  url: https://ssw.com.au/people/ryan-tee
  noimage: true
related: []
redirects: []

---

Whenever we rename a file in Visual Studio .NET, the file becomes a new file in SourceSafe. If the file has been checked-out, the status of old file will remain as checked-out in SourceSafe.

The step by step to rename a file that under SourceSafe control:

<!--endintro-->

1. Save and close the file in Visual Studio .NET, and check in the file if it is checked-out.
2. Open Visual SourceSafe Explorer and rename the file.
3. Rename it in Visual Studio .NET, click "Continue with change" to the 2 pop-up messages:
        
![Figure: Warning message of renaming files under source control.](RenameVSS1_small.jpg)  

        
            
![Figure: You are seeing this as the new file name already exists in SourceSafe, just click "Continue with change".](RenameVSS2_small.jpg)  

        
    



 Visual Studio .NET should find the file under source control and it will come up with a lock icon
