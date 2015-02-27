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
  <img class="ms-rteCustom-ImageArea" src="/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/VersionConsistent1.jpg" alt="" /> <br>
<font class="ms-rteCustom-FigureNormal" size="+0">Figure&#58; Keep these two versions consistent</font> If you are not using the GAC, it is important to keep AssemblyVersion, AssemblyFileVersion and AssemblyInformationalVersionAttribute the same, otherwise it can lead to support and maintenance nightmares. By default these version values are defined in the AssemblyInfo file. In the following examples, the first line is the version of the assembly and the second line is the actual version display in file properties.<br>
 </span>

<font class="ms-rteCustom-CodeArea" size="+0"> [assembly&#58; AssemblyVersion(<font class="ms-rteCustom-Highlight" size="+0">&quot;2.0.0.*&quot;</font>)]<br> [assembly&#58; AssemblyFileVersion(<font class="ms-rteCustom-Highlight" size="+0">&quot;2.0.0.*&quot;</font>)]<br> [assembly&#58; AssemblyInformationalVersion​(<font class="ms-rteCustom-Highlight">&quot;2.0.0.*&quot;</font>)] </font> 
<font class="ms-rteCustom-FigureBad" size="+0">Bad example - AssemblyFileVersion and AssemblyInformationalVersion don't support the asterisk (*) character</font> 
<p>If you use an asterisk in the AssemblyVersion, the version will be generated as described in the <a href="https&#58;//msdn.microsoft.com/en-us/library/system.reflection.assemblyversionattribute.assemblyversionattribute%28v=vs.110%29.aspx">MSDN documentation</a>. If you use an asterisk in the AssemblyFileVersion, you will see a warning, and the asterisk will be replaced with&#160;zeroes. If you use an asterisk in the AssemblyInformationVersion, the asterisk will be stored, as this version property is stored as a string.<img src="/SoftwareDevelopment/RulesToBetterDotNETProjects/SiteAssets/Pages/KeepAssemblyVersionConsistent/AssemblyFileVersion-Warning.png" alt="AssemblyFileVersion-Warning.png" style="font-size&#58;12px;line-height&#58;1.6;margin&#58;5px;width&#58;650px;" /><span style="font-size&#58;12px;line-height&#58;1.6;background-color&#58;#f5f5f5;">
   </span><span class="ssw15-rteStyle-Caption">Figure&#58; Warning when you use an asterisk in the AssemblyFileVersion</span><span style="font-size&#58;12px;line-height&#58;1.6;background-color&#58;#f5f5f5;">​</span></p><font class="ms-rteCustom-CodeArea" size="+0"><br>[assembly&#58; AssemblyVersion(<font class="ms-rteCustom-Highlight" size="+0">&quot;2.0.*&quot;</font>)]<br> [assembly&#58; AssemblyFileVersion(<font class="ms-rteCustom-Highlight" size="+0">&quot;2.0.1.1&quot;</font>)]<br> [assembly&#58; AssemblyInformationalVersion(<font class="ms-rteCustom-Highlight" size="+0">&quot;2.0&quot;</font>)] </font> 
<font class="ms-rteCustom-FigureGood" size="+0">Good example - MSBuild will automatically set the Assembly version on build (when not using the GAC)</font> 
<p>Having MSBuild or Visual Studio automatically set the AssemblyVersion on build can be useful if you don't have a build server configured.</p><p>If you are using the GAC, you should adopt a single AssemblyVersion and AssemblyInformationalVersionAttribute and update the AssemblyFileVerison with each build.</p> 
<font class="ms-rteCustom-CodeArea" size="+0"> [assembly&#58; AssemblyVersion(<font class="ms-rteCustom-Highlight" size="+0">&quot;2.0.0.0&quot;</font>)]<br> [assembly&#58; AssemblyFileVersion(<font class="ms-rteCustom-Highlight" size="+0">&quot;2.0.0.1&quot;</font>)]<br> [assembly&#58; AssemblyInformationalVersion(<font class="ms-rteCustom-Highlight" size="+0">&quot;v2 RTM&quot;</font>)] </font> 
<font class="ms-rteCustom-FigureGood" size="+0">Good example - the best way for Assembly versioning (when using the GAC)</font> 
<p>If you're working with SharePoint farm solutions (2007, 2010, or 2013), in most circumstances the assemblies in your SharePoint WSPs will be deployed to the GAC. For this reason development is much easier&#160;if you don't change your&#160;AssemblyVersion, and increment your AssemblyFileVersion instead.​</p><p> Note&#58; It would be good if Microsoft changed the default behaviour of AssemblyInformationalVersionAttribute to default to the AssemblyVersion. <a href="http&#58;//msdn.microsoft.com/en-us/library/system.reflection.assemblyinformationalversionattribute.aspx">See Mikes suggestion for improving the version number in the comments here.</a> </p>


