---
type: rule
archivedreason: 
title: Authentication - Do you have a user friendly registration and sign in screen?
guid: 9cf4dfa1-7faf-4401-984d-599872ae16fc
uri: authentication-do-you-have-a-user-friendly-registration-and-sign-in-screen
created: 2014-12-09T19:50:46.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

For a website that expects a lot of first-time visitors, it is wise to put the                     user registration form on the same page as the sign in dialog. This saves having the                     user click on another link to enter their details.

<!--endintro-->


::: bad  
![Figure: Bad example - non-friendly sign in screen](BadloginDialog.gif)  
:::

The image is a bad example of a dialog box because:

* You can easily enter the correct data and click the wrong hyperlink (i.e. Join or sign in)
* By well-established convention, buttons should be used whenever form data is to be submitted back to the server
* The "Forgot my Password" link is ambiguous - Does it take me to a new page or do I have to enter the email address field first?
* A button, not a link, should be used for submitting data, as links don't allow the user to hit "enter"



::: good  
![Figure: Good example - friendly sign in screen for many new visitors](GoodloginScreen.gif)  
:::

For a website that expects few first-time visitors, this is a good sign in screen, as it is clean and concise:


::: good  
![Figure: Good example - friendly sign in screen for few new visitors](GoodloginScreen-few.gif)  
:::

**Note:** Generally, the action buttons should be aligned to the right.
