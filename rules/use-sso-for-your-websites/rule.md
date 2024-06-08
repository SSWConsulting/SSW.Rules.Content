---
type: rule
archivedreason: 
title: Do you use SSO (Single sign-on) for your websites?
guid: 00b89044-1873-4acd-87c7-3771c7807dc4
uri: use-sso-for-your-websites
created: 2016-11-11T19:12:04.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-use-sso-single-sign-on-for-your-websites
- do-you-use-sso-(single-sign-on)-for-your-websites

---

Many companies have more than one web applications running under different versions of .NET framework in different subdomains, or even in different domains. They want to let the user sign in once and stay logged in when switching to a different website, and this is SSO (Single Sign-On).

In ASP.NET the logged-in user status is persisted by storing the cookie on the client computer, base on this mechanism, they are two possible solutions:


<!--endintro-->

1. Share one cookie across the web applications. 
The Forms authentication cookie is nothing but the container for forms authentication ticket. The ticket is encrypted and signed using the &lt;machineKey&gt; configuration element of the server's Machine.config file. So if the web applications are hosted on the same machine, the point is to create a shared authentication cookie. Configure the web.config and create the cookie manually can achieve this. 
Following scenarios may suit this solution
    * SSO for parent and child application in the virtual sub-directory
    * SSO for two applications in two sub-domains of the same domain
2. Create its own cookie for each site by calling a page which can create cookie in its own domain. 
If the web applications are hosted on different machine, it is not possibly to share a cookie. In this case each site will need to create its own cookie, call the other sites and ask them to create their own ones. 
Following scenarios may suit this solution.
    * SSO for two applications in different domains
