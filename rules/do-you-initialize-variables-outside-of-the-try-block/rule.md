---
type: rule
title: Do you initialize variables outside of the try block?
uri: do-you-initialize-variables-outside-of-the-try-block
created: 2018-04-26T21:41:56.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>You should initialize variables outside of the try block.​<br></p><strong></strong> </span>

<p class="ssw15-rteElement-CodeArea">Cursor cur;<br>try<br>&#123;<br>...<br>cur = Cursor.Current; //Bad Code - initializing the variable inside the try block<br>Cursor.Current = Cursors.WaitCursor;<br>...<br>&#125;<br>finally<br>&#123;<br>Cursor.Current = cur;<br>&#125; <br></p><dd class="ssw15-rteElement-FigureBad"> Bad Example&#58; Because of the initializing code inside the try block. If it failed on this line then you will get a NullReferenceException in Finally<br></dd><p class="ssw15-rteElement-CodeArea">Cursor cur = Cursor.Current; //Good Code - initializing the variable outside the try block<br>try<br>&#123;<br>...<br>Cursor.Current = Cursors.WaitCursor;<br>...<br>&#125;<br>finally<br>&#123;<br>Cursor.Current = cur;<br>&#125;</p><dd class="ssw15-rteElement-FigureGood">Good Example &#58; Because the initializing code is outside the try​​​ block​​<br></dd>


