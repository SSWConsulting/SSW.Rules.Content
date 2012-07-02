---
type: rule
title: HTML/CSS - Do you know how to create spaces in a web page?
uri: htmlcss---do-you-know-how-to-create-spaces-in-a-web-page
created: 2012-07-02T14:19:41.0000000Z
authors:
- id: 16
  title: Tiago Araujo

---



<span class='intro'> <p>There are many scenarios where you need some extra space in a web page. No matter which one you are at, CSS is the answer.- </p> </span>

<p>Sometimes the first thing that comes to the developer mind is to use the &quot;break line&quot; tag or the <a href="http&#58;//en.wikipedia.org/wiki/ASCII">ASCII character code</a> for &quot;space&quot; to create these extra spaces. It's wrong. CSS is the way to go. You can use both &quot;margin&quot; or &quot;padding&quot; CSS properties to get the result you want.

</p>
<div class="ms-rteCustom-GreyBox">
&lt;ul&gt;<br>
&lt;li&gt;&amp;#160;&amp;#160;&amp;#160;List item&lt;/li&gt;<br>
&lt;/ul&gt;<br>
</div>
<span class="ms-rteCustom-FigureBad">Figure&#58; Bad Example - Using the &quot;space&quot; ASCII character to create a padding on that list</span>

<div class="ms-rteCustom-GreyBox">
&lt;ul&gt;<br>
&lt;li&gt;List item&lt;/li&gt;<br>
&lt;/ul&gt;<br>
&lt;br /&gt;<br>
&lt;br /&gt;<br>
&lt;br /&gt;
</div>
<span class="ms-rteCustom-FigureBad">Figure&#58; Bad Example - Using the &lt;br /ul&gt; tag to create a space at the bottom of that list</span>

<div class="ms-rteCustom-GreyBox">
ul &#123;margin-bottom&#58;15px;&#125;<br>
</div>
<span class="ms-rteCustom-FigureGood">Figure&#58; Good Example - Using CSS to create the padding on each list item and the margin at the bottom</span>

<p><strong>Tip&#58;</strong> You might be not familiar with editing a CSS file. In this case, contact a designer. He/She will be more than happy to help you.</p>


