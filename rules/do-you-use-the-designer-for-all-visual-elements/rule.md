---
type: rule
title: Do you use the designer for all visual elements?
uri: do-you-use-the-designer-for-all-visual-elements
created: 2009-04-28T02:20:39.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 17
  title: Ryan Tee

---



<span class='intro'> This field should not be null (Remove me when you edit this field). </span>


  <p>Things that do not belong in the designer&#58;</p>
<ul>
    <li>Connections </li>
    <li>Commands </li>
    <li>DataAdapters </li>
</ul>
<p>However, and <b>DataAdapter</b> objects should not be dragged onto forms, as they belong in the business tier. Strongly typed <b>DataSet</b> objects should be in the designer as they are simply passed to the business layer. Avoid writing code for properties that can be set in the designer.</p>
<img alt="" class="ms-rteCustom-ImageArea" src="/Standards/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/BadDesigner.gif" /> <span class="ms-rteCustom-FigureBad">Bad example - Connection and Command objects in the Designer</span> <img alt="" class="ms-rteCustom-ImageArea" src="/Standards/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/GoodDesigner.gif" /> <span class="ms-rteCustom-FigureGood">Good example - Only visual elements in the designer</span>



