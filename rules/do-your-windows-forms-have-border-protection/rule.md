---
type: rule
title: Do your Windows Forms have border protection?
uri: do-your-windows-forms-have-border-protection
created: 2014-12-01T01:03:09.0000000Z
authors: []

---



<span class='intro'> <p>Border protection helps us design Windows Forms properly without placing
 controls too near to the border. Maintain a consistent alignment makes 
the Windows Forms look better, especially on designing wizard forms 
where all forms have the same size.</p> </span>

<dl class="goodImage"><dt> 
      <img alt="Designing border protection." src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/BorderProtectionExample.gif" style="margin&#58;5px;width&#58;600px;" /> 
   </dt><dd>Figure&#58; Good Example - Good border protection on a form at run time. The only problem is you would have to imagine these blue lines to get consistency</dd></dl><p> 
   <strong>Border protection in action&#58;</strong></p><dl class="badImage"><dt> 
      <img alt="SSW Link Auditor - UI without border protection." src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/BorderProtectionBad.gif" style="margin&#58;5px;" /> 
   </dt><dd>Figure&#58; Bad Example - Controls placed very near to the border and not aligned correctly</dd></dl><dl class="goodImage"><dt> 
      <img alt="SSW Link Auditor - UI with border protection." src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/BorderProtectionGood.gif" style="margin&#58;5px;" /> 
   </dt><dd>Figure&#58; Good Example - All controls are in the border protection area and aligned correctly</dd></dl><dl class="image"><dt> 
      <img alt="SSW Link Auditor - UI with border protection." src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/BorderProtectionDesign.gif" style="margin&#58;5px;" /> 
   </dt><dd>Figure&#58; Design mode</dd></dl><p>The way to implement border protection (the 2 vertical red lines) is implement it in the base form or base user control, and all other forms and user controls inherit the base class to get consistent border protection lines.</p><dl class="code"><dt><pre>            private void BaseForm_Paint(object sender, PaintEventArgs e)
            &#123;
                // Draw border protection lines 
                if (this.DesignMode) 
                &#123; 
                   Pen pen = new Pen(Color.Red); 
                   e.Graphics.DrawLine(pen,
                            23, 0, 23, this.Height); 
                            e.Graphics.DrawLine(pen, this.Width - 23, 0, this.Width - 23, this.Height); 
                &#125; 
            &#125;
            </pre></dt></dl><table class="clsSSWTable"><tbody><tr><td valign="top"> 
            <strong>Q&#58;</strong></td><td> 
            <strong>Why don't we put a panel on the form and set the form DockPadding property which does a similar thing?</strong></td></tr><tr><td valign="top">A&#58;</td><td><ol><li>Adding more panels docking to a form reduces the performance significantly because of the extra SuspendLayout and ResumeLayout calls.</li><li>In certain cases we might really want a control to stick at the border, if we use DockPadding Property, we can't make any exceptions. And still, these red lines actually just act like a ruler to help us easily see whether the controls are aligned nicely.</li></ol></td></tr></tbody></table>


