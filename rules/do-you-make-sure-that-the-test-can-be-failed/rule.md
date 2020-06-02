

---
uri: do-you-make-sure-that-the-test-can-be-failed
title: Do you make sure that the test can be failed?
created: YYYY-03-DD 23:16:37
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> <p class="ssw15-rteElement-P">You should make sure that the unit test you created can actually fail. It is very easy and common to create a test that never fails. It is very important to take baby steps and not to make any assumptions.<br></p><p class="ssw15-rteElement-P">This is a fundamental principle in Test Driven Development called Red/Green/Refactor.<br></p>One of the ways you can do this is by returning NotImplementedException() from the method you are writing tests for. For Example&#58;<br> </span>

<p class="ssw15-rteElement-CodeArea">[Test]<br> public void Test_ABC_MethodReturns_XYZ()<br> &#123;<br>&#160; &#160;MyClass classObj = new MyClass();<br>&#160; &#160;Assert.IsNotNull(classObj.Get_XYZ());<br> &#125;<br> <br> //The method to test in class MyClass ...<br> public int Get_XYZ()<br> &#123;<br>&#160; &#160; throw new NotImplementedException(&quot;Write a test&quot;);<br> &#125;</p><dd class="ssw15-rteElement-FigureNormal">Figure&#58; Example of how to use NotImplementedException​​​<br></dd>


