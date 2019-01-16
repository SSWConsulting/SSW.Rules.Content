---
type: rule
title: Do you know the right place to store Employee Data?
uri: do-you-know-the-right-place-to-store-employee-data
created: 2019-01-15T17:52:46.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 69
  title: Jean Thirion
- id: 32
  title: Mehmet Ozdemir

---



<span class='intro'> <p class="ssw15-rteElement-P">​If you use Office 365 products eg. Teams, SharePoint, Exchange then the User Profiles need to be up-to-date.​​<br></p> </span>

<h3 class="ssw15-rteElement-H3">Where should the source of truth be?</h3><p class="ssw15-rteElement-P"><b>A&#58; </b>Simple - If you are happy with just names and address and simple pick lists then User Profiles work great.</p><p>Office 365 User Profile Service is a good tool at managing fields related to users, but it does not offer any functionality to maintain related data such as responsibilities and projects. Therefore it cannot be used as a single source of truth if you have complex profile data. Think of all the stuff you see on LinkedIn. Maybe this will change in the future now that Microsoft owns LinkedIn.<br></p><p class="ssw15-rteElement-P">Eg. &#160;[Diagram of User Profiles &gt; Automatically to Teams, SharePoint etc&#160;<br>Manually to CRM etc</p><p><b>Tip&#58; </b>Keep User Profiles up-to-date with <a href="https&#58;//www.hyperfish.com/">hyperfish.com​</a><br><br><b>B&#58; </b>Rich - If you want richer relationships eg. Many skills, many languages, past projects and roles on them etc. then you want to add a ‘Source of truth’ Eg. CRM, Salesforce etc.<br></p><p class="ssw15-rteElement-P">Companies want bots to answer more than just simple questions. If you have rich data then your bot can answer questions like “Who worked in Education and knows French”</p><p class="ssw15-rteElement-P"><span style="color&#58;#ff0000;">TODO&#58;</span> Therefore companies often need to store related data in CRM and integrate the simplified field information back into User Profile Service.</p><p>This sync engine (integration eg. SSIS pipeline) would need to be written<br>Then other external systems such as the public employee pages, Power BI reports and bots can query CRM directly.<br>Eg. [Diagram of CRM (sync engine) &gt; User Profiles &gt; Teams, SharePoint etc<br></p><p class="ssw15-rteElement-P"><b>Note&#58;</b> you cannot use https&#58;//www.hyperfish.com (as it would be overwritten)​​<br></p><p><b>Note&#58; </b>Delve profile pages can only read from user profiles. Delve is a nice UI over User Profiles, but it should not be mandated to use. You will find it will not be heavily used.</p><p class="ssw15-rteElement-P">Delve is more useful in big companies where the “discovery” aspect is needed.</p><p><br><span style="color&#58;#ff0000;">TODO&#58;&#160;</span>[screenshot of CRM – skills]<br><span style="color&#58;#ff0000;">TODO&#58;</span>&#160;[screenshot of Delve – skills]<br><br><br><br></p>


