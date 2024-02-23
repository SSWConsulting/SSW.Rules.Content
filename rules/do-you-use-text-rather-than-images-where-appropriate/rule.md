---
type: rule
title: Do you use text rather than images where appropriate?
uri: do-you-use-text-rather-than-images-where-appropriate
authors: []
related: []
redirects: []
created: 2015-10-13T00:08:16.000Z
archivedreason: null
guid: d1c7e65e-61de-44db-8f7d-e9f95f8d4e6c
---
Using text rather than images has multiple advantages:

* Downloads faster - a users patience extends to about 7 seconds.
* Cheaper to update - a simple find and replace.
* Discoverable by search engines - if people can't get to your site, what's the point of it being there?
* Readable on an iPhone - Images will either be resized or require scrolling, which would create difficulties for readability.

<!--endintro-->

```html
<img src="Images/Heading_Welcome.gif>
```

::: bad 
Bad Example - Using image for text header
:::

```hcl
<h1>Welcome to My Page</h1>
```

::: good
Good Example - This text can be easily rendered by the browser and recognized by search engine
:::