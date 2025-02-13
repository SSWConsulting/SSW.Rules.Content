---
seoDescription: Avoid empty reports by using database queries to set valid default parameter values in SQL Reporting Services, ensuring meaningful results for users.
type: rule
archivedreason:
title: Parameters - Do you avoid showing empty reports?
guid: 31728c17-c348-458c-b8e3-601d30987706
uri: avoid-showing-empty-reports
created: 2024-08-02T10:30:33.0000000Z
authors: 
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
related:
- when-to-use-reporting-services
redirects: []

---

When a user opens a report, they expect to see something. It is the developer's job to get the default values for parameters right. Default parameters allow the user to see what they expect... a report, and they also show users the expected format for parameters and make it easier to run validation tests to see if all the reports on your server are working correctly And of course you don't get it right by hard coding defaults.

<!--endintro-->

::: bad  
![Figure: Bad example - Making a user select the parameters before seeing the data](RSRulesNoEmptyReportT07.jpg)  
:::

The following report shows nothing, because the parameters are using meaningless default values (in this case, old dates for the year 2006)

::: bad  
![Figure: Bad example - Empty report caused by incorrect parameter default values (probably hard coded for when the developer wrote the report in 2006)](RSRulesNoEmptyReportT7.jpg)  
:::

::: good  
![Figure: Good example - This report shows initial data as the developer configure useful parameters (in this case default values for the entire month of October Note: in US date format)](RSRulesNoEmptyReportT8.gif)
:::

In SQL Reporting Services, parameters can be:

* hard coded
* an expression, or
* from a query

Hard coded values should never be used. Expressions may be good for some instances, but because it's not linked with your data, it may not be good enough.

```sql
--Expression to get the 1st day of the previous month (aka Start Date)
DateSerial(iif( Month(DateTime.Now)=1, Year(DateTime.Now)-1, Year(DateTime.Now)), iif( Month(DateTime.Now)=1, 12, Month(DateTime.Now) - 1), 1)

--Expression to get the 1st day of the current month (aka End Date)
DateSerial(Year(DateTime.Now), Month(DateTime.Now),1)

--Expression to get the 1st day of the next month
DateSerial(iif( Month(DateTime.Now)=12, Year(DateTime.Now)+1, Year(DateTime.Now)), iif( Month(DateTime.Now)=12, 1, Month(DateTime.Now) + 1), 1)
```

::: bad  
Bad example - Expressions to set the date range to the current month
:::

::: bad  
![Figure: Bad example - Using an Expression to set the default values.(This will not be good enough if there is no data in the current month)](RSRulesNoEmptyReportT11.jpg)  
:::

The Solution:

In order to give report parameters correct default values, you should always use query to generate these values from database. This will ensure your default values come from your data, so they won't fail to give some records.

```sql
**--Query to generate valid date from existing data**
SELECT
CONVERT(
DATETIME, 
'1, ' + 
DATENAME(month, DATEADD(month, 1, MAX(OrderDate)))+ 
DATENAME(year, DATEADD(month, 1, MAX(OrderDate)))
) AS EndOfMonth,
CONVERT(
DATETIME, 
'1,'+ 
DATENAME(month, MAX(OrderDate))+ 
DATENAME(year, MAX(OrderDate)) 
) AS StartOfMonth
FROM Orders
```

::: good  
Good example - Using a query to retrieve the last month of available data
:::

::: good  
![Figure: Good example - Using a query to set default values for report parameters](RSRulesNoEmptyReportT10.jpg)
:::

The dataset 'ValidDates' looks similar to this:

![Figure: Create a dataset to query the data and provide useful default parameter values for your report](RSRulesNoEmptyReportT9.jpg)
