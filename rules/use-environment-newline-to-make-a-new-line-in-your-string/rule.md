---
type: rule
title: Do you use Environment.NewLine to make a new line in your string?
uri: use-environment-newline-to-make-a-new-line-in-your-string
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Matt Wicks
    url: https://ssw.com.au/people/matt-wicks
related: []
redirects:
  - do-you-use-environment-newline-to-make-a-new-line-in-your-string
created: 2018-04-26T22:46:14.000Z
archivedreason: null
guid: 200df127-6aaf-415d-a54d-933a228b14fe
---
When you need to create a new line in your string, make sure you use Environment.NewLine, and then literally begin typing your code on a new line for readability purposes.

<!--endintro-->

```csharp
string strExample = "This is a very long string that is \r\n not properly implementing a new line.";
```

::: bad
Bad example - The string has implemented a manual carriage return line feed pair `\r\n`
:::

```csharp
string strExample = "This is a very long string that is " + Environment.NewLine +
		 " properly implementing a new line.";
```

::: good
OK example - The new line is created with Enviroment.NewLine (but strings are immutable)

:::

```csharp
var example = new StringBuilder();

example.AppendLine("This is a very long string that is ");

example.Append(" properly implementing a new line.");
```

::: good
Good example - The new line is created by the StringBuilder and has better memory utilisation
:::
