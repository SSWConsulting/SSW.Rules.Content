---
type: rule
archivedreason: 
title: Data - Dates - Do you make sure you have valid date data in your database?
guid: 08365107-7d14-4ce5-a7f3-2079689322d6
uri: make-sure-you-have-valid-date-data-in-your-database
created: 2019-11-25T19:27:33.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- data-dates-do-you-make-sure-you-have-valid-date-data-in-your-database

---

SQL Server dates can range from the year 1900 up to the year 9999. However, certain date data in your database just wouldn't make any sense in the context of your business. For example, if your company started trading in 2015 you should not have any dates in your database before 2015 (unless you are tracking start dates of your clients, but this is an exception). An invoice date of 2013 wouldn't make sense at all. 



There are two methods to avoid this:


<!--endintro-->

* Using Validation Queries
> You can run validation queries to ensure no rubbish date data gets into your database.

* Using Constraints
> Alternatively, you can use Constraints to limit the date range from your own earliest specified date.

> Here’s an example of implementing a date range constraint.

```sql
CONSTRAINT chk_INVOICE_DATE CHECK (INVOICE_DATE > TO_DATE('2015-01-01', 'yyyy-mm-dd'))
```
