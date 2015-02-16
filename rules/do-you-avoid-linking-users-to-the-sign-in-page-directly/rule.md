---
type: rule
archivedreason: 
title: Do you avoid linking users to the sign in page directly?
guid: 162ede00-8bad-4e09-848f-f7f922d5b20b
uri: do-you-avoid-linking-users-to-the-sign-in-page-directly
created: 2015-02-16T02:57:35.0000000Z
authors: []
related: []
redirects: []

---


<p>
                    When you are adding a hyperlink which links to a web 
     application that requires a
                    
                    login, do not use the login page (login.asp or login.aspx or 
     login.php) for the value of the &quot;href&quot; attribute, use the 
     default page (or other pages) instead.
                </p><p>
                    Thus, if a user is already logged in, he will go to the 
     default page. If not, the
                    
                    page will redirect him to the login page. But if you use the 
     sign in page, the user has to sign in again though he's 
     already logged in.
                </p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="badImage"><dt>
      <img src="http&#58;//www.ssw.com.au/SSW/Standards/Rules/Images/BadNoUseLogin.GIF" alt="Bad" style="margin&#58;5px;" />
   </dt><dd>Figure&#58; Bad Example - Linked to the login page.</dd></dl><dl class="goodImage"><dt> 
      <img src="http&#58;//www.ssw.com.au/SSW/Standards/Rules/Images/GoodNoUseLogin.GIF" alt="Good" style="margin&#58;5px;" />
   </dt><dd>Figure&#58; Good Example - Linked to the default page.</dd></dl>


