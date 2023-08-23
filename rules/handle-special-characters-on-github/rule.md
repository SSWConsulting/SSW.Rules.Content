---
type: rule
title: Do you know how to handle special characters in GitHub Secrets and
  Variables?
uri: handle-special-characters-on-github
authors:
  - title: Zach Keeping
    url: https://ssw.com.au/people/zach-keeping/
created: 2023-08-21T01:00:02.774Z
guid: 0576bb6b-684d-4896-b494-0c4ee014a490
---
GitHub Secrets and Variables are an invaluable way to store sensitive information such as API keys, connection strings, and passwords for use in your GitHub Actions. However, it's important to understand how special characters are handled in order to avoid issues in your workflows.

<!--endintro-->

When storing Secrets and Variables in GitHub, it's common that these are stored with special characters (such as "$", "&", "(", ")", "<", ">") which can cause issues if these are used in your GitHub Actions as-is.

[bad example]

One simple way to avoid this is to wrap your Secrets or Variables in single or double quotes when using them in your GitHub Actions. This will ensure that these are not interpreted incorrectly and will be treated as a string.

[good example]

However, it's important to note that this can still cause issues in certain scenarios. For instance, if the Secret or Variable contains a double quote and is wrapped by double quotes, it will have trouble parsing this and will throw an error.

[bad example]

A better way to handle this is to escape these special characters when storing your Secret or Variable. This can be done by adding a backslash ("\") before each special character. This will ensure that these characters are interpreted as literal characters and will also help prevent potential ambiguity from using enclosing quotes.

[better example]