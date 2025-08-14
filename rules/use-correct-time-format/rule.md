---
seoDescription: Clear, unambiguous dates and times prevent missed meetings, costly travel mistakes, and confusion across countries and time zones.
type: rule
title: Appointments - Do you use the correct time and date format?
uri: use-correct-time-format
authors:
  - title: Jimmy Chen
    url: https://www.ssw.com.au/people/jimmy-chen
related:
  - human-friendly-date-and-time
  - add-days-to-dates
redirects:
  - do-you-use-the-correct-time-and-date-format
  - use-correct-time-and-date-format
created: 2025-08-14T00:00:00.000Z
guid: afaf5136-9229-48b3-9b5e-c2b781e782b2
---

Clear, unambiguous dates and times prevent missed meetings, costly travel mistakes, and confusion across countries and time zones. 

::: greybox
“Catch up moved to 10/05 at 6. See you then”
:::

Think about this, is that 10th of May or 5th of October? Is it 6 AM or 6 PM?

<!--endintro-->

## Dates - kill the ambiguity

People in different regions format the date in different ways: 

::: img-medium  
![Figure: 10/05/25 reads differently to Aussie, American and Chinese](image-use-correct-time-format-1.png)
:::

Software can also misinterpret it. For example, entering 10/05/2025 on an Aussie laptop could be read as October 5th, 2025, if opened on an American system.

This is why you should avoid numeric-only formats... they can cause major confusion. To make it even clearer, [include abbreviated weekdays with dates](/add-days-to-dates).

::: greybox
"This email was sent on 10/05/25."  
:::
::: bad
Bad example - Use slashes on their own, it’s ambiguous
:::

::: greybox
"The email was sent on Sat 10 May 2025."
:::
::: good
Good example - Use "DD MMM YYYY" and include the abbreviated day of the week
:::

## Times - 24-hour or am/pm — both are fine (correctly!)

Use valid formats to avoid confusion - both 24-hour and 12-hour formats are universal when used correctly:

::: greybox
  - The user group will start at 18:00 tomorrow (24-hour format)
  - The user group will start at 6 PM tomorrow (12-hour format)
:::
::: good
Good example - Correct formatting for time
:::

::: greybox
  - The user group will start at 6 (is this AM or PM?)
  - The user group will start at 18 PM (invalid format)
  - The user group will start at 6.00 PM (use of dot)
:::
::: bad
Bad example - Incorrect or ambiguous times
:::

Avoid the 12 PM / 12 PM trap.
  - Use "noon" or "midnight" to the end of the time instead of just 12:00. E.g., 12:00 noon.
  - For boundaries (e.g., validity periods), avoid 00:00; use 00:01 for start and 23:59 for end (common airline practice) to remove doubt.

::: img-medium  
![Figure: Will you attend this event on the night of the 14th or the 15th?](image-use-correct-time-format-2.png)
:::

Always include a time zone for cross-location events: AEST (UTC+10), AEDT (UTC+11), PT (UTC–8), etc.

### Extra tips

  - Use leading zeros in 24-hour times: 09:05, not 9:5
  - Don’t mix separators: use “:” for time, not “. “or “h.”
  - It is recommended to use the ISO standard (YYYY-MM-DD) for your filenames, so they can be sorted in descending or ascending order by time
      - e.g., 2025-08-15-sprint-review-notes.md
