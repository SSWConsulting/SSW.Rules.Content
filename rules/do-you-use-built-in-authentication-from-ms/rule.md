---
type: rule
archivedreason: This rule has been replaced by [Do you choose the best method of authentication for your situation?](/rules/choose-the-best-method-of-authentication-for-your-situation)
title: '[DEPRECATED] Do you use built in authentication from MS?'
guid: ddcc3cb1-7b5b-402b-ad6d-425efe194a18
uri: do-you-use-built-in-authentication-from-ms
created: 2013-05-02T21:19:33.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- deprecated-do-you-use-built-in-authentication-from-ms

---

Assuming you want:

* Full blown user management
* Nice Controls eg. Login, Change Password
* To be able to implement authentication without a Security Consultant to check

The options are:

<!--endintro-->

### Option 1: ASP.Net Membership provider (original)

Use their ugly table structure.

Resilient to errors/attacks/omissions. "Better the devil you know, than the one you don't".

So if it is simple, straightforward, standardized, integrated well with the existing platform, well documented, and sufficient for your current requirements - why would someone want to go and do something custom?

No OAuth eg. Facebook

### Option 2: [ASP.NET](http&#58;//www.asp.net/) Membership provider (custom)

(Inherits from Option 1)

Typically if you want to use your own database tables (even non SQL)

Easy. A typical implementation of a custom membership or role provider is a simple SELECT query against a database.

Potentially a glorified ValidateUser/GetRoles method.

Little messy if you  **don’t** want full blown user management. Then you must leave a number of NotImplementedException methods (because you are not going to administer the store through the provider). In that case implement a base class, leave 28 methods not implemented, implement ValidateUser that takes two strings and returns a bool ;)

Most clients have more concerns about them making mistakes in the custom security code, that would compromise the security of the application, then about using a bloated existing platform security mechanism correctly (when there are thousands of samples and documentation out there about how to do so correctly).

Yes to OAuth eg. Facebook

Hard to unit test.

### Option 3: Universal provider (Updated ASP.NET Membership provider)

(Inherits from Option 1)

Use their table structure.

The default for VS 2012 Web Forms

Universal Providers are intended for cases where you have an existing ASP.NET Membership Provider and you want to use it with another SQL Server database backend (other than SQL Server).

Yes to OAuth eg. Facebook (out of the box)

### Option 4: SimpleMembershipProvider (New)

(Inherits from Option 1)

Use their table structure.

The default for VS 2012 MVC 4 templates.

Yes to OAuth eg. Facebook (out of the box)

**Note:** If you need to use for Web Forms see [Adding the SimpleMembership provider to an ASP.NET Web Forms app](http&#58;//blogs.msmvps.com/luisabreu/blog/2012/09/24/adding-the-simplemembership-provider-to-an-asp-net-web-forms-app/).

### Option 5: Use “Membership Reboot” on GitHub (a Gurus one) (RECOMMENDED)

A solid, more flexible and open source alternative to the ASP.NET membership provider

Typically if you want to use your own database tables (even non SQL)

**Description:** [Think twice about using MembershipProvider (and SimpleMembership)](http&#58;//brockallen.com/2012/09/02/think-twice-about-using-membershipprovider-and-simplemembership/)

**Source:** [https://github.com/brockallen/BrockAllen.MembershipReboot](https&#58;//github.com/brockallen/BrockAllen.MembershipReboot)

This OSS account management library manages these sorts of things for you:

* PBKDF2 (Proper password storage)
* Password reset
* Account lockout for password guessing
* Account confirmation via email, etc

Bonus:

* It is multi-tenant
* It is claims aware (some complicated security thing from Microsoft that will revolutionize security)

The design is different than ASP.NET Membership in that the security goo is packaged separately from the persistence (the database). You’d not normally need to change the security stuff (though it is extensible).

You implement a repository if you want a custom storage (or you can just use EF and whatever EF-enabled DB you want).

### Option 6: Roll your own

Risk, Risk, Risk... Unless you are a security consultant you are likely to leave a security hole.

Of course you should not roll your own security. This option is building your own authentication and authorization routines to tie into FormsAuth (instead of using providers).

The ASP.NET membership provider is wired in at a deep level in the ASP.NET pipeline. A roll your own solution loses you the benefits of leveraging this integration eg. In Silverlight and the WebAPI

An example of completely removing ASP.NET Membership Providers: [Kicking ASP.NET Providers to the Curb](http&#58;//www.devproconnections.com/article/aspnet2/Kicking-ASP-NET-Providers-to-the-Curb-129584) - And that actually works fine, but with one big, ugly, drawback. The site is able to authenticate and authorize as needed, but you drop in a few .ashx or other things like Elmah, CacheManagement, etc, and then tried to restrict access to them... it obviously is not able to.

**Note:** Gurus use Windows Identity Foundation (and IdentityModel).
