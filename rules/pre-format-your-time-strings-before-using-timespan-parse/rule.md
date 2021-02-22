---
type: rule
archivedreason: 
title: Do you pre-format your time strings before using TimeSpan.Parse()?
guid: 6d9bcd83-531e-4667-adf6-727ce4c4ce1c
uri: pre-format-your-time-strings-before-using-timespan-parse
created: 2018-04-25T22:00:38.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-pre-format-your-time-strings-before-using-timespan-parse
- do-you-pre-format-your-time-strings-before-using-timespan-parse()

---

TimeSpan.Parse() constructs a Timespan from a time indicated by a specified string. The acceptable parameters for this function are in the format "d.hh:mm" where "d" is the number of days (it is optional), "hh" is hours and is between 0 and 23 and "mm" is minutes and is between 0 and 59. If you try to pass, as a parameter, as a string such as "45:30" (meaning 45 hours and 30 minutes), TimeSpan.Parse() function will crash. (The exact exception received is: "System.OverflowException: TimeSpan overflowed because duration is too long".) Therefore it is recommended that you should always pre-parse the time string before passing it to the "TimeSpan.Parse()" function. This pre-parsing is done by the FormatTimeSpanString( ) function. This function will format the input string correctly. Therefore, a time string of value "45:30" will be converted to "1.21:30" (meaning 1 day, 21 hours and 30 minutes). This format is perfectly acceptable for TimeSpan.Parse() function and it will not crash.


<!--endintro-->



```
ts = TimeSpan.Parse(cboMyComboBox.Text)
```




::: bad
Figure: Bad code because a value greater than 24hours will crash eg. 45:30

:::



```
ts = TimeSpan.Parse(FormatTimeSpanString(cboMyComboBox.Text))
```




::: good
Figure: Good code because we are using a wrapper method to pre-parse the string containing the 
TimeSpan value. [(Look it up in CodeBase)](https&#58;//www.ssw.com.au/ssw/Standards/Rules/RulestoBetterCode.aspx#)

:::

We have a program called [SSW Code Auditor](https&#58;//www.ssw.com.au/ssw/CodeAuditor/Rules.aspx#TimeSpan) to check for this rule.
