---
type: rule
title: Do you do your validation with Return?
uri: do-your-validation-with-exit-sub
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-do-your-validation-with-return
created: 2018-04-25T23:05:48.000Z
archivedreason: null
guid: bcd97bcb-132f-493e-87e7-67d5799d9c72
---
The return statement can be very useful when used for validation filtering.

Instead of a deep nested If, use Return to provide a short execution path for conditions which are invalid.

<!--endintro-->

```csharp
private void AssignRightToLeft()
{
  // Validate Right 
  if (paraRight.SelectedIndex >= 0)
  { 
    // Validate Left 
    if (paraLeft.SelectedIndex >= 0)
    {
       string paraId = paraRight.SelectedValue.ToString();
       Paragraph para = new Paragraph();
       para.MoveRight(paraId);
       RefreshData();
    }
  }
}
```

::: bad
Figure: Bad example - Using nested if for validation

:::

```csharp
private void AssignRightToLeft()
{
  // Validate Right 
  if (paraRight.SelectedIndex < 0)
  {
    return; 
  }
  
  // Validate Left 
  if (paraLeft.SelectedIndex < 0)
  {
    return;
  }

  string paraId = paraRight.SelectedValue.ToString();
  Paragraph para = new Paragraph();
  para.MoveRight(paraId);
  RefreshData();
}
```

::: good
Figure: Good example - Using Return to exit early if invalid 

:::
