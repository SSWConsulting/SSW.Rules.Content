---
type: rule
archivedreason: 
title: Do you keep the URL next to each link on printing?
guid: b91ec62e-beea-42b3-8d70-6349dd1fc889
uri: print-url
created: 2016-06-08T21:04:47.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Tiago Araujo
  url: https://ssw.com.au/people/tiago-araujo
related: []
redirects:
- do-you-keep-the-url-next-to-each-link-on-printing

---

We have a rule on [using relevant words on links](/relevant-words-on-links). How to make sure people will know which words are links and what the links are after printing a page?

<!--endintro-->

As a good practice, you should use CSS to print the URL's next to each link when printing:

```
@media print {
  a[href]:after {
    content: " (" attr(href) ")";
  }
}
```

In specific cases, like on breadcrumbs and logo, you don't want these URL's, so you should override the style:

```
@media print {
  .breadcrumba[href]:after {
  content: none;
}
```
::: good  
![Figure: Good example - printing links on the content but avoiding it on obvious places, like the logo and bradcrumbs](print-url.jpg)  
:::
