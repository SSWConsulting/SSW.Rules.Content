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



<span class='intro'> <i style="font-size&#58;15px;font-family&#58;calibri, sans-serif;line-height&#58;normal;">“Aim for simplicity. I want to code to read like poetry”&#160;</i><span style="font-size&#58;15px;font-family&#58;calibri, sans-serif;line-height&#58;normal;">– Terje Sandstrom&#160;</span>  </span>

<strong>[Use&#160;ssw red&#160;heading and heading 2??]​</strong><div><strong>Good code has&#58;</strong><div>&#160; &#160;-Meaningful names</div>
<div>&#160; &#160;-Functions&#58;Prefer exceptions &#160;to returning error codes</div>
<div>&#160; &#160;-Functions&#58;Don't repeat yourself</div>
<div>&#160; -Comments should explain the&#160;intent</div>
<div>&#160;&#160;-Formatting</div>
<div class="ssw-rteStyle-Tip">Tip&#58;Read this book&#160;&lt;&lt;<a href="http&#58;//www.google.com.hk/url?sa=t&amp;rct=j&amp;q=clean+code+download&amp;source=web&amp;cd=2&amp;ved=0CDgQFjAB&amp;url=http&#58;//www.e-reading.org.ua/bookreader.php/134601/Clean_Code_-_A_Handbook_of_Agile_Software_Craftsmanship.html&amp;ei=2jRoT8yfM_LSiAKK9piWBw&amp;usg=AFQjCNEGQx__eAf7t0yM_dYGtaaxJ6TqJA">Clean Code&#58; A Handbook of Agile Software Craftsmanship</a>&gt;&gt;-Robert.C.Martin&#160;</div>
<div><strong><br></strong></div>
<div><strong>Good code is&#160;</strong><span></span><strong>declartive&#58;&#160;</strong></div>
<div><strong></strong><strong>e.g.</strong>I want to show some products where the&#160;unit price less than 20, and also&#160;to know how many&#160;products in&#160;every&#160;category.</div>
<div class="ssw-rteStyle-CodeArea"><font size="2" face="consolas, monaco, 'lucida console', 'liberation mono', 'dejavu sans mono', 'bitstream vera sans mono', 'courier new', 宋体"><span style="white-space&#58;pre-wrap;"><div>Dictionary&lt;string, Grouping&gt; groups = new Dictionary&lt;string, Grouping&gt;();<br><span style="background-color&#58;rgb(255, 255, 0);"><span style="background-color&#58;rgb(255, 255, 0);">foreach</span></span> (Product p in products)<br>&#123;<br>&#160;&#160;&#160; <span style="background-color&#58;rgb(255, 255, 0);"><span style="background-color&#58;rgb(255, 255, 0);">if (p.UnitPrice &gt;= 20)</span></span><br>&#160;&#160;&#160; &#123;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;<span style="background-color&#58;rgb(255, 255, 0);"> if (!groups.ContainsKey(p.CategoryName))</span><br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#123;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; Grouping r = new Grouping();<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; r.CategoryName = p.CategoryName;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; r.ProductCount = 0;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; groups[p.CategoryName] = r;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#125;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; groups[p.CategoryName].ProductCount++;<br>&#160;&#160;&#160; &#125;<br>&#125;</div>
<div>List&lt;Grouping&gt; result = new List&lt;Grouping&gt;(groups.Values);<br>result.Sort(delegate(Grouping x, Grouping y)<br>&#123;<br>&#160;&#160;&#160; return<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; x.ProductCount &gt; y.ProductCount ? -1 &#58;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; x.ProductCount &lt; y.ProductCount ? 1 &#58;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; 0;<br>&#125;);</div></span></font></div>
<pre class="ssw-rteStyle-FigureNormal"><span style="font-family&#58;verdana, arial, sans-serif;white-space&#58;normal;">Figure&#58;&#160;Bad example -&#160;Not using LINQ.&#160;The <span style="background-color&#58;rgb(255, 255, 0);">yellow </span>gives it away.</span></pre>
<pre class="ssw-rteStyle-Tip"><font face="verdana, arial, sans-serif"><span style="white-space&#58;normal;">Tip&#58; Resharper on&#160;foreach can automatically convert the code.</span></font></pre>
<pre><font face="verdana, arial, sans-serif"><span style="white-space&#58;normal;">&#160;</span></font></pre>
<div class="ssw-rteStyle-CodeArea"><pre><span> </span>result = products
    .Where(p =&gt; p.UnitPrice &gt;= 20)
    .GroupBy(p =&gt; p.CategoryName)
    .OrderByDescending(g =&gt; g.Count())
    .Select(g =&gt; <span>n</span><span>ew</span><span> </span>&#123; CategoryName = g.Key, ProductCount = g.Count() &#125;);</pre></div>
<div><b>Figure&#58; Good example - using LINQ</b><strong></strong></div>
<div><b><br></b></div>
<div><strong>More information on why&#160;declartive programming&#160;(aka LINQ, SQL, HTML</strong><strong>) is great. Anders explains why having your code “t</strong><strong>ell&#160;what,&#160;not how</strong><strong>“&#160;</strong>[<a href="http&#58;//channel9.msdn.com/blogs/adebruyn/techdays-2010-developer-keynote-by-anders-hejlsberg">TechD</a><span>ays 2010 Keynote by Anders Hejlsberg&#58; Trends and future directions in programming&#160;​languages​</span>]
<b></b></div>
<div><br></div>
<div><div><strong>Clean front-end code -&#160;html</strong></div>
<div>Anyone who creates their own HTML pages today should aim to make their markup semantically correct.(<strong></strong><a href="http&#58;//www.webdesignfromscratch.com/html-css/semantic-html/">http&#58;//www.webdesignfromscratch.com/html-css/semantic-html/</a>)</div>
<div>&lt;p&gt;<span></span>&#160;is for a paragraph,&#160;not for defining a section;</div>
<div>&lt;b&gt; is for bolding,&#160;not for&#160;emphasizing,&#160;&lt;strong&gt;,&#160;&lt;em&gt; do that.</div>
<div><br></div>
<div><span></span><span></span><strong>Clean front-end code -&#160;JavaScript</strong></div>
<div><strong>[TODO]</strong></div>
<div><strong>bad example - not using Jquery</strong></div>
<div><strong>good example&#160;</strong><strong>- using Jquery​</strong></div>
<div><strong>[TODO&#58; remove&#160;dash from the URL]​</strong></div></div>
<div><b><br></b></div></div>


