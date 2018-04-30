---
type: rule
title: Do you avoid using if-else instead of switch block?
uri: do-you-avoid-using-if-else-instead-of-switch-block
created: 2018-04-30T22:12:26.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>The .NET framework and the C# language provide two methods for conditional handling where multiple distinct values can be selected from. The switch statement is less flexible than the if-else-if tree but is generally considered to be more efficient. .NET compiler generates a jump list for switch block for that reason it is faster for long list of condition. And also complier has the ability to optimize the switch block. Condition in the switch block is faster as compiler evaluated the condition once but for if-else block, compiler need to evaluate the condition for each 'else if' block</p><p><b>Note&#58; </b>Performance is very much negligible when number of condition is less than 5. So if the code design is clearer &amp; easily maintainable by using if-else block, then Developer should use if-else block for fewer conditions.<br></p><br> </span>

<p class="ssw15-rteElement-CodeArea">int DepartmentId = GetDepartmentId()<br>if(DepartmentId == 1)<br>&#123;<br>// do something<br>&#125;<br>else if(DepartmentId == 2)<br>&#123;<br>// do something #2<br>&#125;<br>else if(DepartmentId == 3)<br>&#123;<br>// do something #3<br>&#125;<br>else if(DepartmentId == 4)<br>&#123;<br>// do something #4<br>&#125;<br>else if(DepartmentId == 5)<br>&#123;<br>// do something #5<br>&#125;<br>else <br>&#123;<br>// do something #6<br>&#125; <br></p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad example of coding practice</dd><p>​<br></p><p class="ssw15-rteElement-CodeArea">int DepartmentId = GetDepartmentId()<br>switch(DepartmentId)<br>&#123;<br>case 1&#58;<br>// do something<br>break;<br>case 2&#58;<br>// do something # 2<br>break;<br>case 3&#58;<br>// do something # 3<br>break;<br>case 4&#58;<br>// do something # 4<br>break;<br>case 1&#58;<br>// do something # 5<br>break;<br>case 1&#58;<br>// do something # 6<br>break;<br>default&#58;<br>//Do something here<br>break;<br>&#125;</p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good example of coding practice which will result better performance <br></dd><p class="ssw15-rteElement-P">Further Reading&#58;&#160;<a href="http&#58;//www.blackwasp.co.uk/SpeedTestIfElseSwitch.aspx">Speed Test&#58; Switch vs If-Else-If</a>​<br><br></p>


