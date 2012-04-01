---
type: rule
archivedreason: 
title: Do you start reading code?
guid: 86eae955-ca88-429d-abde-70cc608f6ada
uri: do-you-start-reading-code
created: 2012-03-20T03:46:01.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Adam Stephensen
  url: https://ssw.com.au/people/adam-stephensen
- title: Damian Brady
  url: https://ssw.com.au/people/damian-brady
related: []
redirects: []

---


<i style="font-size&#58;15px;font-family&#58;calibri, sans-serif;line-height&#58;normal;">“Aim for simplicity. I want to code to read like poetry”&#160;</i><span style="font-size&#58;15px;font-family&#58;calibri, sans-serif;line-height&#58;normal;">– Terje Sandstrom&#160;</span> 
<br><excerpt class='endintro'></excerpt><br>
<strong>​Clean Back-end Code</strong> <div>&#160; &#160;-Meaningful names</div>
<div>&#160; &#160; -Functions</div>
<div>&#160; &#160; &#160; &#160; &#160;Prefer exceptions to returning error codes</div>
<div>&#160; &#160; &#160; &#160; &#160;don't repeat yourself</div>
<div>&#160; &#160;-Comments</div>
<div>&#160; &#160;-Fommating</div>
<div>[TODO&#58;reference should be deleted&#160;</div>
<div>{ltHTMLChar}{ltHTMLChar}<a href="http&#58;//www.google.com.hk/url?sa=t&amp;rct=j&amp;q=clean+code+download&amp;source=web&amp;cd=2&amp;ved=0CDgQFjAB&amp;url=http&#58;//www.e-reading.org.ua/bookreader.php/134601/Clean_Code_-_A_Handbook_of_Agile_Software_Craftsmanship.html&amp;ei=2jRoT8yfM_LSiAKK9piWBw&amp;usg=AFQjCNEGQx__eAf7t0yM_dYGtaaxJ6TqJA">Clean Code&#58; A Handbook of Agile Software Craftsmanship</a>{gtHTMLChar}{gtHTMLChar}-Robert.C.Martin&#160;]</div>
<div><br></div>
<div><strong>Clean front-end code -&#160;semantics html</strong></div>
<div><span>Anyone who creates their own HTML pages today should aim to make their markup semantically correct.(</span><strong></strong><a href="http&#58;//www.webdesignfromscratch.com/html-css/semantic-html/">http&#58;//www.webdesignfromscratch.com/html-css/semantic-html/</a>)</div>
<div>{ltHTMLChar}p{gtHTMLChar} is for a paragraph,not for defining a section;{ltHTMLChar}b{gtHTMLChar} is for bolding,not for&#160;emphasizing,{ltHTMLChar}strong{gtHTMLChar},{ltHTMLChar}em{gtHTMLChar} do that.</div>
<div><strong><br></strong></div>
<div><span></span><strong>declartive programming(</strong><strong>Question&#58;</strong><strong>s</strong><strong>hould we force to use Linq???)</strong><strong>&#160;- Tell what,not how</strong>[<a href="http&#58;//channel9.msdn.com/blogs/adebruyn/techdays-2010-developer-keynote-by-anders-hejlsberg">TechDays 2010 Keynote by Anders Hejlsberg&#58; Trends and future directions in programming&#160;​languages​</a></div>
<span></span><div>]</div>
<div></div>
<div><strong>e.g.</strong>I want to show some products which unit price less than 20,and also &#160;to know how many &#160;products in every&#160;category.</div>
<div>one&#160;way to solve the problem&#58;<span></span><strong>Tell</strong><strong> how without Linq</strong></div>
<div class="ssw-rteStyle-CodeArea"><font size="2" face="consolas, monaco, 'lucida console', 'liberation mono', 'dejavu sans mono', 'bitstream vera sans mono', 'courier new', 宋体"><span style="white-space&#58;pre-wrap;"><div>Dictionary{ltHTMLChar}string, Grouping{gtHTMLChar} groups = new Dictionary{ltHTMLChar}string, Grouping{gtHTMLChar}();<br>foreach (Product p in products)<br>&#123;<br>&#160;&#160;&#160; if (p.UnitPrice {gtHTMLChar}= 20)<br>&#160;&#160;&#160; &#123;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; if (!groups.ContainsKey(p.CategoryName))<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#123;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; Grouping r = new Grouping();<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; r.CategoryName = p.CategoryName;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; r.ProductCount = 0;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; groups[p.CategoryName] = r;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#125;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; groups[p.CategoryName].ProductCount++;<br>&#160;&#160;&#160; &#125;<br>&#125;</div>
<div>List{ltHTMLChar}Grouping{gtHTMLChar} result = new List{ltHTMLChar}Grouping{gtHTMLChar}(groups.Values);<br>result.Sort(delegate(Grouping x, Grouping y)<br>&#123;<br>&#160;&#160;&#160; return<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; x.ProductCount {gtHTMLChar} y.ProductCount ? -1 &#58;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; x.ProductCount {ltHTMLChar} y.ProductCount ? 1 &#58;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; 0;<br>&#125;);</div>
</span></font></div>
<pre><span style="font-family&#58;verdana, arial, sans-serif;white-space&#58;normal;">the other way&#160;to so</span><span style="font-family&#58;verdana, arial, sans-serif;white-space&#58;normal;">lv</span><span style="font-family&#58;verdana, arial, sans-serif;white-space&#58;normal;">e the problem&#58;<b>Tell what with Linq(I can understand the developer's intenstion quickly)</b></span>
</pre>
<div class="ssw-rteStyle-CodeArea"><pre><span> </span>result = products
    .Where(p ={gtHTMLChar} p.UnitPrice {gtHTMLChar}= 20)
    .GroupBy(p ={gtHTMLChar} p.CategoryName)
    .OrderByDescending(g ={gtHTMLChar} g.Count())
    .Select(g ={gtHTMLChar} <span>n</span><span>ew </span>&#123; CategoryName = g.Key, ProductCount = g.Count() &#125;);</pre></div>
<div><b><br></b><strong></strong></div>
<div><b><br></b></div>


