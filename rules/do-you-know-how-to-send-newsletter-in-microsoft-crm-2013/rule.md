---
type: rule
archivedreason: 
title: Do you know how to send newsletter in Microsoft CRM 2013?
guid: 511bb081-084a-49d2-8c58-f64714978ade
uri: do-you-know-how-to-send-newsletter-in-microsoft-crm-2013
created: 2013-03-13T14:14:13.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 4
  title: Ulysses Maclaren
related: []

---


<p>​​​Email newsletters&#160;can be sent and responses can be tracked using Microsoft Dynamic CRM 2013&#58;<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p>There is more than one way to distribute a newsletter through CRM, such as through Campaigns and Quick Campaigns. The way detailed below is the simplest method, using Quick Campaigns.&#160;</p><ol><li>Find contacts that you&#160;will send the newsletters to. 
      <br>The first&#160;time - use 
      <strong>Advanced Find</strong> in CRM 2013, then save it as a System View. In the example&#160;below, we're only interested in New Zealand contacts.<br><span style="line-height&#58;21px;">Subsequent times -&#160;Use the&#160;</span><span style="line-height&#58;21px;"><strong>System View</strong></span><span style="line-height&#58;21px;">, so everyone is using&#160;</span><span style="line-height&#58;21px;">the same list</span><span style="line-height&#58;21px;">.</span><span style="line-height&#58;21px;"> </span>
      <br></li><dl class="image"><dt> 
         <img src="/PublishingImages/crm01.png" alt="crm01.png" style="width&#58;600px;" /> 
      </dt><dd>Figure&#58; From the CRM home screen, hover your mouse over “Workplace”, and then click “Contacts” in the menu that drops down</dd></dl><dl class="image"><dt> 
         <img src="/PublishingImages/crm02.png" alt="crm02.png" style="width&#58;600px;height&#58;147px;" /> 
      </dt><dd>Figure&#58; From the “Activities” page, click “…” | “Advanced Find”. This will activate a pop-up.</dd></dl><dl class="image"><dt> 
         <img src="/PublishingImages/crm03.png" alt="crm03.png" style="margin&#58;0px;width&#58;600px;height&#58;327px;" /> 
      </dt><dd>Figure&#58; Select Contacts at Look For and specify a set of criteria to search for newsletter contacts<br></dd></dl>
         <dl class="image"><dt> 
               <img src="/PublishingImages/crm04%20-%20results.png" alt="crm04 - results.png" style="width&#58;600px;height&#58;192px;" /> 
            </dt><dd>Figure&#58; then select &quot;Results&quot; to bring up contacts which match your search query</dd></dl><dl class="image"><dt> 
               <img src="/PublishingImages/crm05%20-%20contacts%20list.png" alt="crm05 - contacts list.png" style="width&#58;600px;height&#58;438px;" /> 
            </dt><dd>Figure&#58; The result contacts that will get newsletter&#58; these contacts allow us to &quot;Send Marketing Material&quot; and have a New Zealand email address or living country is New Zealand<br></dd></dl><li>​First time only, save this as a System View. You will need a SysAdmin for this.</li><li>Create the newsletter in Microsoft CRM 2013 using a 
            <strong>Quick Campaign</strong>
            <dl class="image"><dt> 
                  <img src="/PublishingImages/crm06%20-%20create%20quick%20campaign.png" alt="Create Quick Campaign" style="width&#58;600px;height&#58;438px;" /> 
               </dt><dd>Figure&#58; Select &quot;For All Records on All Pages&quot; to create a Quick Campaign from the current contact list. This will bring up a Quick Campaign Wizard<br></dd></dl></li><dl class="image"><dt> 
               <img src="/PublishingImages/crm07%20-%20name%20quick%20campaign.png" alt="Specify name of quick campaign" style="width&#58;600px;height&#58;438px;" /> 
            </dt><dd>Figure&#58; Click Next and then specify the name of the quick campaign.</dd></dl><dl class="image"><dt> 
               <img src="/PublishingImages/crm08-%20own%20quick%20campaign.png" alt="Select the Activity Type and Owner" style="width&#58;600px;height&#58;438px;" /> 
            </dt><dd>Figure&#58; Select the Activity Type and Owner.</dd></dl><dl class="image"><dt> 
               <img src="/PublishingImages/crm09%20-%20add%20content.png" alt="Fill in newsletter Content" style="width&#58;600px;height&#58;438px;" /> 
            </dt><dd>Figure&#58; Fill in newsletter content.</dd></dl><p class="ssw15-rteElement-SSW-Only">
            <strong>Attention&#58; SSW Employees</strong><br>You need to follow the&#160;instructions in SSW Standards Internal for preparing the newsletter. It's a manual checklist so you don't make any mistakes.<br></p> ​ 
         <p>Use your preferred browser&#160;to view the content of the newsletter, select all (or use &quot;Ctrl&quot; + &quot;A&quot;)&#160;and then&#160;copy and paste it in the Quick Campaign&#160;text area.<br></p><dl class="image"><dt> 
               <img src="/PublishingImages/crm10%20-%20unsubscribe.png" alt="Newsletter Ubsubscribe" style="width&#58;600px;height&#58;438px;" /> 
            </dt><dd>Figure&#58; Highlight the keyword and click the&#160;Unsubscribe button to make a link for subscribers to unsubscribe themselves.</dd></dl><li>Click 
            <b>Next</b> to create all email activities in Microsoft CRM 2013.</li><li>Now you have to wait while the emails send out&#58;
            <ul><li>
                  <b>Bad Example -&#160;Microsoft CRM Outlook</b> for outgoing email, then you need to open your Microsoft Outlook, so the email activities can be promoted to Outlook and sent out. This method is slow because of the synchronization process between CRM and Microsoft Outlook and you need to leave outlook open during the entire process.</li><li>
                  <b>Bad Example - Email router</b> for outgoing email, then those email activities will be sent out automatically by Email router. This method is our preferred method of sending the newsletter, CRM email router can be configured to send out newsletters immediately and the user doesn't have to open Outlook while the emails are being processed.&#160;​As per Crm tip of the day (<a href="https&#58;//crmtipoftheday.com/979/start-planning-farewell-party-for-email-router/">https&#58;//crmtipoftheday.com/979/start-planning-farewell-party-for-email-router/ </a>) the email router is now deprecated<br></li><li>​<strong>Good Example - Server side sync&#160;</strong>&#160;for outgoing email, then those email activities will be sent out automatically by server side sync. This method is our preferred method of sending the newsletter, CRM Server side sync&#160;can be configured to send out newsletters immediately and the user doesn't have to open Outlook while the emails are being processed.<br></li></ul></li></ol>


