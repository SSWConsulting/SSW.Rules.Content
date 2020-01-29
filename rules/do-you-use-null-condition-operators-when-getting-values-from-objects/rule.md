---
type: rule
archivedreason: 
title: Do you use null condition operators when getting values from objects
guid: af72188f-fb7d-452b-a23e-348ecaca6093
uri: do-you-use-null-condition-operators-when-getting-values-from-objects
created: 2020-01-29T05:20:27.0000000Z
authors:
- id: 66
  title: Liam Elliott
- id: 78
  title: Matt Wicks
related: []

---


​Null-conditional operators - makes checking for null as easy as inserting a single question mark. The Null-conditional operators feature boils down all of the previously laborious clunky code into a single question mark.<br>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-CodeArea">int length = customer&#160;!= null &amp;&amp; customer.name != null&#160;? customer.name.length &#58; 0;&#160;&#160;</p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad Example - Verbose and complex code checking for nulls<br></dd><p class="ssw15-rteElement-CodeArea">int length = customers?.name?.length ?? 0;<br></p><dd class="ssw15-rteElement-FigureGood">​​Figure&#58; Good Example - Robust and easier to read code<br></dd>


