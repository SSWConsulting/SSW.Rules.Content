---
type: rule
title: Do you reference "most" .dlls by Project?
uri: do-you-reference-most-dlls-by-project
created: 2009-04-28T03:36:16.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 17
  title: Ryan Tee

---



<span class='intro'> This field should not be null (Remove me when you edit this field). </span>


  <p>When you face a bug, there are 2 types of emails you can send&#58; </p>
<ol>
    <li>Dan, I get this error calling your Registration.dll? or </li>
    <li>Dan, I get this error calling your Registration.dll and I have investigated it. As per our conversation, I have changed this xxx to this xxx. </li>
</ol>
<p>The 2nd option is preferable.</p>
<b>The simple rule is&#58;</b>
<ul>
    <li>If there are no bugs then reference the assembly, and </li>
    <li>If there are bugs in the project (or any project it references [See note below]) then reference the project. </li>
</ul>
<p>Since most applications have bugs, therefore most of the time you should be using the second option.</p>
<p>If it is a well tested component and it is not changing constantly, then use the first option.</p>
<ol>
    <li>Add the project to solution (if it is not in the solution). <img class="ms-rteCustom-ImageArea" alt="Add existing project" src="/Standards/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/ReferenceProject1.gif" /> <span class="ms-rteCustom-FigureGood">Figure&#58; Add existing project</span> </li>
    <li>Select the &quot;References&quot; folder of the project you want to add references to, right click and select &quot;Add Reference...&quot;. <br>
    <img class="ms-rteCustom-ImageArea" alt="Add reference" src="/Standards/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/ReferenceProject2.gif" /> <span class="ms-rteCustom-FigureGood">Figure&#58; Add reference</span> </li>
    <li>Select the projects to add as references and click OK. <img class="ms-rteCustom-ImageArea" alt="Select projects to reference" src="/Standards/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/ReferenceProject3.gif" /> <span class="ms-rteCustom-FigureGood">Figure&#58; Select the projects to add as references</span> </li>
</ol>
<p>Note&#58; We have run into a situation where we reference a stable project A, and an unstable project B. Project A references project B. Each time project B is built, project A needs to be rebuilt.</p>
<p>Now, if we reference stable project A by dll, and unstable project B by project according to this standard, then we might face referencing issues, where Project A will look for another version of Project B ?the one it is built to, rather than the current build, which will cause Project A to fail.</p>
<p>To overcome this issue, we then reference by project rather than by assembly, even though Project A is a stable project. This will mitigate any referencing errors.</p>
<ul></ul>



