---
type: rule
archivedreason: 
title: Do you do your validation with Return?
guid: bcd97bcb-132f-493e-87e7-67d5799d9c72
uri: do-you-do-your-validation-with-return
created: 2018-04-25T23:05:48.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

The return statement can be very useful when used for validation filtering.
Instead of a deep nested If, use Return to provide a short execution path for conditions which are invalid.

<!--endintro-->

private void AssignRightToLeft()
{
  // Validate Right 
  if (paraRight.SelectedIndex &gt;= 0)
  { 
    // Validate Left 
    if (paraLeft.SelectedIndex &gt;= 0)
    {
       string paraId = paraRight.SelectedValue.ToString();
       Paragraph para = new Paragraph();
       para.MoveRight(paraId);
       RefreshData();
    }
  }
}


::: bad
Figure: Bad example - using nested if for validation

:::




private void AssignRightToLeft()
{
  // Validate Right 
  if (paraRight.SelectedIndex &gt;= 0)
  {
    return; 
  }
  
  // Validate Left 
  if (paraLeft.SelectedIndex &gt;= 0)
  {
    return;
  }

  string paraId = paraRight.SelectedValue.ToString();
  Paragraph para = new Paragraph();
  para.MoveRight(paraId);
  RefreshData();
}


::: good
Figure: Good example - using Return to exit early if invalid 

:::
