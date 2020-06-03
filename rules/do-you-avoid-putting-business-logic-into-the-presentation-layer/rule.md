---
type: rule
title: Do you avoid putting business logic into the presentation layer?
uri: do-you-avoid-putting-business-logic-into-the-presentation-layer
created: 2018-04-26T22:25:39.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> Be sure you are aware of what is business logic and what isn't. Typically, looping code will be placed in the business layer. This ensures that no redundant code is written and other projects can reference this logic as well.<br><br> </span>

<p class="ssw15-rteElement-CodeArea">private void btnOK_Click(object sender, EventArgs e)<br>&#123;<br>rtbParaText.Clear();<br>var query =<br>from p in dc.GetTable()<br>select p.ParaID;<br>foreach (var result in query)<br>&#123;<br>var query2 =<br>from t in dc.GetTable()<br>where t.ParaID == result<br>select t.ParaText;<br>rtbParaText.AppendText(query2.First() + &quot;\r\n&quot;);<br>&#125;<br>&#125;</p><dd class="ssw15-rteElement-FigureBad"> Bad Example&#58;&#160;A UI method mixed with business logics</dd><p><br></p><p class="ssw15-rteElement-CodeArea">private void btnOK_Click(object sender, EventArgs e)<br>&#123;<br>string paraText = Business.GetParaText();<br>rtbParaText.Clear();<br>rtbParaText.Add(paraText);<br>&#125;</p><dd class="ssw15-rteElement-FigureGood">Good Example &#58; Putting business logics into the business project, just call the relevant method when needed​​<br></dd><p><br></p>


