---
type: rule
archivedreason: 
title: Do you use dashes in your URLs?
guid: 9eec1cdc-ff5f-47cf-b4a6-0936ec4c62d4
uri: do-you-use-dashes-in-your-urls
created: 2015-11-09T20:51:46.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 16
  title: Tiago Araujo
related: []

---

For maximum readability and SEO use kebab-case (dashes) in your URLs.

<!--endintro-->


::: greybox
https://northwind.com/ **pageonworddocumentation** 
:::



::: bad
Figure: Bad example - No kebab-case in URL 


:::



::: greybox
https://northwind.com/ **PageOnWordDocumentation** 
:::



::: bad
Figure: Bad example - PascalCase (better readability and still works in small caps, but other people might share it without the MixedCase)


:::



::: greybox
https://northwind.com/ **page on word documentation** 

...will become

 https://northwind.com/ **page20%on20%word20%documentation** 
:::



::: bad
Figure: Bad example - spaces it will show up in your URL structure as 20%, which is bad for readability and SEO


:::



::: greybox
https://northwind.com/ **page\_on\_word\_documentation** 
:::

 **Figure: OK example - underscored (snake\_case) URLs have good readability but are not recommended by Google

** 

::: greybox
https://northwind.com/ **page-on-word-documentation** 
:::



::: good
Figure: Good example - kebab-case is recommended by Google


:::


**Note:** this is only for the pages and documents within a website - not for the domain. Domains are bad when they have "-" in them!

Read more on [SEO 101: Hyphens vs. Underscores in URLs](https://www.seomechanic.com/seo-101-hyphens-underscores-_-urls/)

### More info

You can install the IIS [URL Rewrite Module](http://learn.iis.net/page.aspx/460/using-the-url-rewrite-module/) for IIS7 you can make ugly URL's much more friendly.
<dl class="image">&lt;dt&gt;<img src="friendly-url-rule.jpg" alt="Rewrite the HTML" style="margin:5px;">&lt;/dt&gt;<dd>Figure: Rewrite both the HTML in the page and the incoming URL's to be friendly</dd></dl>
The caveat here is that it will only work if the URL is in the clear on the page.

**Note:** This could only be done with certain links as others are postbacks as well.
