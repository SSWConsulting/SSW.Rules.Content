---
type: rule
title: Do you reference websites when you implement something you found on Google?
uri: do-you-reference-websites-when-you-implement-something-you-found-on-google
created: 2018-04-26T22:18:56.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> If you end up using someone else's code, or even idea, that you found online, make sure you add a reference to this in your source code. There is a good chance that you or your team will revisit the website. And of course, it never hurts to tip your hat off to other coders.<br>​​<br> </span>

<p class="ssw15-rteElement-CodeArea">​private void HideToSystemTray()<br>&#123;<br> // Hide the windows form in the system tray<br> if (FormWindowState.Minimized == WindowState)<br> &#123; <br> Hide();<br> &#125; <br>&#125;    </p><dd class="ssw15-rteElement-FigureBad">​​​Bad Example&#58;&#160;The website where the solution was found IS NOT referenced in the comments</dd><p><br></p><p class="ssw15-rteElement-CodeArea">private void HideToSystemTray()<br>&#123;<br> // Hide the windows form in the system tray<br> // I found this solution at http&#58;//www.developer.com/net/csharp/article.php/3336751<br> if (FormWindowState.Minimized == WindowState)<br> &#123; <br> Hide();<br> &#125; <br>&#125;    </p><dd class="ssw15-rteElement-FigureGood">Good Example&#58; The website where the solution was found is referenced in the comments​​<br></dd><p>​<br></p>


