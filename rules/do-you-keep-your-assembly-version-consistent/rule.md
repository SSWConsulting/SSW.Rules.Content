---
type: rule
title: Do you keep your Assembly Version Consistent?
uri: do-you-keep-your-assembly-version-consistent
created: 2009-04-28T07:03:16.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 17
  title: Ryan Tee

---



<span class='intro'> 
  <img alt="" class="ms-rteCustom-ImageArea" src="/Standards/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/VersionConsistent1.jpg" /> <br>
<font class="ms-rteCustom-FigureNormal" size="+0">Figure&#58; Keep these two versions consistent</font> If you are not using the GAC, it is important to keep AssemblyVersion, AssemblyFileVersion and AssemblyInformationalVersionAttribute the same, otherwise it can lead to support and maintenance nightmares. By default these version values are defined in the AssemblyInfo file. In the following examples, the first line is the version of the assembly and the second line is the actual version display in file properties.<br>
 </span>


  <font class="ms-rteCustom-CodeArea" size="+0">[assembly&#58; AssemblyVersion(<font class="ms-rteCustom-Highlight" size="+0">&quot;2.0.*&quot;</font>)]<br>
[assembly&#58; AssemblyFileVersion(<font class="ms-rteCustom-Highlight" size="+0">&quot;1.0.0.3&quot;</font>)] </font>
  <font class="ms-rteCustom-FigureBad" size="+0">Bad example - the common assembly versioning method.</font> <font class="ms-rteCustom-CodeArea" size="+0">[assembly&#58; AssemblyVersion(<font class="ms-rteCustom-Highlight" size="+0">&quot;2.0.*&quot;</font>)]<br>
[assembly&#58; AssemblyFileVersion(<font class="ms-rteCustom-Highlight" size="+0">&quot;2.0.*&quot;</font>)] <br>
[assembly&#58; AssemblyInformationalVersion(<font class="ms-rteCustom-Highlight" size="+0">&quot;2.0.*&quot;</font>)] </font><font class="ms-rteCustom-FigureGood" size="+0">Good example - the best way for Assembly versioning (when not using the GAC)</font> If you are using the GAC, you should adopt a single AssemblyVersion and AssemblyInformationalVersionAttribute and update the AssemblyFileVerison with each build.<br>
<br>
<font class="ms-rteCustom-CodeArea" size="+0">[assembly&#58; AssemblyVersion(<font class="ms-rteCustom-Highlight" size="+0">&quot;2.0.0.0&quot;</font>)]<br>
[assembly&#58; AssemblyFileVersion(<font class="ms-rteCustom-Highlight" size="+0">&quot;2.0.*&quot;</font>)]<br>
[assembly&#58; AssemblyInformationalVersion(<font class="ms-rteCustom-Highlight" size="+0">&quot;2.0.0.0&quot;</font>)] </font><font class="ms-rteCustom-FigureGood" size="+0">Good example - the best way for Assembly versioning (when using the GAC)</font> Note&#58; It would be good if Microsoft changed the default behaviour of AssemblyInformationalVersionAttribute to default to the AssemblyVersion.<a href="http&#58;//msdn.microsoft.com/en-us/library/system.reflection.assemblyinformationalversionattribute.aspx">See Mikes suggestion for improving the version number in the comments here. </a>



