---
type: rule
archivedreason: 
title: Do you provide a warning before the program exits?
guid: 46cc1b38-8001-481a-b8ca-98ea6dc45398
uri: do-you-provide-a-warning-before-the-program-exits
created: 2012-11-27T03:10:56.0000000Z
authors: []
related: []

---


<p>​A product should not close without providing a warning. We use the following message box to warn the user before closing a program&#58;</p>
<br><excerpt class='endintro'></excerpt><br>
​<dl class="goodImage"><dt><img alt="SSW Exchange Reporter - Are you sure you want to exit?" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/CloseWarning.gif" /></dt>
<dd>Figure&#58; Good Example - Standard warning before a program exits</dd></dl>
<dl class="code"><dt><pre>        private void OnExit(object sender) 
             &#123; 
                EventHandler handler = ExitRequest; 
                if (handler!= null ) 
                &#123; 
                   handler(sender, EventArgs.Empty);
                   return;
                &#125; 
                string closeTitle = string.Format(&quot;Exiting&#123;0&#125;&quot;, Application.ProductName);
                string closeMessage = string.Format(&quot;Are you sure you want to exit &#123;0&#125;&quot;, Application.ProductName);
                DialogResult result = MessageBox.Show(closeMessage,closeTitle, MessageBoxButtons.YesNo,MessageBoxIcon.Warning);
                if (result == DialogResult.Yes)
                &#123; 
                   Application.Exit();
                &#125; 
             &#125;
                        </pre></dt></dl>
<div>We have an example of this in the <a href="http&#58;//www.ssw.com.au/ssw/NETToolkit/">SSW .NET Toolkit</a>.</div>



