---
type: rule
title: Do you know how to rename files that under SourceSafe control?
uri: do-you-know-how-to-rename-files-that-under-sourcesafe-control
created: 2009-05-06T08:46:37.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 17
  title: Ryan Tee

---



<span class='intro'> This field should not be null (Remove me when you edit this field). </span>

<ol>
<li>Save and close the file in Visual Studio .NET, and check in the file if it is checked-out. 
<li>Open Visual SourceSafe Explorer and rename the file. 
<li>Rename it in Visual Studio .NET, click &quot;Continue with change&quot; to the 2 pop-up messages&#58;<br>
<dl class="image">
<dt><img style="border-right&#58;0px solid;border-top&#58;0px solid;border-left&#58;0px solid;border-bottom&#58;0px solid;" src="/Standards/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/RenameVSS1_small.jpg" border="0" /> </dt>
<dd>Figure&#58; Warning message of renaming files under source control.</dd></dl>
<dl class="image">
<dt><img style="border-right&#58;0px solid;border-top&#58;0px solid;border-left&#58;0px solid;border-bottom&#58;0px solid;" src="/Standards/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/RenameVSS2_small.jpg" border="0" /> </dt>
<dd>Figure&#58; You are seeing this as the new file name already exists in SourceSafe, just click &quot;Continue with change&quot;.</dd></dl></li></ol>
<p></p>Visual Studio .NET should find the file under source control and it will come up with a lock icon


