---
type: rule
title: Do you know the difference between Calculated Columns and Measures in Power BI?
uri: do-you-know-the-difference-between-calculated-columns-and-measures-in-power-bi
created: 2016-10-24T06:02:07.0000000Z
authors: []

---



<span class='intro'> When you run into a wall in Power BI and feel like you've exhausted the out of the box functionality, that when it's time to investigate what a bit of DAX can do for you.&#160;<br> </span>

<p>There are 2 different things​ you can do with DAX, create a Measure or a Calculated Column.​<br></p><p>Calculated columns&#58;<br></p><ul><li>Stored in the database<br></li><li>Often used to filter/group data<br></li></ul><p></p><p>Measures&#58;<br></p><p></p><ul><li>Computed on aggregates of values<br></li><li>Computed at query time<br></li><li>Often used to give a numerical metric<br></li></ul><div><br></div><p class="ssw15-rteElement-CodeArea">GroupingColumn =&#160;if(value&lt;x, small, if(value&lt;y, medium, large))<br></p><dd class="ssw15-rteElement-FigureGood">Figure -&#160;Good Example&#58;&#160;Nested if statements are a great way to split up your data into groups<br></dd><p></p>


