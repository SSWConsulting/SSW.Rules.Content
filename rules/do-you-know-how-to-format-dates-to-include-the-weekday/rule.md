---
type: rule
title: Do you know how to format dates to include the weekday?
uri: do-you-know-how-to-format-dates-to-include-the-weekday
created: 2009-06-26T10:07:46.0000000Z
authors:
- id: 9
  title: William Yin

---



<span class='intro'> This field should not be null (Remove me when you edit this field). </span>

To achieve this , you can &#58; 
<p style="margin-top&#58;0px;margin-bottom&#58;0px;vertical-align&#58;middle;"><span style="font-family&#58;calibri;font-size&#58;11pt;" lang="en-AU">Step1&#58; &#160;List Settings - columns -Create column - </span><span style="font-family&#58;calibri;font-size&#58;11pt;" lang="en-US">Calculated (calculation based on other columns),then you can see the columns of this list in the &quot;Insert Column&quot;, add the column you want to change format,<span>&#160; </span>and custom the code in &quot;Formula&quot; like below&#58;</span></p>
<p><span><span class="ms-rteCustom-ImageArea"><img border="0" src="/Standards/CodeAndApplicationDesign/RulesToBetterSharePoint/PublishingImages/CalculatedColumnWithFormulaCode.gif" /></span><br></span><span class="ms-rteCustom-FigureNormal">Figure&#58; Calculated column with Formula code.</span></p>
<p><span>Step2&#58; Change the views of the list to use the new Calculated column(WeekDate) instead of the original date column(Date)&#58;</span></p>
<p><span><span class="ms-rteCustom-ImageArea"><img border="0" src="/Standards/CodeAndApplicationDesign/RulesToBetterSharePoint/PublishingImages/ReplaceOldDate.gif" /></span></span><br><span class="ms-rteCustom-FigureNormal"><span>Figure&#58; Replace the old Date column(Date) with new Calculated column(WeekDate).</span> </span></p>


