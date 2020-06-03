---
type: rule
title: Do you use a regular expression to validate an email address?
uri: do-you-use-a-regular-expression-to-validate-an-email-address
created: 2018-04-25T23:15:46.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p class="ssw15-rteElement-P">A regex is the best way to verify an email address.​​<br></p> </span>

<p class="ssw15-rteElement-CodeArea">​public bool IsValidEmail(string email)<br>&#123;<br> // Return true if it is in valid email format.<br> if (email.IndexOf(&quot;@&quot;) &lt;= 0) return false; <br> if (email.EndWith(&quot;@&quot;)) return false; <br> if (email.IndexOf(&quot;.&quot;) &lt;= 0) return false; <br> if ( ... <br>&#125; </p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad example of verify email address​​<br></dd><p class="ssw15-rteElement-CodeArea">public bool IsValidEmail(string email) <br>&#123; <br> // Return true if it is in valid email format.<br> return System.Text.RegularExpressions.Regex.IsMatch( email, <br> @&quot;^([\w-\.]+)@(([[0-9]&#123;1,3&#125;\.[0-9]&#123;1,3&#125;\.[0-9]&#123;1,3&#125;\.)|(([\w-]+\.)+))([a-zA-Z]&#123;2,4&#125;|[0-9]&#123;1,3&#125;)(\]?)$&quot;;<br>&#125; </p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good example of verify email address​​<span style="font-size&#58;13px;">​</span></dd>


