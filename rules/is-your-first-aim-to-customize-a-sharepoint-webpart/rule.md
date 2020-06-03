---
type: rule
title: Is your first aim to customize a SharePoint webpart?
uri: is-your-first-aim-to-customize-a-sharepoint-webpart
created: 2009-02-28T09:14:44.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 8
  title: John Liu

---



<span class='intro'> 
  <p>You should always try to configure existing out-of-the-box SharePoint webparts before you roll your own.</p>
The Content Query web part in particular&#160;is very flexible – allowing contents from different lists to be presented in different ways. <br>
 </span>


  <p>These are some of the fields in the CQWP that are often configured&#58;</p>
<p><strong>MainXslLink, ItemXslLink&#58;</strong></p>
<p>These two controls the main and item XSL file paths.&#160; Set these to your new XSL file under /Style Library/XSL Style Sheets/SSW/SSWMainContent.xsl and SSWItem.xsl files</p>
<p><strong>ItemLimit </strong></p>
<p>The default number of items that are displayed on a Content Query web part is 15.&#160; With unlimited pages.&#160; Sometimes you want this number to be a lot higher (or -1 for no limit).</p>
<p>Note&#58; If you do make this unlimited - make sure your page is designed to grow infinitely or the layout may look strange.</p>
<p><strong>CommonViewFields </strong></p>
<p>The Content Query web part automatically selects a few of the common fields for any query.&#160; But sometimes you want a particular field that isn't selected by default.&#160; This is when you should use CommonViewFields.</p>
<p>The syntax is &quot;fieldname,fieldtype;&quot;</p>
<p>E.g. PublishingContent,PublishingHTML;</p>
<p><strong>Query and QueryOverride </strong></p>
<p>The Content Query web part gives the user a lot of flexibility to design the query in the UI toolpart.&#160; However if your needs are perculiar you can use the QueryOverride to skip over defining the query and use your supplied CAML directly.</p>
<p>&#160;</p>
<dl class="badCode">
    <dt>
    <pre>[Guid(&quot;5bbdb385-5076-4a4b-85e8-691664b7f575&quot;)]<br> public class WebPart1 &#58; System.Web.UI.WebControls.WebParts.WebPart<br>&#123;<br>    public WebPart1() &#123; &#125;<br>    protected override void CreateChildControls()<br>    &#123;<br>        base.CreateChildControls();<br>        // TODO&#58; add custom rendering code here.<br>        Label label = new Label();<br>        label.Text = &quot;Hello World&quot;;<br>        this.Controls.Add(label);<br>    &#125;<br>&#125;</pre>
    </dt>
    <dd>Bad Example&#58; Inherit from System.Web.UI.WebControls.WebParts.WebPart</dd>
</dl>
<p>&#160;</p>
<p>&#160;</p>
<dl class="goodCode">
    <dt>
    <pre>public class RelatedContentByQueryWebPart&#58;CustomContentByQueryWebPart<br>&#123;<br>    public string RulesKeyWords //get the column name from SharePoint<br>    &#123;<br>        get;<br>        set;<br>    &#125;<br>    protected override void OverrideQuery()<br>    &#123;<br>        StringBuilder query = new StringBuilder();<br>        SPListItem item = SPContext.Current.ListItem;<br>        string[] rulesKeyWords = &#123;&#125;;<br>        if (item != null)<br>        &#123;<br>            ......<br>        &#125;<br>        this.QueryOverride = query.ToString(); // pass the query<br>    &#125;<br>&#125;</pre>
    </dt>
    <dd>Good Example&#58; Inherit from CustomContentByQueryWebPart</dd>
</dl>
<p>&#160;</p>



