---
type: rule
title: Do you avoid logic errors by using Else If?
uri: do-you-avoid-logic-errors-by-using-else-if
created: 2018-04-25T17:44:41.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> We see a lot of programmers doing this, they have two conditions - true and false - and they do not consider other possibilities - e.g. an empty string. Take a look at this example. We have an If statement that checks what backend database is being used.<br> </span>

<p class="ssw15-rteElement-P">In the example the only expected values are &quot;Development&quot; and &quot;Production&quot;.&#160;<br></p><p class="ssw15-rteElement-CodeArea">void Load(string environment)<br>&#123;<br>&#160; if (environment == &quot;Development&quot;)<br>&#160; &#123;<br>&#160; &#160; // set Dev environment variables<br>&#160; &#125;<br>&#160; else<br>&#160; &#123;<br>&#160; &#160; // set Production environment variables	<br>&#160; &#125;<br>&#125;<br></p><dd class="ssw15-rteElement-FigureBad"> Figure&#58; Bad example with If statement</dd><p>Consider later that extra environments may be added&#58; e.g. &quot;Staging&quot;<br></p><p>By using the above code, the wrong code will run because the above code assumes two possible situations. To avoid this problem, change the code to be defensive .g. Use an Else If statement (like below).<br></p><p>Now the code will throw an exception if an unexpected value is provided.<br></p><p class="ssw15-rteElement-CodeArea">void Load(string environment)<br>&#123;<br>&#160; if (environment == &quot;Development&quot;)<br>&#160; &#123;<br>&#160; &#160; // set Dev environment variables<br>&#160; &#125;<br>&#160; else if (environment == &quot;Production&quot;)<br>&#160; &#123;<br>&#160; &#160; // set Production environment variables	<br>&#160; &#125;<br>&#160; else<br>&#160; &#123;<br>&#160; &#160; throw new InvalidArgumentException(environment);&#160;<br>&#160; &#125;<br>&#125;<br></p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good example with If statement<br></dd>


