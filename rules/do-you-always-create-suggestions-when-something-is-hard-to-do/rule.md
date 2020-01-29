---
type: rule
title: Do you always create suggestions when something is hard to do?
uri: do-you-always-create-suggestions-when-something-is-hard-to-do
created: 2018-04-30T22:04:43.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>One of our goals is to make the job of the developer as easy as possible. If you have to write a lot of code for something that you think you should not have to do, you should make a suggestion and add it to the relevant page.<br></p><p>If you have to add a suggestion, make sure that you put the link to that suggestion into the comments of your code.​​<br></p> </span>

<p class="ssw15-rteElement-CodeArea">/// &lt;summary&gt;<br>/// base class for command implementations<br>/// This is a work around as standard MVVM commands<br>/// are not provided by default. <br>/// &lt;/summary&gt;<br>/// &lt;remarks&gt;&lt;/remarks&gt;<br>public class Command &#58; ICommand<br>&#123;<br>&#160;// code<br>&#125;​</p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad example - The link to the suggestion should be in the comments​<br></dd><p class="ssw15-rteElement-CodeArea">​/// &lt;summary&gt;<br>/// base class for command implementations<br>/// This is a work around as standard MVVM commands<br>/// are not provided by default. <br>/// <br>/// &#160;Issue Logged here&#58; https&#58;//github.com/SSWConsulting/SSW.Rules/issues/3<br>/// &lt;/summary&gt;<br>/// &lt;remarks&gt;&lt;/remarks&gt;<br>public class Command &#58; ICommand<br>&#123;<br>&#160;// code<br>&#125;<br></p><dd class="ssw15-rteElement-FigureGood">​Figure&#58; Good example - Wh​​en you link to a suggestion everyone can find it and vote it up</dd><p>​<br></p>


