---
type: rule
title: Do you format "Environment.NewLine" at the end of a line?
uri: format-environment-newline-at-the-end-of-a-line
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-format-environment-newline-at-the-end-of-a-line
created: 2018-04-26T21:46:51.000Z
archivedreason: null
guid: 283e068f-6fa7-4385-b022-b1a80dfe92bf
---
You should format "Environment.NewLine" at the end of a line.

<!--endintro-->

```csharp
string message = "The database is not valid." + Environment.NewLine + "Do you want to upgrade it? ";
```

::: bad
Bad example - "Environment.NewLine" isn't at the end of the line 
:::

```csharp
string message = "The database is not valid." + Environment.NewLine;
message += "Do you want to upgrade it? ";
```

::: good
Good example -  "Environment.NewLine" is at the end of the line 
:::

```csharp
return string.Join(Environment.NewLine, paragraphs);
```

::: good
Good example - "Environment.NewLine" is an exception for String.Join\
:::
