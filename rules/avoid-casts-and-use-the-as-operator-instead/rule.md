---
type: rule
archivedreason: 
title: Do you avoid casts and use the "as operator" instead?
guid: b44fe59b-11ab-4ec9-bd57-15c8b93c679e
uri: avoid-casts-and-use-the-as-operator-instead
created: 2018-04-30T18:40:09.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-avoid-casts-and-use-the-as-operator-instead

---


Use casts only if&#58;<br>a. You know 100% that you get that type back<br>b. You want to perform a user-defined conversion <br>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-CodeArea">​ private void AMControlMouseLeftButtonUp(object sender, MouseButtonEventArgs e)<br>&#123;<br> var auc = (AMUserControl)sender; 
   <br> var aucSessionId = auc.myUserControl.Tag;<br> // snip snip snip<br>&#125;</p><dd class="ssw15-rteElement-FigureBad">Bad example​​​<br></dd><p class="ssw15-rteElement-CodeArea">private void AMControlMouseLeftButtonUp(object sender, MouseButtonEventArgs e)<br>&#123;<br> var auc = sender as AMUserControl; 
   <br> if (auc != null)<br> &#123;<br> var aucSessionId = auc.myUserControl.Tag;<br> // snip snip snip<br> &#125; 
   <br>&#125;</p><dd class="ssw15-rteElement-FigureGood">​Good example​<br></dd>

More info here&#58;&#160;​<a href="http&#58;//blog.gfader.com/2010/08/avoid-type-casts-use-operator-and-check.html">http&#58;//blog.gfader.com/2010/08/avoid-type-casts-use-operator-and-check.html</a><br>


