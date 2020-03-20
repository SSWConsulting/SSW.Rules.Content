---
type: rule
archivedreason: Sending emails in applications is usually handled through 3rd party providers nowadays e.g. SendGrid. As a result mail sending checks should be covered off by HealthChecks
title: Do you have a integration test for your send mail code?
guid: 993bfcb8-ade1-45b0-9a91-2307123edd91
uri: do-you-have-a-integration-test-for-your-send-mail-code
created: 2020-03-12T20:42:54.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


The code below shows how you could use TestSmtpServer&#160;to test your send mail code&#58;​<br>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-CodeArea">​DotNetOpenMailProvider provider = new DotNetOpenMailProvider();<br>NameValueCollection configValue = new NameValueCollection();<br>configValue[&quot;smtpServer&quot;] = &quot;127.0.0.1&quot;;<br>configValue[&quot;port&quot;] = &quot;8081&quot;;<br>provider.Initialize(&quot;providerTest&quot;, configValue);<br>TestSmtpServer receivingServer = new TestSmtpServer();<br>try<br>&#123;<br> receivingServer.Start(&quot;127.0.0.1&quot;, 8081);<br> provider.Send(&quot;phil@example.com&quot;, <br> &quot;nobody@example.com&quot;, <br> &quot;Subject to nothing&quot;, <br> &quot;Mr. Watson. Come here. I need you.&quot;);<br>&#125;<br>finally<br>&#123;<br> receivingServer.Stop();<br>&#125;<br>// So Did It Work?<br>Assert.AreEqual(1, receivingServer.Inbox.Count);<br>ReceivedEmailMessage received = receivingServer.Inbox[0];<br>Assert.AreEqual(&quot;phil@example.com&quot;, received.ToAddress.Email);</p><dd class="ssw15-rteElement-FigureGood">Figure&#58; This code could help you validate the send mail code​​<br></dd>


