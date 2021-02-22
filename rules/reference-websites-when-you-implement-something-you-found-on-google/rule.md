---
type: rule
archivedreason: 
title: Do you reference websites when you implement something you found on Google?
guid: 1f721330-54cd-4d93-93c8-a38ca5874026
uri: reference-websites-when-you-implement-something-you-found-on-google
created: 2018-04-26T22:18:56.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-reference-websites-when-you-implement-something-you-found-on-google

---


If you end up using someone else's code, or even idea, that you found online, make sure you add a reference to this in your source code. There is a good chance that you or your team will revisit the website. And of course, it never hurts to tip your hat, to thank&#160;other coders.<br>​​<br>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-CodeArea">​private void HideToSystemTray()<br>&#123;<br>&#160; &#160; &#160; &#160;// Hide the windows form in the system tray<br>&#160; &#160; &#160; &#160;if (FormWindowState.Minimized == WindowState)<br>&#160; &#160; &#160; &#160;&#123; <br>&#160; &#160; &#160; &#160; &#160; &#160; &#160; Hide();<br>&#160; &#160; &#160; &#160;&#125; <br>&#125;			 </p><dd class="ssw15-rteElement-FigureBad">​​​Bad Example&#58;&#160;The website where the solution was found IS NOT referenced in the comments</dd><p><br></p><p class="ssw15-rteElement-CodeArea">private void HideToSystemTray()<br>&#123;<br> &#160; &#160; &#160; &#160;// Hide the windows form in the system tray<br>&#160; &#160; &#160; &#160;// I found this solution at http&#58;//www.developer.com/net/csharp/article.php/3336751<br>&#160; &#160; &#160; &#160;if (FormWindowState.Minimized == WindowState)<br>&#160; &#160; &#160; &#160;&#123; <br>&#160; &#160; &#160; &#160; &#160; &#160; &#160; Hide();<br>&#160; &#160; &#160; &#160;&#125; <br>&#125;			 </p><dd class="ssw15-rteElement-FigureGood">Good Example&#58; The website where the solution was found is referenced in the comments​​<br></dd><p>​<br></p>


