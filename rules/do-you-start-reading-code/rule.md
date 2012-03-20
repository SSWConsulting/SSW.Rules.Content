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



<span class='intro'> <i style="font-family&#58;calibri, sans-serif;font-size&#58;15px;line-height&#58;normal;text-align&#58;-webkit-auto;">“Aim for simplicity. I want to code to read like poetry”&#160;</i><span style="font-family&#58;calibri, sans-serif;font-size&#58;15px;line-height&#58;normal;text-align&#58;-webkit-auto;">– Terje Sandstrom&#160;</span>
 </span>

<strong>​Clean Back-end Code</strong><div> &#160; &#160;-Meaningful names</div>
<div>&#160; &#160; -Functions</div>
<div>&#160; &#160; &#160; &#160; &#160;Prefer exceptions to returning error codes</div>
<div>&#160; &#160; &#160; &#160; &#160;don't repeat yourself</div>
<div>&#160; &#160;-Comments</div>
<div>&#160; &#160;-Fommating</div>
<div>[TODO&#58;reference should be deleted&#160;</div>
<div>&lt;&lt;<a href="http&#58;//www.google.com.hk/url?sa=t&amp;rct=j&amp;q=clean+code+download&amp;source=web&amp;cd=2&amp;ved=0CDgQFjAB&amp;url=http&#58;//www.e-reading.org.ua/bookreader.php/134601/Clean_Code_-_A_Handbook_of_Agile_Software_Craftsmanship.html&amp;ei=2jRoT8yfM_LSiAKK9piWBw&amp;usg=AFQjCNEGQx__eAf7t0yM_dYGtaaxJ6TqJA">Clean Code&#58; A Handbook of Agile Software Craftsmanship</a>&gt;&gt;-Robert.C.Martin&#160;]</div>
<div><br></div>
<div><strong>Clean front-end code -&#160;semantics html</strong></div>
<div><span>Anyone who creates their own HTML pages today should aim to make their markup semantically correct.(</span><strong></strong><a href="http&#58;//www.webdesignfromscratch.com/html-css/semantic-html/">http&#58;//www.webdesignfromscratch.com/html-css/semantic-html/</a>)</div>
<div>&lt;p&gt; is for a paragraph,not for defining a section;&lt;b&gt; is for bolding,not for&#160;emphasizing,&lt;strong&gt;,&lt;em&gt; do that.</div>
<div><strong><br></strong></div>
<div><strong>Domain specific language,declartive programming&#160;- Tell what,not how</strong>[<a href="http&#58;//channel9.msdn.com/blogs/adebruyn/techdays-2010-developer-keynote-by-anders-hejlsberg">TechDays 2010 Keynote by Anders Hejlsberg&#58; Trends and future directions in programming&#160;​languages​</a></div>
<span></span><div>]</div>
<div></div>
<div>e.g.I want to show some products which unit price less than 20,and also &#160;to know how many &#160;products in every&#160;category.</div>
<div>one&#160;way to solve the problem&#58;<span></span><strong>Tell</strong><strong> how without Linq</strong></div>
<div><pre class="code" style="font-size&#58;10pt;border-top-width&#58;1px;border-right-width&#58;1px;border-bottom-width&#58;1px;border-left-width&#58;5px;border-top-style&#58;dashed;border-right-style&#58;dashed;border-bottom-style&#58;dashed;border-left-style&#58;solid;padding-top&#58;8px;padding-right&#58;8px;padding-bottom&#58;8px;padding-left&#58;8px;white-space&#58;pre-wrap;word-wrap&#58;break-word;font-family&#58;consolas, monaco, 'lucida console', 'liberation mono', 'dejavu sans mono', 'bitstream vera sans mono', 'courier new', 宋体;margin-top&#58;10px;margin-bottom&#58;10px;"><span>Dictionary</span>&lt;<span style="color&#58;blue;">string</span>, <span>Grouping</span>&gt; groups = <span style="color&#58;blue;">new </span><span>Dictionary</span>&lt;<span style="color&#58;blue;">string</span>, <span>Grouping</span>&gt;();
<span style="color&#58;blue;">foreach </span>(<span>Product </span>p <span style="color&#58;blue;">in </span>products)
&#123;
    <span style="color&#58;blue;">if </span>(p.UnitPrice &gt;= 20)
    &#123;
        <span style="color&#58;blue;">if </span>(!groups.ContainsKey(p.CategoryName))
        &#123;
            <span>Grouping </span>r = <span style="color&#58;blue;">new </span><span>Grouping</span>();
            r.CategoryName = p.CategoryName;
            r.ProductCount = 0;
            groups[p.CategoryName] = r;
        &#125;
        groups[p.CategoryName].ProductCount++;
    &#125;
&#125;

<span>List</span>&lt;<span>Grouping</span>&gt; result = <span style="color&#58;blue;">new </span><span>List</span>&lt;<span>Groupi</span><span>ng</span>&gt;(groups.Values);
result.Sort(<span style="color&#58;blue;">delegate</span>(<span>Grouping </span>x, <span>Grouping </span>y)
&#123;
    <span style="color&#58;blue;">return
      </span><span style="color&#58;blue;">  </span>x.ProductCount &gt; y.ProductCount ? -1 &#58;
        x.ProductCount &lt; y.ProductCount ? 1 &#58;
        0;
&#125;);</pre>
<font face="consolas, monaco, 'lucida console', 'liberation mono', 'dejavu sans mono', 'bitstream vera sans mono', 'courier new', 宋体" size="2"><span style="white-space&#58;pre-wrap;"></span></font></div>
<pre>Tell what with Linq(If I read the code,i can understand the programmer's purpose quickly)</pre>
<div><pre class="code" style="font-size&#58;10pt;border-top-width&#58;1px;border-right-width&#58;1px;border-bottom-width&#58;1px;border-left-width&#58;5px;border-top-style&#58;dashed;border-right-style&#58;dashed;border-bottom-style&#58;dashed;border-left-style&#58;solid;padding-top&#58;8px;padding-right&#58;8px;padding-bottom&#58;8px;padding-left&#58;8px;white-space&#58;pre-wrap;word-wrap&#58;break-word;font-family&#58;consolas, monaco, 'lucida console', 'liberation mono', 'dejavu sans mono', 'bitstream vera sans mono', 'courier new', 宋体;margin-top&#58;10px;margin-bottom&#58;10px;"><span style="color&#58;blue;"> </span>result = products
    .Where(p =&gt; p.UnitPrice &gt;= 20)
    .GroupBy(p =&gt; p.CategoryName)
    .OrderByDescending(g =&gt; g.Count())
    .Select(g =&gt; <span style="color&#58;blue;">n</span><span style="color&#58;blue;">ew </span>&#123; CategoryName = g.Key, ProductCount = g.Count() &#125;);</pre></div>

<div><strong>Question&#58;</strong><strong>s</strong><strong>hould we force to use Linq???</strong></div>
<div><b><br></b></div>


