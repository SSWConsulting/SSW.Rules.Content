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


<p>​A product should not close without providing a warning. We use the following message box to warn the user before closing a program:</p>
<br><excerpt class='endintro'></excerpt><br>
​<dl class="goodImage"><dt><img alt="SSW Exchange Reporter - Are you sure you want to exit?" src="../../assets/CloseWarning.gif" /></dt>
<dd>Figure: Good Example - Standard warning before a program exits</dd></dl>
<dl class="code"><dt><pre>        private void OnExit(object sender) 
             { 
                EventHandler handler = ExitRequest; 
                if (handler!= null ) 
                { 
                   handler(sender, EventArgs.Empty);
                   return;
                } 
                string closeTitle = string.Format("Exiting{0}", Application.ProductName);
                string closeMessage = string.Format("Are you sure you want to exit {0}", Application.ProductName);
                DialogResult result = MessageBox.Show(closeMessage,closeTitle, MessageBoxButtons.YesNo,MessageBoxIcon.Warning);
                if (result == DialogResult.Yes)
                { 
                   Application.Exit();
                } 
             }
                        </pre></dt></dl>
<div>We have an example of this in the <a href="http://www.ssw.com.au/ssw/NETToolkit/">SSW .NET Toolkit</a>.</div>



