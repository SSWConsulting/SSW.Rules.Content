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



<span class='intro'> <p class="greyBox"><em>“Aim for simplicity. I want to code to read like poetry”</em><br>
- Terje Sandstrom</p> </span>

<h3 class="ssw15-rteElement-H3">Good code​​<br></h3>
<ul>
<li>Is clear and easy to read</li>
<li>Has consistent and meaningful names for everything</li>
<li>Has no repeated or redundant code</li>
<li>Has neat formatting</li>
<li>Explains &quot;why&quot; when you read down, and &quot;how&quot; when you read left to right</li></ul>

<span class="ssw-rteStyle-CodeArea">public IEnumerable&lt;Customer&gt; GetSupplierCustomersWithMoreThanZeroOrders(int supplierId)<br>&#123;<br>&#160;&#160;&#160; var supplier = _repository.Suppliers.Single(s =&gt; s.Id == supplierId);<br><br>&#160;&#160;&#160; if (supplier == null)<br>&#160;&#160;&#160; &#123;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;return&#160;Enumerable.Empty&lt;Customer&gt;();<br>&#160;&#160;&#160; &#125;<br>&#160;&#160;&#160;&#160;var customers = supplier.Customers<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; .Where(c =&gt; c.Orders &gt; 0);<br><br>&#160;&#160;&#160; return customers;<br>&#125;</span><span class="ssw-rteStyle-FigureNormal">Figure&#58; This code explains what it is doing as you read left to right, and why it is doing it when you read top to bottom.</span>
<p><strong>Tip&#58; </strong>Read the book <a href="http&#58;//www.google.com.hk/url?sa=t&amp;rct=j&amp;q=clean+code+download&amp;source=web&amp;cd=2&amp;ved=0CDgQFjAB&amp;url=http&#58;//www.e-reading.org.ua/bookreader.php/134601/Clean_Code_-_A_Handbook_of_Agile_Software_Craftsmanship.html&amp;ei=2jRoT8yfM_LSiAKK9piWBw&amp;usg=AFQjCNEGQx__eAf7t0yM_dYGtaaxJ6TqJA">Clean Code&#58; A Handbook of Agile Software Craftsmanship</a> by Robert. C. Martin.</p>
<h3 class="ssw15-rteElement-H3">Good code is declarative​​<br></h3>
<p>For example, I want to show all the products where the&#160;unit price less than 20, and also&#160;how many&#160;products are in each category.</p>
<div class="ssw-rteStyle-CodeArea">Dictionary&lt;string, ProductGroup&gt; groups = new Dictionary&lt;string, ProductGroup&gt;();<br><span style="background-color&#58;#ffff00;"><span style="background-color&#58;#ffff00;">foreach</span></span> (var product in products)<br>&#123;<br>&#160;&#160;&#160; <span style="background-color&#58;#ffff00;"><span style="background-color&#58;#ffff00;">if (product.UnitPrice &gt;= 20)</span></span><br>&#160;&#160;&#160; &#123;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;<span style="background-color&#58;#ffff00;"> if (!groups.ContainsKey(product.CategoryName))</span><br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#123;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; ProductGroup productGroup = new ProductGroup();<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; productGroup.CategoryName = product.CategoryName;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; productGroup.ProductCount = 0;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; groups[product.CategoryName] = productgroup;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#125;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; groups[p.CategoryName].ProductCount++;<br>&#160;&#160;&#160; &#125;<br>&#125;var&#160;result = new List&lt;ProductGroup&gt;(groups.Values);<br>result.Sort(delegate(ProductGroup groupX, ProductGroup groupY)<br>&#123;<br>&#160;&#160;&#160; return<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; groupX.ProductCount &gt; groupY.ProductCount ? -1 &#58;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; groupX.ProductCount &lt; groupY.ProductCount ? 1 &#58;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; 0;<br>&#125;);</div>
<span class="ssw-rteStyle-FigureBad">Figure&#58;&#160;Bad example -&#160;Not using LINQ.&#160;The <span style="background-color&#58;#ffff00;">yellow</span> gives it away.</span>
<p><strong>Tip&#58;</strong> Resharper can automatically convert this code.</p>
<div class="ssw-rteStyle-CodeArea"><pre>result = products
    .Where(product =&gt; product.UnitPrice &gt;= 20)
    .GroupBy(product =&gt; product.CategoryName)
    .OrderByDescending(group =&gt; group.Count())
    .Select(group =&gt; <span>n</span><span>ew</span><span> </span>&#123; CategoryName = group.Key, ProductCount = group.Count() &#125;);</pre></div>
<span class="ssw-rteStyle-FigureGood">Figure&#58; Good example - using LINQ</span>

<p><strong>Tip&#58; </strong>For more information on why&#160;declarative programming&#160;(aka LINQ, SQL, HTML) is great,&#160;watch the <a href="http&#58;//channel9.msdn.com/blogs/adebruyn/techdays-2010-developer-keynote-by-anders-hejlsberg"></a>TechDays 2010 Keynote by Anders Hejlsberg.Anders explains why it's better to have code &quot;tell&#160;what,&#160;not how&quot;.</p>
<h3 class="ssw15-rteElement-H3">Clean front-end code - HTML (This one is questionable as HTML is generally a designer issue)​​<br></h3>
<p>Anyone who creates their own HTML pages today should aim to make their markup semantically correct. For more information on semantic markup, see <a href="http&#58;//www.webdesignfromscratch.com/html-css/semantic-html/">http&#58;//www.webdesignfromscratch.com/html-css/semantic-html/</a>.</p>
<p>For example&#58;</p>
<ul><li>&lt;p&gt;&#160;is for a paragraph,&#160;not for defining a section.</li>
<li>&lt;b&gt; is for bolding,&#160;not for&#160;emphasizing&#160;(&lt;strong&gt; and&#160;&lt;em&gt;) do that.</li>
</ul>
<h3 class="ssw15-rteElement-H3">Clean Front-End code​<br></h3>
<p></p><p>Clean code and consistent coding standards are not just for server-side code.&#160; It is important that you apply your coding standards to your front-end code as well e.g. JavaScript, TypeScript, React, Angular, Vue, CSS, etc.</p><p>You should use a linter and code formatter like Prettier to make development easier and more consistent.<br></p>



