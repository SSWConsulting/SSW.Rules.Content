---
type: rule
title: Do you know not to use LinkButton?
uri: do-you-know-not-to-use-linkbutton
created: 2016-09-01T17:57:47.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> If we want to refresh and data bind the same page from client side, we can use the javascript function calls &quot;__doPostBack&quot;. We shouldn't fire this post back in LinkButton. Otherwise, there will be an error.<br> </span>

<dl class="image"><dt><img src="/PublishingImages/RightClickLink.gif" alt="RightClickLink.gif" /></dt><dd>Figure&#58; Right click the link with __doPostBack event&#160; ​
</dd></dl><dl class="image"><dt><img src="/PublishingImages/PostBack.gif" alt="PostBack.gif" /></dt><dd>Figure&#58; New window with incorrect URL</dd></dl>

   <p class="ssw15-rteElement-CodeArea">ASPX&#58;<br>&lt;asp&#58;Panel runat=&quot;server&quot; ID=&quot;mUpdatePanel&quot; OnLoad=&quot;mUpdatePanel_Load&quot;&gt;<br> &lt;asp&#58;Label runat=&quot;server&quot; ID=&quot;lblTime&quot; /&gt;<br> &lt;br /&gt;<br> &lt;asp&#58;GridView ID=&quot;gvList&quot; runat=&quot;server&quot; AutoGenerateColumns=&quot;false&quot;&gt;<br> &lt;Columns&gt;<br> &lt;asp&#58;BoundField DataField=&quot;ID&quot; HeaderText=&quot;ID&quot; /&gt;<br> &lt;/Columns&gt;<br> &lt;Columns&gt;<br> &lt;asp&#58;BoundField DataField=&quot;Name&quot; HeaderText=&quot;Name&quot; /&gt;<br> &lt;/Columns&gt;<br> &lt;/asp&#58;GridView&gt;<br> &lt;br /&gt;<br> ID&#58;&lt;asp&#58;TextBox ID=&quot;txtID&quot; runat=&quot;server&quot;/&gt;<br> Name&#58;&lt;asp&#58;TextBox ID=&quot;txtName&quot; runat=&quot;server&quot;/&gt;<br>&lt;/asp&#58;Panel&gt;<br>C#&#58;<br>protected void mUpdatePanel_Load(object sender, EventArgs e)<br>&#123;<br> lblTime.Text = DateTime.Now.ToLongTimeString();<br> ArrayList mList = (ArrayList)ViewState[&quot;List&quot;];<br> if (txtName.Text.Length &gt; 0)<br> &#123;<br> Client mClient = new Client();<br> mClient.ID = Int32.Parse(txtID.Text);<br> mClient.Name = txtName.Text;<br> mList.Add(mClient);<br> ViewState[&quot;List&quot;] = mList;<br> gvList.DataSource = mList;<br> gvList.DataBind();<br> &#125;<br>&#125;<br></p><dd class="ssw15-rteElement-FigureNormal"> Sample Code​​​ </dd><p class="ssw15-rteElement-CodeArea">​​​&lt;a href=&quot;javascript&#58;__doPostBack('mUpdatePanel','');&quot;&gt;Refresh&lt;/a&gt; </p><dd class="ssw15-rteElement-FigureBad"> Bad Code​ </dd><p class="ssw15-rteElement-CodeArea">&lt;input type=&quot;button&quot; onclick=&quot;javascript&#58;__doPostBack('mUpdatePanel','');&quot; value=&quot;Refresh&quot; /&gt; </p><dd class="ssw15-rteElement-FigureGood"> Good Code​ </dd><p class="ssw15-rteElement-YellowBorderBox">We have a program called&#160;<a href="https&#58;//www.ssw.com.au/ssw/CodeAuditor/">SSW Code Auditor</a>&#160;to check for this rule.​<br></p><p>​<br></p>


