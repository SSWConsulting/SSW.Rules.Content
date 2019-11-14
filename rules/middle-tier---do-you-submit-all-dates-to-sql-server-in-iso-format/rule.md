---
type: rule
title: Middle Tier - Do you submit all dates to SQL Server in ISO format?
uri: middle-tier---do-you-submit-all-dates-to-sql-server-in-iso-format
created: 2019-11-14T22:25:52.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p class="ssw15-rteElement-P">All dates submitted to SQL Server must be in ISO format date. This ensures that language or database settings do not interfere with inserts and updates of data. You should&#160;NEVER&#160;need to change the default language of users or of the database in SQL Server. For example, any insert into a SQL Server database with Visual Basic should call Format(ctlStartDate,&quot;yyyy-mm-dd&quot;) or VB.NET Ctype(ctlStartDate.Text,Date).ToString(&quot;yyyy-MM-dd&quot;) before attempting the insert or update. This will ensure consistency of treatment when dealing with dates in your SQL Server backend.​​<br></p> </span>

<p class="ssw15-rteElement-CodeArea">​SET DATEFORMAT mdy<br><br> print convert( datetime, '2003-07-01' )<br><br> -- returns Jul 1 2003 12&#58;00AM<br><br> print convert( datetime, '01/07/2003' )<br><br> -- returns Jan 7 2003 12&#58;00AM<br><br> print convert( datetime, '20030701' )<br><br> -- returns Jul 1 2003 12&#58;00AM<br><br>SET DATEFORMAT dmy<br><br> print convert( datetime, '2003-07-01' )<br><br> -- returns Jan 7 2003 12&#58;00AM, opposite of above<br><br> print convert( datetime, '01/07/2003' )<br><br> -- returns Jul 1 2003 12&#58;00AM, opposite of above<br><br> print convert( datetime, '20030701' )<br><br> -- returns Jul 1 2003 12&#58;00AM, only one which is same as above</p><dd class="ssw15-rteElement-FigureGood">​Code - ISO format date is the best.​</dd><p><br>The extended format can still mix up month &amp; day in some circumstances, whereas the basic format is the only one that always works correctly.</p><p>To be even more pedantic, when you include the time as well as the date, the value isn't really an ISO value at all! The ISO representation of a date/time would be '20030701T0958', whereas for SQL you should send it as '20030701 09&#58;58'. This isn't even the extended ISO format as it is missing the obligatory &quot;T&quot; character (ref. section 5.4.1 of the standard).</p><p>(The standard does allow you to &quot;be omitted in applications where there is no risk of confusing&quot;, but it doesn't allow you to add a space or mix basic date with extended time.)</p><p>So, if you want to be absolutely correct then it may be best to remove the reference to ISO, so that your rule works for date/time as well as just dates.</p><p>The technical term used in the SQL help is &quot;Unseparated String Format&quot; (easily searched for).</p><p>The help specifies that this format is unaffected by the SET DATEFORMAT command (which depends on any locale settings for SQL Server or the computer it is installed on).</p><p>&quot;The SET DATEFORMAT session setting does not apply to all-numeric date entries (numeric entries without separators). Six- or eight-digit strings are always interpreted as ymd.&quot;</p><p><a href="https&#58;//www.w3.org/QA/Tips/iso-date">​What is ISO format date?&#160;​</a><br></p>


