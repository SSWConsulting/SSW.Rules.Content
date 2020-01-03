---
type: rule
title: Data - Do you avoid spaces and empty lines at the start of character columns?
uri: data---do-you-avoid-spaces-and-empty-lines-at-the-start-of-character-columns
created: 2019-11-25T19:01:24.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 99
  title: Christian Morford-Waite

---



<span class='intro'> <p class="ssw15-rteElement-P">​​Text in character columns (char, varchar, text, nchar, varchar, text) can start with spaces which is usually data entry error.​<br></p><p class="ssw15-rteElement-P">The best way to avoid this issue is to handle whitespace in the middle-tier before it reaches the database.<br>However, if you are using stored procedures you can also remove leading&#160;spaces using <a href="https&#58;//docs.microsoft.com/en-us/sql/t-sql/functions/ltrim-transact-sql?view=sql-server-ver15">LTRIM (Transact-SQL)​</a>.<br></p> </span>




