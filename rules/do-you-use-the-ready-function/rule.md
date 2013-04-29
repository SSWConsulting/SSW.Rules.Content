---
type: rule
title: Do you use the .ready() function?
uri: do-you-use-the-ready-function
created: 2013-04-29T06:39:55.0000000Z
authors:
- id: 23
  title: Damian Brady

---



<span class='intro'> Putting your initialization JavaScript&#160;code inside the .ready function is not always required, but it's much safer to do so. </span>

<p>​jQuery exposes a <a href="http&#58;//api.jquery.com/ready/">.ready event</a> which fires when the Document Object Model (DOM) is fully loaded and ready to be manipulated.</p><p>You can attach a function to this event so you can be sure the page is ready for you to work on.</p><p><span class="ssw-rteStyle-CodeArea">$('#login').addClass('hidden');</span></p><p><span class="ssw-rteStyle-FigureBad">Figure&#58; Bad Example - if this jQuery is in the wrong place, the #login element may not exist!</span></p><p><span class="ssw-rteStyle-CodeArea">$(function() &#123;<br><span style="line-height&#58;20px;">&#160; &#160; $('</span><span style="line-height&#58;20px;">#login</span><span><span style="line-height&#58;20px;">').addClass('hidden');<br></span></span><span style="line-height&#58;1.6;">&#125;);</span></span></p><p>Figure&#58; Good Example - this code won't run until the DOM is fully loaded</p>


