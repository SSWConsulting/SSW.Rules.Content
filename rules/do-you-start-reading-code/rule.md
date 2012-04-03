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



<span class='intro'> <i style="line-height&#58;normal;font-family&#58;calibri, sans-serif;font-size&#58;15px;">“Aim for simplicity. I want to code to read like poetry”&#160;</i><span style="line-height&#58;normal;font-family&#58;calibri, sans-serif;font-size&#58;15px;">– Terje Sandstrom&#160;</span>  </span>

<div><strong>Good code&#58;</strong> <ul><li>Is clear and easy to read</li>
<li>Has consistent and meaningful names for everything</li>
<li>Has no repeated or redundant code</li>
<li>Includes comments that explain the&#160;intent (the why rather than the what)</li>
<li>Has consistent styles and formatting</li></ul>
<ul>Tip&#58; Read this book&#160;<a href="http&#58;//www.google.com.hk/url?sa=t&amp;rct=j&amp;q=clean+code+download&amp;source=web&amp;cd=2&amp;ved=0CDgQFjAB&amp;url=http&#58;//www.e-reading.org.ua/bookreader.php/134601/Clean_Code_-_A_Handbook_of_Agile_Software_Craftsmanship.html&amp;ei=2jRoT8yfM_LSiAKK9piWBw&amp;usg=AFQjCNEGQx__eAf7t0yM_dYGtaaxJ6TqJA">Clean Code&#58; A Handbook of Agile Software Craftsmanship</a>&#160;by Robert. C. Martin</ul>
<div><strong>Good code is declarative&#58;</strong></div>
<div>For example, I want to show all the products where the&#160;unit price less than 20, and also&#160;how many&#160;products are in each category.</div>
<div class="ssw-rteStyle-CodeArea"><div>Dictionary&lt;string, Grouping&gt; groups = new Dictionary&lt;string, Grouping&gt;();<br><span style="background-color&#58;rgb(255,255,0);"><span style="background-color&#58;rgb(255,255,0);">foreach</span></span> (Product p in products)<br>&#123;<br>&#160;&#160;&#160; <span style="background-color&#58;rgb(255,255,0);"><span style="background-color&#58;rgb(255,255,0);">if (p.UnitPrice &gt;= 20)</span></span><br>&#160;&#160;&#160; &#123;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;<span style="background-color&#58;rgb(255,255,0);"> if (!groups.ContainsKey(p.CategoryName))</span><br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#123;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; Grouping r = new Grouping();<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; r.CategoryName = p.CategoryName;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; r.ProductCount = 0;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; groups[p.CategoryName] = r;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#125;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; groups[p.CategoryName].ProductCount++;<br>&#160;&#160;&#160; &#125;<br>&#125;</div>
<div>List&lt;Grouping&gt; result = new List&lt;Grouping&gt;(groups.Values);<br>result.Sort(delegate(Grouping x, Grouping y)<br>&#123;<br>&#160;&#160;&#160; return<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; x.ProductCount &gt; y.ProductCount ? -1 &#58;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; x.ProductCount &lt; y.ProductCount ? 1 &#58;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; 0;<br>&#125;);</div></div>
<pre class="ssw-rteStyle-FigureBad"><span style="font-family&#58;verdana, arial, sans-serif;white-space&#58;normal;">Figure&#58;&#160;Bad example -&#160;Not using LINQ.&#160;The <span style="background-color&#58;rgb(255,255,0);">yellow </span>gives it away.</span></pre>
<pre class="ssw-rteStyle-Tip"><font face="verdana, arial, sans-serif"><span style="white-space&#58;normal;">Tip&#58; Resharper can automatically convert this code.</span></font></pre>
<pre><font face="verdana, arial, sans-serif"><span style="white-space&#58;normal;"></span></font></pre>
<div class="ssw-rteStyle-CodeArea"><pre>result = products
    .Where(p =&gt; p.UnitPrice &gt;= 20)
    .GroupBy(p =&gt; p.CategoryName)
    .OrderByDescending(g =&gt; g.Count())
    .Select(g =&gt; <span>n</span><span>ew</span><span> </span>&#123; CategoryName = g.Key, ProductCount = g.Count() &#125;);</pre></div>
<div class="ssw-rteStyle-FigureGood"><b>Figure&#58; Good example - using LINQ</b><strong></strong></div>
<div><b><br></b></div>
<div><strong>Tip&#58; For more information on why&#160;declarative programming&#160;(aka LINQ, SQL, HTML</strong><strong>) is great,&#160;watch the <a href="http&#58;//channel9.msdn.com/blogs/adebruyn/techdays-2010-developer-keynote-by-anders-hejlsberg">TechDays 2010 Keynote by Anders Hejlsberg.</a> Anders explains why it's better to have code &quot;tell&#160;what,&#160;not how&quot;</strong></div>
<p><strong>Clean front-end HTML code</strong></p>
<div>Anyone who creates their own HTML pages today should aim to make their markup semantically correct.(<strong></strong><a href="http&#58;//www.webdesignfromscratch.com/html-css/semantic-html/">http&#58;//www.webdesignfromscratch.com/html-css/semantic-html/</a>)</div>
<div>&lt;p&gt;&#160;is for a paragraph,&#160;not for defining a section;</div>
<div>&lt;b&gt; is for bolding,&#160;not for&#160;emphasizing,&#160;&lt;strong&gt;,&#160;&lt;em&gt; do that.</div>
<div><br></div>
<div><strong>Clean front-end code -&#160;JavaScript</strong></div>
<div><strong>[TODO]</strong></div>
<div><strong>bad example - not using Jquery</strong></div>
<div><strong>good example&#160;</strong><strong>- using Jquery​</strong></div>
<div><strong>[TODO&#58; remove&#160;dash from the URL]​</strong></div></div>
<div><b><br></b></div>
<div>&#160;</div>


