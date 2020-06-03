---
type: rule
title: Do you know how to format dates to include the weekday?
uri: do-you-know-how-to-format-dates-to-include-the-weekday
created: 2009-06-26T10:07:46.0000000Z
authors:
- id: 9
  title: William Yin

---



<span class='intro'>   <img alt="" class="ms-rteCustom-ImageArea" src="/PublishingImages/BadDateFormat.gif" /> <br>
<span class="ms-rteCustom-FigureBad">Figure&#58; Bad example - using the default Date Format</span><br>
<br>
<img alt="" class="ms-rteCustom-ImageArea" src="/PublishingImages/GoodDateFormat.gif" /><br>
<span class="ms-rteCustom-FigureGood">Figure&#58; Good example - using the Date Format with 'ddd'</span><br>
<br>
<strong>How do you do this ?</strong><br>
 </span>

By default, the date type column only have two format options&#58;<br>
<br>
&#160;&#160;&#160;&#160; <img alt="" class="ms-rteCustom-ImageArea" src="/PublishingImages/DateFormateDateOnly.gif" />&#160;<font class="ms-rteCustom-FigureNormal">Figure&#58; Date Format #1 </font><img alt="" class="ms-rteCustom-ImageArea" src="/PublishingImages/DateFormateDateAndTime.gif" border="0" /> <font class="ms-rteCustom-FigureNormal">Figure&#58; Date Format #2 <br>
</font>To add the week day(eg.Wed) you need to&#58;
<ol>
    <li>Select List Settings&#160;| Columns |Create column&#160;| Calculated (calculation based on other columns) </li>
    <li>See the columns of this list in the &quot;Insert Column&quot;, add the column you want to change format, and custom the code in &quot;Formula&quot; like below&#58;&#160; <img alt="" class="ms-rteCustom-ImageArea" src="/PublishingImages/CalculatedColumnWithFormulaCode.gif" />&#160;<br>
    <font class="ms-rteCustom-FigureNormal">Figure&#58; Calculated column with Formula code </font></li>
    <li>&#160;Change the views of the list to use the new Calculated column (WeekDate) instead of the original date column (Date)&#58; <img alt="" class="ms-rteCustom-ImageArea" src="/PublishingImages/ReplaceOldDate.gif" /> <font class="ms-rteCustom-FigureNormal">Figure&#58; Replace the old Date column (Date) with new Calculated column (WeekDate It should not be this hard - see <a href="http&#58;//www.ssw.com.au/ssw/Standards/BetterSoftwareSuggestions/SharePointTeamServices.aspx#ChangeDateFormatShouldBeEasier">suggestion to the SharePoint team to make date formatting easier</a>. </font></li>
</ol>



