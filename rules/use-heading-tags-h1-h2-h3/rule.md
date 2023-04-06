---
type: rule
archivedreason: 
title: Do you use heading tags where appropriate (H1, H2, H3...)?
guid: a8ecbdff-44f9-4b73-b7fe-4285629e3f1f
uri: use-heading-tags-h1-h2-h3
created: 2016-08-05T17:30:06.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Tiago Araujo
  url: https://ssw.com.au/people/tiago-araujo
related: 
- make-title-h1-and-h2-tags-descriptive
redirects:
- do-you-use-heading-tags-where-appropriate-h1-h2-h3
- do-you-use-heading-tags-where-appropriate-(h1-h2-h3-)

---

You should understand the hierarchy and try to use the heading tags (&lt;H1&gt;, &lt;H2&gt; or &lt;H3&gt;...) for titles and subtitles.

It's also important to customize these headings via CSS, making the font bigger, bold or in a different color. This way page looks nice and organized.

The following benefits of using heading tags:

<!--endintro-->

* Improves the ranking with the search engines (extra weighting is given to text in H1 and H2)
* Makes cleaner and leaner HTML

``` html
<p><span class="Heading">Introduction</span> 
      
Lets chatter about...</p>
```
::: bad
Figure: Bad example -  Using span tags and CSS classes to insert headings to content
:::

``` html
<h2>Introduction</h2>
```
::: good
Figure: Good example - Using heading tags
:::
