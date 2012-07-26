---
type: rule
title: Do You Place Scripts at the Bottom of Your Page?
uri: do-you-place-scripts-at-the-bottom-of-your-page
created: 2012-07-24T18:10:46.0000000Z
authors:
- id: 16
  title: Tiago Araujo

---



<span class='intro'> Bear in mind that the load time is a very important aspect on web development.
The goal is to make the page load as quickly as possible for the user.  </span>

<p>It's known that when a browser loads a script, it can’t continue on until the entire file has been loaded.</p>
<p>Once JavaScript files have the purpose to add functionality — something happen after a button is clicked for example — there is no good reason to load the JS file before the button itself.</p>
<p>So go ahead and place JS files at the bottom of the HTML, just before the closing body tag.</p>

<div class="ms-rteCustom-CodeArea">
<p>&lt;script type=&quot;text/javascript&quot; src=&quot;file.js&quot;&gt;&lt;/script&gt; <br> 
&lt;/body&gt; <br>
&lt;/html&gt;
</p>
</div>
<span class="ms-rteCustom-FigureGood">Figure&#58; Place JavaScript at the bottom of your HTML</span>

<p>Tests at a big online sales company revealed that every 100 ms increase in load time decreased sales by 1%.</p>



