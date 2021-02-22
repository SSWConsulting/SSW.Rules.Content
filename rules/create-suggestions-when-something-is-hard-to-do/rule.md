---
type: rule
archivedreason: 
title: Do you always create suggestions when something is hard to do?
guid: 7058fd5e-0a18-4f25-b085-c499a2c5ab17
uri: create-suggestions-when-something-is-hard-to-do
created: 2018-04-30T22:04:43.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-always-create-suggestions-when-something-is-hard-to-do

---


<p>One of our goals is to make the job of the developer as easy as possible. If you have to write a lot of code for something that you think you should not have to do, you should make a suggestion and add it to the relevant page.<br></p><p>If you have to add a suggestion, make sure that you put the link to that suggestion into the comments of your code.​​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-CodeArea">/// &lt;summary&gt;<br>/// base class for command implementations<br>/// This is a work around as standard MVVM commands<br>/// are not provided by default. <br>/// &lt;/summary&gt;<br>public class Command &#58; ICommand<br>&#123;<br>&#160;// code<br>&#125;​</p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad example - The link to the suggestion should be in the comments​<br></dd><p class="ssw15-rteElement-CodeArea">​/// &lt;summary&gt;<br>/// base class for command implementations<br>/// This is a work around as standard MVVM commands<br>/// are not provided by default. <br>/// &lt;/summary&gt;<br>///<br>/// &lt;remarks&gt;<br>/// &#160;Issue Logged here&#58; https&#58;//github.com/SSWConsulting/SSW.Rules/issues/3<br>///&lt;/remarks&gt;<br>public class Command &#58; ICommand<br>&#123;<br>&#160;// code<br>&#125;<br></p><dd class="ssw15-rteElement-FigureGood">​Figure&#58; Good example - Wh​​en you link to a suggestion everyone can find it and vote it up</dd><p>​<br></p>


