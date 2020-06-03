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



<span class='intro'> <p class="ssw15-rteElement-P">Office 365 products eg. Teams, SharePoint, Exchange use User Profile Service as their source of truth. Therefore, if you use them in your organization, the information needs to be up-to-date.</p><p class="ssw15-rteElement-P">The User Profile is simply a layer of information on top of Active Directory properties. As long as Azure AD is up to date (i.e. in sync with you On-Premises AD), the information in the User Profile Service will also be. You can then add new custom properties to store information such as extra phone numbers or skills coming from a predefined list. &#160;User Profile does not, however, allow complex custom scenarios.<br></p> </span>

<h3 class="ssw15-rteElement-H3">Where should the source of truth be?</h3><p class="ssw15-rteElement-P">
   <b>A&#58; </b>Simple - If you are happy with just names and address and simple pick lists then User Profiles work great.</p><p>Office 365 User Profile Service is a good tool at managing fields related to users, but it does not offer any functionality to maintain related data such as responsibilities and projects. Therefore it cannot be used as a single source of truth if you have complex profile data. Think of all the stuff you see on LinkedIn. Maybe this will change in the future now that Microsoft owns LinkedIn.<br></p><dl class="image"><dt> 
      <img src="/PublishingImages/onpremisesad1.png" alt="onpremisesad1.png" /> 
   </dt><dd>Figure&#58; AD, UserProfile and O365 Services interactions </dd></dl><p>
   <b>Tip&#58; </b>Keep User Profiles up-to-date with 
   <a href="https&#58;//www.hyperfish.com/">hyperfish.com </a>
   <br>
   <br>
   <b>B&#58; </b>Rich - If you want richer relationships eg. Many skills, many languages, past projects and roles on them etc. then&#160;you want to add an external 'Source of truth' Eg. Dynamics 365, Salesforce etc. that supports that kind of relationships.<br></p><p class="ssw15-rteElement-P">Companies want bots to answer more than just simple questions. If you have rich data then your bot can answer questions like &quot;Who worked in Education and knows French&quot;.&#160;This is unfortunately not possible with AD/UserProfile custom fields and properties. In those instances, the alternative is to use Dynamics 365&#160;(or SalesForce) as a single source of truth; and then sync back the data to simple fields in User Profile.​​<br></p><dl class="image"><dt><img src="/PublishingImages/onpremisesad2.png" alt="onpremisesad2.png" /></dt><dd>Figure&#58; CRM (Dynamics 365) used a source of truth</dd></dl>
​In this scenario, a custom sync mechanism (i.e. SSIS pipeline) will have to be implemented. Both Dynamics 365 and User Profile Service exposes APIs that can read and write properties/fields for such a system.<div>Then other external systems such as the public employee pages, Power BI reports and bots can query Dynamics 365&#160;directly.<br><br><p class="ssw15-rteElement-P">
   <b>Note&#58;</b> you cannot use https&#58;//www.hyperfish.com (as it would be overwritten) 
   <br></p><p>
   <b>Note&#58; </b>Delve profile pages can only read from user profiles. Delve is a nice UI over User Profiles, but it should not be mandated to use. You will find it will not be heavily used.</p><p class="ssw15-rteElement-P">Delve is more useful in companies where the “discovery” aspect is needed.</p><p>
   <br>
   <span style="color&#58;#ff0000;">TODO&#58;&#160;</span>[screenshot of Dynamics 365&#160;– skills]<br><span style="color&#58;#ff0000;">TODO&#58;</span>&#160;[screenshot of Delve – skills]​<br></p></div>


