---
type: rule
title: Do you know how to format dates to include the weekday?
uri: do-you-know-how-to-format-dates-to-include-the-weekday
created: 2009-06-26T10:07:46.0000000Z
authors:
- id: 9
  title: William Yin

---



<span class='intro'> <p><span class="ms-rteCustom-ImageArea"><img style="border-bottom&#58;0px solid;border-left&#58;0px solid;border-top&#58;0px solid;border-right&#58;0px solid;" border="0" src="/Standards/SoftwareDevelopment/RulesToBetterSharePoint/PublishingImages/BadDateFormat.gif" /></span><br><span class="ms-rteCustom-FigureBad">Figure&#58; Bad example - using the default Date Format</span></p>
<p><span class="ms-rteCustom-ImageArea"><img style="border-bottom&#58;0px solid;border-left&#58;0px solid;border-top&#58;0px solid;border-right&#58;0px solid;" border="0" src="/Standards/SoftwareDevelopment/RulesToBetterSharePoint/PublishingImages/GoodDateFormat.gif" /></span><br><span class="ms-rteCustom-FigureGood">Figure&#58; Good example - using the Date Format with 'ddd'</span></p>
<p><strong>How do you do this ?</strong></p> </span>

<p>By default, the date type column only have two format options&#58;<br><br>&#160;&#160;&#160;&#160; <span class="ms-rteCustom-ImageArea">&#160;<img style="border-bottom&#58;0px solid;border-left&#58;0px solid;border-top&#58;0px solid;border-right&#58;0px solid;" border="0" src="/Standards/SoftwareDevelopment/RulesToBetterSharePoint/PublishingImages/DateFormateDateOnly.gif" /></span></p>
<blockquote style="margin-right&#58;0px;" dir="ltr"><span style="margin&#58;0in;font-family&#58;calibri;font-size&#58;11pt;" lang="en-AU" class="ms-rteCustom-FigureNormal">&#160;&#160; &#160;&#160; Figure&#58; Date Format #1</span><span style="margin&#58;0in;font-family&#58;calibri;font-size&#58;11pt;" lang="en-AU" class="ms-rteCustom-FigureNormal"></span><span style="margin&#58;0in;font-family&#58;calibri;font-size&#58;11pt;" lang="en-AU" class="ms-rteCustom-FigureNormal"><span class="ms-rteCustom-ImageArea"><img style="border-bottom&#58;0px solid;border-left&#58;0px solid;border-top&#58;0px solid;border-right&#58;0px solid;" border="0" src="/Standards/SoftwareDevelopment/RulesToBetterSharePoint/PublishingImages/DateFormateDateAndTime.gif" /></span></span><span style="margin&#58;0in;font-family&#58;calibri;font-size&#58;11pt;" lang="en-AU" class="ms-rteCustom-FigureNormal">&#160; &#160;&#160;&#160; Figure&#58; Date Format #2</span><span style="margin&#58;0in;font-family&#58;calibri;font-size&#58;11pt;" lang="en-AU" class="ms-rteCustom-FigureNormal"></span></blockquote>
<p style="margin&#58;0in;font-family&#58;calibri;font-size&#58;11pt;" lang="en-AU">To add the week day(eg.Wed) you need to&#58;</p>
<p style="margin-top&#58;0px;margin-bottom&#58;0px;vertical-align&#58;middle;"><span style="font-family&#58;calibri;font-size&#58;11pt;" lang="en-AU">1)&#160;Select List Settings&#160;| Columns |Create column&#160;| </span><span style="font-family&#58;calibri;font-size&#58;11pt;" lang="en-US">Calculated (calculation based on other columns)</span></p>
<p style="margin-top&#58;0px;margin-bottom&#58;0px;vertical-align&#58;middle;"><span style="font-family&#58;calibri;font-size&#58;11pt;" lang="en-US">2) See the columns of this list in the &quot;Insert Column&quot;, add the column you want to change format,<span>&#160; </span>and custom the code in &quot;Formula&quot; like below&#58;</span></p>
<p><span><span class="ms-rteCustom-ImageArea"><img border="0" src="/Standards/SoftwareDevelopment/RulesToBetterSharePoint/PublishingImages/CalculatedColumnWithFormulaCode.gif" /></span><br></span><span class="ms-rteCustom-FigureNormal">Figure&#58; Calculated column with Formula code</span></p>
<p><span>3)&#160;Change the views of the list to use the new Calculated column (WeekDate) instead of the original date column (Date)&#58;</span></p><span>
<p><span class="ms-rteCustom-ImageArea"><img border="0" src="/Standards/SoftwareDevelopment/RulesToBetterSharePoint/PublishingImages/ReplaceOldDate.gif" /></span></span><br></p><span class="ms-rteCustom-FigureNormal"><span>Figure&#58; Replace the old Date column (Date) with new Calculated column (WeekDate)</span></span><span class="ms-rteCustom-FigureNormal"></span><span class="ms-rteCustom-FigureNormal"></span>It should not be this hard - see <a title="" href="http&#58;//www.ssw.com.au/ssw/Standards/BetterSoftwareSuggestions/SharePointTeamServices.aspx#ChangeDateFormatShouldBeEasier">suggestion to the SharePoint team to make date formatting easier</a>.


