

---
authors:

---




<span class='intro'> <p>
      How come there are so many pages I see that don't have an email address on the page?
      Every page on your site should have an email hyperlink.
     </p><p>
      Even better make it easy for visitors to report the actual page they are referring
      to. A simple mail link will give users an easy way to report bugs or give feedback
      (check out the bottom of this page). By putting this code in your footer template,
      users will see this link on every page.
     </p> </span>

<p>
      &lt;a href=&quot;mailto&#58;infomation@***.com.au?subject=FeedBack&amp;body=&lt;%=Request.ServerVariables(&quot;URL&quot;)%&gt;&quot;&gt;
      Feedback Please &lt;/a&gt;
     </p>


