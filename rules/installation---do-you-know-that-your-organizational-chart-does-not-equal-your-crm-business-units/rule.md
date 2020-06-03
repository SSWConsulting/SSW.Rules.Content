---
type: rule
title: Installation - Do you know that your organizational chart does not equal your CRM Business Units?
uri: installation---do-you-know-that-your-organizational-chart-does-not-equal-your-crm-business-units
created: 2012-12-10T17:59:51.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>Usually there is not much point creating an over-complicated organizational structure in MSCRM, a flatter organizational chart will achieve the same end result. Whilst the security model of Microsoft CRM is highly configurable, most organizations do no need to have excessive differentiation of data ownership and hence could cut down on unnecessary work. It is recommended to use the &quot;out of the box&quot; roles for almost all organizations less than 30 users.</p>
                 </span>

<dl class="image">
                    <dt><img alt="Microsoft CRM Default Security Roles are good enough to start with" src="/PublishingImages/CRM-Default-Role.jpg" /></dt>
                    <dd>Figure&#58; Microsoft CRM Default Security Roles are good enough to start with - this is not a thing to stuff with early on</dd>
                </dl>
                <p>First thing first... <strong>never</strong> delete an Out of the Box (OOTB) role. Instead just disable... Period. The reason is it can cause system instability when the only solution can be to start from scratch with a New Organization.</p>
                <p>CRM Roles and Business Units (BUs) are related but quite separate in concept. When designing security roles, there are two schools of thought - job function oriented and functional task oriented. Hybrid model is commonly seen as well.</p>
                <p>BU's don't normally equate to an Organization Chart in real life, and more often than you might realize.</p>
                <p>Considerations when designing BU's&#58;</p>
                <ul>
                    <li>Security</li>
                    <li>Data ownership</li>
                    <li>Operations and collaborations</li>
                    <li>Business functions</li>
                    <li>Geographical locations</li>
                </ul>
                <p>In CRM 2011, two new features help in simplifying security design&#58;</p>
                <ol>
                    <li>Multiple forms per entity can be assigned to different security roles</li>
                    <li>Field level security to add to the next level of security granularity</li>
                </ol>



