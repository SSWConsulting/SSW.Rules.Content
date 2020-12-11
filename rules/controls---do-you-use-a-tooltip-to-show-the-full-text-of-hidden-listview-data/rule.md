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

When you can't see all the text for an item in a ListView you need to expose the full text via a ToolTip.

<!--endintro-->
<dl class="badImage">&lt;dt&gt;
      <img alt="ListView control without Tooltip." src="../../assets/ListViewWithoutToolTip.gif">
   &lt;/dt&gt;<dd>Figure: Bad Example - Users can't see all the text and the ListView doesn't use a Tooltip</dd></dl><dl class="goodImage">&lt;dt&gt;
      <img alt="ListView control with Tooltip." src="../../assets/ListViewWithToolTip.gif">
   &lt;/dt&gt;<dd>Figure: Good Example - Users can't see all the text, but the ListView shows all the text via a Tooltip</dd></dl>
The code to do this is:
<dl class="code">&lt;dt&gt;<p>private ListViewItem hoveredItem;<br> private void listView1_MouseMove(object sender, MouseEventArgs e)<br> { <br> ListView lv = (ListView) sender; <br> ListViewItem item = lv.GetItemAt(e.X, e.Y);<br> int columnIndex = 1;<br> if (item != hoveredItem)<br> { <br> hoveredItem = item; <br> if (item == null) <br> { <br> toolTip1.SetToolTip(lv, ""); <br> } <br> else <br> { <br> // Make sure the mouse hovered row has the subitem <br> if (item.SubItems.Count > columnIndex)<br> { <br> toolTip1.SetToolTip(lv, item.SubItems[columnIndex].Text);<br> } <br> else <br> { <br> toolTip1.SetToolTip(lv,""); <br> } <br> } <br> } <br> }<br></p>&lt;/dt&gt;</dl>
