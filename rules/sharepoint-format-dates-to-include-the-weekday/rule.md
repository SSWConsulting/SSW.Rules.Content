---
seoDescription: Format dates to include weekdays using calculated columns and formulas in SharePoint.
type: rule
archivedreason:
title: Do you know how to format dates to include the weekday in SharePoint?
guid: 11a7a554-2fd9-4dad-a588-a06f7e56c68f
uri: sharepoint-format-dates-to-include-the-weekday 
created: 2009-06-26T10:07:46.0000000Z
authors:
  - title: William Yin
    url: https://ssw.com.au/people/william-yin
related: 
  - human-friendly-date-and-time
  - add-days-to-dates
redirects:
  - do-you-know-how-to-format-dates-to-include-the-weekday
---

Format dates to include weekdays using calculated columns and formulas in SharePoint.

<!--endintro-->

::: bad
![Figure: Bad example - Using the default Date Format](BadDateFormat.gif)
:::

::: good
![Figure: Good example - Using the Date Format with 'ddd'](GoodDateFormat.gif)
:::

## How do you do this?

By default, the date type column only have two format options:

![Figure: Date Format #1](DateFormateDateOnly.gif)

![Figure: Date Format #2](DateFormateDateAndTime.gif)

To add the week day(eg.Wed) you need to:

1. Select List Settings | Columns |Create column | Calculated (calculation based on other columns)
2. See the columns of this list in the "Insert Column", add the column you want to change format, and custom the code in "Formula" like below:

![Figure: Calculated column with Formula code](CalculatedColumnWithFormulaCode.gif)

3. Change the views of the list to use the new Calculated column (WeekDate) instead of the original date column (Date):

![Figure: Replace the old Date column (Date) with new Calculated column (WeekDate It should not be this hard)](ReplaceOldDate.gif)
