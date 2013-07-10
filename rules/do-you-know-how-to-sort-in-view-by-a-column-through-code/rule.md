---
type: rule
title: Do you know how to sort in view by a column through code
uri: do-you-know-how-to-sort-in-view-by-a-column-through-code
created: 2013-07-08T05:40:10.0000000Z
authors:
- id: 9
  title: William Yin
- id: 34
  title: Brendan Richards

---



<span class='intro'> You may know that it is quite&#160;easy to sort view by a column through the UI.<dl class="ssw15-rteElement-ImageArea"><img src="/SoftwareDevelopment/RulesToBetterSharePoint/PublishingImages/SortInView.png" alt="SortInView.png" style="margin&#58;5px;width&#58;650px;" /><br></dl><div>But when you are trying to do that via code, you may find a pretty tricky issue.</div> </span>

You can use some code like&#58;<div><p class="ssw15-rteElement-CodeArea">view.Query = &quot;&lt;OrderBy&gt;&lt;FieldRef Name=\&quot;Modified\&quot; Ascending=\&quot;FALSE\&quot; /&gt;&lt;/OrderBy&gt;&quot;;</p><div>but the below code won't work&#58;<br></div><div><p class="ssw15-rteElement-CodeArea">view.Query = &quot;&lt;OrderBy&gt;&lt;FieldRef Name=\&quot;Modified\&quot; Ascending=\&quot;False\&quot; /&gt;&lt;/OrderBy&gt;&quot;;</p><div>​<br></div><div>The full code should be some code&#160;​like&#58;</div><div><p class="ssw15-rteElement-CodeArea">SPView view = list.DefaultView;<br>view.Query = &quot;&lt;OrderBy&gt;&lt;FieldRef Name=\&quot;Modified\&quot; Ascending=\&quot;FALSE\&quot; /&gt;&lt;/OrderBy&gt;&quot;;<br>view.Update();​​​​<br></p>​<br>​</div><br></div><div>&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;</div><div>&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&#160;</div><div>&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&#160;</div><br></div>


