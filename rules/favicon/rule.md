---
type: rule
archivedreason: 
title: Do you add a favicon to your website?
guid: d9136030-ff29-4617-8d0b-074096ae8120
uri: favicon
created: 2015-10-13T00:47:56.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Tiago Araujo
  url: https://ssw.com.au/people/tiago-araujo
related:
- does-your-sharepoint-site-have-a-favicon
redirects:
- do-you-have-a-favicon-in-your-webpage

---

A Favicon is an image file included on professionally developed sites. The favicon reflects the look and feel of the website or the organizations' visual identity.

<!--endintro-->

::: bad  
![Figure: Bad example - When you don't add a favicon the user sees the generic browser's icon](favicon-bad.jpg)  
:::

::: good  
![Figure: Good example - Using the favicon gives your website professional look and feel](favicon-good.jpg)  
:::

### Which formats and sizes to use?

The format of the image must be one of PNG (a W3C standard), GIF, or ICO. You can export your favicon in all necessary sizes on [Favicon Generator website](https://realfavicongenerator.net).

### How to implement the favicon?

1. Copy your company's favicon to the root of the site
2. Add the highlighted code below inside the `<head>` tag in your HTML

``` html
<head>
<title>Page Title</title>
<link rel="shortcut icon" href="/images/favicon.ico" type="image/x-icon" />
</head>
```
**Figure: One line of HTML lets you add your company's icon to your web page** 

This works for most websites, including ASPX WebForms, MVC and WordPress.
