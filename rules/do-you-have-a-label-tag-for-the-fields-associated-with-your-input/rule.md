---
type: rule
title: Do you have a label tag for the fields associated with your input?
uri: do-you-have-a-label-tag-for-the-fields-associated-with-your-input
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []
created: 2014-12-16T18:47:45.000Z
archivedreason: null
guid: 8fb2c2cb-b780-4ac3-bd5a-2a7b58d15459
---
When adding input boxes to collect data, please always have a \<label\> tag associated with your \<input\> tag to link the labels with their respective edit controls. This improves accessibility and gives nice focusing stuff (when you click the label).

<!--endintro-->


```html
<p>
    <label for="EmailAddress">Email Address</label>
    <input id="EmailAddress" type="text"/>
</p>
```


**Tip:** To do this in ASP.NET use the AssociatedControlID parameter on your \<asp:Label /\>; controls.


```html
<p>
    <asp:Label ID="EmailLabel" runat="server" Text="Email Address" AssociatedControlID="EmailAddress"/>
    <asp:TextBox ID="EmailAddress" runat="server"/>
</p>
```

**Tip:** For a nicer user experience, consider using adaptive labels and inputs with a UI Library like [Material UI](https://material-ui.com/components/text-fields/).
