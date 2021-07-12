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

According to [SonarSource](https://rules.sonarsource.com/html/RSPEC-1094) and World Wide Web Consortium (W3C), Meta tags should not be used to refresh or redirect. Specifically, It is discouraged to use ```<meta http-equiv="refresh">```

<!--endintro--> 

This is a bad practice for many reasons. For example, if a user clicks the 'Back' button, some browers will go back to the redirecting page, which will prevent the user from actually going back.

Instead, a better practice to refresh the page is to use Ajax, to refresh only what needs to be refreshed and not the whole page. And to redirect to another page, we should use the HTTP response status code 301 'Moved Permanently' and 302 'Found'.

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
