---
type: rule
title: Data - Dates - Do you make sure you have valid date data in your database?
uri: data---dates---do-you-make-sure-you-have-valid-date-data-in-your-database
created: 2019-11-25T19:27:33.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> SQL Server dates can range from year 1900 up to year 9999. However, certain date data in your database just wouldn't make any sense in the context of your business. For example, if your company started trading in 2005 you should not have any dates in your database before 2005 (unless you are tracking start dates of your clients, but this is an exception). An invoice date of 2003 wouldn't make sense at all. You should run validation queries to ensure no rubbush date data gets into your database.​<br> </span>




