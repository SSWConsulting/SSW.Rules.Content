---
type: rule
archivedreason: 
title: Data - Dates - Do you know DateTime fields must be converted to universal time?
guid: 96636654-80f5-46c9-adb0-a8ddfe98e7e3
uri: datetime-fields-must-be-converted-to-universal-time
created: 2019-11-25T19:54:23.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Christian Morford-Waite
  url: https://ssw.com.au/people/christian-morford-waite
related: []
redirects:
- data-dates-do-you-know-datetime-fields-must-be-converted-to-universal-time

---

Any DateTime fields must be converted to universal time from the application to the stored procedures when storing data into the database.

We can simplify dealing with datetime conversions by using a date and time API such as [Noda TIme](https://nodatime.org).

<!--endintro-->

Noda Time uses the concept of an Instant representing a global point in time, which is first converted to UTC time and then to the users local time when required for display.
An Instant is the number of nanoseconds since January 1st 1970. Using an Instant gives more granularity than datetime because it uses nanoseconds rather than ticks (100 nanoseconds).

```csharp
//------ .NET DateTime Examples
int year, month, day;
int hour, minute, second;

long nowInTicks = DateTime.Now.Ticks;             //      637158251390332189
DateTime now = DateTime.Now;                    
DateTime nowUtc = DateTime.UtcNow;
DateTime date = new DateTime(2020, 1, 2);        //      2/01/2020 12:00:00 AM
TimeSpan time = new TimeSpan(16, 20, 0);        //      16:20:00
DateTime dateTime = date + time;                     //      2/01/2020 4:20:00 PM

date = dateTime.Date;
time = dateTime.TimeOfDay;
year = date.Year;
month = date.Month;
day = date.Day;
hour = time.Hours;
minute = time.Minutes;
second = time.Seconds;

int startDate = (int)date.DayOfWeek;
int target = (int)DayOfWeek.Wednesday;
if (target <= startDate)
    target += 7;
DateTime nextWednesday = date.AddDays(target - startDate);     //     8/01/2020 12:00:00 AM

startDate = (int)date.DayOfWeek;
target = (int)DayOfWeek.Friday;
if (target > startDate)
    target -= 7;
DateTime lastFriday = date.AddDays(-(startDate - target));         //     27/12/2019 12:00:00 AM

TimeSpan t1 = TimeSpan.FromDays(1.0);
TimeSpan t2 = TimeSpan.FromHours(1.0);

int timespanCheck = TimeSpan.Compare(t1, t2);
TimeSpan longestSpan;
TimeSpan shortestSpan;
if(timespanCheck > 0)
{
    longestSpan = t1;
    shortestSpan = t2;
} 
else if(timespanCheck < 0)
{
    shortestSpan = t1;
    longestSpan = t2;
}
```

::: bad
Figure: Bad example - Using .NET DateTime to manipulate dates and times
:::

```csharp
//------    Noda Time Examples
int year, month, day;
int hour, minute, second;

Instant nowAsInstant = SystemClock.Instance.GetCurrentInstant(); //   2020-01-28T05:18:26Z

DateTimeZone zone = DateTimeZoneProviders.Tzdb["Australia/Melbourne"];
ZonedClock utcClock = SystemClock.Instance.InUtc();
ZonedClock localClock = SystemClock.Instance.InZone(zone);
LocalDate ntDate = new LocalDate(2020, 1, 2);   //      Thursday, 2 January 2020
LocalTime ntTime = new LocalTime(16, 20);       //      4:20:00 PM
LocalDateTime ntdateTime = ntDate.At(ntTime);   //      2/01/2020 4:20:00 PM

ntdateTime.Deconstruct(out ntDate, out ntTime);
ntDate.Deconstruct(out year, out month, out day);
ntTime.Deconstruct(out hour, out minute, out second);

LocalDate ntNextWednesday = ntDate.Next(IsoDayOfWeek.Wednesday); //    Wednesday, 8 January 2020
LocalDate ntLastFriday = ntDate.Previous(IsoDayOfWeek.Friday);   //    Friday, 27 December 2019

Duration d1 = Duration.FromDays(1);
Duration d2 = Duration.FromHours(1);
Duration longestDuration = Duration.Max(d1, d2);
Duration shortestDuration = Duration.Min(d1, d2);
```

::: good
Figure: Good example - Using Noda Time to manipulate dates and times
:::

When retrieving data from the database it must be converted back to the local time of the user.

That way you get an accurate representation of the time someone entered data into the database (i.e. the DateUpdated field).
The exception to this rule, however, is for already existing databases that deal with DateTime as part of their queries.
e.g. SSW TimePro is an application that allows employees to enter their timesheet.
The table used for storing this information has an important field that has a DateTime data type.

This cannot be converted to UTC in the database because that would mean:

1. Converting every single entry since entries began being stored (in SSW's case since 1996) to keep information consistent;
2. Other separate applications currently using the timesheet information in the database for reporting will also have to be entirely modified.

Currently, there will be an issue if for example, someone from the US (Pacific time) has 19 hours difference between their local time and our servers.

**Example:** Sally in the US enters a timesheet for the 21/04/05. (which will default to have a time of 12:00:00 AM since the time was not specified)
Our servers will store it as 21/04/05 19:00:00 in other words 21/04/05 07:00:00 PM because the .NET Framework will automatically convert the time accordingly for our Web Service.
Therefore our servers have to take the Date component of the DateTime and add the Time component as 12:00:00 AM to make it stored in our local time format.

```csharp
[WebMethod] 
public double GetDateDifference(DateTime dateRemote) 
{ 
    DateTime dateLocal = dateRemote.Date; 
    return (dateRemote.TimeOfDay.TotalHours - dateLocal.TimeOfDay.TotalHours); 
}
```

**Figure: When dateRemote is passed in from the remote machine, .NET Framework will have already converted it to the UTC equivalent for the local server (i.e. the necessary hours would have been added to cater for the local server time)**

In the above code snippet, the .Date property would cut off the Time portion of the DateTime variable and set the Time portion to "12:00:00 AM" as default.

This is for applications we currently have that:

1. Consider the DateTime component integral for the implementation of the application.
2. Will be used world-wide.
