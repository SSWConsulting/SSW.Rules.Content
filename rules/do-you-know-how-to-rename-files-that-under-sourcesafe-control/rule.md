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
related: []
redirects: []

---



  <p>Whenever we rename a file in Visual Studio .NET, the file becomes a new file in SourceSafe. If the file has been checked-out, the status of old file will remain as checked-out in SourceSafe.</p>
<p>The step by step to rename a file that under SourceSafe control&#58; </p>

<br><excerpt class='endintro'></excerpt><br>

  <ol>
    <li>Save and close the file in Visual Studio .NET, and check in the file if it is checked-out. </li>
    <li>Open Visual SourceSafe Explorer and rename the file. </li>
    <li>Rename it in Visual Studio .NET, click &quot;Continue with change&quot; to the 2 pop-up messages&#58;<br>
    <dl class="image">
        <dt><img alt="" style="border-bottom&#58;0px solid;border-left&#58;0px solid;border-top&#58;0px solid;border-right&#58;0px solid;" border="0" src="/PublishingImages/RenameVSS1_small.jpg" /> </dt>
        <dd>Figure&#58; Warning message of renaming files under source control.</dd>
    </dl>
    <dl class="image">
        <dt><img alt="" style="border-bottom&#58;0px solid;border-left&#58;0px solid;border-top&#58;0px solid;border-right&#58;0px solid;" border="0" src="/PublishingImages/RenameVSS2_small.jpg" /> </dt>
        <dd>Figure&#58; You are seeing this as the new file name already exists in SourceSafe, just click &quot;Continue with change&quot;.</dd>
    </dl>
    </li>
</ol>
<p>&#160;</p>
Visual Studio .NET should find the file under source control and it will come up with a lock icon



