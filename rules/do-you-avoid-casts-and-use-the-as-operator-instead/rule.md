---
type: rule
title: Do you avoid casts and use the "as operator" instead?
uri: do-you-avoid-casts-and-use-the-as-operator-instead
created: 2018-04-30T18:40:09.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> Use casts only if&#58;<br>a. You know 100% that you get that type back<br>b. You want to perform a user-defined conversion <br> </span>

<p class="ssw15-rteElement-CodeArea">​ private void AMControlMouseLeftButtonUp(object sender, MouseButtonEventArgs e)<br>&#123;<br> var auc = (AMUserControl)sender; 
   <br> var aucSessionId = auc.myUserControl.Tag;<br> // snip snip snip<br>&#125;</p><dd class="ssw15-rteElement-FigureBad">Bad example​​​<br></dd><p class="ssw15-rteElement-CodeArea">private void AMControlMouseLeftButtonUp(object sender, MouseButtonEventArgs e)<br>&#123;<br> var auc = sender as AMUserControl; 
   <br> if (auc != null)<br> &#123;<br> var aucSessionId = auc.myUserControl.Tag;<br> // snip snip snip<br> &#125; 
   <br>&#125;</p><dd class="ssw15-rteElement-FigureGood">​Good example​<br></dd>

More info here&#58;&#160;​<a href="http&#58;//blog.gfader.com/2010/08/avoid-type-casts-use-operator-and-check.html">http&#58;//blog.gfader.com/2010/08/avoid-type-casts-use-operator-and-check.html</a><br>


