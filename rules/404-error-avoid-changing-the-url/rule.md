---
type: rule
archivedreason: 
title: Do you avoid changing the URL on a 404 error?
guid: 0d3576ad-6b39-4682-b425-3d68751a100b
uri: 404-error-avoid-changing-the-url
created: 2016-08-11T18:08:44.0000000Z
authors: []
related: []
redirects:
- do-you-avoid-changing-the-url-on-a-404-error

---

When you request a URL of a file that doesn't exist, you will get an error message. You should make sure that the URL in the browser doesn't change. This way, it's easy for the user to correct. 
E.g. The user doesn't have to retype the whole URL if there is a spelling mistake or a forgotten/mixed up letter

<!--endintro-->

In .NET you are allowed to define a custom error page. When a user tries to access a URL which doesn't exist, .NET changes the URL and redirects to the custom error page. The original URL is passed as a parameter to the new URL.

The advantage of this solution is, that the page looks nice and you can customize it according to the design and layout of your whole site.

The disadvantage is, that .NET changes the URL. So if the user wants to correct the URL he entered, for example, because he just mixed up a letter, then this means quite a lot of work for him. He has to retype the whole URL or at least copy and paste the parameter out of the new URL. This is very uncomfortable for the user.


::: bad  
![Figure: Bad example - URL changes](url\_asp.gif)  
:::

Our solution is to show the customized error page while not change the original URL. So if the user wants to do any corrections, e.g. a mixed up letter, he can do that by just editing the URL in the address bar.
The advantages of this solution are, that the site looks nice and matches the design of the whole site and that the user can easily change the original URL he typed.

You can try any page name that doesn't exist like xxx.asp on the URL and it will open our 404 error page. The original URL is not changed in the address bar. It should look like this:


::: good  
![Figure: Good example - Customized 404 error page without change the URL](404-good.jpg)  
:::

In order to show the customized error page while not change the original URL, you can use Server.Transfer() to keep the original URL.



```
Server.Transfer("/ssw/ErrorPage.aspx")
```


 **Figure: Custom error page handler in Global.asax ** 
### Related rule


* [Do you replace the 404 error with a useful error page?](/404-useful-error-page)
