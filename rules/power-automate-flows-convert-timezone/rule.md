---
type: rule
title: Do you if you are using correct timezone when using flows?
uri: power-automate-flows-convert-timezone
authors:
  - title: Aman Kumar
    url: https://ssw.com.au/people/aman-kumar
related: []
created: 2023-10-12T12:33:21.000Z
guid: f20c1d67-fbd5-4fa6-99ba-58b4c8f53fd7
---

When working with Power Automate flows, there are instances where we need to display or compare the time in your flow, by default, it's set to UTC.

However, there are chances that you inadvertently not using the right timezone for you flow.

<!--endintro-->

Here is bad example of comparing datetime in PA Flows:

::: bad
![Figure: Bad example - You are comparing the UTC with UTC](comparing-timedate-without-converting.png)
:::

So to convert the timezone you can use built-in expression in your flow:

```json
convertTimeZone({{ array/object }}?[{{ 'timedate variable' }}], 'UTC', 'AUS Eastern Standard Time')
```

::: good
![Figure: Good example - You are comparing it in local timezone (i.e AEST with AEST)](convert-timezone-expression.gif)
:::

For further details on converting timezones in Power Automate Flow, refer to the [Microsoft Learn - Converting time zone](https://learn.microsoft.com/en-us/troubleshoot/power-platform/power-automate/converting-time-zone-power-automate).
For default timezones, refer to the [Microsoft Learn - Default time zones](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/default-time-zones?view=windows-11).
