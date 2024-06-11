---
seoDescription: Encapsulate form values using the Browsable attribute to maintain consistency and prevent unintended changes.
type: rule
title: Do you encapsulate (aka lock) values of forms?
uri: do-you-encapsulate-aka-lock-values-of-forms
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
created: 2014-03-14T02:44:00.000Z
guid: 295d928f-5ede-4e4c-91b5-26b6fff34eeb
---

One useful feature of inherited forms is the ability to lock the value of certain properties on the inherited copy. E.g.:

<!--endintro-->

- **Font** - we want to maintain a consistent font across all forms
- **BackColor** - changing the background color prevents the form from being themed
- **Icon** - we want all of our forms to have the company Icon

This can be achieved with the following code, which works by hiding the existing property from the designer using the **Browsable** attribute. The **Browsable** attribute set to **False** means "don't show in the the designer". There is also an attribute called **EditorBrowsable**, which hides the property from intellisense.

**C#:**

```cs
using System.ComponentModel;

[Browsable(false)] // Browsable = show property in the Designer
public new Font Font
{
    get
    {
        return base.Font;
    }
    set
    {
        //base.Font = value; //normal property syntax
        base.Font = new Font("Tahoma", 8.25);
        // Must be hard coded - cannot use Me.
    }
}
```

**VB.NET:**

```vb
Imports System.ComponentModel

<Browsable(False)> _
Public Shadows Property Font() As Font
    Get
        Return MyBase.Font
    End Get
    Set(ByVal Value As Font)
        'MyBase.Font = Value 'normal property syntax
        MyBase.Font = Me.Font
    End Set
End Property
```

![Figure: Font Property Visible](fontpropertyvisible.gif)

![Figure: Font Property Hidden](fontpropertyhidden.gif)
