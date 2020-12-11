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

If we want to refresh and data bind the same page from client side, we can use the javascript function calls "\_\_doPostBack". We shouldn't fire this post back in LinkButton. Otherwise, there will be an error.

<!--endintro-->
<dl class="image">&lt;dt&gt;<img src="RightClickLink.gif" alt="RightClickLink.gif">&lt;/dt&gt;<dd>Figure: Right click the link with __doPostBack event  
</dd></dl><dl class="image">&lt;dt&gt;<img src="PostBack.gif" alt="PostBack.gif">&lt;/dt&gt;<dd>Figure: New window with incorrect URL</dd></dl>
ASPX:
<asp:panel runat="server" id="mUpdatePanel" onload="mUpdatePanel_Load"><br> <asp:label runat="server" id="lblTime"></asp:label><br> <br><br> <asp:gridview id="gvList" runat="server" autogeneratecolumns="false"><br> <columns><br> <asp:boundfield datafield="ID" headertext="ID"></asp:boundfield><br> </columns><br> <columns><br> <asp:boundfield datafield="Name" headertext="Name"></asp:boundfield><br> </columns><br> </asp:gridview><br> <br><br> ID:<asp:textbox id="txtID" runat="server"></asp:textbox><br> Name:<asp:textbox id="txtName" runat="server"></asp:textbox><br></asp:panel>
C#:
protected void mUpdatePanel\_Load(object sender, EventArgs e)
{
 lblTime.Text = DateTime.Now.ToLongTimeString();
 ArrayList mList = (ArrayList)ViewState["List"];
 if (txtName.Text.Length > 0)
 {
 Client mClient = new Client();
 mClient.ID = Int32.Parse(txtID.Text);
 mClient.Name = txtName.Text;
 mList.Add(mClient);
 ViewState["List"] = mList;
 gvList.DataSource = mList;
 gvList.DataBind();
 }
}
 **Sample Code** 
[Refresh](javascript:__doPostBack%28'mUpdatePanel',''%29;)


::: bad
Bad Code
:::


<input type="button" onclick="javascript:__doPostBack('mUpdatePanel','');" value="Refresh">


::: good
Good Code
:::


We have a program called [SSW Code Auditor](https://www.ssw.com.au/ssw/CodeAuditor/) to check for this rule.
