---
type: rule
archivedreason: 
title: C# Code - Do you use string literals?
guid: 849c1ee3-a72d-4471-b7db-8c363b663e0e
uri: how-string-should-be-quoted
created: 2018-04-30T22:20:15.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Daniel Mackay
  url: https://ssw.com.au/people/daniel-mackay
related: []
redirects:
- c-code-do-you-use-string-literals

---

Do you know String should be @-quoted instead of using escape character for "\\"?
The @ symbol specifies that escape characters and line breaks should be ignored when the string is created.

As per: [Strings](https://docs.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2008/c84eby0h(v=vs.90)?redirectedfrom=MSDN)

<!--endintro-->

``` cs
string p2 = "\\My Documents\\My Files\\";
```
::: bad
Figure: Bad example - Using "\\"  
:::

``` cs
string p2 = @"\My Documents\My Files\";
```
::: good
Figure: Good example - Using @
:::

## Raw String Literals

In C#11 and later, we also have the option to use raw string literals.  These are great for embedding blocks of code from another language into C# (e.g. SQL, HTML, XML, etc.).  They are also useful for embedding strings that contain a lot of escape characters (e.g. regular expressions).

Another advantage of Raw String Literals is that the redundant whitespace is trimmed from the start and end of each line, so you can indent the string to match the surrounding code without affecting the string itself.

```cs
var bad = "<html>" +
           "<body>" +
           "<p class=\"para\">Hello, World!</p>" +
           "</body>" +
           "</html>";
```

::: bad
Figure: Bad example - Single quotes  
:::

```cs
var good = """
           <html>
           <body>
           <p class="para">Hello, World!</p>
           </body>
           </html>
           """;
```

::: good
Figure: Good example - Using raw string literals
:::

For more information on Raw String literals see [learn.microsoft.com/en-us/dotnet/csharp/language-reference/tokens/raw-string](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/tokens/raw-string)
