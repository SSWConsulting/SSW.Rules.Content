---
type: rule
archivedreason: 
title: Do you use Public/Protected Properties instead of Public/Protected Fields?
guid: 4c1a9b37-6a57-4c6f-81df-950f5d3afe12
uri: use-public-protected-properties-instead-of-public-protected-fields
created: 2018-04-25T21:45:02.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-use-public-protected-properties-instead-of-public-protected-fields

---

Public/Protected properties have a number of advantages over public/protected fields:

* **Data validation** 
Data validation can be performed in the get/set accessors of a public property. This is especially important when working with the Visual Studio .NET Designer.
* **Increased flexibility** 
Properties conceal the data storage mechanism from the user, resulting in less broken code when the class is upgraded. Properties are a recommended object-oriented practice for this reason.
* **Compatibility with data binding** 
You can only bind to a public property, not a field.
* **Minimal performance overhead** 
The performance overhead for public properties is trivial. In some situations, public fields can actually have inferior performance to public properties.


<!--endintro-->



```
public int Count;
```




::: bad
Figure: Bad code. Variable declared as a Field

:::



```
public int Count
{
 get
 {
 return _count;
 }
 set
 {
 _count = value; 
 }
}
```




::: good
Figure: Good code. Variable declared as a Property

:::

We agree that the syntax is tedious and think [Microsoft should improve this.](https&#58;//www.ssw.com.au/ssw/Standards/BetterSoftwareSuggestions/VisualStudio.aspx#PropertyShortcut)
