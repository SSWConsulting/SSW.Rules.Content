---
type: rule
title: "Do you avoid using mailto: on your website?"
uri: avoid-using-mailto-on-your-website
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-avoid-using-mailto-on-your-website
created: 2016-11-16T17:15:31.000Z
archivedreason: null
guid: 527b3e90-652e-4832-bb18-17d39421ec0e
---

Don't ever display valid individual email addresses or `mailto:` on a website. Nasty people on the web have created "Email Harvesting" tools. These programs search public areas on the Internet to compile, capture, or otherwise "harvest" lists of email addresses from web pages, newsgroups, and chat rooms. Any email address that is spelled out can be captured and therefore gets attacked with spam.

The best way to avoid it is not to display valid individual email addresses in text format (especially in the form of "mailto:") on your website.

<!--endintro-->

::: greybox
FirstnameSurname@ssw.com.au
:::

::: bad
Figure: Bad way - normal email address in text format
:::

###  Better way: encryption technique 

1. Store email addresses in the web.config file

```xml
<configuration> 
    <appSettings> 
        <add key="SampleEncodedEmailAddress" value="David@sample.com.au" /> 
        ...
    </appSettings> 
</configuration>
```

2. Encode them on the server using the BitConverter class

```vbnet
Dim email As String = ConfigurationSettings
        .AppSettings("SampleEncodedEmailAddress")

Application("SampleEncodedEmailAddress") = BitConverter
        .ToString( _ ASCIIEncoding.ASCII.GetBytes(email))
        .Replace("-", "")
```

3. Decode on the client with a JavaScript function in the JavaScript

```html
<a id="linkContact" href="javascript:sendEmail('44617669644073616D706C652E636F6D2E6175')">
    CONTACT David
</a>
```

We have a program called [SSW CodeAuditor](https://codeauditor.com) to check for this rule.
