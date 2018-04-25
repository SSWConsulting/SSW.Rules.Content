---
type: rule
title: Do you avoid logic errors by using Else If?
uri: do-you-avoid-logic-errors-by-using-else-if
created: 2018-04-25T17:44:41.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> We see a lot of programmers doing this, they have two conditions - true and false - and they do not consider other possibilities - e.g. an empty string. Take a look at this example. We have an If statement that checks what backend database is being used. This is being stored as a property - Backend in config file. At the moment only Access and SQL Server are options.<br><br> </span>

<p class="ssw15-rteElement-CodeArea">Private Sub Command0_Click()<br>If My.MySettings.Default.Backend = &quot;Access&quot; Then<br>'Call this code ie. SQL commands<br>Else<br>'Must be SQL Server<br>'Call this other code ie. Stored Proc<br>End If<br>.....processing code<br>End Sub <br></p><dd class="ssw15-rteElement-FigureBad"> Figure&#58; Bad example with If statement</dd><p>Consider later on this code is updated... the programmer wishes to add an Oracle backend database option. So they modify the Backend property to include Oracle...<br></p><p>By using the above code, the wrong code will run because the above code assumes two possible situations. To avoid this problem, change the code to be defensive .g. Use an Else If statement (like below).</p><p>The user will then get a Logic Error and can report it to the programmer.​<br></p><p class="ssw15-rteElement-CodeArea">Private Sub Command0_Click()<br>If My.MySettings.Default.Backend = &quot;Access&quot; Then<br>'Call this code ie. SQL<br>ElseIf My.MySettings.Default.Backend = &quot;SQL Server&quot; Then<br>'Call this other code ie. Stored Proc<br>Else<br>Throw New Exception( &quot;Logic Error -- BackEnd is&#58; &quot;<br>&amp; My.MySettings.Default.Backend)<br>End If<br>End Sub<br></p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good example with If statement</dd><p class="ssw15-rteElement-P"><br>When writing code to trap Logic Errors, use &quot;Select Case&quot; or &quot;switch&quot; statements to enhance readability. e.g. in VB.NET <br></p><p class="ssw15-rteElement-CodeArea">Private Sub Command0_Click()<br>Select Case mDataset.Tables(0).Rows(0)(&quot;Key&quot;)<br>Case &quot;1&quot;<br>' Initialize the column list<br>strTempColumn = &quot;&quot;<br>Case &quot;2&quot;<br>' Ignore<br>End Select<br>.....processing code<br>End Sub<br></p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad example with Case statement in VB.NET <br></dd><p class="ssw15-rteElement-CodeArea">Private Sub Command0_Click()<br>Select Case mDataset.Tables(0).Rows(0)(&quot;Key&quot;)<br>Case &quot;1&quot;<br>' Initialize the column list<br>strTempColumn = &quot;&quot;<br>Case &quot;2&quot;<br>' IgnoreCase Else<br>Throw New Exception(&quot;Logic Error&quot;)<br>End Select<br>.....processing code<br>End Sub<br></p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good example - Use 'Select Case' or 'Switch' statements to enhance readability when coding to find logic errors <br></dd>


