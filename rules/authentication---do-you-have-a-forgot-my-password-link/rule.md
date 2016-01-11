---
type: rule
title: Authentication - Do you have a 'Forgot my password' link?
uri: authentication---do-you-have-a-forgot-my-password-link
created: 2014-12-11T20:10:16.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 44
  title: Duncan Hunter

---



<span class='intro'> <p>It's easy and common for users to forget their passwords, the vital key which grants
                    them access to the services they are eligible for. To cater for this instance, it
                    is important to have a 'Forgot my password' link on the sign in page.</p> </span>

​​<img src="/SiteAssets/authentication-do-you-have-a-forgot-my-password-link/bad.png" alt="bad.png" style="margin&#58;5px;" />
<dl class="badImage"><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad example - what will happen for the poor user that forgot his password?​​</dd></dl>
​<img src="/SiteAssets/authentication-do-you-have-a-forgot-my-password-link/good.png" alt="good.png" style="margin&#58;5px;" /> &#160;<p></p><dl class="goodImage"><dd class="ssw15-rteElement-FigureGood">​Figure&#58; Good example - users have an option if they forget their password​&#160;</dd></dl><p class="ssw15-rteElement-P"></p><p class="ssw15-rteElement-P">​<img src="/SiteAssets/authentication-do-you-have-a-forgot-my-password-link/reset%20example.png" alt="reset example.png" style="margin&#58;5px;" /><br></p><dd class="ssw15-rteElement-FigureGood"> ​​​​Figure&#58; Good example - users can enter their email to get a new password&#160;​​</dd><p class="ssw15-rteElement-P">​​​<br></p><h3 class="ssw15-rteElement-H3">​​Do you avoid a&#160;username enumeration attack?<br></h3><p>
      <span style="color&#58;#393939;font-family&#58;'segoe ui', verdana, helvetica, sans-serif;font-size&#58;14.4px;line-height&#58;20.16px;">This practice also opens up the risk of “username enumeration” where an entire collection of usernames or email addresses can be validated for existence on the website simply by batching requests and looking at the responses.</span>​ You can read more on Tryp Hunts blog here&#160;http&#58;//www.troyhunt.com/2012/05/everything-you-ever-wanted-to-know.html​. You should always aim to not disclose if a user is registered with your site or not.<br></p><p class="ssw15-rteElement-P">​<br></p><p class="ssw15-rteElement-P">
      <img src="/SiteAssets/authentication-do-you-have-a-forgot-my-password-link/2016-01-05_15-20-06.png" alt="2016-01-05_15-20-06.png" style="margin&#58;5px;" />
      <br>
   </p><dd class="ssw15-rteElement-FigureBad">​<span style="color&#58;#555555;font-size&#58;14.4px;font-weight&#58;bold;line-height&#58;16px;">Figure&#58; Bad example - Displaying information that a user does not exist?​</span><span style="color&#58;#555555;font-size&#58;14.4px;font-weight&#58;bold;line-height&#58;16px;">​​</span><br></dd><p class="ssw15-rteElement-P"> 
      <img src="/SiteAssets/authentication-do-you-have-a-forgot-my-password-link/demo.png" alt="demo.png" style="margin&#58;5px;" /> 
      <br> 
   </p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Bad example - what will happen for the poor user that forgot his password?​​</dd><p class="ssw15-rteElement-P">​​​</p>


