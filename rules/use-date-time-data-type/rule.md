---
type: rule
archivedreason:
title: Parameters/Internationalization - Do you use the DateTime data type for date parameters?
guid: 26752bb7-6b48-46a7-a232-e4a54382f904
uri: use-date-time-data-type
created: 2024-08-02T10:38:33.0000000Z
authors: 
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
related:
- when-to-use-reporting-services
redirects: []

---

Use the DateTime data type for date parameters instead of using strings. There are 3 reasons to do this:

<!--endintro-->

1. Stop the bug "Cannot read the next data row for the data set"
Although a hardcoded string will work, it will not work for all users regional date/time settings.
E.g. a string data type parameter with a value of "26/01/2006" is correct for "dd/mm/yyyy", but it is wrong for "mm/dd/yyyy"

2. When SQL Reporting Services is using the DateTime data type parameter, it will get the datetime value on the users setting (aka the Culture DateTime format).

3. Your users also get the advantage of a date/time picker control, which automatically works out the correct regional date format. This solves the US/Australian date problem. (i.e. DD and MM are reversed).

::: bad  
![Figure: Bad example - Using the String data type for date parameter](RSRulesUseDateTimeType1.jpg)  
:::

::: good  
![Figure: Good example - Use DateTime data type for the date parameter - you will not get internationalization bugs and it gives users a calendar control](RSRulesUseDateTimeType2.jpg)
:::

::: greybox
We have a program called [SSW Code Auditor](https://codeauditor.com) to check for this rule.
:::
