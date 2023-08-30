---
type: rule
title: Do you use a regular expression to validate an URL?
uri: use-a-regular-expression-to-validate-an-uri
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-use-a-regular-expression-to-validate-an-url
created: 2018-04-26T17:31:11.000Z
archivedreason: null
guid: 45e21c54-baae-4c39-a245-8ce58c49978a
---
A regex is the best way to verify an URI.

<!--endintro-->

```csharp
public bool IsValidUri(string uri)
{
try 
{ 
Uri testUri = new Uri(uri); 
return true; 
} 
catch (UriFormatException ex)
{ 
return false; 
} 
}
```

::: bad
Figure: Bad example of verifying URI

:::

```csharp
public bool IsValidUri(string uri) 
{ 
// Return true if it is in valid Uri format.
return System.Text.RegularExpressions.Regex.IsMatch( uri,@"^(http|ftp|https)://([^\/][\w-/:]+\.?)+([\w- ./?/:/;/\%&=]+)?(/[\w- ./?/:/;/\%&=]*)?"); 
}
```

::: good
Figure: Good example of verifying URI 

:::

You should have unit tests for it, see our [Rules to Better Unit Tests](https://www.ssw.com.au/ssw/Standards/Rules/RulesToBetterUnitTests.aspx) for more information.