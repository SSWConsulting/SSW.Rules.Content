---
type: rule
title: Do you avoid absolute internal links?
uri: avoid-absolute-internal-links
authors:
  - title: Adam Cogan
    url: https://www.ssw.com.au/people/adam-cogan
created: 2023-05-29T18:50:27.379Z
guid: 95153625-a5a1-4e5a-8831-378c18e50cce
---
It is generally advisable to avoid using absolute internal links whenever possible.  Absolute links include the full URL, including the domain name, when linking to internal pages within the same website.

Using absolute internal links can lead to challenges during website migration or domain name changes. If the website's domain or URL structure is modified, all absolute links within the website would require updating. This can be a time-consuming and error-prone process, potentially resulting in broken links and a negative user experience.
      
<!--endintro-->

Using relative internal links, which specify the path to the linked page relative to the current page, is often preferred as it offers more flexibility and can prevent issues when migrating or changing domain names. Relative links are less prone to breaking and make it easier to maintain the website's structure and navigation.

``` html
<a href="https://ssw.com.au/Company/ContactUs/">Contact us</a>
```
::: bad
Figure: Bad example - Using absolute paths for internal links
:::

``` html
<a href="/Company/ContactUs/">Contact us</a>
```
::: good
Figure: Good example - Using relative paths for internal links
:::

While there may be some scenarios where absolute internal links are necessary, like [on newsletters](/use-absolute-paths-on-newsletters), it is generally advisable for website developers to prioritize the use of relative links. Relative links offer greater flexibility, ease of maintenance, and scalability, ultimately contributing to a more robust and user-friendly website.