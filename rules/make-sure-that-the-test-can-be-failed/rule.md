---
type: rule
archivedreason: 
title: Do you make sure that the test can be failed?
guid: fec2a216-ace7-4720-866f-9db216f9d0a9
uri: make-sure-that-the-test-can-be-failed
created: 2020-03-12T23:16:37.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Jason Taylor
  url: https://ssw.com.au/people/jason-taylor
related: []
redirects:
- do-you-make-sure-that-the-test-can-be-failed

---


<p class="ssw15-rteElement-P"></p><p class="ssw15-rteElement-P">​You should make sure that the unit tests you create can actually fail. A test that never fails is not useful to anyone.​<br></p><p class="ssw15-rteElement-P">This is a fundamental principle in Test Driven Development (TDD) called Red/Green/Refactor.<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p>A common approach is by returning NotImplementedException() from the method you are writing tests for. For Example&#58;<br></p><p class="ssw15-rteElement-CodeArea">[Test]<br>public void ShouldAddTwoNumbers()<br>&#123;<br>&#160;&#160; var calculator = new Calculator();<br>&#160;&#160; var result = calculator.Sum(10, 11);<br><br><br>&#160;&#160; Assert.Equal(21, result);<br>&#125;<br><br>// The method to test in class Calculator ...<br>public int Sum(int x, int y)<br>&#123;<br>&#160;&#160; throw new NotImplementedException();<br>&#125;</p><dd class="ssw15-rteElement-FigureBad">Bad Example&#58; The test fails by throwing a NotImplementedException​​​​<br></dd><p>This test fails for the wrong reason, by throwing a NotImplementedException. In production, this is not a valid reason for this test to fail.&#160;</p><p>A better approach would be to return a value that is invalid&#58;<br></p><p class="ssw15-rteElement-CodeArea">// The method to test in class Calculator ...<br>public int Sum(int x, int y)<br>&#123;<br>&#160;&#160; return 0;<br>&#125;</p><dd class="ssw15-rteElement-FigureGood">Good Example&#58; The test fails by returning an invalid result​​​​<br></dd><p>In this case, the test will fail because the behavior is incorrect. It is not correctly adding the two numbers.<br></p>


