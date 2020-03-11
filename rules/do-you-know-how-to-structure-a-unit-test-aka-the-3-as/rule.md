---
type: rule
archivedreason: 
title: Do you know how to structure a unit test (aka the 3 a's)?
guid: 5af6b8fd-5e65-4c68-8342-527090a61125
uri: do-you-know-how-to-structure-a-unit-test-aka-the-3-as
created: 2020-03-11T16:51:15.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


A test verifies expectations. Traditionally it has the form of 3 major steps&#58;<div><ol><li>Arrange</li><li>Act</li><li>Assert<br></li></ol></div>
<br><excerpt class='endintro'></excerpt><br>
<p>​In the &quot;Arrange&quot; step we get everything ready and make sure we have all things handy for the &quot;Act&quot; step.</p><p class="ssw15-rteElement-P">The &quot;Act&quot; step executes the relevant code piece that we want to test.​<br></p><p class="ssw15-rteElement-P">The &quot;Assert&quot; step verifies our expectations by stating what we were expecting from the system under test.​​<br></p><p class="ssw15-rteElement-P">Developers call this the &quot;AAA&quot; syntax.​​<br></p><p class="ssw15-rteElement-CodeArea">[TestMethod]<br>public void TestRegisterPost_ValidUser_ReturnsRedirect()<br>&#123;<br>&#160;&#160;&#160;// Arrange<br>&#160;&#160;&#160;AccountController controller = GetAccountController();<br>&#160;&#160;&#160;RegisterModel model = new RegisterModel()<br>&#160;&#160;&#160;&#123;<br>&#160;&#160;&#160;&#160;&#160;&#160;UserName = &quot;someUser&quot;,<br>&#160;&#160;&#160;&#160;&#160;&#160;Email = &quot;goodEmail&quot;,<br>&#160;&#160;&#160;&#160;&#160;&#160;Password = &quot;goodPassword&quot;,<br>&#160;&#160;&#160;&#160;&#160;&#160;ConfirmPassword = &quot;goodPassword&quot;<br>&#160;&#160;&#160;&#125;;<br>&#160;&#160;&#160;// Act<br>&#160;&#160;&#160;ActionResult result = controller.Register(model);<br>&#160;&#160;&#160;// Assert<br>&#160;&#160;&#160;RedirectToRouteResult redirectResult = (RedirectToRouteResult)result;<br>&#160;&#160;&#160;Assert.AreEqual(&quot;Home&quot;, redirectResult.RouteValues[&quot;controller&quot;]);<br>&#160;&#160;&#160;Assert.AreEqual(&quot;Index&quot;, redirectResult.RouteValues[&quot;action&quot;]);<br>&#125;</p><dd class="ssw15-rteElement-FigureGood">Figure&#58; A good structure for a unit test​​<br></dd>


