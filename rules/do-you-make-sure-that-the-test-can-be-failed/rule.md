---
type: rule
archivedreason: 
title: Do you make sure that the test can be failed?
guid: fec2a216-ace7-4720-866f-9db216f9d0a9
uri: do-you-make-sure-that-the-test-can-be-failed
created: 2020-03-12T23:16:37.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 81
  title: Jason Taylor
related: []

---


<p class="ssw15-rteElement-P">You should make sure that the unit test you created can actually fail. It is very easy and common to create a test that never fails. It is very important to take baby steps and not to make any assumptions.</p>One of the ways you can do this is by returning NotImplementedException() from the method you are writing tests for. For Example&#58;<br>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-CodeArea">[Test]<br> public void Test_ABC_MethodReturns_XYZ()<br> &#123;<br> MyClass classObj = new MyClass();<br> Assert.IsNotNull(classObj.Get_XYZ());<br> &#125;<br> <br> //The method to test in class MyClass ...<br> public int Get_XYZ()<br> &#123;<br> throw new NotImplementedException(&quot;Write a test&quot;);<br> &#125;</p><dd class="ssw15-rteElement-FigureNormal">Figure&#58; Example of how to use NotImplementedException​​​<br></dd>


