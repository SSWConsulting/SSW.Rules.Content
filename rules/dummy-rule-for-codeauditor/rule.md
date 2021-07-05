---
type: rule
title: Dummy Rule for CodeAuditor Testing
uri: dummy-rule-for-codeauditor
authors:
  - title: Tom
created: 2021-07-02T07:20:08.801Z
guid: 3facc7b4-daae-46f5-9a96-0f944a22c9c7
---
1. Anchor names must be valid

\- Bad Example:

<a name="#Anchor">Text1</a>

<a name="123Anchor">Text2</a>

<a name="This Is Anchor">Text3</a>

2. Meta tags must not redirect

\- Bad Example:

<meta http-equiv="refresh" content="5">meta1</meta>

<meta name="description" content="...">meta2</meta>

FONT tags must not be used

\- Bad Example:

<font color="red">Text</font>

4. No UNC in HTML Link

\- Bad Example:

<a href="\\hippo\ssw\">hippo UNC</a>

5. Pages must contain META description

\- Bad Example:

<meta content="The Sydney Morning Herald - News online - News">meta3</meta>

6. URLs should not have space

\- Bad Example:

<a href="https://www.ssw.com.au/rules/how to get better at coding">hippo UNC</a>

7. Documents should not contain "click here"

\- Bad Example:

<a href="https://www.google.com/?client=safari">Click Here</a>

8. Specify rel icon at the site level

\- Bad Example:

<link rel="blahblah" href="/images/favicon.ico" type="image/x-icon">bad link</link>

\- Good Example:

<head>

<title>Page Title</title>

<link rel="icon" href="/images/favicon.ico" type="image/x-icon">good link</link>

</head>

9. HTML pages must have DocType

\- Good Example:

<!DOCTYPE>

10. No email address in all web pages.

\- Bad Example:

<p>tomisawesome@gmail.com</p>