---
type: rule
title: Do you change the connection timeout to 5 seconds?
uri: do-you-change-the-connection-timeout-to-5-seconds
created: 2018-04-25T20:09:55.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 16
  title: Tiago Araujo

---



<span class='intro'> ​By default, the connection timeout is 15 seconds. When it comes to testing if a connection is valid or not, 15 seconds is a long time for the user to wait. You should change the connection timeout inside your connection strings to 5 seconds.​<br><br> </span>

<p class="ssw15-rteElement-CodeArea">&quot;Integrated Security=SSPI;Initial Catalog=SallyKnoxMedical;Data <br>Source=TUNA&quot;</p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad Connection String<br></dd><p class="ssw15-rteElement-CodeArea">&quot;Integrated Security=SSPI;Initial Catalog=SallyKnoxMedical;Data Source=TUNA;<br>Connect Timeout=5&quot;​<br></p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good Connection String with a 5-second connection timeout<br></dd>


