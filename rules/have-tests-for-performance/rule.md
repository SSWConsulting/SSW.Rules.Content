---
type: rule
archivedreason: 
title: Do you have tests for Performance?
guid: a0b93a9e-1367-4a8c-985a-e46df21db9d1
uri: have-tests-for-performance
created: 2020-03-12T19:58:01.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-have-tests-for-performance

---


​Typically there are User Acceptance Tests that need to be written to measure the performance of your application. As a general rule of thumb, Forms should not load in more than 4 seconds. This can be automated with your unit testing framework.<br>
<br><excerpt class='endintro'></excerpt><br>
<p><b>​Sample Code&#58;</b></p><p class="ssw15-rteElement-CodeArea"> public abstract class FormTestBase{ltHTMLChar}F{gtHTMLChar}<br> where F &#58; Form, new()<br> &#123;<br> protected TimeSpan _ExpectedLoadTime = TimeSpan.FromSeconds(4);<br> [Test]<br> public void LoadTest()<br> &#123;<br> Stopwatch stopwatch = new Stopwatch();<br> stopwatch.Start();<br> F testForm = new F();<br> testForm.Show();<br> testForm.Close();<br> stopwatch.Stop();<br> Console.WriteLine(&quot;Form [&#123;0&#125;] took &#123;1&#58;#,##0.0&#125; seconds to open&quot;, typeof(F), stopwatch.Elapsed.TotalSeconds);<br> Assert.IsTrue(stopwatch.Elapsed {ltHTMLChar} _ExpectedLoadTime, <br> string.Format(&quot;Loading time (&#123;0&#58;#,##0.0&#125; seconds) exceed the expected time (&#123;1&#58;#,##0.0&#125; seconds).&quot;, <br> stopwatch.Elapsed.TotalSeconds, _ExpectedLoadTime.TotalSeconds));<br> &#125;<br> &#125;<br> <br> [TestFixture]<br> public class LoginFormTests &#58; FormTestBase{ltHTMLChar}LoginForm{gtHTMLChar}<br> &#123;<br> &#125;<br><br> [TestFixture]<br> public class MainFormTests &#58; FormTestBase{ltHTMLChar}MainForm{gtHTMLChar}<br> &#123;<br> &#125;</p><dd class="ssw15-rteElement-FigureNormal">​Figure&#58; This code tests that the LoginForm and MainForm load in under 4 seconds​<br></dd>


