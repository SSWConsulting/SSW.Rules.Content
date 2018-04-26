---
type: rule
archivedreason: 
title: Do you initialize variables outside of the try block?
guid: ef08f3ac-8434-4e07-bfea-c33b7e03ae38
uri: initialize-variables-outside-of-the-try-block
created: 2018-04-26T21:41:56.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-initialize-variables-outside-of-the-try-block

---


<p>You should initialize variables outside of the try block.​<br></p><strong></strong>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-CodeArea">Cursor cur;<br>try<br>&#123;<br>...<br>cur = Cursor.Current; //Bad Code - initializing the variable inside the try block<br>Cursor.Current = Cursors.WaitCursor;<br>...<br>&#125;<br>finally<br>&#123;<br>Cursor.Current = cur;<br>&#125; <br></p><dd class="ssw15-rteElement-FigureBad"> Bad Example&#58; Because of the initializing code inside the try block. If it failed on this line then you will get a NullReferenceException in Finally<br></dd><p class="ssw15-rteElement-CodeArea">Cursor cur = Cursor.Current; //Good Code - initializing the variable outside the try block<br>try<br>&#123;<br>...<br>Cursor.Current = Cursors.WaitCursor;<br>...<br>&#125;<br>finally<br>&#123;<br>Cursor.Current = cur;<br>&#125;</p><dd class="ssw15-rteElement-FigureGood">Good Example &#58; Because the initializing code is outside the try​​​ block​​<br></dd>


