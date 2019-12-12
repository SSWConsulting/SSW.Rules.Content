---
type: rule
title: Do you choose the best method of authentication for your situation?
uri: do-you-choose-the-best-method-of-authentication-for-your-situation
created: 2016-05-02T18:27:29.0000000Z
authors:
- id: 81
  title: Jason Taylor
- id: 97
  title: Matt Goldman
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>​​Authentication and authorisation are complicated, and it is risky&#160;to try and implement it yourself.&#160; Use this rule for a guide on choosing the right service or framework for your situation.​​<br></p><dl class="image"><dt>​<img src="/PublishingImages/security-icon-ssw.jpg" alt="security-icon-ssw.jpg" style="width&#58;80px;height&#58;80px;" />​<br></dt></dl> </span>

<p class="ssw15-rteElement-P">​​Choosing the right 
    <a href="https&#58;//www.youtube.com/watch?v=i0d9iTmWIOw">authentication and authorisation</a> approach for your situation can be tricky. It is a multi-facted problem with many variables, and what seems like the right choice in one situation may not be in the other.<br></p><h3 class="ssw15-rteElement-H3">Start with the Questions​​<br></h3><p class="ssw15-rteElement-P"></p><ol><li>Scope -&#160;Is it an enterprise application for internal user&#160;or a consumer application for external use?<br></li><li>Social - Do you need to support 
       <a href="https&#58;//oauth.net/2/">OAuth2</a>&#160;or 
       <a href="https&#58;//openid.net/connect/">OICD</a>?<br></li><li>MFA - Do you need to support 
       <a href="https&#58;//en.wikipedia.org/wiki/Multi-factor_authentication">MFA</a>?<br></li><li>Scope - Do you need to share the identity across multiple applications?</li><li>Volume -&#160;Do you have an estimate for how many users you need to support?​</li></ol><p></p><p class="ssw15-rteElement-P">Without the answers to these questions, it will be difficult to choose the right option. With the answers to these questions, you can use the flow charts below to help you choose the right solution.<br></p><h3 class="ssw15-rteElement-H3"> External Applications<br></h3><p class="ssw15-rteElement-P">
    <br>
 </p><p class="ssw15-rteElement-P">
    <strong> 
       <img src="/PublishingImages/Flow%20Chart%20-%20External.png" alt="Flow Chart - External.png" style="margin&#58;5px;" /> 
       <br></strong></p><p class="ssw15-rteElement-P">
    <strong>Figure&#58; WebAPI (Public facing/consumer Application) - Authentication selection flow chart</strong></p><p class="ssw15-rteElement-P">
    <strong> 
       <br></strong></p><p class="ssw15-rteElement-P"><strong>Example Template to Customer</strong><br></p><p class="ssw15-rteElement-GreyBox">
    <strong>Scenario&#58;</strong><br>Scope - You are building a consumer facing service that will have multiple clients, including a SPA and a mobile app. 
    <br>Social - You want to allow your users to sign up with their social identities (Google, Facebook, Twitter, etc.) but want to allow them to create an account with you if they don't have a social login or don't want to use it. 
    <br>All users will have the same level of access once logged in. 
    <br>Volume -&#160;You anticipate 20,000 active users. 
    <br>MFA - You would like to allow users to enable MFA. 
    <br><br>
    <strong>Your choices&#58;</strong><br><strong>Option A</strong> - Auth0 - Auth0 will meet most of these requirements, however your volume of users will exceed the free tier and you don't need the additional functionality of the paid tier. 
    <br>
    <strong>Option B</strong>&#160;- Azure AD B2C (recommended) - B2C provides all of the functionality you need and is free for up to 50,000 monthly users.<br><strong>Option C</strong>&#160;- Identity Server - This would work but as it doesn't include MFA this would need to be provided via an additional service. Also due to your expected volume of users you would need to manage scaling for this yourself.<br> ​ </p><dd class="ssw15-rteElement-FigureGood">
    <strong>Good Example&#58; The chosen solution meets the requirements<strong></strong></strong></dd> 
 <br>
 <h3 class="ssw15-rteElement-H3"> Internal Applications<br></h3><p class="ssw15-rteElement-P">
    <strong> 
       <br></strong></p><p class="ssw15-rteElement-P">
    <img src="/PublishingImages/Flow%20Chart%20-%20Internal.png" alt="Flow Chart - Internal.png" style="margin&#58;5px;" />
    <br>
 </p><p class="ssw15-rteElement-P">
    <strong>Figure&#58; WebAPI (Internal Enterprise Application) - Authentication selection flow chart</strong><br></p><p class="ssw15-rteElement-P">Note #1&#58; Assuming an ASP.NET Core application with ASP.NET Core Identity<br></p><p class="ssw15-rteElement-P">Note #2&#58; Consider other factors too when making your decision, e.g. cost, potential crossover scenarios, etc.<br></p><p class="ssw15-rteElement-P"><br></p><p class="ssw15-rteElement-P"><strong>Example Template to Customer</strong><br></p><p class="ssw15-rteElement-GreyBox">
    <strong>Scenario&#58;</strong><br>Scope - You have an internal enterprise application, which will support approxiamtely 1,000 users. 
    <br>You already have Active Directory in place, and are syncing with an Azure AD tenant. 
    <br>Your users will need to access this application from anywhere. 
    <br>MFA - As per your company security policy, you must enforce MFA. 
    <br><br>
    <strong>Your choices&#58;</strong><br> 
    <strong>Option A</strong>&#160;- Azure Active Directory (recommended) - most of the infrastructure for this is already in place for you, and it already meets all your requirements. We would just need to wire up your application to it.<br><strong>Option B</strong>&#160;- Active Directory - while your users are already in AD, it doens't give you MFA or access outside your network.<br> 
    <strong>Option C</strong>&#160;- Okta - this is an expensive option which, for this scenario, doesn't provide any advantages over Azure AD.<br> ​ </p><dd class="ssw15-rteElement-FigureGood">
    <strong>Good Example&#58; The chosen solution meets the requirements without adding unnecessary additional costs<strong></strong></strong></dd>
 <br>
 <h3>ASP.NET Core Identity (simple and free)<br></h3><p>ASP.NET Core has some built in identity functionality that allows you to create users and roles, and manage the security of your web applications. It is extremely capable and can be used to support a broad number of scenarios. However, it is intended for use in simple web applications, and while it can be extended to support other clients, you will need to build and wire up a lot of the UI for these scenarios yourself. Your identity store will be limited to this one application, so your users will not be able to users to share this identity across multiple applications.<br></p><p>
    <br>
 </p><dd class="ssw15-rteElement-FigureGood"> Advantages​​&#58;<br></dd><ul><li></li><li>Free</li><li>Easy to set up and use</li><li>Supports OAuth2/OICD providers</li></ul><dd class="ssw15-rteElement-FigureBad"> Disadvantages​​&#58;<br></dd><p></p><ul><li>It is recommended by Microsoft that&#160;for advanced requirements you don't use this on its own - so need to add one of the below</li><li>Does not scale well across multiple applications - so need to add one of the below</li><li>Does not&#160;include&#160;MFA</li><li>For anything other than an ASP.NET Core Web app (e.g. Angular, React&#160;or mobile), you have to build all UI yourself, such as&#58;&#160;<span style="background-color&#58;initial;">sign up, l</span><span style="background-color&#58;initial;">og, p</span><span style="background-color&#58;initial;">assword reset,&#160;e</span><span style="background-color&#58;initial;">tc.</span></li></ul><p class="ssw15-rteElement-P">
    <strong>Use&#160;this option if...</strong>&#160;you need to add identity to a simple application. You can support additional clients (e.g. SPA or mobile) however you will need to wire up a lot of the functionality yourself, which means if vulnerabilities are discovered for your scenario you will need to fix these yourself.​<br></p><p class="ssw15-rteElement-P">
    <br>
 </p><h3 class="ssw15-rteElement-H3" style="background-color&#58;initial;">​Identity Server (full control)</h3><p>
    <a href="https&#58;//identityserver.io/">Identity Server 4</a>&#160;is a free and open source solution that is built on top of ASP.NET Core Identity. It has extensive support for a number of authentication and authorisation scenarios and supports multiple identity providers (OAuth2/OICD) out of the box. ID4 extends ASP.NET Core Identity to natively support multiple client types and can be used as a single identity across multiple applications.</p><dd class="ssw15-rteElement-FigureGood"> Advantages​&#58;<br></dd><ul><li></li><li>Free</li><li>Supports multiple applications/identity consumers</li><li>Supports multiple clients and client types</li><li>Supports OAuth/OICD</li></ul><dd class="ssw15-rteElement-FigureBad"> Disadvantages​​&#58;<br></dd><ul><li></li><li>Steep learning curve<br></li><li>No included MFA</li><li>Requires additional setup​<br></li></ul><div><div class="ms-rtestate-read ms-rte-embedcode ms-rte-embedil ms-rtestate-notify"> 
       <iframe width="760" height="428" src="https&#58;//www.youtube.com/embed/5OUQZAvxZuA?ecver=1" frameborder="0"></iframe>&#160;</div> 
    <br> 
 </div><p class="ssw15-rteElement-P">
    <br>
 </p><p class="ssw15-rteElement-P">
    <b>Use this option if...</b><br></p><ul class="ssw15-rteElement-P"><li>You expect to support multiple clients (e.g. web, mobile etc), and/or&#58;</li><li>​You expect to support multiple applications<br></li></ul><div>
    <br>
 </div><h3>Active Directory (for Internal Enterprise Applications)<br></h3><p>
    <a href="https&#58;//www.google.com/url?sa=t&amp;rct=j&amp;q=&amp;esrc=s&amp;source=web&amp;cd=14&amp;cad=rja&amp;uact=8&amp;ved=2ahUKEwih5qiG2a_mAhU96XMBHXqUBF8QFjANegQIBhAB&amp;url=https&#58;//docs.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview&amp;usg=AOvVaw3F3S9r96_chfuRhAceNFE8">​Active Directory</a>&#160;has been the de facto enterprise identity store for most of the world for decades. Many organisations already have AD as it provides a lot of additional capability and is integrated with most of their existing enterprise applications. AD supports multiple authentication protocols, including&#58;&#160;<br></p><ul><li>LDAP/LDAPS&#58; simple to use but old tech, requires multiple queries to check permissions, roles not natively supported and need to be managed by groups.</li><li>Kerberos&#58; Excellent experience for users as it provides a silent and transparent login. But is a difficult and complex protocol not well understood by many developers and requires complex and difficult setup for both the devs and the sysadmins.<br></li><li>ADFS/SAML&#58; Modern application authentication against AD is done via ADFS with SAML. This is often extended through third party tools such as Okta to support applications that use JWT and claims.<br></li><li>Proprietary Microsoft&#58; Basic, NTLM etc.​<br></li></ul><dd class="ssw15-rteElement-FigureGood">​​Advantages<br></dd><ul class="ssw15-rteElement-P"><li>​​Already in place in most enterprise organisations</li><li>Users do not require an additional identity</li><li>Can make the application compliant with the organisation's existing security policies​<br></li></ul><dd class="ssw15-rteElement-FigureBad">​Disadvantages<br></dd><ul class="ssw15-rteElement-P"><li>​​Not suited to external use</li><li>Can require a lot of setup to work well with company RBAC (e.g. AD groups for authorisation)</li><li>Will require significant developer work to make application roles work with AD groups (if required)</li><li>Not natively supported off-premises​</li><li>No MFA included<br></li></ul><div>
    <strong>Use this option if...</strong><br></div><div><ul><li>Your application, domain controllers and clients are all on the same network, and&#58;<br></li><li>You already have AD in place and have a security policy that states that all your users must authenticate against your centralised corporate identity, and/or&#58;</li><li>You want to enable pass-through/silent authentication for your users​<br></li></ul></div><p></p><h3>Azure AD (for Internal Enterprise Applications)<br></h3><p>
    <a href="https&#58;//www.google.com/url?sa=t&amp;rct=j&amp;q=&amp;esrc=s&amp;source=web&amp;cd=1&amp;cad=rja&amp;uact=8&amp;ved=2ahUKEwiDsL6i2a_mAhXijOYKHR5WAh8QFjAAegQIAxAB&amp;url=https&#58;//azure.microsoft.com/en-au/services/active-directory/&amp;usg=AOvVaw3X8CyXRWZ1KOOeEVYx0ubs">Azure AD</a>&#160;is Microsoft's cloud based version of its traditional on-premises enterprise identity store - Active Directory. Azure AD is different in that it is fundamentally identity only (it doesn't provide endpoint and user management features such as Group Policy) and as such provides strong identity features not natively supported by AD, such as MFA and self-service password recovery. Being cloud based, it can authenticate users anywhere in the world (rather than just on-premises on corporate computers).​<br></p><dd class="ssw15-rteElement-FigureGood">​​Advantages<br></dd><ul class="ssw15-rteElement-P"><li>​​​Many organisations already have AAD</li><li>Extends existing enterprise identity to the cloud (i.e. is supported off-premises)</li><li>Can be used to ensure compliance with existing company security policies</li><li>MFA support included​<br></li></ul><dd class="ssw15-rteElement-FigureBad">​Disadvantages<br></dd><p class="ssw15-rteElement-P"></p><ul><li>​Not suited for external or consumer facing uses</li></ul>
 <strong>Use this option if...</strong><br><strong></strong>
 <p></p><ul class="ssw15-rteElement-P"><li>You want to support internal/enterprise users, and&#58;</li><li>You already have Azure AD set up, and/or&#58;</li><li>Your users require access from off-site, and/or&#58;</li><li>You 
       <strong>need </strong>to enforce MFA​<br></li></ul><div>
    <br>
 </div><h3>Azure B2C (simple Auth as a Service)<br></h3><p>
    <a href="https&#58;//www.google.com/url?sa=t&amp;rct=j&amp;q=&amp;esrc=s&amp;source=web&amp;cd=1&amp;cad=rja&amp;uact=8&amp;ved=2ahUKEwiB4Nmz2a_mAhV14XMBHW6pC7sQFjAAegQIAxAB&amp;url=https&#58;//azure.microsoft.com/en-in/services/active-directory-b2c/&amp;usg=AOvVaw3lcpqnMW7GThYUAYNlGEQu">AAD B2C</a>&#160;sits on top of Azure AD and includes all the benefits it provides, as well as enabling consumer friendly features. These include integration with OAuth2/OICD provider and more flexible/customisable login flows. B2C is well tailored to support authentication, and while it can be extended to support additional capabilities, this requires custom development.​<br></p><dd class="ssw15-rteElement-FigureGood">Advantages<br></dd><ul class="ssw15-rteElement-P"><li>Inexpensive and generous free tier</li><li>Native support for multiple OAuth2/OICD providers</li><li>MFA support included</li><li>Relatively straightforward to setup</li><li>Ongoing security maintained by Microsoft<br></li></ul><dd class="ssw15-rteElement-FigureBad">​Disadvantages<br></dd><ul class="ssw15-rteElement-P"><li>​​Very limited flexibility</li><li>Can support roles and other extended functionality, but requires significant development​<br></li></ul><div>
    <strong>Use this option if...</strong><br>
    <ul><li>You want to support MFA, and/or&#58;<br></li><li>Your users are external/consumers, and&#58;</li><li>You anticipate a high volume of users, and/or&#58;</li><li>You only require basic authentication and limited or no authorisation<br></li></ul><div>
       <br>
    </div></div><h3>Auth0 (sophisticated Auth as a Service)<br></h3><p>
    <a href="https&#58;//www.google.com/url?sa=t&amp;rct=j&amp;q=&amp;esrc=s&amp;source=web&amp;cd=1&amp;cad=rja&amp;uact=8&amp;ved=2ahUKEwjI2-PG2a_mAhXK7XMBHa6-CpAQFjAAegQIEBAC&amp;url=https&#58;//auth0.com/&amp;usg=AOvVaw1vSnM9ruwib43vxq4g0jjS">Auth0</a>&#160;is a commercial identity product aimed at developers. It is cloud hosted and offers out of the box functionality for user signup and login, self-service password recovery, OAuth2/OICD integration, and other consumer and user friendly features. MFA is supported out of the box, and significant sophisticated functionality is available on the paid tiers.​<br></p><dd class="ssw15-rteElement-FigureGood">Advantages<br></dd><p class="ssw15-rteElement-P"></p><ul><li>Good free tier</li><li>Very easy to set up and use</li><li>MFA support included</li><li>Supports multiple OAuth2/OICD providers</li><li>Significant extensibility​</li></ul><dd class="ssw15-rteElement-FigureBad">​Disadvantages<br></dd><ul class="ssw15-rteElement-P"><li>​Free tier is more limited in volume than competition (B2C)<br></li><li>Free tier only includes the&#160;basic functionality (same as B2C)<br></li><li>Free tier only supports 2 social identity providers​<br></li></ul><div>
    <strong>Use this option if...</strong><br><strong></strong>
    <ul><li>You want to enforce MFA, and/or&#58;<br></li><li>Your users are external/consumers, and/or&#58;</li><li>You require authorisation or complex authentication<br></li></ul><div>
       <br>
    </div></div><p></p><h3>Okta (for Commercial Enterprise Applications $)<br></h3><p>
    <a href="https&#58;//www.okta.com/?utm_campaign=search_google_apac_anz_ao_it_branded-okta_exact&amp;utm_medium=cpc&amp;utm_source=google&amp;utm_term=okta&amp;utm_page=%7burl%7d&amp;gclid=EAIaIQobChMI1PKg2tmv5gIVjCQrCh3RHAImEAAYASAAEgLW2fD_BwE">Okta</a>&#160;is a commercial identity product aimed at enterprises. Many enterprise-centric software products, for example Salesforce, have Okta connectors. Okta is intended to bridge the gap between enterprise authentication (such as AD) and modern software and SaaS products.​<br></p><dd class="ssw15-rteElement-FigureGood">​Advantages<br></dd><ul class="ssw15-rteElement-P"><li>​Integrates with anything</li><li>Very well supported in the enterprise</li><li>Can simplify integration with AD​<br></li></ul><dd class="ssw15-rteElement-FigureBad">​Disadvantages<br></dd><ul class="ssw15-rteElement-P"><li>​Expensive</li><li>No free tier</li><li>Not suited to consumer facing scenarios​<br></li></ul><div>
    <strong>Use this option if...</strong><br>
    <ul><li>Your application is for internal/enterprise users, and&#58;</li><li>You already have Okta in place, and/or&#58;</li><li>Your application is a product that you intend to commercialise (Okta is prevalent in the enterprise and having an Okta connector is a good selling point)​<br></li></ul><div>
       <br>
    </div></div><h3>Roll your own (a solution looking for a problem &#58;-) )<br></h3><p>It is entirely possible to create a users table and a roles table in your database and create and manage users yourself.</p><dd class="ssw15-rteElement-FigureGood"> Advantages​​&#58;<br></dd><ul><li>Developers feel like they're ninjas for a little while<br></li><li>Can be a quick and dirty solution to the absolute most basic situation<br></li></ul><dd class="ssw15-rteElement-FigureBad"> ​​Disadvantages&#58;<br></dd><p></p><p></p><p>You have to reinvent the wheel&#58;</p><p>
    <span style="background-color&#58;initial;">&#160; &#160;-&#160;Identity</span></p><p>
    <span style="background-color&#58;initial;">&#160; &#160;-&#160;Roles</span></p><p>
    <span style="background-color&#58;initial;">&#160; &#160;- Email verification</span></p><p>
    <span style="background-color&#58;initial;">&#160; &#160;- Login/Signup/Password reset</span></p><p>
    <span style="background-color&#58;initial;">&#160; &#160;- Claim</span><span style="background-color&#58;initial;">s manag</span><span style="background-color&#58;initial;">ement</span></p><p>Significant risk</p><p>High maintenance overhead</p><p>Masses of technical debt</p>​<strong>Use this option if...</strong><br>
 <ul><li>You want a side project to learn more about how you might roll your own, but of course you know never intend to put it into production &#58;-)​</li></ul><p></p> ​<br><br>​<br>


