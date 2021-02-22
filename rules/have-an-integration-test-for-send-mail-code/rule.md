---
type: rule
archivedreason: Sending emails in applications is usually handled through 3rd party providers nowadays e.g. SendGrid. As a result mail sending checks should be covered off by HealthChecks
title: Do you have a integration test for your send mail code?
guid: 993bfcb8-ade1-45b0-9a91-2307123edd91
uri: have-an-integration-test-for-send-mail-code
created: 2020-03-12T20:42:54.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-have-a-integration-test-for-your-send-mail-code

---

The code below shows how you could use TestSmtpServer to test your send mail code:

<!--endintro-->



```
DotNetOpenMailProvider provider = new DotNetOpenMailProvider();
NameValueCollection configValue = new NameValueCollection();
configValue["smtpServer"] = "127.0.0.1";
configValue["port"] = "8081";
provider.Initialize("providerTest", configValue);
TestSmtpServer receivingServer = new TestSmtpServer();
try
{
 receivingServer.Start("127.0.0.1", 8081);
 provider.Send("phil@example.com", 
 "nobody@example.com", 
 "Subject to nothing", 
 "Mr. Watson. Come here. I need you.");
}
finally
{
 receivingServer.Stop();
}
// So Did It Work?
Assert.AreEqual(1, receivingServer.Inbox.Count);
ReceivedEmailMessage received = receivingServer.Inbox[0];
Assert.AreEqual("phil@example.com", received.ToAddress.Email);
```




::: good
Figure: This code could help you validate the send mail code

:::
