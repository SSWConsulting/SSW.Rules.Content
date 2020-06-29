---
type: rule
title: Do you use 'read more' WordPress tag to show summary only on a blog list?
uri: do-you-use-read-more-wordpress-tag-to-show-summary-only-on-a-blog-list
created: 2014-06-09T15:12:04.0000000Z
authors:
- id: 16
  title: Tiago Araujo
- id: 1
  title: Adam Cogan

---



<span class='intro'> By default, WordPress shows the whole article content on a post list. Knowing that some posts are quite long - taking a lot of real estate on the page - it's a good idea to summarize it and add a &quot;read more&quot; link. <br> </span>

<p>You can split your blog entries so that only the first part of certain posts is displayed on the home and archive pages. When you do this, a link will be placed after the intro, pointing the reader to the full post.</p>To do so, you can either edit the source index.php (or similar) file; or just click the &quot;Read More&quot; tag button in the first row of the visual editor toolbar (or press <strong>Alt+Shift+T</strong>)&#58;<p></p><dl class="badImage"><p class="ssw15-rteElement-CodeArea">replace &lt;?php the_content(); ?&gt; with &lt;?php&#160;the_excerpt();&#160;?&gt;</p><dd>Figure&#58; Bad example - changing source PHP files is complicated and require developer skills </dd></dl><dl class="goodImage"><dt> <img src="readmore-tag.png" alt="" /> </dt><dd>Figure&#58; Good example - click on the &quot;Read More&quot; tag on the post visual editor</dd></dl><p>
   <strong>Note&#58;</strong> This is out-of-the-box with WordPress. You won't need a plugin.</p><h3>Custom Read More Message</h3><p>To customize the message, simply add a space after <strong> &lt;!--more</strong> and insert the text you want to show&#58;</p><dl class="image"><dt><p class="ssw15-rteElement-CodeArea">&lt;!--more Read the full post --&gt; ​<br></p><br></dt><dd>Figure&#58; Custom &quot;read more&quot; link<br></dd></dl><h3>Some WordPress themes do this automatically</h3><p>Many WordPress themes will have an option to not show the full blog content on the homepage. E.g. in Avada (one of the most popular themes) it has this&#58;</p><dl class="goodImage"><dt> <img src="excerpt.png" alt="excerpt.png" /> </dt><dd>Figure&#58; Many WordPress themes make it easier for you</dd></dl><p></p><p>Always check theme options before going back through posts to add in the Read More tags manually.</p>


