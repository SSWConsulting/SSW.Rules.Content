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


<p>When you can't see all the text for an item in a ListView you need to expose the full text via a ToolTip.</p>
<br><excerpt class='endintro'></excerpt><br>
​<dl class="badImage"><dt><img alt="ListView control without Tooltip." src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/ListViewWithoutToolTip.gif" /></dt>
<dd>Figure&#58; Bad Example - Users can't see all the text and the ListView doesn't use a Tooltip</dd></dl>
<dl class="goodImage"><dt><img alt="ListView control with Tooltip." src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/ListViewWithToolTip.gif" /></dt>
<dd>Figure&#58; Good Example - Users can't see all the text, but the ListView shows all the text via a Tooltip</dd></dl>
<div>The code to do this is&#58;</div>
<dl class="code"><dt><pre>            private ListViewItem hoveredItem;
            private void listView1_MouseMove(object sender, MouseEventArgs e)
            &#123; 
               ListView lv = (ListView) sender; 
               ListViewItem item = lv.GetItemAt(e.X, e.Y);
               int columnIndex = 1;
               if (item != hoveredItem)
               &#123; 
                  hoveredItem = item; 
                  if (item == null) 
                  &#123; 
                     toolTip1.SetToolTip(lv, &quot;&quot;); 
                  &#125; 
                  else 
                  &#123; 
                     // Make sure the mouse hovered row has the subitem 
                     if (item.SubItems.Count &gt; columnIndex)
                     &#123; 
                        toolTip1.SetToolTip(lv, item.SubItems[columnIndex].Text);
                     &#125; 
                     else 
                     &#123; 
                        toolTip1.SetToolTip(lv,&quot;&quot;); 
                     &#125; 
                  &#125; 
                &#125; 
             &#125;</pre></dt></dl>



