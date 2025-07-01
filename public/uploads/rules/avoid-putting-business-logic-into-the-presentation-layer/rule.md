---
seoDescription: Avoid mixing business logic into presentation layer code by separating concerns and placing business logic in a separate layer for reuse and maintainability.
type: rule
archivedreason:
title: Do you avoid putting business logic into the presentation layer?
guid: 4e3ec478-ea2b-4065-a0a6-4c3667c5b71a
uri: avoid-putting-business-logic-into-the-presentation-layer
created: 2018-04-26T22:25:39.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-avoid-putting-business-logic-into-the-presentation-layer
---

Be sure you are aware of what is business logic and what isn't. Typically, looping code will be placed in the business layer. This ensures that no redundant code is written and other projects can reference this logic as well.

<!--endintro-->

```cs
private void btnOK_Click(object sender, EventArgs e)
{
  rtbParaText.Clear();
  var query =
    from p in dc.GetTable()
    select p.ParaID;
  foreach (var result in query)
  {
    var query2 =
      from t in dc.GetTable()
      where t.ParaID == result
      select t.ParaText;
    rtbParaText.AppendText(query2.First() + "\r\n");
  }
}
```

::: bad
Bad Example: A UI method mixed with business logics  
:::

```cs
private void btnOK_Click(object sender, EventArgs e)
{
  string paraText = Business.GetParaText();
  rtbParaText.Clear();
  rtbParaText.Add(paraText);
}
```

::: good
Good Example : Putting business logics into the business project, just call the relevant method when needed

:::
