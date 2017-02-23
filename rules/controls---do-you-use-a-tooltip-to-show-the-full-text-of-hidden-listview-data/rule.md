---
type: rule
archivedreason: 
title: Controls - Do you use a ToolTip to show the full text of hidden ListView data?
guid: c025f79b-669a-4be5-8ece-28755c263c01
uri: controls---do-you-use-a-tooltip-to-show-the-full-text-of-hidden-listview-data
created: 2012-11-27T09:14:27.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


<p>​When you can't see all the text for an item in a ListView you need to expose the full text via a ToolTip.<br></p>
<br><excerpt class='endintro'></excerpt><br>
​
<dl class="badImage"><dt>
      <img alt="ListView control without Tooltip." src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/ListViewWithoutToolTip.gif" />
   </dt><dd>Figure&#58; Bad Example - Users can't see all the text and the ListView doesn't use a Tooltip</dd></dl><dl class="goodImage"><dt>
      <img alt="ListView control with Tooltip." src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/ListViewWithToolTip.gif" />
   </dt><dd>Figure&#58; Good Example - Users can't see all the text, but the ListView shows all the text via a Tooltip</dd></dl><div>The code to do this is&#58;</div><dl class="code"><dt><p>private ListViewItem hoveredItem;<br> private void listView1_MouseMove(object sender, MouseEventArgs e)<br> &#123; <br> ListView lv = (ListView) sender; <br> ListViewItem item = lv.GetItemAt(e.X, e.Y);<br> int columnIndex = 1;<br> if (item != hoveredItem)<br> &#123; <br> hoveredItem = item; <br> if (item == null) <br> &#123; <br> toolTip1.SetToolTip(lv, &quot;&quot;); <br> &#125; <br> else <br> &#123; <br> // Make sure the mouse hovered row has the subitem <br> if (item.SubItems.Count &gt; columnIndex)<br> &#123; <br> toolTip1.SetToolTip(lv, item.SubItems[columnIndex].Text);<br> &#125; <br> else <br> &#123; <br> toolTip1.SetToolTip(lv,&quot;&quot;); <br> &#125; <br> &#125; <br> &#125; <br> &#125;​<br></p></dt></dl>


