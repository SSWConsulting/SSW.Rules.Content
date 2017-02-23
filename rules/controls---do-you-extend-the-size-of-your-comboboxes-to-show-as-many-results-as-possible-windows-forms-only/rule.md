---
type: rule
archivedreason: 
title: Controls - Do you extend the size of your ComboBoxes to show as many results as possible? (Windows Forms Only)
guid: c632ba59-8d03-48e9-a02b-aaad31dd875e
uri: controls---do-you-extend-the-size-of-your-comboboxes-to-show-as-many-results-as-possible-windows-forms-only
created: 2012-11-27T09:20:17.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


<p>​​When designing your form, it's a good idea to help your user whenever it's possible. So it's a good idea to extend your ComboBoxes to show as many results as possible to save your user from scrolling. Also, you should extend the width of the dropdown in order to show the longest items.<br></p>
<br><excerpt class='endintro'></excerpt><br>
​
<div>However, you should not extend your ComboBox without limit, normally the maximum number of items should be under 10 and the maximum width of the drop-down should be smaller than your hosting form.</div><dl class="badImage"><dt>
      <img alt="Options Form - ComboBox with text cut off" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/ComboBox-Size-1.jpg" />
   </dt><dd>Figure&#58; Bad Example - You have to scroll to see all the result, and the long results are cut off</dd></dl><dl class="goodImage"><dt>
      <img alt="Options Form - ComboBox with Extended Height and Width" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/ComboBox-Size-2.jpg" />
   </dt><dd>Figure&#58; Good Example - The size of the drop down has been extended to allow user to see as much as possible</dd></dl><div>Changing the maximum items is easy, just include the following code in your form&#58;</div><dl class="code"><dt><p>cbxOUList.MaxDropDownItems = cbxOUList.Items.Count;​<br></p>
   </dt></dl><div>Changing the drop down size is a bit of tricky</div><dl class="code"><dt><p>Graphics g = Graphics.FromHwnd(this.Handle);<br> SizeF stringSize = new SizeF();<br> stringSize = g.MeasureString(longString, cbx.Font, 600);<br> int adjustedSize = cbx.DropDownWidth;<br> if ( adjustedSize&lt;(int)stringSize.Width )<br> &#123;<br> adjustedSize = (int)stringSize.Width;<br> &#125;<br> cbx.DropDownWidth = adjustedSize;​<br></p></dt></dl>


