---
type: rule
archivedreason: 
title: Do you know how to sort in view by a column through code
guid: 19d582ea-4667-4b80-a4a3-3dc5a9e515c3
uri: do-you-know-how-to-sort-in-view-by-a-column-through-code
created: 2013-07-08T05:40:10.0000000Z
authors:
- title: William Yin
  url: https://ssw.com.au/people/william-yin
- title: Brendan Richards
  url: https://ssw.com.au/people/brendan-richards
related: []
redirects: []

---


​​​You may know that it is quite easy to sort view by a column through the UI.<dl class="ssw15-rteElement-ImageArea"><img src="SortInView.png" alt="SortInView.png" style="margin:5px;width:650px;" /></dl><dd class="ssw15-rteElement-FigureNormal">Figure: Change view <span style="color:#555555;font-size:11px;font-weight:bold;">column </span>​sort from web UI</dd><div>But when you are trying to do that via code, you may find a pretty tricky issue.</div>
<br><excerpt class='endintro'></excerpt><br>
You can use some code like:<div><p class="ssw15-rteElement-CodeArea">view.Query = "&lt;OrderBy&gt;&lt;FieldRef Name=\"Modified\" Ascending=\"<strong>FALSE</strong>\" /&gt;&lt;/OrderBy&gt;";</p><dd class="ssw15-rteElement-FigureNormal">Figure: Use code to change view sort</dd><div>but the below code won't work:<br></div><div><p class="ssw15-rteElement-CodeArea">view.Query = "&lt;OrderBy&gt;&lt;FieldRef Name=\"Modified\" Ascending=\"<strong>False</strong>\" /&gt;&lt;/OrderBy&gt;";</p><dd class="ssw15-rteElement-FigureBad">Bad Example - the Ascending attribute is case-sensitive<br></dd><div>The full code should be some code ​like:</div><div><p class="ssw15-rteElement-CodeArea">SPView view = list.DefaultView;<br>view.Query = "&lt;OrderBy&gt;&lt;FieldRef Name=\"Modified\" Ascending=\"<strong>FALSE</strong>\" /&gt;&lt;/OrderBy&gt;";<br>view.Update();​​​​<br></p><dd class="ssw15-rteElement-FigureGood">​Good Example - the Ascending attribute is using capital charactors as it is case-sensitive</dd>                 </div></div><div>                    </div><div>                    </div><br></div>


