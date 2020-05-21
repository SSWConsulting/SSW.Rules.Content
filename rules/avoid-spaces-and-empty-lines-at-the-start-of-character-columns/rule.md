---
type: rule
archivedreason: 
title: Data - Do you avoid spaces and empty lines at the start of character columns?
guid: 848bd3dc-36eb-408f-a216-ce06bb730c54
uri: avoid-spaces-and-empty-lines-at-the-start-of-character-columns
created: 2019-11-25T19:01:24.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Christian Morford-Waite
  url: https://ssw.com.au/people/christian-morford-waite
related: []
redirects:
- data-do-you-avoid-spaces-and-empty-lines-at-the-start-of-character-columns

---


<p class="ssw15-rteElement-P">​​​​​​​Text in character columns (char, varchar, text, nchar, varchar, text) can start with spaces or empty lines which is usually data entry error.​&#160;<br></p><p class="ssw15-rteElement-P">The best way to avoid this issue is to handle whitespace in the middle-tier before it reaches the database.​​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p>Here’s an example of removing whitespace and carriage returns in the middle-tier using Regex&#58;​</p><p class="ssw15-rteElement-CodeArea">static string Trim(string inputText)<br>&#123;<br>&#160; Match m = Regex.Match(inputText, @&quot;[^\s]&quot;);<br>&#160; return m.Success ? inputText.Substring(m.Index) &#58; inputText;<br>&#125;<br></p><dd class="ssw15-rteElement-FigureNormal">​​Figure&#58; <span style="background-color&#58;initial;">C# Removing whitespace and carriage returns in middle-tier<br></span></dd><p class="ssw15-rteElement-P">The code above&#58;<br></p><ul><li>Uses Regular Expressions (Regex) to match the first non-whitespace character (includes tabs, spaces, line feeds and carriage returns).</li><li>Retrieves the index of the character</li><li>Returns the text from the character onwards, thus removing the whitespace at the start<br></li></ul>This code could be triggered in the middle-tier before inserting into the database.​<br><p></p>


