---
type: rule
archivedreason: 
title: Do you avoid using if-else instead of switch block?
guid: 669b5f2d-6e38-4e12-be49-4619960435b2
uri: avoid-using-if-else-instead-of-switch-block
created: 2018-04-30T22:12:26.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-avoid-using-if-else-instead-of-switch-block

---


<p>The .NET framework and the C# language provide two methods for conditional handling where multiple distinct values can be selected from. The switch statement is less flexible than the if-else-if tree but is generally considered to be more efficient.&#160;<br></p><p>The .NET compiler generates a jump list for switch blocks, resulting in far better performance than if/else for evaluating conditions. The performance gains are negligible when the number of conditions is trivial (i.e. fewer than 5), so if the code is clearer and more maintainable using if/else blocks, then you can use your discretion. But be prepared to refactor to a switch block if the number of conditions exceeds 5.​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-CodeArea">int DepartmentId = GetDepartmentId()<br>if(DepartmentId == 1)<br>&#123;<br>// do something<br>&#125;<br>else if(DepartmentId == 2)<br>&#123;<br>// do something #2<br>&#125;<br>else if(DepartmentId == 3)<br>&#123;<br>// do something #3<br>&#125;<br>else if(DepartmentId == 4)<br>&#123;<br>// do something #4<br>&#125;<br>else if(DepartmentId == 5)<br>&#123;<br>// do something #5<br>&#125;<br>else <br>&#123;<br>// do something #6<br>&#125; <br></p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad example of coding practice</dd><p>​<br></p><p class="ssw15-rteElement-CodeArea">int DepartmentId = GetDepartmentId()<br>switch(DepartmentId)<br>&#123;<br>case 1&#58;<br>// do something<br>break;<br>case 2&#58;<br>// do something # 2<br>break;<br>case 3&#58;<br>// do something # 3<br>break;<br>case 4&#58;<br>// do something # 4<br>break;<br>case 1&#58;<br>// do something # 5<br>break;<br>case 1&#58;<br>// do something # 6<br>break;<br>default&#58;<br>//Do something here<br>break;<br>&#125;</p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good example of coding practice which will result better performance <br></dd><p class="ssw15-rteElement-P">Further Reading&#58;&#160;<a href="http&#58;//www.blackwasp.co.uk/SpeedTestIfElseSwitch.aspx">Speed Test&#58; Switch vs If-Else-If</a>​<br><br><br></p>


