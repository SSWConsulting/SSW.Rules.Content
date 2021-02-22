---
type: rule
archivedreason: 
title: Do you know not to use LinkButton?
guid: d96e7ee3-d0eb-46a6-8177-8d96cac2ca44
uri: do-not-use-linkbutton
created: 2016-09-01T17:57:47.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-know-not-to-use-linkbutton

---


If we want to refresh and data bind the same page from client side, we can use the javascript function calls "__doPostBack". We shouldn't fire this post back in LinkButton. Otherwise, there will be an error.<br>
<br><excerpt class='endintro'></excerpt><br>
<dl class="image"><dt><img src="RightClickLink.gif" alt="RightClickLink.gif" /></dt><dd>Figure: Right click the link with __doPostBack event  ​
</dd></dl><dl class="image"><dt><img src="PostBack.gif" alt="PostBack.gif" /></dt><dd>Figure: New window with incorrect URL</dd></dl>

   <p class="ssw15-rteElement-CodeArea">ASPX:<br>&lt;asp:Panel runat="server" ID="mUpdatePanel" OnLoad="mUpdatePanel_Load"&gt;<br> &lt;asp:Label runat="server" ID="lblTime" /&gt;<br> &lt;br /&gt;<br> &lt;asp:GridView ID="gvList" runat="server" AutoGenerateColumns="false"&gt;<br> &lt;Columns&gt;<br> &lt;asp:BoundField DataField="ID" HeaderText="ID" /&gt;<br> &lt;/Columns&gt;<br> &lt;Columns&gt;<br> &lt;asp:BoundField DataField="Name" HeaderText="Name" /&gt;<br> &lt;/Columns&gt;<br> &lt;/asp:GridView&gt;<br> &lt;br /&gt;<br> ID:&lt;asp:TextBox ID="txtID" runat="server"/&gt;<br> Name:&lt;asp:TextBox ID="txtName" runat="server"/&gt;<br>&lt;/asp:Panel&gt;<br>C#:<br>protected void mUpdatePanel_Load(object sender, EventArgs e)<br>{<br> lblTime.Text = DateTime.Now.ToLongTimeString();<br> ArrayList mList = (ArrayList)ViewState["List"];<br> if (txtName.Text.Length &gt; 0)<br> {<br> Client mClient = new Client();<br> mClient.ID = Int32.Parse(txtID.Text);<br> mClient.Name = txtName.Text;<br> mList.Add(mClient);<br> ViewState["List"] = mList;<br> gvList.DataSource = mList;<br> gvList.DataBind();<br> }<br>}<br></p><dd class="ssw15-rteElement-FigureNormal"> Sample Code​​​ </dd><p class="ssw15-rteElement-CodeArea">​​​&lt;a href="javascript:__doPostBack('mUpdatePanel','');"&gt;Refresh&lt;/a&gt; </p><dd class="ssw15-rteElement-FigureBad"> Bad Code​ </dd><p class="ssw15-rteElement-CodeArea">&lt;input type="button" onclick="javascript:__doPostBack('mUpdatePanel','');" value="Refresh" /&gt; </p><dd class="ssw15-rteElement-FigureGood"> Good Code​ </dd><p class="ssw15-rteElement-YellowBorderBox">We have a program called <a href="https://www.ssw.com.au/ssw/CodeAuditor/">SSW Code Auditor</a> to check for this rule.​<br></p><p>​<br></p>


