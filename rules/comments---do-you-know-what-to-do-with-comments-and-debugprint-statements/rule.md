---
type: rule
title: Comments - Do you know what to do with comments and Debug.Print statements
uri: comments---do-you-know-what-to-do-with-comments-and-debugprint-statements
created: 2018-04-25T18:12:19.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>​​​When you create comments in your code, it is better to document why you've done something a certain way than to document how you did it. The code itself should tell the reader what is happening, there's no need to create &quot;how&quot; comments that merely restate the obvious unless you're using some technique that won't be apparent to most readers.<br></p> </span>

<p class="ssw15-rteElement-P">​What do you do with your print statements? Sometimes a programmer will place print statements at critical points in the program to print out debug statements for either bug hunting or testing. After the testing is successful, often the print statements are removed from the code. This is a bad thing to do.</p><p class="ssw15-rteElement-P">Debugging print statements are paths that show where the programmer has been. <strong>They should be commented out, but the statements should be left in the code in the form of comments.</strong> Thus, if the code breaks down later, the programmers (who might not remember or even know the program to start with), will be able to see where testing has been done and where the fault is likely to be - i.e., elsewhere.</p><p class="ssw15-rteElement-CodeArea">private void&#160;Command0_Click() &#123;<br>&#160; &#160; rst.Open(&quot;SELECT * FROM Emp&quot;) //&#160;Open recordset with employee records​<br>&#160;&#160; &#160;<span style="background-color&#58;#ff3300;">//&#160;Debug.Print(&quot;Got &quot; +&#160;intCount + &quot; results&quot;);</span><br>&#160; &#160; if&#160;(intCount &gt; 1000) &#123;<br>&#160;&#160; &#160; &#160; &#160;&#160;<span style="background-color&#58;#ff3300;">//&#160;Debug.Print(&quot;too many records - returning early&quot;);</span><br>&#160; &#160; &#160; &#160; return;<br>&#160; &#160;&#160;&#125; else&#160; &#123;<br>&#160; &#160; .....processing code<br>&#125;<br></p><dd class="ssw15-rteElement-FigureBad">Bad Example​ - Debug code has&#160;just been commented out<br></dd><p class="ssw15-rteElement-CodeArea">private void&#160;Command0_Click() &#123;<br>&#160; &#160; rst.Open(&quot;SELECT * FROM Emp&quot;)<br>​&#160; &#160; <span style="background-color&#58;#ffff00;">//&#160;Count will exceed 1,000 during eighteenth century</span><br style="background-color&#58;#ffff00;"><span style="background-color&#58;#ffff00;">&#160; &#160; //&#160;leap years, which we aren't prepared to handle.</span><br>&#160; &#160; if&#160;(intCount &gt; 1000) &#123;<br>&#160; &#160;&#160;&#160; &#160;&#160;return<br>&#160; &#160;&#160;&#125; else&#160; &#123;<br>&#160; &#160;&#160;.....processing code<br>&#125;<br></p><dd class="ssw15-rteElement-FigureGood"> Good Example - the debug commands have been rafactored into meaningful comments for the next developer<br></dd>


