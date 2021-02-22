---
type: rule
archivedreason: 
title: Do you format "Environment.NewLine" at the end of a line?
guid: 283e068f-6fa7-4385-b022-b1a80dfe92bf
uri: format-environment-newline-at-the-end-of-a-line
created: 2018-04-26T21:46:51.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-format-environment-newline-at-the-end-of-a-line

---

You should format "Environment.NewLine" at the end of a line.


<!--endintro-->



```
string message = "The database is not valid." + Environment.NewLine + "Do you want to upgrade it? ";
```




::: bad
Bad Example: "Environment.NewLine" isn't at the end of the line 

:::





```
string message = "The database is not valid." + Environment.NewLine;
message += "Do you want to upgrade it? ";
```




::: good
Good Example:  "Environment.NewLine" is at the end of the line 

:::





```
return string.Join(Environment.NewLine, paragraphs);
```




::: good
Good Example: "Environment.NewLine" is an exception for String.Join  
:::
