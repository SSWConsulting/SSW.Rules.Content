---
type: rule
archivedreason: 
title: Do you use Environment.NewLine to make a new line in your string?
guid: 200df127-6aaf-415d-a54d-933a228b14fe
uri: use-environment-newline-to-make-a-new-line-in-your-string
created: 2018-04-26T22:46:14.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Matt Wicks
  url: https://ssw.com.au/people/matt-wicks
related: []
redirects:
- do-you-use-environment-newline-to-make-a-new-line-in-your-string

---

When you need to create a new line in your string, make sure you use Environment.NewLine, and then literally begin typing your code on a new line for readability purposes.

<!--endintro-->



```
string strExample = "This is a very long string that is \r\n not properly implementing a new line.";
```




::: bad
Bad Example: The string has implemented a manual carriage return line feed pair (\r\n)  
:::





```
string strExample = "This is a very long string that is " + Environment.NewLine +		 " properly implementing a new line.";
```






::: good
OK Example: The new line is created with Enviroment.NewLine (but strings are immutable)

:::



```
var example = new StringBuilder();

example.AppendLine("This is a very long string that is ");

example.Append(" properly implementing a new line.");
```






::: good
Good Example: The new line is created by the StringBuilder and has better memory utilisation

:::
