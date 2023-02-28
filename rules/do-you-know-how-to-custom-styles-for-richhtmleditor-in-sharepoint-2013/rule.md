---
type: rule
archivedreason: Outdated and content contains HTML
title: Do you know how to custom styles for RichHtmlEditor in SharePoint 2013?
guid: 9120f632-a360-4fcb-b5ea-18e6a1fc8f91
uri: do-you-know-how-to-custom-styles-for-richhtmleditor-in-sharepoint-2013
created: 2013-07-08T07:31:15.0000000Z
authors:
- title: William Yin
  url: https://ssw.com.au/people/william-yin
- title: Brendan Richards
  url: https://ssw.com.au/people/brendan-richards
related: []
redirects: []

---

As a CMS system, it's obviously necessary to apply standard styles to all content, so the whole site looks consistent.

This rule outlines how to use custom styles in the SharePoint  RichHTMLEditor.

In SharePoint, we can use the below way to apply custom styles:

![Figure: custom RichHtmlEditor styles give your content editors a visual preview of your custom styles](CustomStylesInSharePoint.png) 

<!--endintro-->

To do this:

1. You can use "**PrefixStyleSheet**" property to apply the custom styles to a build-in **RichHtmlField** in page layout or master page. In my case, I applied them to a custom control "**ParsedRichHtmlField**" which inherited from the system build-in one.


``` html
<SSW:ParsedRichHtmlField **PrefixStyleSheet="ssw15-rte"** CssClass="ssw-inputeditorfield" id="Content" FieldName="PublishingPageContent" InputFieldLabel="Rule Summary Info" runat="server"/>
```

2. Refer an additional css file in the page layout or master page (apply to display mode content).

``` html
<SharePointWebControls:CssRegistration ID="CssRegistration3"   Name=" **Themable/ssw.core.styles.v15.css** " runat="server"  EnableCssTheming="True"/>
```

3. Refer the additional css file again in " **edit mode** " in the page layout or master page (apply to edit mode editor).

``` html
<PublishingWebControls:EditModePanel ID="EditModePanel1" runat="server">
<!-- Styles for edit mode only-->

<SharePointWebControls:CssRegistration ID="CssRegistration2" name="<% $SPUrl:~sitecollection/Style Library/~language/Themable/Core Styles/editmode15.css %>"

After="<% $SPUrl:~sitecollection/Style Library/~language/Themable/Core Styles/pagelayouts15.css >" runat="server"/>

<SharePointWebControls:CssRegistration ID="CssRegistration3"   Name=" **Themable/ssw.core.styles.v15.css** " runat="server"  EnableCssTheming="True"

After="<%$SPUrl:~sitecollection/Style Library/~language/Themable/Core Styles/ **editmode15.css** >" />

</PublishingWebControls:EditModePanel>
```

Use " **After** " property to ensure that it will be loaded after the " **editmode15.css** ", which is SharePoint default edit mode style. The custom style css file will be applied to the ribbon after users change to edit mode.

4. Add your custom styles definitions into the additional css file, all styles' names should start with the value you set for  **PrefixStyleSheet** , in our case, it's " **ssw15-rte** ". The custom styles can be applied to different areas (cases) in the ribbon.

1) .ssw15-rte **Language -** As SharePoint support multiple language, this definition will tell SharePoint which language will use those custom styles. E.g.

``` css
.ssw15-rteLanguage-en {

-ms-name: English;

}
```

2) .ssw15-rte **Element -** tell SharePoint which element will be applied with this style. When you press "Enter" in SharePoint editor, it will automatically start a new paragraph with "&lt;P&gt;&lt;/P&gt;", so it's a brilliant choice to make some custom "paragraph" elements. E.g.

``` css
P.ssw15-rteElement-CodeArea

{-ms-name:"Code Area";
border: solid #CCC;
border-width: 1px 1px 1px 10px;
background: #EEE;
padding: 5px 10px;
margin: 8px;
overflow-x:auto;
display:block;
width:93%;
font-size:12px;
}
```

This  **Code Area** style will come up in "Page Elements" section:

![Figure: Code Area style come up in "Page Elements" section](CodeArea.png

While applying a "Page Elements" style, it will

* Remove all the styles for the children elements
* It may change both the class name and the parent element type, it depends on which html element has been specified in the definition.

For example, we change the style from

``` css
p.ssw15-rteElement-CodeArea`
```

to
``` css
`dd.ssw15-rteElement-FigureGood`
```

Its html code will change from

``` html
<img src="page_element_p.png" alt="page_element_p.png" style="margin:5px;width:650px;">
<p>Figure: "Code Area style" with parent element</p>

```

to

``` html
<img src="page_element_dd.png" alt="page_element_dd.png" style="margin:5px;width:650px;"><span style="color:#555555;font-size:11px;font-weight:bold;">
```
**Figure: "Good Figure style" changed the parent element from `<p>` to `<dd>`**

3) .ssw15-rte **Style -** this style could be applied to **Text Styles**. E.g.

``` css

.ssw15-rteStyle-Highlight

{

<-ms-name:"Highlight";
background-color: #FFFF00;

}

```

This  **Highlight** style will come up in "Text Styles" section:

``` html
<img src="HighLight.png" alt="HighLight.png" style="margin:5px;">
```
**Figure: Highlight style will come up in "Text Styles" section**

While applying a "Text Styles" style, it will:

* nest the text in a &lt;span&gt; tag with the style class if the text is not already inside an HTML tag
* replace the class of the HTML tag if this tag is a &lt;span&gt; tag


That means all "Text Styles" will apply to `<span>` tag, and you cannot apply two "Text Styles" to one `<span>` (e.g. apply both Strike and Hightlight), you may have to do that via changing html source code manually, or creating a "combined" "Text Styles".


4) .ssw15-rte **Table -** Tell SharePoint the definition of custom table styles. After inserting a table, you can see the styles under "Design" tab. E.g. The below is a " **SSW Table** " style definition:

``` css
.ssw15-rte **Table-** default

{
<-ms-name:"SSW Table";
border:1px solid #ddd;
margin: 8px;
width:98%;
background-color:#f0f0f0;
}

```

After finishing the definitions of custom styles, make a package and deploy to a SharePoint site, Create a page using the page layout or master page which you added custom RichHtmlField style, then you should be able to see the custom styles in the ribbon.
