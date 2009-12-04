---
type: rule
archivedreason: 
title: Do you use the designer for all visual elements?
guid: d402bae6-c5e4-4e99-9287-bc33c14bb5ac
uri: do-you-use-the-designer-for-all-visual-elements
created: 2009-04-28T02:20:39.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ryan Tee
  url: https://ssw.com.au/people/ryan-tee
related: []
redirects: []

---


This field should not be null (Remove me when you edit this field).
<br><excerpt class='endintro'></excerpt><br>

  <p>Things that do not belong in the designer&#58;</p>
<ul>
    <li>Connections </li>
    <li>Commands </li>
    <li>DataAdapters </li>
</ul>
<p>However, and <b>DataAdapter</b> objects should not be dragged onto forms, as they belong in the business tier. Strongly typed <b>DataSet</b> objects should be in the designer as they are simply passed to the business layer. Avoid writing code for properties that can be set in the designer.</p>
<img alt="" class="ms-rteCustom-ImageArea" src="/Standards/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/BadDesigner.gif" /> <span class="ms-rteCustom-FigureBad">Bad example - Connection and Command objects in the Designer</span> <img alt="" class="ms-rteCustom-ImageArea" src="/Standards/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/GoodDesigner.gif" /> <span class="ms-rteCustom-FigureGood">Good example - Only visual elements in the designer</span>



