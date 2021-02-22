---
type: rule
archivedreason: 
title: Do you always check your button's event handler hook-up?
guid: a2a5ba5a-ed9c-4640-974e-747af2860cf9
uri: always-check-your-buttons-event-handler-hook-up
created: 2018-04-26T21:27:02.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-always-check-your-buttons-event-handler-hook-up

---

Sometimes the button's event handler hook-up could be lost by accident, but there will be no warning or error reported when you compile your applications. 

<!--endintro-->



```
this.button1 = new System.Windows.Forms.Button();
this.button1.FlatStyle = System.Windows.Forms.FlatStyle.System;
this.button1.Location = new System.Drawing.Point(419, 115);
this.button1.Name = "button1";
this.button1.Size = new System.Drawing.Size(75, 23);
this.button1.TabIndex = 60;
this.button1.UseVisualStyleBackColor = true;
```




::: bad
Bad Example - the event handler hook-up is lost, so there will be no response after you click the button

:::



```
this.btnResetAll = new System.Windows.Forms.Button();
this.btnResetAll.FlatStyle = System.Windows.Forms.FlatStyle.System;
this.btnResetAll.Location = new System.Drawing.Point(417, 410);
this.btnResetAll.Name = "btnResetAll";
this.btnResetAll.Size = new System.Drawing.Size(75, 23);
this.btnResetAll.TabIndex = 54;
this.btnResetAll.Text = "Reset &All";
this.btnResetAll.UseVisualStyleBackColor = true;
this.btnResetAll.Click += new System.EventHandler(this.btnResetAll_Click);
```




::: good
Good Example : keep the event handler hook-up together with the initialization of the button

:::
