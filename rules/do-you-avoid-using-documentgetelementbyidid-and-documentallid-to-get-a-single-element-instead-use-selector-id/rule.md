---
type: rule
title: Do you avoid using document.getElementById(id) and document.all(id) to get a single element, instead use selector $(#id)?
uri: do-you-avoid-using-documentgetelementbyidid-and-documentallid-to-get-a-single-element-instead-use-selector-id
created: 2016-11-17T15:17:08.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>$(#id) is a selector of jQuery. It gets the single element with the given id.</p><p><a href="http&#58;//jquery.com/" target="_blank">jQuery</a>&#160;​is a fast and concise JavaScript Library that simplifies how you traverse HTML documents, handle events, perform animations, and add Ajax interactions to your web pages. jQuery is designed to change the way that you write JavaScript.​<br></p> </span>

<p>​With jQuery, you can write less code but do more work.<br></p><p class="ssw15-rteElement-CodeArea">&lt;h1 id=&quot;Head1&quot;&gt;Hello&lt;/h1&gt; &lt;script type=&quot;text/javascript&quot; language=&quot;javascript&quot;&gt;<br><span style="font-size&#58;1rem;">document.all(&quot;Head1&quot;)<br></span><span style="font-size&#58;1rem;">.style.color=&quot;red&quot;; &lt;/script&gt;</span></p><dd class="ssw15-rteElement-FigureBad">
Figure - Bad Code​​​
</dd><p class="ssw15-rteElement-CodeArea">&lt;h1 id=&quot;Head1&quot;&gt;Hello&lt;/h1&gt; &lt;script type=&quot;text/javascript&quot; language=&quot;javascript&quot;&gt;​​<br><span style="font-size&#58;1rem;">document.getElementById(&quot;Head1&quot;)<br></span><span style="font-size&#58;1rem;">.style.color=&quot;red&quot;; &lt;/script&gt;</span></p><dd class="ssw15-rteElement-FigureBad">
Figure&#58; Bad Code​
</dd><p class="ssw15-rteElement-CodeArea">&lt;h1 id=&quot;Head1&quot;&gt;Hello&lt;/h1&gt; &lt;script type=&quot;text/javascript&quot; language=&quot;javascript&quot;&gt;<br><span style="font-size&#58;1rem;">$(&quot;#Head1&quot;)<br></span><span style="font-size&#58;1rem;">.css(&quot;color&quot;,&quot;red&quot;); &lt;/script&gt;</span></p><dd class="ssw15-rteElement-FigureGood">
Figure&#58; Good Code - Using $(&quot;#Head1&quot;)​​​<br></dd>


