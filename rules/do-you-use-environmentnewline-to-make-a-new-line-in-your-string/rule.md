---
type: rule
title: Do you use Environment.NewLine to make a new line in your string?
uri: do-you-use-environmentnewline-to-make-a-new-line-in-your-string
created: 2018-04-26T22:46:14.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 78
  title: Matt Wicks

---



<span class='intro'> When you need to create a new line in your string, make sure you use Environment.NewLine, and then literally begin typing your code on a new line for readability purposes.​<br> </span>

<p class="ssw15-rteElement-CodeArea">String strExample = &quot;This is a very long string that is \r\n not properly implementing a new line.&quot;; <br></p><dd class="ssw15-rteElement-FigureBad"> Bad Example&#58; The string has implemented a manual carriage return line feed pair (\r\n)</dd><p>  </p><p class="ssw15-rteElement-CodeArea">String strExample = &quot;This is a very long string that is &quot; + Environment.NewLine +<br>    &quot; properly implementing a new line.&quot;;</p><p>   </p><dd class="ssw15-rteElement-FigureGood">Good Example&#58; The new line is created with Enviroment.NewLine</dd><p>​​<br></p>


