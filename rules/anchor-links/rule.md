---
seoDescription: Learn how to use named anchor links to link to specific places within a page, providing "jump-to" functionality and customizable URLs.
type: rule
archivedreason:
title: Do you know how to use anchor links?
guid: 599548c1-a1ff-4f0a-aed8-5938acb6fe83
uri: anchor-links
created: 2012-07-17T20:11:55.0000000Z
authors:
  - title: Tiago Araujo
    url: https://ssw.com.au/people/tiago-araujo
related:
  - efficient-anchor-names
redirects:
  - do-you-know-how-to-use-named-anchor-links
---

The attribute "name" allows you to link to specific places within the page, via the `<a>` tag.

This is especially useful in long pages that can be separated into sections. You can create a named anchor in each of these section headings to provide "jump-to" functionality. In other words, you can have a different URL for each piece of content on the same page.

<!--endintro-->

```html
<h2><a name="get-started"></a>Get Started</h2>
```

**Figure: This is how you add an anchor name to an specific section of your page. Note it doesn't have the hash mark and the anchor tag is empty**

You now have a custom URL that points to the specific section of the page. It is the page URL followed by the hashtag plus the name you chose:

::: greybox
yourpage.com#get-started
:::
**Figure: This is how your custom URL will look like**

You can use this new URL to point users to that specific section of your page.

To create a link to your anchor named section inside the same page, simply add a new "href" anchor tag - now with a hash mark followed by the name you chose:

```html
<a href="#get-started">Go to Get Started section</a>
```

**Figure: This is how you add a link to that anchor name you created inside the same page. Remember to add the hashtag**

**Tip:** Use a hashtag **alone** to link to the top of a page. E.g. `<a href="#">&Go to top</a>`
