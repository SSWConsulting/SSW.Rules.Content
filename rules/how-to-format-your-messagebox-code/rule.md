---
type: rule
archivedreason: 
title: Do you know how to format your MessageBox code?
guid: 5993ec82-d9bc-4a99-bac1-de957f030ab0
uri: how-to-format-your-messagebox-code
created: 2018-04-25T23:10:49.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-know-how-to-format-your-messagebox-code

---

You should always write each parameter of MessageBox in a separate line. So it will be more clear to read in the code. Format your message text in code as you want to see on the screen.

<!--endintro-->

``` cs
Private Sub ShowMyMessage()
 MessageBox.Show("Are
 you sure you want to delete the team project """ + strProjectName
 + """?" + Environment.NewLine + Environment.NewLine + "Warning:
 Deleting a team project cannot be undone.", strProductName + "
 " + strVersion(), MessageBoxButtons.YesNo, MessageBoxIcon.Warning, MessageBoxDefaultButton.Button2)
```

::: bad
Figure: Bad example of MessageBox code format
:::

``` cs
Private Sub ShowMyMessage()
 MessageBox.Show( _ 
 "Are you sure you want to delete the team project """ + strProjectName + """?"
 _ + Environment.NewLine _ +
 Environment.NewLine _ +
 "Warning: Deleting a team project cannot be undone.", _
 strProductName + " " + strVersion(), _
 MessageBoxButtons.YesNo, _
 MessageBoxIcon.Warning, _
 MessageBoxDefaultButton.Button2)
End Sub
```

::: good
Figure: Good example of MessageBox code format
:::
