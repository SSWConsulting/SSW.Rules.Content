---
type: rule
title: Middle Tier - Do you submit all dates to SQL Server in ISO format?
uri: submit-all-dates-to-sql-server-in-iso-format
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - middle-tier-do-you-submit-all-dates-to-sql-server-in-iso-format
created: 2019-11-14T22:25:52.000Z
archivedreason: Replaced by [https://ssw.com.au/rules/parameterize-all-input-to-your-database](/rules/parameterize-all-input-to-your-database)
guid: bbe5b2b7-2422-4f31-a559-1f32c35965f3
---

All dates submitted to SQL Server must be in ISO format date. This ensures that language or database settings do not interfere with inserts and updates of data. You should NEVER need to change the default language of users or of the database in SQL Server.

For example, any insert into a SQL Server database with Visual Basic should call `Format(ctlStartDate,"yyyy-mm-dd")` or VB.NET `Ctype(ctlStartDate.Text,Date).ToString("yyyy-MM-dd")` before attempting the insert or update. This will ensure consistency of treatment when dealing with dates in your SQL Server backend.

<!--endintro-->

```sql
SET DATEFORMAT mdy

 print convert( datetime, '2020-07-01' )

 -- returns Jul 1 2020 12:00AM

 print convert( datetime, '01/07/2020' )

 -- returns Jan 7 2020 12:00AM

 print convert( datetime, '20200701' )

 -- returns Jul 1 2020 12:00AM

SET DATEFORMAT dmy

 print convert( datetime, '2020-07-01' )

 -- returns Jan 7 2020 12:00AM, opposite of above

 print convert( datetime, '01/07/2020' )

 -- returns Jul 1 2020 12:00AM, opposite of above

 print convert( datetime, '20200701' )

 -- returns Jul 1 2020 12:00AM, only one which is same as above
```

::: good
Code - ISO format date is the best
:::

The extended format can still mix up month & day in some circumstances, whereas the basic format is the only one that always works correctly.

To be even more pedantic, when you include the time as well as the date, the value isn't really an ISO value at all! The ISO representation of a date/time would be '20200701T0958', whereas for SQL you should send it as '20200701 09:58'. This isn't even the extended ISO format as it is missing the obligatory "T" character (ref. section 5.4.1 of the standard).

(The standard does allow you to "be omitted in applications where there is no risk of confusing", but it doesn't allow you to add a space or mix basic date with extended time.)

So, if you want to be absolutely correct then it may be best to remove the reference to ISO, so that your rule works for date/time as well as just dates.

The technical term used in the SQL help is "Unseparated String Format" (easily searched for).

The help specifies that this format is unaffected by the SET DATEFORMAT command (which depends on any locale settings for SQL Server or the computer it is installed on).

"The SET DATEFORMAT session setting does not apply to all-numeric date entries (numeric entries without separators). Six- or eight-digit strings are always interpreted as ymd."

[What is ISO format date?](https://www.w3.org/QA/Tips/iso-date)
