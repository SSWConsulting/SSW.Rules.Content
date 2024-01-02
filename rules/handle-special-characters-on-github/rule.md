---
type: rule
title: Do you know how to handle special characters in GitHub Secrets and Variables?
uri: handle-special-characters-on-github
authors:
  - title: Zach Keeping
    url: https://ssw.com.au/people/zach-keeping
created: 2023-08-21T01:00:02.774Z
guid: 0576bb6b-684d-4896-b494-0c4ee014a490
---
GitHub Secrets and Variables are an invaluable way to store sensitive information such as API keys, tokens, and passwords for use in your GitHub Actions. However, it's important to understand how special characters are handled in order to avoid issues in your workflows.

<!--endintro-->

When storing Secrets and Variables in GitHub, it's common that these are stored with special characters (for example: "$", "&", "(", ")", "<", ">"). We have a few ways to use these in our GitHub Actions:

1. ❌ **Bad** - Referencing the raw text as-is
2. ✅ **Good** - Referencing the raw text in enclosing quotes
3. ✅ **Best** - Escaping all special characters when saving the Secret or Variable

### ❌ Referencing as-is

Storing text containing special characters Secret or Variable and referencing this directly in our Action can lead to issues as it might not be interpreted as text as intended.

![Figure: A Secret or Variable with special characters can cause issues if improperly handled](secret-with-parentheses.png)

::: bad
![Figure: Bad example - Accessing this Secret as-is will lead to a syntax error in our Action](action-no-quotes.png)
:::

![Figure: A syntax error is thrown due to the special characters](parentheses-error.png)

### ✅ Referencing in quotes

One simple way to avoid this is to wrap your Secrets or Variables in single or double quotes when using them in your GitHub Actions. This will ensure that these are not interpreted incorrectly and will be treated as a string.

::: good
![Figure: Good example - Wrapping our Secret in quotes means it will be correctly treated as text](action-with-quotes.png)
:::

![Figure: Our Secret is now handled correctly when wrapped in quotes](output-with-quotes.png)

However, it's important to note that this can still cause issues in certain scenarios. For instance, if the Secret or Variable contains double quotes and is also wrapped by double quotes in our Action, it will have trouble parsing this and will throw an error.

::: bad
![Figure: Bad example - Trying to wrap this Secret in double quotes will lead to an error](secret-with-quote.png)
:::

![Figure: The lone double quote character means this string cannot be interpreted correctly](quote-error.png)

### ✅ Escaping all special characters when storing Secret or Variable (Recommended)

A better way to handle this is to escape these special characters when storing your Secret or Variable. This can be done by adding a backslash ("") before each special character. This will ensure that these characters are interpreted as literal characters and will also help prevent potential ambiguity from using enclosing quotes.

::: good
![Figure: Good (best) example - Escaping the special characters mean this string will be interpreted correctly](escaped-secret.png)
:::

![Figure: The escaped characters mean our string is now interpreted correctly without the need to wrap in quotes](output-escaped.png)
