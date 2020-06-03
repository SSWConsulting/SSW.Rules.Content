---
type: rule
title: Do you know how to format your MessageBox code?
uri: do-you-know-how-to-format-your-messagebox-code
created: 2018-04-25T23:10:49.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p class="ssw15-rteElement-P">You should always write each parameter of MessageBox in a separate line. So it will be more clear to read in the code. Format your message text in code as you want to see on the screen.<br></p> </span>

<p class="ssw15-rteElement-CodeArea">​Private Sub ShowMyMessage()<br> MessageBox.Show(&quot;Are<br> you sure you want to delete the team project &quot;&quot;&quot; + strProjectName<br> + &quot;&quot;&quot;?&quot; + Environment.NewLine + Environment.NewLine + &quot;Warning&#58;<br> Deleting a team project cannot be undone.&quot;, strProductName + &quot;<br> &quot; + strVersion(), MessageBoxButtons.YesNo, MessageBoxIcon.Warning, MessageBoxDefaultButton.Button2)<br></p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad example of MessageBox code format​<br></dd><p class="ssw15-rteElement-CodeArea">Private Sub ShowMyMessage()<br> MessageBox.Show( _ <br> &quot;Are you sure you want to delete the team project &quot;&quot;&quot; + strProjectName + &quot;&quot;&quot;?&quot;<br> _ + Environment.NewLine _ +<br> Environment.NewLine _ +<br> &quot;Warning&#58; Deleting a team project cannot be undone.&quot;, _<br> strProductName + &quot; &quot; + strVersion(), _<br> MessageBoxButtons.YesNo, _<br> MessageBoxIcon.Warning, _<br> MessageBoxDefaultButton.Button2)<br>End Sub</p><p></p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good example of MessageBox code format​​<br></dd>


