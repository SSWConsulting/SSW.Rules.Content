---
type: rule
archivedreason: 
title: Do you avoid Empty code blocks?
guid: 87d8d6e4-deba-44bf-a5db-4cc8b2c937b5
uri: avoid-empty-code-block
created: 2018-04-30T22:08:47.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-avoid-empty-code-blocks

---


<p>​Empty Visual C# .NET methods consume&#160;program resources unnecessarily. Put a ​​comment in code block if its stub for future application.</p>Don’t add empty C# methods to your code. If you are adding one as a placeholder for future development, add a comment with a TODO.<div><br>Also, to avoid unnecessary resource consumption, you should keep the entire method commented until it has been implemented.</div><div><br>If the class implements an inherited interface method, ensure the method throws NotImplementedException.<br></div>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-CodeArea">​public class Example<br> &#123;<br>&#160; &#160; &#160; &#160;public double salary()<br>&#160; &#160; &#160; &#160;&#123;&#160;
   <br>&#160; &#160; &#160; &#160;&#125;<br> &#125;</p><dd class="ssw15-rteElement-FigureBad">​​Figure&#58; Bad Example - Method is empty​​​​​<br></dd><p class="ssw15-rteElement-CodeArea">​public class Sample<br> &#123;<br>&#160; &#160; &#160; &#160;public double salary()<br>&#160; &#160; &#160; &#160;&#123;<br> &#160; &#160; &#160; &#160; &#160; &#160; &#160;&#160;return 2500.00;<br> &#160; &#160; &#160; &#160;&#125;<br> &#125;</p><dd class="ssw15-rteElement-FigureGood">​Figure&#58; G​ood Example - Method implements some code<br></dd><p class="ssw15-rteElement-CodeArea">

public interface IDemo<br> &#123;<br>&#160; &#160; &#160; &#160;void DoSomethingUseful();<br>&#160; &#160; &#160; &#160;void SomethingThatCanBeIgnored();<br> &#125;<br>public class Demo &#58; IDemo<br> &#123;<br>&#160; &#160; &#160; &#160;public void DoSomethingUseful()<br>&#160; &#160; &#160; &#160;&#123;<br>&#160; &#160; &#160; &#160; &#160; &#160; &#160; // no audit issues<br>&#160; &#160; &#160; &#160; &#160; &#160; &#160;Console.WriteLine(&quot;Useful&quot;);<br>&#160; &#160; &#160; &#160;&#125;<br>&#160; &#160; &#160; &#160;// audit issues <br>&#160; &#160; &#160; public void SomethingThatCanBeIgnored()<br>&#160; &#160; &#160; &#123; <br>&#160; &#160; &#160; &#125; <br> &#125; </p><dd class="ssw15-rteElement-FigureBad">​Figure&#58; Bad Example - No Comment within empty code block</dd><p class="ssw15-rteElement-CodeArea">​​​public interface IDemo<br> &#123;<br>&#160; &#160; &#160; &#160;void DoSomethingUseful();<br>&#160; &#160; &#160; &#160;void SomethingThatCanBeIgnored();<br> &#125;<br>public class Demo &#58; IDemo<br> &#123;<br>&#160; &#160; &#160; &#160;public void DoSomethingUseful()<br>&#160; &#160; &#160; &#160;&#123;<br>&#160; &#160; &#160; &#160; &#160; &#160; &#160; // no audit issues<br>&#160; &#160; &#160; &#160; &#160; &#160; &#160; Console.WriteLine(&quot;Useful&quot;);<br>&#160; &#160; &#160; &#160;&#125;<br>&#160; &#160; &#160; &#160;// No audit issues <br>&#160; &#160; &#160; &#160;public void SomethingThatCanBeIgnored() <br>&#160; &#160; &#160; &#160;&#123;<br>&#160; &#160; &#160; &#160; &#160; &#160; &#160; // stub for IDemo interface<br>&#160; &#160; &#160; &#160;&#125; <br> &#125; </p><dd class="ssw15-rteElement-FigureGood">​​​Figure&#58; Good Example - Added comment within Empty Code block method of interface&#160;class</dd>​<br><br><br>


