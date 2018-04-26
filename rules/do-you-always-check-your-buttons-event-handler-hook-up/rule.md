---
type: rule
title: Do you always check your button's event handler hook-up?
uri: do-you-always-check-your-buttons-event-handler-hook-up
created: 2018-04-26T21:27:02.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> Sometimes the button's event handler hook-up could be lost by accident, but there will be no warning or error reported when you complie your applications. <br> </span>

<p class="ssw15-rteElement-CodeArea">​​this.button1 = new System.Windows.Forms.Button();<br>this.button1.FlatStyle = System.Windows.Forms.FlatStyle.System;<br>this.button1.Location = new System.Drawing.Point(419, 115);<br>this.button1.Name = &quot;button1&quot;;<br>this.button1.Size = new System.Drawing.Size(75, 23);<br>this.button1.TabIndex = 60;<br>this.button1.UseVisualStyleBackColor = true;<br></p><dd class="ssw15-rteElement-FigureBad">Bad Example - the event handler hook-up is lost, so there will be no response after you click the butto​​n​<br></dd><p class="ssw15-rteElement-CodeArea">this.btnResetAll = new System.Windows.Forms.Button();<br>this.btnResetAll.FlatStyle = System.Windows.Forms.FlatStyle.System;<br>this.btnResetAll.Location = new System.Drawing.Point(417, 410);<br>this.btnResetAll.Name = &quot;btnResetAll&quot;;<br>this.btnResetAll.Size = new System.Drawing.Size(75, 23);<br>this.btnResetAll.TabIndex = 54;<br>this.btnResetAll.Text = &quot;Reset &amp;All&quot;;<br>this.btnResetAll.UseVisualStyleBackColor = true;<br>this.btnResetAll.Click += new System.EventHandler(this.btnResetAll_Click); <br></p><dd class="ssw15-rteElement-FigureGood">Good Example &#58; keep the event handler hook-up together with the initialization of the button​​​​<br></dd><p>​<br><br></p>


