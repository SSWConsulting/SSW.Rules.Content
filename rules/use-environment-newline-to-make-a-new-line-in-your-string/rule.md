---
type: rule
archivedreason: 
title: Do you use Environment.NewLine to make a new line in your string?
guid: 200df127-6aaf-415d-a54d-933a228b14fe
uri: use-environment-newline-to-make-a-new-line-in-your-string
created: 2018-04-26T22:46:14.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Matt Wicks
  url: https://ssw.com.au/people/matt-wicks
related: []
redirects:
- do-you-use-environment-newline-to-make-a-new-line-in-your-string

---


When you need to create a new line in your string, make sure you use Environment.NewLine, and then literally begin typing your code on a new line for readability purposes.​<br>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-CodeArea">​string strExample = &quot;This is a very long string that is \r\n not properly implementing a new line.&quot;; 
   <br></p><dd class="ssw15-rteElement-FigureBad"> Bad Example&#58; The string has implemented a manual carriage return line feed pair (\r\n)</dd><p></p><p class="ssw15-rteElement-CodeArea">string strExample = &quot;This is a very long string that is &quot; + Environment.NewLine +<br>			 &quot; properly implementing a new line.&quot;;</p><p></p><dd class="ssw15-rteElement-FigureGood">OK Example&#58; The new line is created with Enviroment.NewLine (but strings are immutable)<br></dd><p class="ssw15-rteElement-CodeArea">
​var&#160;example = new StringBuilder();<br>
example.AppendLine(&quot;This is a very long string that is &quot;);<br>
example.Append(&quot; properly implementing a new line.&quot;);</p><p></p><dd class="ssw15-rteElement-FigureGood">Good Example&#58; The new line is created by the StringBuilder and has better memory utilisation<br></dd>


