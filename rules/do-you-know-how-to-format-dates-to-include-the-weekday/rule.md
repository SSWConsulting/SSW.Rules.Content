---
type: rule
archivedreason: 
title: Do you know how to format dates to include the weekday?
guid: 11a7a554-2fd9-4dad-a588-a06f7e56c68f
uri: do-you-know-how-to-format-dates-to-include-the-weekday
created: 2009-06-26T10:07:46.0000000Z
authors:
- id: 9
  title: William Yin
related: []

---

[[badExample]]
| ![using the default Date Format](BadDateFormat.gif)


[[goodExample]]
| ![using the Date Format with 'ddd'](GoodDateFormat.gif)

**How do you do this ?** 

<!--endintro-->
 By default, the date type column only have two format options:


![Date Format #1](DateFormateDateOnly.gif)
![Date Format #2](DateFormateDateAndTime.gif)
** To add the week day(eg.Wed) you need to: 
1. Select List Settings | Columns |Create column | Calculated (calculation based on other columns)
2. See the columns of this list in the "Insert Column", add the column you want to change format, and custom the code in "Formula" like below:  
![Calculated column with Formula code](CalculatedColumnWithFormulaCode.gif)
3. Change the views of the list to use the new Calculated column (WeekDate) instead of the original date column (Date): 
![Replace the old Date column](ReplaceOldDate.gif)(Date) with new Calculated column (WeekDate It should not be this hard - see [suggestion to the SharePoint team to make date formatting easier](http://www.ssw.com.au/ssw/Standards/BetterSoftwareSuggestions/SharePointTeamServices.aspx#ChangeDateFormatShouldBeEasier).**
