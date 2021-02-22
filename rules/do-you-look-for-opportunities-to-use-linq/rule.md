---
type: rule
archivedreason: 
title: Do you look for opportunities to use Linq?
guid: 3e87484c-47eb-4c38-9a83-3e530fed7498
uri: do-you-look-for-opportunities-to-use-linq
created: 2012-04-01T09:23:06.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Damian Brady
  url: https://ssw.com.au/people/damian-brady
related: []
redirects: []

---


<p>Linq is a fantastic addition to .Net which lets you write clear and beautiful declarative code. Linq allows you to focus more on the <strong>what</strong> and less on the <strong>how</strong>.</p>
<p>You should look for opportunities to replace your existing code with Linq.</p>
<br><excerpt class='endintro'></excerpt><br>
<p>​For example, replace your foreach loops with Linq.</p><div class="ssw-rteStyle-CodeArea"><pre>var lucrativeCustomers = new List&lt;Customer&gt;();
foreach (var customer in Customers)
&#123;
    if (customer.Orders.Count &gt; 0)
    &#123;
        lucrativeCustomers.Add(customer);
    &#125;
&#125;</pre></div> 
<span class="ssw-rteStyle-FigureBad">Figure&#58; Bad Example - imperative programming using a foreach loop</span> 
<div class="ssw-rteStyle-CodeArea"><pre>var lucrativeCustomers = Customers.Where(c =&gt; c.Orders.Count &gt; 0).ToList();</pre></div> 
<span class="ssw-rteStyle-FigureGood">Figure&#58; Good Example - declarative programming using Linq</span>


