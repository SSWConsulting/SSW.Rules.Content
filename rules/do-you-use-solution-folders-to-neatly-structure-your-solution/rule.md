---
type: rule
title: Do you use Solution Folders to Neatly Structure your Solution?
uri: do-you-use-solution-folders-to-neatly-structure-your-solution
created: 2009-04-27T08:57:42.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 17
  title: Ryan Tee

---



<span class='intro'> All the DLL references and files needed to create a setup.exe should be included in your solution. However, just including them as solution items is not enough, they will look very disordered (especially when you have a lot of solution items). And from the screenshot below, you might be wondering what the _Instructions.txt is used for... 
 </span>


  <img class="ms-rteCustom-ImageArea" alt="unstructured solution folder" src="/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/WithoutReferencesAndSetupFolders.gif" /> <br>
<font class="ms-rteCustom-FigureBad">Bad example - An unstructured solution folder</font>
<p>An ideal way is to create &quot;sub-solution folders&quot; for the solution items, the common ones are &quot;References&quot; and &quot;Setup&quot;. This feature is only available in Visual Studio 2005. This will make your solution items look neat and in order. Look at the screenshot below, now it makes sense, we know that the _Instructions.txt contains the instructions of what to do when creating a setup.exe. </p>
<img class="ms-rteCustom-ImageArea" alt="A well structured solution folder has 2 folders - &quot;References&quot; and &quot;Setup&quot;" src="/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/WithReferencesAndSetupFolders.gif" /> <br>
<font class="ms-rteCustom-FigureGood">Good example - A well structured solution folder has 2 folders - &quot;References&quot; and &quot;Setup&quot; <br>
</font>
<table class="clsSSWProductTable" summary="Code Auditor">
    <tbody>
        <tr>
            <td>We have a program called <a href="http&#58;//www.ssw.com.au/ssw/CodeAuditor/Default.aspx">SSW Code Auditor</a> to check for this rule. </td>
        </tr>
    </tbody>
</table>



