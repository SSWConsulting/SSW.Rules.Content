---
seoDescription: Use a Web Service to securely send emails from your Windows application without storing email server configurations.
type: rule
title: Do you use Web Service to send emails?
uri: use-web-service-to-send-emails
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T01:48:00.000Z
guid: df81ed0a-c8a1-46bf-82ea-892929c7191f
---

In a Windows application, if you need to send mail, please use a WebService to do this, because using WebService to send emails is safer.You don't need to store the email server configuration in your application.config file, which can be installed on the client and be exposed to someone who could take advantage of it.

<!--endintro-->

```cs
SmtpClient client = new SmtpClient();
try
{
    client.Host = "****.***.com.au";
    client.Port = 25;
    client.UseDefaultCredentials = true;

    MailAddress from = new MailAddress("test@ssw.com.au");

    string unrecAddy = "test@ssw.com.au";
    MailAddress to = new MailAddress(unrecAddy);

    MailMessage mailMessage = new MailMessage(from, to);

    mailMessage.Subject = "aaa";
    string strVer = "aaa";
    mailMessage.Body = "aaa";

    client.Send(mailMessage);

}
catch(Exception ex)
{
    client.SendAsyncCancel();
    MessageBox.Show(ex.ToString());
}
```

::: bad
Bad example - Send mail without webservice
:::

```cs
Emailer.PubicFunction pf = new EmailWebServices.Emailer.Publiction();
pf.SendMail("Test", textBox3.Text, textBox1.Text, textBox2.Text, false, "", null);
```

::: good
Good example - Send mail use webservice
:::
