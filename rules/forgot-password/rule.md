---
seoDescription: Forgetting passwords can be frustrating, but providing a 'Forgot my password' link on the sign-in page makes it easy to regain access.
type: rule
archivedreason:
title: Authentication - Do you have a 'Forgot your password' link?
guid: 07cac45a-80f4-4acb-a9df-7408987536c0
uri: forgot-password
created: 2014-12-11T20:10:16.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Duncan Hunter
    url: https://ssw.com.au/people/duncan-hunter
related:
  - keep-your-websites-clean-and-simple
redirects:
  - authentication-do-you-have-a-forgot-my-password-link

---

Users often forget their passwords — the key to accessing their accounts. To handle this, include a "Forgot your password?" link on the sign-in page.

<!--endintro-->

::: bad  
![Figure: Bad example - What will happen for the poor user that forgot their password?](bad.png)  
:::

::: good  
![Figure: Good example - Users have an option if they forget their password](good.png)  
:::

::: good  
![Figure: Good example - Users enter their email to get a new password](reset example.png)  
:::

## Avoid extra wording

For best UX, “Forgot your password?” should usually be a single clickable link — the question itself is enough to imply “Click here to reset.”

::: greybox
Forgot your password? [Click here to reset your password](#)
:::
::: bad
Figure: Bad example - Unnecessary text for a common action
:::

::: greybox
[Forgot your password?](#)
:::
::: good
Figure: Good example - Short, clean, standard on most sites
:::

::: info
**Note:** In UI text, use "**your** password" rather than "**my** password" to speak directly to the user.
:::

## Avoid username enumeration attacks

This practice also opens up the risk of "username enumeration" where an entire collection of usernames or email addresses can be validated for existence on the website simply by batching requests and looking at the responses.

Read more on Troy Hunt's blog post ["Everything you ever wanted to know about building a secure password reset feature"](http://www.troyhunt.com/2012/05/everything-you-ever-wanted-to-know.html).

You should always aim to not disclose if a user is registered with your site or not.

::: bad  
![Figure: Bad example - Displaying information whether a user exists or not](2016-01-05_15-20-06.png)  
:::

::: good  
![Figure: Good example - Do not disclose whether a user is registered with your site](demo.png)  
:::
