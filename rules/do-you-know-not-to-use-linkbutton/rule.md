---
type: rule
archivedreason: 
title: Do you know not to use LinkButton?
guid: d96e7ee3-d0eb-46a6-8177-8d96cac2ca44
uri: do-you-know-not-to-use-linkbutton
created: 2016-09-01T17:57:47.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


If we want to refresh and data bind the same page from client side, we can use the javascript function calls "__doPostBack". We shouldn't fire this post back in LinkButton. Otherwise, there will be an error.<br>
<br><excerpt class='endintro'></excerpt><br>
<dl class="image"><dt><img src="RightClickLink.gif" alt="RightClickLink.gif" /></dt><dd>Figure: Right click the link with __doPostBack event  ​
</dd></dl><dl class="image"><dt><img src="PostBack.gif" alt="PostBack.gif" /></dt><dd>Figure: New window with incorrect URL</dd></dl>

   <p class="ssw15-rteElement-CodeArea">ASPX:<br><asp:Panel runat="server" ID="mUpdatePanel" OnLoad="mUpdatePanel_Load"><br> <asp:Label runat="server" ID="lblTime" /><br> <br /><br> <asp:GridView ID="gvList" runat="server" AutoGenerateColumns="false"><br> <Columns><br> <asp:BoundField DataField="ID" HeaderText="ID" /><br> </Columns><br> <Columns><br> <asp:BoundField DataField="Name" HeaderText="Name" /><br> </Columns><br> </asp:GridView><br> <br /><br> ID:<asp:TextBox ID="txtID" runat="server"/><br> Name:<asp:TextBox ID="txtName" runat="server"/><br></asp:Panel><br>C#:<br>protected void mUpdatePanel_Load(object sender, EventArgs e)<br>{<br> lblTime.Text = DateTime.Now.ToLongTimeString();<br> ArrayList mList = (ArrayList)ViewState["List"];<br> if (txtName.Text.Length > 0)<br> {<br> Client mClient = new Client();<br> mClient.ID = Int32.Parse(txtID.Text);<br> mClient.Name = txtName.Text;<br> mList.Add(mClient);<br> ViewState["List"] = mList;<br> gvList.DataSource = mList;<br> gvList.DataBind();<br> }<br>}<br></p><dd class="ssw15-rteElement-FigureNormal"> Sample Code​​​ </dd><p class="ssw15-rteElement-CodeArea">​​​<a href="javascript:__doPostBack('mUpdatePanel','');">Refresh</a> </p><dd class="ssw15-rteElement-FigureBad"> Bad Code​ </dd><p class="ssw15-rteElement-CodeArea"><input type="button" onclick="javascript:__doPostBack('mUpdatePanel','');" value="Refresh" /> </p><dd class="ssw15-rteElement-FigureGood"> Good Code​ </dd><p class="ssw15-rteElement-YellowBorderBox">We have a program called <a href="https://www.ssw.com.au/ssw/CodeAuditor/">SSW Code Auditor</a> to check for this rule.​<br></p><p>​<br></p>


