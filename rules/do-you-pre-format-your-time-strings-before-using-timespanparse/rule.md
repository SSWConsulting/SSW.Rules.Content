---
type: rule
title: Do you pre-format your time strings before using TimeSpan.Parse()?
uri: do-you-pre-format-your-time-strings-before-using-timespanparse
created: 2018-04-25T22:00:38.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> TimeSpan.Parse() constructs a Timespan from a time indicated by a specified string. The acceptable parameters for this function are in the format &quot;d.hh&#58;mm&quot; where &quot;d&quot; is the number of days (it is optional), &quot;hh&quot; is hours and is between 0 and 23 and &quot;mm&quot; is minutes and is between 0 and 59. If you try to pass, as a parameter, as a string such as &quot;45&#58;30&quot; (meaning 45 hours and 30 minutes), TimeSpan.Parse() function will crash. (The exact exception received is&#58; &quot;System.OverflowException&#58; TimeSpan overflowed because duration is too long&quot;.) Therefore it is recommended that you should always pre-parse the time string before passing it to the &quot;TimeSpan.Parse()&quot; function. This pre-parsing is done by the FormatTimeSpanString( ) function. This function will format the input string correctly. Therefore, a time string of value &quot;45&#58;30&quot; will be converted to &quot;1.21&#58;30&quot; (meaning 1 day, 21 hours and 30 minutes). This format is perfectly acceptable for TimeSpan.Parse() function and it will not crash.<br>​<br> </span>

<p class="ssw15-rteElement-CodeArea">​ts = TimeSpan.Parse(cboMyComboBox.Text)<br></p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad code because a value greater than 24hours will crash eg. 45&#58;30<br></dd><p class="ssw15-rteElement-CodeArea">ts = TimeSpan.Parse(FormatTimeSpanString(cboMyComboBox.Text))​<br></p><dd class="ssw15-rteElement-FigureGood">
   Figure&#58; Good code because we are using a wrapper method to pre-parse the string containing the&#160;<br>TimeSpan value.&#160;<a href="https&#58;//www.ssw.com.au/ssw/Standards/Rules/RulestoBetterCode.aspx#">(Look it up in CodeBase)</a>​<br></dd><p class="ssw15-rteElement-YellowBorderBox">We have a program called&#160;<a href="https&#58;//www.ssw.com.au/ssw/CodeAuditor/Rules.aspx#TimeSpan">SSW Code Auditor</a>&#160;to check for this rule.<br></p>
​<br>


