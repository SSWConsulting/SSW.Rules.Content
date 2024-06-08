---
type: rule
title: Do you use a regular expression to validate an email address?
uri: use-a-regular-expression-to-validate-an-email-address
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-use-a-regular-expression-to-validate-an-email-address
created: 2018-04-25T23:15:46.000Z
archivedreason: null
guid: 1b6d9a4c-f7b7-4774-9c80-c722e27389a3
---
A regex is the best way to verify an email address.

<!--endintro-->

```csharp
public bool IsValidEmail(string email)
{
 // Return true if it is in valid email format.
 if (email.IndexOf("@") <= 0) return false; 
 if (email.EndWith("@")) return false; 
 if (email.IndexOf(".") <= 0) return false; 
 if ( ... 
}
```

::: bad
Figure: Bad example of verify email address

:::

```csharp
public bool IsValidEmail(string email) 
{ 
 // Return true if it is in valid email format.
 return System.Text.RegularExpressions.Regex.IsMatch( email, 
 @"^([\w-\.]+)@(([[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$";
}
```

::: good
Figure: Good example of verify email address
:::