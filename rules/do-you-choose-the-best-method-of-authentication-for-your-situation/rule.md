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



<span class='intro'> <p>Authentication and authorization are complicated, and it is dangerous to try and implement it yourself.&#160; Use this rule for a guide on choosing the right service or framework for your situation.​​<br></p><dl class="image"><dt>​<img src="/PublishingImages/security-icon-ssw.jpg" alt="security-icon-ssw.jpg" style="width&#58;80px;height&#58;80px;" />​<br></dt></dl> </span>

<h3>Simple and free</h3><p>If you're looking for a free solution, and most of your users already have an account with either Facebook, Google, Twitter,&#160;Microsoft or WeChat, then an easy solution is to simply use these services for your authentication. ​They all provide some external authentication endpoint, either using OpenId Connect or OAuth2.</p><dd class="ssw15-rteElement-FigureGood">
   Advantages​​&#58;<br></dd><ul><li>Free</li><li>Simple to set up</li><li>Good user experience – often a one-click sign in</li><li>Plenty of documentation out there</li></ul><dd class="ssw15-rteElement-FigureBad">
   Disadvantages​​&#58;<br></dd><ul><li>People must have an account with an external service</li><li>No control over accounts or signup process</li><li>Profile management can be​ tricky – do you use Google's display name or your own?</li></ul><h3>Simple, managed as a service</h3><p>There are providers out there which offer server identities and access control.</p><dd class="ssw15-rteElement-FigureGood">
   Advantages​​​&#58;<br></dd><ul><li>Much more control of access control and user profiles</li><li>Quick and easy to set up, with plenty of samples</li><li>Support</li></ul><dd class="ssw15-rteElement-FigureBad">
   Disadvantages​&#58;<br></dd><ul><li>Costs money for more advanced features</li><li>Externally hosted, which may not be desired in some enterprises</li></ul><p>There are several providers to choose from – here are some of the more popular ones. Be sure to choose ones that fit your situation, as they each have different levels of compliance, features, support, and pricing.</p><ul><li><b>Auth0</b> (first 7,000 users free) – <a href="https&#58;//auth0.com/">https&#58;//auth0.com​</a><br></li><li><b>Azure AD B2C</b><b></b> (first 50,000 users free) - <a href="https&#58;//azure.microsoft.com/en-au/services/active-directory-b2c/">https&#58;//azure.microsoft.com/en-au/services/active-directory-b2c​</a><br></li></ul><div>Azure AD B2C is the best choice in terms of pricing and is generally the default choice when using AD on premise. Review the associated <a href="https&#58;//azure.microsoft.com/en-au/case-studies/?term=B2C">case studies</a> for additional information.​<br></div><h3>Active Directory</h3><p>It's not uncommon for an organization to already be using LDAP, and IIS can supply windows identities out of the box. It's quick and easy to set up, but not very powerful and often all-or-nothing.</p><dd class="ssw15-rteElement-FigureGood">
   Advantages​&#58;<br></dd><ul><li>Good user experience</li><li>No management of users required at all</li><li>Leverages existing user storage</li><li>Companies like to use their Active Directory accounts everywhere</li></ul><dd class="ssw15-rteElement-FigureBad">
   Disadvantages​&#58;<br></dd><ul><li>Role-based authorization can be difficult as the Active Directory API isn't simple&#160;</li><li>Can be slow, depending on AD setup</li></ul><h3 class="ssw15-rteElement-H3">Full control</h3><p>The above options are about delegating identity access and authorization to another party, which may not be a good fit for your enterprise.&#160; If full control over everything is required, then going with <a href="https&#58;//github.com/IdentityServer/IdentityServer3">Identity Server</a>&#160;for authentication and&#160;<a href="https&#58;//docs.microsoft.com/en-us/aspnet/core/security/authentication/identity?view=aspnetcore-3.0&amp;tabs=visual-studio">ASP.NET Core Identity​</a>&#160;for user storage is the best idea.&#160; It does all the heavy lifting, allowing secure, robust and configurable storage of identities with industry standard authentication schemes.&#160; The best part is you don't have to be a security consultant to implement it – though it is a good idea to have a solid understanding of security principals.</p><dd class="ssw15-rteElement-FigureGood">
   Advantages​&#58;<br></dd><ul><li>On-premises</li><li>Highly configurable</li><li>Uses industry-standard best practices for security</li></ul><dd class="ssw15-rteElement-FigureBad">
   Disadvantages​​&#58;<br></dd><ul><li>Steep learning curve</li><li>Takes a lot of development time to implement well</li><li>Requires vigilance to keep up-to-date to ensure any security issues are addressed as soon as they're raised<br></li></ul><div><div class="ms-rtestate-read ms-rte-embedcode ms-rte-embedil ms-rtestate-notify">
      <iframe width="760" height="428" src="https&#58;//www.youtube.com/embed/5OUQZAvxZuA?ecver=1" frameborder="0"></iframe>&#160;</div>
   <br>
</div><h3>Roll your own</h3><p>One of the more common options for enterprises is to try and roll their own implementation.&#160;This usually results in poor security and difficult to maintain code.</p><dd class="ssw15-rteElement-FigureGood">
   Advantages​​&#58;<br></dd><ul><li>Developers feel like they're ninjas for a little while</li></ul><dd class="ssw15-rteElement-FigureBad">
   ​​Disadvantages&#58;<br></dd><ul><li>Insecure&#160;</li><li>Developers stop feeling like ninjas when they realize how complicated it is</li><li>High-maintenance&#160;</li><li>Quickly turns into code that everyone wants to avoid</li><li>Very expensive to develop and maintain</li><li><strong>Insecure</strong> – this needs to be mentioned again. Security is <em style="line-height&#58;1.6;">very</em> difficult to do correctly and best left to experts<br></li></ul>


