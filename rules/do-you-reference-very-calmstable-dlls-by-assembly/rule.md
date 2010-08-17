---
type: rule
title: Do you reference "very calm/stable" .dlls by Assembly?
uri: do-you-reference-very-calmstable-dlls-by-assembly
created: 2009-04-28T06:33:27.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 17
  title: Ryan Tee

---



<span class='intro'> 
  <br>
If we lived in a happy world with no bugs, I would be recommending this approach of using shared components from source safe. As per the prior rule, you can see we like to reference &quot;most&quot; .dlls by project. <br>
However if you do choose to reference a .dll without the source, then the important thing is that if the .dll gets updated by another developer, then there is <b>*nothing*</b> to do for all other developers ?they get the last version when they do your next build. Therefore you need to follow this&#58; 
 </span>


  <p>As the component user, there are six steps, but you only need to do them once&#58;</p>
<ol>
    <li>First, we need to get the folder and add it to our project, so in SourceSafe, right click your project and create a subfolder using the Create Project (yes, it is very silly name) menu. <img class="ms-rteCustom-ImageArea" alt="Use Create VSS Folder" src="/Standards/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/use_createvssfolder.jpg" /> <span class="ms-rteCustom-FigureNormal">Figure&#58; Create 'folder' in Visual Source Safe</span>
    <p>Name it References</p>
    <img class="ms-rteCustom-ImageArea" alt="Use References Folder" src="/Standards/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/use_referencesfolder.jpg" /> <span class="ms-rteCustom-FigureNormal">Figure&#58; 'References' folder</span> </li>
    <li>Share the dll from the directory, so if I want SSW.Framework.Configuration, I go to $/ssw/SSWFramework/Configuration/bin/Release/<br>
    I select both the dll and the dll.xml files, right-click and drag them into my $/ssw/zzRefs/References/ folder that I just created in step 1. <img class="ms-rteCustom-ImageArea" alt="Use Dlls Xml" src="/Standards/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/use_dllsxml.jpg" /> <span class="ms-rteCustom-FigureNormal">Figure&#58; Select the dlls that I want to use</span> <img class="ms-rteCustom-ImageArea" alt="Use right click to share" src="/Standards/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/use_rightclicktoshare.jpg" /> <span class="ms-rteCustom-FigureNormal">Figure&#58; Right drag, and select &quot;Share&quot;</span> </li>
    <li>Still in SourceSafe, select the References folder, run get latest?to copy the latest version onto your working directory.<br>
    <img class="ms-rteCustom-ImageArea" alt="Use Get Latest" src="/Standards/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/use_getlatest.jpg" /> <span class="ms-rteCustom-FigureNormal">Figure&#58; Get Latest from Visual Source Safe</span> VSS may ask you if you want to create the folder, if it doesnt exist. Yes, we do. </li>
    <li>Back in VS.NET, select the project and click the show-all files button in the solution explorer, include the References folder into the project (or get-latest if its already there)<br>
    <img class="ms-rteCustom-ImageArea" alt="Use Include Invs" src="/Standards/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/use_includeinvs.jpg" /> <span class="ms-rteCustom-FigureNormal">Figure&#58; Include the files into the current project</span> </li>
    <li>IMPORTANT! If the files are checked-out to you when you include them into your project, you MUST un-do checkout immediately.<br>
    You should never check in these files, they are for get-latest only.<br>
    <img class="ms-rteCustom-ImageArea" alt="Use Undo Checkout" src="/Standards/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/use_undocheckout.jpg" /> <span class="ms-rteCustom-FigureNormal">Figure&#58; Undo Checkout, when VS.NET checked them out for you...</span> </li>
    <li>Add Reference?in VS.NET, browse to the References?subfolder and use the dll there. </li>
    <li>IMPORTANT! You need to keep your 'References' folder, and not check the files directly into your bin directory. Otherwise when you 'get latest', you won't be able to get the latest shared component. </li>
</ol>
<p>All done. In the future, whenever you do get-latest?on the project, the any updated dlls should come down and be linked the next time you compile. Also, if anyone checks out your project from Source Safe, they will have the project linked and ready to go.</p>



