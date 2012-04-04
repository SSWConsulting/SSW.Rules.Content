---
type: rule
title: Do you know the common Design Principles? (Part 2 - Example)
uri: do-you-know-the-common-design-principles-part-2---example
created: 2012-04-02T01:45:17.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 24
  title: Adam Stephensen
- id: 23
  title: Damian Brady

---



<span class='intro'> The hot spots identified in your solution often indicate violations of common design principles. </span>

​<img src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/CodeMetrics_3.png" alt="" style="margin&#58;5px;width&#58;600px;" /><div class="ssw-rteStyle-FigureNormal">Figure&#58; Check Address.Save() and Customer.LoadCustomer() looking for SOLID refactor opportunities</div>
<p>The most common problem encountered will be code that violates the Single Responsibility Principle (SRP). Addressing SRP issues will see a reduction in the following 3 metrics&#58;</p>
<ol><li>&quot;Cyclomatic Complexity&quot; which indicates that your methods are complex, then</li>
<li>&quot;High Coupling&quot; indicates that your class/method relies on many other classes, then</li>
<li>&quot;Number of Lines&quot; indicates code structures that are long and unwieldy.</li></ol>
<p>Let's just look at one example.</p>
<p>This code does more than one thing, and therefore breaks the Single Responsibility Principle.</p>
<pre class="ssw-rteStyle-CodeArea">public class PrintServer 
&#123;
    public string CreateJob(PrintJob data) &#123; //...
    &#125;
    public int GetStatus(string jobId) &#123; //...
    &#125;
    public void Print(string jobId, int startPage, int endPage) &#123; //...
    &#125;
    public List GetPrinterList() &#123; //...
    &#125;
    public bool AddPrinter(Printer printer) &#123; //...
    &#125;
    public event EventHandler PrintPreviewPageComputed;
    public event EventHandler PrintPreviewReady;
    // ...
&#125;
</pre>
<div class="ssw-rteStyle-FigureBad">Figure&#58; Bad example - This class does two distinct jobs. It creates print jobs and manages printers.</div>
<pre class="ssw-rteStyle-CodeArea">public class Printers &#123;
    public string CreateJob(PrintJob data) &#123; //...
    &#125;
    public int GetStatus(string jobId) &#123; //...
    &#125;
    public void Print(string jobId, int startPage, int endPage) &#123; //...
    &#125;
&#125;
public class PrinterManager &#123;
    public List GetPrinterList() &#123; //...
    &#125;
    public bool AddPrinter(Printer printer) &#123; //...
    &#125;
&#125;
</pre>
<div class="ssw-rteStyle-FigureGood">Figure&#58; Good Example - Each class has a single responsibility.</div>
<p>Additionally, code that has high coupling violates the Dependency Inversion principle. This makes code difficult to change, but can be resolved by implementing the Inversion of Control <strong>*and*</strong> Dependency Injection patterns.</p>
<p>TODO&#58; Replace example with TailSpin</p>
<p>TODO&#58; Updated Code Metrics diagram after fix</p>


