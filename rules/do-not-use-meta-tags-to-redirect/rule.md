---
type: rule
archivedreason:
title: Meta tags should not be used to refresh or redirect
guid: 8b687b7d-87cc-4fa3-8e4c-124181c00c88
uri: do-not-use-meta-tags-to-redirect
created: 2021-06-28T02:47:34.0000000Z
authors:
  - title: Tom Bui
    url: https://www.ssw.com.au/people/tom-bui
related:

---
### Meta tags should not be used to refresh or redirect

According to [SonarSource](https://rules.sonarsource.com/html/RSPEC-1094), Meta tags should not be used to refresh or redirect

<!--endintro-->

Use of ```<meta http-equiv="refresh">``` is discouraged by the World Wide Web Consortium (W3C).

If a user clicks the 'Back' button, some browers will go back to the redirecting page, which will prevent the user from actually going back.

To refresh the page, a better alternative is to use Ajax, to refresh only what needs to be refreshed and not the whole page.

To redirect to another page, using the HTTP response status code 301 'Moved Permanently' and 302 'Found' is a better option.

``` html
<head>
  <meta http-equiv="refresh" content="5">   <!-- Non-Compliant -->
  <meta name="description" content="...">
</head>
```
**Figure: Bad Example that uses meta tags to refresh**

``` html
<head>
  <meta name="description" content="...">
</head>
```
**Figure: Good Example that does not use meta tags to refresh**
