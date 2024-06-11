---
seoDescription: Prevent unnecessary login prompts by linking to default pages instead of the sign-in page, allowing users to seamlessly access protected content if already logged in.
type: rule
archivedreason:
title: Do you avoid linking users to the sign in page directly?
guid: 162ede00-8bad-4e09-848f-f7f922d5b20b
uri: do-you-avoid-linking-users-to-the-sign-in-page-directly
created: 2015-02-16T02:57:35.0000000Z
authors:
  - title: Rebecca Liu
    url: https://ssw.com.au/people/rebecca-liu
related: []
redirects: []
---

When you are adding a hyperlink which links to a web application that requires a login, do not use the login page (login.asp or login.aspx or login.php) for the value of the "href" attribute, use the default page (or other pages) instead.

Thus, if a user is already logged in, they will go to the default page.
If not, the page will redirect them to the login page.
But if you use the sign in page, the user has to sign in again though they're already logged in.

<!--endintro-->

::: bad  
![Figure: Bad Example - Linked to the login page.](../../assets/BadNoUseLogin.gif)  
:::

::: good  
![Figure: Good Example - Linked to the default page.](../../assets/GoodNoUseLogin.gif)  
:::
