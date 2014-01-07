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



<span class='intro'> ​All the DLL references and files needed to create a setup.exe should be included in your solution. However, just including them as solution items is not enough, they will look very disordered (especially when you have a lot of solution items). And from the screenshot below, you might be wondering what the _Instructions.docx&#160;is used for... 
 </span>

<dl class="ssw15-rteElement-ImageArea"><img src="/PublishingImages/SSW%20-%20Rules%20.NET%20Projects%20-%20Bad%20Solution.png" alt="SSW - Rules .NET Projects - Bad Solution.png" style="margin&#58;5px;" /></dl>
<font class="ms-rteCustom-FigureBad">Bad example - An unstructured solution folder</font>
<p>An ideal way is to create &quot;sub-solution folders&quot; for the solution items, the common ones are &quot;References&quot; and &quot;Setup&quot;. This will make your solution items look neat and in order. Look at the screenshot below, now it makes sense, we know that the _Instructions.docx&#160;contains the instructions of what to do when creating a setup.exe. </p><dl class="ssw15-rteElement-ImageArea">
<img src="/PublishingImages/SSW%20-%20Rules%20.NET%20Projects%20-%20Good%20Solution.png" alt="SSW - Rules .NET Projects - Good Solution.png" style="margin&#58;5px;width&#58;375px;" /></dl>
<font class="ms-rteCustom-FigureGood">Good example - A well structured solution folder has 2 folders - &quot;References&quot; and &quot;Setup&quot; <br>
</font>
<table class="clsSSWProductTable" summary="Code Auditor">
    <tbody>
        <tr>
            <td>We have a program called <a href="http&#58;//www.ssw.com.au/ssw/CodeAuditor/Default.aspx">SSW Code Auditor</a> to check for this rule. </td>
        </tr>
    </tbody>
</table>



