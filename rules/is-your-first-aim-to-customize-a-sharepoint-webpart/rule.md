---
type: rule
title: Is your first aim to customize a SharePoint webpart?
uri: is-your-first-aim-to-customize-a-sharepoint-webpart
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: John Liu
    url: https://ssw.com.au/people/john-liu
related: []
redirects: []
created: 2009-02-28T09:14:44.000Z
archivedreason: null
guid: 8b78be7a-6ce0-4391-b4be-8650f0a0ba4d
---

You should always try to configure existing out-of-the-box SharePoint webparts before you roll your own.
 The Content Query web part in particular is very flexible – allowing contents from different lists to be presented in different ways. 

<!--endintro-->

These are some of the fields in the CQWP that are often configured:

**MainXslLink, ItemXslLink:**

These two controls the main and item XSL file paths.  Set these to your new XSL file under /Style Library/XSL Style Sheets/SSW/SSWMainContent.xsl and SSWItem.xsl files

**ItemLimit**

The default number of items that are displayed on a Content Query web part is 15.  With unlimited pages.  Sometimes you want this number to be a lot higher (or -1 for no limit).

Note: If you do make this unlimited - make sure your page is designed to grow infinitely or the layout may look strange.

**CommonViewFields**

The Content Query web part automatically selects a few of the common fields for any query.  But sometimes you want a particular field that isn't selected by default.  This is when you should use CommonViewFields.

The syntax is "fieldname,fieldtype;"

E.g. PublishingContent,PublishingHTML;

**Query and QueryOverride**

The Content Query web part gives the user a lot of flexibility to design the query in the UI toolpart.  However if your needs are perculiar you can use the QueryOverride to skip over defining the query and use your supplied CAML directly.

```csharp
[Guid("5bbdb385-5076-4a4b-85e8-691664b7f575")]
public class WebPart1 : System.Web.UI.WebControls.WebParts.WebPart
{
    public WebPart1() { }
    protected override void CreateChildControls()
    {
        base.CreateChildControls();
        // TODO: add custom rendering code here.
        Label label = new Label();
        label.Text = "Hello World";
        this.Controls.Add(label);
    }
}
```

**Bad Example: Inherit from System.Web.UI.WebControls.WebParts.WebPart**

```csharp
public class RelatedContentByQueryWebPart:CustomContentByQueryWebPart
{
    public string RulesKeyWords //get the column name from SharePoint
    {
        get;
        set;
    }
    protected override void OverrideQuery()
    {
        StringBuilder query = new StringBuilder();
        SPListItem item = SPContext.Current.ListItem;
        string[] rulesKeyWords = {};
        if (item != null)
        {
            ......
        }
        this.QueryOverride = query.ToString(); // pass the query
    }
}
```
**Good Example: Inherit from CustomContentByQueryWebPart**
