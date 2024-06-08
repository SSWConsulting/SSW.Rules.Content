---
type: rule
archivedreason: 
title: Do you use 'read more' WordPress tag to show summary only on a blog list?
guid: 18e3c2af-0fc0-4e83-9afd-f8a6c1b60e56
uri: do-you-use-read-more-wordpress-tag-to-show-summary-only-on-a-blog-list
created: 2014-06-09T15:12:04.0000000Z
authors:
- title: Tiago Araujo
  url: https://ssw.com.au/people/tiago-araujo
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-use-read-more’-wordpress-tag-to-show-summary-only-on-a-blog-list

---

By default, WordPress shows the whole article content on a post list. Knowing that some posts are quite long - taking a lot of real estate on the page - it's a good idea to summarize it and add a "read more" link. 

<!--endintro-->

You can split your blog entries so that only the first part of certain posts is displayed on the home and archive pages. When you do this, a link will be placed after the intro, pointing the reader to the full post.
To do so, you can either edit the source index.php (or similar) file; or just click the "Read More" tag button in the first row of the visual editor toolbar (or press  **Alt+Shift+T** ):

``` php
replace <?php the_content(); ?> with <?php the_excerpt(); ?>
```
::: bad
Figure: Bad example - changing source PHP files is complicated and require developer skills 
:::

::: good  
![Figure: Good example - click on the "Read More" tag on the post visual editor](readmore-tag.png)  
:::

**Note:** This is out-of-the-box with WordPress. You won't need a plugin.

### Custom Read More Message

To customize the message, simply add a space after  **&lt;!--more** and insert the text you want to show:

``` html
<!--more Read the full post -->
```
**Figure: Custom "read more" link**

### Some WordPress themes do this automatically

Many WordPress themes will have an option to not show the full blog content on the homepage. E.g. in Avada (one of the most popular themes) it has this:

::: good  
![Figure: Many WordPress themes make it easier for you](excerpt.png)  
:::

Always check theme options before going back through posts to add in the Read More tags manually.
