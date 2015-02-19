---
type: rule
title: Do you avoid linking users to the sign in page directly?
uri: do-you-avoid-linking-users-to-the-sign-in-page-directly
created: 2015-02-16T02:57:35.0000000Z
authors: []

---



<span class='intro'> <p>
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
                </p> </span>

<dl class="badImage"><dt>
      <img alt="Bad" src="http&#58;//www.ssw.com.au/SSW/Standards/Rules/Images/BadNoUseLogin.GIF" style="margin&#58;5px;" />
   </dt><dd>Figure&#58; Bad Example - Linked to the login page.</dd></dl><dl class="goodImage"><dt> 
      <img alt="Good" src="http&#58;//www.ssw.com.au/SSW/Standards/Rules/Images/GoodNoUseLogin.GIF" style="margin&#58;5px;" />
   </dt><dd>Figure&#58; Good Example - Linked to the default page.</dd></dl>


