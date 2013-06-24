---
type: rule
archivedreason: 
title: Do you use Filtered Views or Fetch for CRM Custom Reports?
guid: 1ae4c974-a66b-4578-8b2f-7e73ebf382c2
uri: do-you-use-filtered-views-or-fetch-for-crm-custom-reports
created: 2012-12-10T18:40:08.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Mehmet Ozdemir
  url: https://ssw.com.au/people/mehmet-ozdemir
related: []
redirects: []

---


<p>
          Directly querying the table bypasses the security and filtering of MSCRM as well
          as not being supported by Microsoft. This​ is not the correct method for reports
          to be written.
          <br>
          The correct filtered views can be found under the Views section of the CRM database
          and these are the Views that should always be used to design SQL Reporting Services
          reports.
        </p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="image">
          <dt>
            <img alt="When developing reports don't go against the base tables - instead use the filtered views of Microsoft CRM 3.0" src="/SoftwareDevelopment/RulesToBetterCRMForDevelopers/PublishingImages/CRM_FilteredView.jpg" />
          </dt>
          <dd>
            Figure&#58; When developing reports don't go against the base tables - instead use the
            filtered views of Microsoft CRM 4</dd></dl><p><span style="color&#58;#000000;text-transform&#58;none;text-indent&#58;0px;letter-spacing&#58;normal;word-spacing&#58;0px;float&#58;none;white-space&#58;normal;display&#58;inline !important;">In CRM 2011 using Filtered Views is enforced with data connector, direct access to tables and other views will be denied.</span></p><dl class="image">
        </dl>



