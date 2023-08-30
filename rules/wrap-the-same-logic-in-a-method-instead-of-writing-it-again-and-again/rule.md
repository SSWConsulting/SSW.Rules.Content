---
type: rule
archivedreason: 
title: DRY - Do you wrap the same logic in a method instead of writing it repeatedly whenever it's used?
guid: 68299342-ec35-4f73-a340-4fdf7eb2144d
uri: wrap-the-same-logic-in-a-method-instead-of-writing-it-again-and-again
created: 2018-04-26T23:35:54.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-wrap-the-same-logic-in-a-method-instead-of-writing-it-again-and-again-whenever-its-used

---

Is your code DRY? Any logic that is used more than once, should be encapsulated in a method, and the method called wherever it is needed.

This will reduce redundancy, decrease maintenance effort, improve efficiency and reusability, and make the code more clear to read.

<!--endintro-->

::: info
DRY, which stands for ‘don’t repeat yourself,’ is a principle of software development that aims at reducing the repetition of patterns and code duplication in favor of abstractions and avoiding redundancy.
:::

```csharp
public class WarningEmail
{
    //...
    public void SendWarningEmail(string pFrom, string pTo, string pCC, string pUser, string pPwd, string pDomain)
    {
        //...
        MailMessage sMessage = new MailMessage();
        sMessage.From = new MailAddress(pFrom);
        sMessage.To.Add(pTo);
        sMessage.CC.Add(pCC);
        sMessage.Subject = "This is a Warning";
        sMessage.Body = GetWarning();
        SmtpClient sSmtpClient = new SmtpClient();
        sSmtpClient.Credentials = new NetworkCredential(pUser, pPwd, pDomain);
        sSmtpClient.Send(sMessage);
        //...
    }
}

public class ErrorEmail
{
    public void SendErrorEmail(string pFrom, string pTo, string pCC, string pUser, string pPwd, string pDomain)
    {
        //...
        MailMessage sMessage = new MailMessage();
        sMessage.From = new MailAddress(pFrom);
        sMessage.To.Add(pTo);
        sMessage.CC.Add(pCC);
        sMessage.Subject = "This is a Error";
        sMessage.Body = GetError();
        SmtpClient sSmtpClient = new SmtpClient();
        sSmtpClient.Credentials = new NetworkCredential(pUser, pPwd, pDomain);
        sSmtpClient.Send(sMessage);
        //...
    }
}
```
::: bad
Bad example - Write the same logic repeatedly 
:::


```csharp
public class WarningEmail
{
    //...
    public void SendWarningEmail(string pFrom, string pTo, string pCC, string pUser, string pPwd, string pDomain)
    {
        //...
        EmailHelper.SendEmail(pFrom, pTo, pCC, "This is a Warning", GetWarning(), pUser, pPwd, pDomain);
        //...
    }
}

public class ErrorEmail
{
    public void SendErrorEmail(string pFrom, string pTo, string pCC, string pUser, string pPwd, string pDomain)
    {
        //...
        EmailHelper.SendEmail(pFrom, pTo, pCC, "This is an Error", GetError(), pUser, pPwd, pDomain);
        //...
    }
}

public class EmailHelper
{ 
    public static void SendEmail(string pFrom, string pTo, string pCC, string pSubject, string pBody, string pUser, string pPwd, string pDomain)
    {
        MailMessage sMessage = new MailMessage();
        sMessage.From = new MailAddress(pFrom);
        sMessage.To.Add(pTo);
        sMessage.CC.Add(pCC);
        sMessage.Subject = pSubject;
        sMessage.Body = pBody;
        SmtpClient sSmtpClient = new SmtpClient();
        sSmtpClient.Credentials = new NetworkCredential(pUser, pPwd, pDomain);
        sSmtpClient.Send(sMessage);
    } 
}
```

::: good
Good example - Put the same logic in a method and make it reusable 
:::
