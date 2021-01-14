---
type: rule
archivedreason: 
title: Search - Do you use default zone URL in search content source
guid: 1cd1d586-7c3a-45ea-9b52-821d0ddfebbb
uri: search-do-you-use-default-zone-url-in-search-content-source
created: 2016-05-20T07:29:19.0000000Z
authors:
- title: Mark Liu
  url: https://ssw.com.au/people/mark-liu
- title: William Yin
  url: https://ssw.com.au/people/william-yin
related: []
redirects:
- use-default-zone-url-in-search-content-source

---

Using default zone URL in search content source, it will be automatically convert to the relative URL on the search result.e.g. if a user access  search center via http://projects.ssw.com.au/search, the result will be like http://projects.ssw.com.au/search/xxx. While another user access search center via http<mark>s</mark>://projects.ssw.com.au/search, the result will be http<mark>s</mark>://projects.ssw.com.au/search/xxx.

![](https-data-source.jpg)
::: bad
Bad example: use https://projects.ssw.com.au  
:::


![](http-data-source.jpg)
::: good
Good example: use http://project.ssw.com.au  
:::




<!--endintro-->
