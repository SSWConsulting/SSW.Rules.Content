---
type: rule
title: Do you build criteria by using a where clause?
uri: do-you-build-criteria-by-using-a-where-clause
created: 2016-11-16T17:07:12.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>It is very common to come up with ways to filter data.&#160;<br>As an example, you could do it like this.</p><p class="ssw15-rteElement-CodeArea">ClientSearch.aspx?Client.ClientID='ssw'&amp;Client.CoName='S'</p><p><strong>Figure&#58; Filtering Data </strong></p><p>This allows you to easily extract fields and values, but it only works for the fields you hard code. You could get around it by writing complex code to build a SQL query or ignore the ones that don't match.</p><p>But this gives exact matches. E.g.&#58;<br></p><br> </span>

<p>​<br></p><p class="ssw15-rteElement-CodeArea">ClientID=ssw</p><p>What if you want to give the ability to allow the user to be able to use a like e.g.</p><p class="ssw15-rteElement-CodeArea">ClientID like '%ssw%'</p><p>Well then I could add something like</p><p class="ssw15-rteElement-CodeArea">ClientSearch.aspx?Client.ClientID=ssw&amp;Client.ClientID.SearchMode=OR</p><p>But why do this when a WHERE clause in SQL can do all this&#160;<br>e.g.</p><p class="ssw15-rteElement-CodeArea">ClientSearch.aspx?Where=Client.ClientID%20like%20'%ssw%'<br></p><p><strong>Figure&#58; Similar matches</strong></p><p>Try this -&#160;<a href="https&#58;//www.ssw.com.au/timeproonline/ClientSearch.aspx?Where=Client.ClientID%20like%20%27%ssw%%27">ClientSearch.aspx?Where=Client.ClientID%20like%20'%ssw%'</a></p><p>The Pros for do this are&#58;</p><ul><li>Quicker development time.</li><li>SQL is very powerful - say I want to JOIN another table in the WHERE, I could use an IN statement and do a sub query - no extra code by the developer.</li><li>Matches HTML syntax (named value pair) and as a developer you can get it easy. e.g.</li><p class="ssw15-rteElement-CodeArea">Request.QueryString(&quot;Where&quot;)</p></ul><p>The CONS&#58;</p><ul><li>It shows the database schema to the users - users maybe should not see the structure of the database.</li><li>Security - the where clause could show data we don't want users to see.</li><li>Got to add a little extra code to avoid&#160;<a href="https&#58;//www.ssw.com.au/ssw/KB/KB.asp?KBID=Q995992">SQL injection</a>.</li></ul><p>​<br></p>


