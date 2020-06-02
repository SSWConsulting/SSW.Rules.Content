

---
uri: do-you-have-a-integration-test-for-your-send-mail-code
title: Do you have a integration test for your send mail code?
created: YYYY-03-DD 20:42:54
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> The code below shows how you could use TestSmtpServer&#160;to test your send mail code&#58;​<br> </span>

<p class="ssw15-rteElement-CodeArea">​DotNetOpenMailProvider provider = new DotNetOpenMailProvider();<br>NameValueCollection configValue = new NameValueCollection();<br>configValue[&quot;smtpServer&quot;] = &quot;127.0.0.1&quot;;<br>configValue[&quot;port&quot;] = &quot;8081&quot;;<br>provider.Initialize(&quot;providerTest&quot;, configValue);<br>TestSmtpServer receivingServer = new TestSmtpServer();<br>try<br>&#123;<br> receivingServer.Start(&quot;127.0.0.1&quot;, 8081);<br> provider.Send(&quot;phil@example.com&quot;, <br> &quot;nobody@example.com&quot;, <br> &quot;Subject to nothing&quot;, <br> &quot;Mr. Watson. Come here. I need you.&quot;);<br>&#125;<br>finally<br>&#123;<br> receivingServer.Stop();<br>&#125;<br>// So Did It Work?<br>Assert.AreEqual(1, receivingServer.Inbox.Count);<br>ReceivedEmailMessage received = receivingServer.Inbox[0];<br>Assert.AreEqual(&quot;phil@example.com&quot;, received.ToAddress.Email);</p><dd class="ssw15-rteElement-FigureGood">Figure&#58; This code could help you validate the send mail code​​<br></dd>


