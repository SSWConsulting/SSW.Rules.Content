---
type: rule
title: Do you start reading code?
uri: do-you-start-reading-code
created: 2012-03-20T03:46:01.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 24
  title: Adam Stephensen
- id: 23
  title: Damian Brady

---



<span class='intro'> <p><span style="line-height&#58;normal;font-family&#58;calibri, sans-serif;font-size&#58;15px;"><em>“Aim for simplicity. I want to code to read like poetry”&#160;- </em><font face="Calibri">Terje Sandstrom</font></span></p> </span>

<div><strong>Good code&#58;</strong></div>
<ul><li>Is clear and easy to read</li>
<li>Has consistent and meaningful names for everything</li>
<li>Has no repeated or redundant code</li>
<li>Includes comments that explain the&#160;intent (the why rather than the what)</li>
<li>Has consistent styles and formatting</li>
<li>Explains &quot;why&quot; when you read down, and &quot;how&quot; when you read left to right</li></ul>
<ul><strong>Tip&#58; </strong>Read the book <a href="http&#58;//www.google.com.hk/url?sa=t&amp;rct=j&amp;q=clean+code+download&amp;source=web&amp;cd=2&amp;ved=0CDgQFjAB&amp;url=http&#58;//www.e-reading.org.ua/bookreader.php/134601/Clean_Code_-_A_Handbook_of_Agile_Software_Craftsmanship.html&amp;ei=2jRoT8yfM_LSiAKK9piWBw&amp;usg=AFQjCNEGQx__eAf7t0yM_dYGtaaxJ6TqJA"><font color="#3a66cc">Clean Code&#58; A Handbook of Agile Software Craftsmanship</font></a> by Robert. C. Martin</ul>
<div><strong>Good code is declarative&#58;</strong></div>
<div>For example, I want to show all the products where the&#160;unit price less than 20, and also&#160;how many&#160;products are in each category.</div>
<div><div class="ssw-rteStyle-CodeArea"><div>Dictionary&lt;string, Grouping&gt; groups = new Dictionary&lt;string, Grouping&gt;();<br><span style="background-color&#58;rgb(255,255,0);"><span style="background-color&#58;rgb(255,255,0);">foreach</span></span> (Product p in products)<br>&#123;<br>&#160;&#160;&#160; <span style="background-color&#58;rgb(255,255,0);"><span style="background-color&#58;rgb(255,255,0);">if (p.UnitPrice &gt;= 20)</span></span><br>&#160;&#160;&#160; &#123;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;<span style="background-color&#58;rgb(255,255,0);"> if (!groups.ContainsKey(p.CategoryName))</span><br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#123;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; Grouping r = new Grouping();<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; r.CategoryName = p.CategoryName;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; r.ProductCount = 0;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; groups[p.CategoryName] = r;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#125;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; groups[p.CategoryName].ProductCount++;<br>&#160;&#160;&#160; &#125;<br>&#125;</div>
<div>List&lt;Grouping&gt; result = new List&lt;Grouping&gt;(groups.Values);<br>result.Sort(delegate(Grouping x, Grouping y)<br>&#123;<br>&#160;&#160;&#160; return<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; x.ProductCount &gt; y.ProductCount ? -1 &#58;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; x.ProductCount &lt; y.ProductCount ? 1 &#58;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; 0;<br>&#125;);</div></div></div>
<pre class="ssw-rteStyle-FigureBad"><span style="font-family&#58;verdana, arial, sans-serif;white-space&#58;normal;">Figure&#58;&#160;Bad example -&#160;Not using LINQ.&#160;The <span style="background-color&#58;rgb(255,255,0);">yellow </span>gives it away.</span></pre>
<p><strong>Tip&#58;</strong> Resharper can automatically convert this code.</p>
<pre><font face="verdana, arial, sans-serif"><span style="white-space&#58;normal;"></span></font></pre>
<div><div class="ssw-rteStyle-CodeArea"><pre>result = products
    .Where(p =&gt; p.UnitPrice &gt;= 20)
    .GroupBy(p =&gt; p.CategoryName)
    .OrderByDescending(g =&gt; g.Count())
    .Select(g =&gt; <span>n</span><span>ew</span><span> </span>&#123; CategoryName = g.Key, ProductCount = g.Count() &#125;);</pre></div></div>
<div class="ssw-rteStyle-FigureGood"><b>Figure&#58; Good example - using LINQ</b><strong></strong></div>
<div><b><br></b></div>
<div><strong>Tip&#58; </strong>For more information on why&#160;declarative programming&#160;(aka LINQ, SQL, HTML) is great,&#160;watch the <a href="http&#58;//channel9.msdn.com/blogs/adebruyn/techdays-2010-developer-keynote-by-anders-hejlsberg">TechDays 2010 Keynote by Anders Hejlsberg.</a> Anders explains why it's better to have code &quot;tell&#160;what,&#160;not how&quot;.</div>
<p><strong>Clean front-end code - HTML (? designers)</strong></p>
<div>Anyone who creates their own HTML pages today should aim to make their markup semantically correct. For more information on semantic markup, see <a href="http&#58;//www.webdesignfromscratch.com/html-css/semantic-html/">http&#58;//www.webdesignfromscratch.com/html-css/semantic-html/</a>.</div>
<div>For example&#58;</div>
<ul><li>&lt;p&gt;&#160;is for a paragraph,&#160;not for defining a section.</li>
<li>&lt;b&gt; is for bolding,&#160;not for&#160;emphasizing&#160;(&lt;strong&gt; and&#160;&lt;em&gt;) do that.</li>
<strong></strong></ul>
<ul><strong>Clean front-end code -&#160;JavaScript</strong></ul>
<div>Clean code and consistent coding standards is not just for server-side code.&#160; It is important that you apply your coding standards to your client-side JavaScript code as well.</div>
<div>You should use a framework like jQuery to make development easier.&#160; jQuery also&#160;contributes to clean and consistent code as you don't need to explicitly code for different browsers and standards.</div>
<div><strong></strong>&#160;</div>
<div class="ssw-rteStyle-CodeArea"><pre>var ajax;</pre>
<pre>if (window.XMLHttpRequest) &#123;
    ajax=new XMLHttpRequest()
&#125; else &#123;
    ajax=new ActiveXObject(&quot;Microsoft.XMLHTTP&quot;);
&#125;
ajax.onreadystatechange = function() &#123;
    // handle response
&#125;</pre>
<pre>ajax.open(&quot;GET&quot;, uri, true); </pre></div>
<div class="ssw-rteStyle-FigureBad"><strong>Figure&#58; Bad Example - This code doesn't use jQuery</strong></div>
<div><strong></strong>&#160;</div>
<div><strong></strong><div class="ssw-rteStyle-CodeArea"><pre>$.ajax(&#123;</pre>
<pre>    type&#58; &quot;GET&quot;,</pre>
<pre>    url&#58; uri</pre>
<pre>&#125;).done(function (html) &#123;</pre>
<pre>    $('results').append(html);</pre>
<pre>&#125;);</pre></div>
</div>
<div class="ssw-rteStyle-FigureGood"><strong>Figure&#58; Good Example&#160;</strong><strong>- using jQuery​, the code is much cleaner and easier to read</strong></div>


