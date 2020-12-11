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

Email newsletters can be sent and responses can be tracked using Microsoft Dynamic CRM 2013:

<!--endintro-->

There is more than one way to distribute a newsletter through CRM, such as through Campaigns and Quick Campaigns. The way detailed below is the simplest method, using Quick Campaigns.

1. Find contacts that you will send the newsletters to. <br>      
The first time - use <br>       **Advanced Find** in CRM 2013, then save it as a System View. In the example below, we're only interested in New Zealand contacts.
Subsequent times - Use the  **System View** , so everyone is using the same list.
<dl class="image">&lt;dt&gt; 
         <img src="crm01.png" alt="crm01.png" style="width:600px;"> 
      &lt;/dt&gt;<dd>Figure: From the CRM home screen, hover your mouse over “Workplace”, and then click “Contacts” in the menu that drops down</dd></dl><dl class="image">&lt;dt&gt; 
         <img src="crm02.png" alt="crm02.png" style="width:600px;height:147px;"> 
      &lt;/dt&gt;<dd>Figure: From the “Activities” page, click “…” | “Advanced Find”. This will activate a pop-up.</dd></dl><dl class="image">&lt;dt&gt; 
         <img src="crm03.png" alt="crm03.png" style="margin:0px;width:600px;height:327px;"> 
      &lt;/dt&gt;<dd>Figure: Select Contacts at Look For and specify a set of criteria to search for newsletter contacts<br></dd></dl><dl class="image">&lt;dt&gt; 
               <img src="crm04 - results.png" alt="crm04 - results.png" style="width:600px;height:192px;"> 
            &lt;/dt&gt;<dd>Figure: then select "Results" to bring up contacts which match your search query</dd></dl><dl class="image">&lt;dt&gt; 
               <img src="crm05 - contacts list.png" alt="crm05 - contacts list.png" style="width:600px;height:438px;"> 
            &lt;/dt&gt;<dd>Figure: The result contacts that will get newsletter: these contacts allow us to "Send Marketing Material" and have a New Zealand email address or living country is New Zealand<br></dd></dl>2. First time only, save this as a System View. You will need a SysAdmin for this.
3. Create the newsletter in Microsoft CRM 2013 using a <br>             **Quick Campaign** <dl class="image">&lt;dt&gt; 
                  <img src="crm06 - create quick campaign.png" alt="Create Quick Campaign" style="width:600px;height:438px;"> 
               &lt;/dt&gt;<dd>Figure: Select "For All Records on All Pages" to create a Quick Campaign from the current contact list. This will bring up a Quick Campaign Wizard<br></dd></dl>
<dl class="image">&lt;dt&gt; 
               <img src="crm07 - name quick campaign.png" alt="Specify name of quick campaign" style="width:600px;height:438px;"> 
            &lt;/dt&gt;<dd>Figure: Click Next and then specify the name of the quick campaign.</dd></dl><dl class="image">&lt;dt&gt; 
               <img src="crm08- own quick campaign.png" alt="Select the Activity Type and Owner" style="width:600px;height:438px;"> 
            &lt;/dt&gt;<dd>Figure: Select the Activity Type and Owner.</dd></dl><dl class="image">&lt;dt&gt; 
               <img src="crm09 - add content.png" alt="Fill in newsletter Content" style="width:600px;height:438px;"> 
            &lt;/dt&gt;<dd>Figure: Fill in newsletter content.</dd></dl>    **Attention: SSW Employees** 
You need to follow the instructions in SSW Standards Internal for preparing the newsletter. It's a manual checklist so you don't make any mistakes.
    Use your preferred browser to view the content of the newsletter, select all (or use "Ctrl" + "A") and then copy and paste it in the Quick Campaign text area.
<dl class="image">&lt;dt&gt; 
               <img src="crm10 - unsubscribe.png" alt="Newsletter Ubsubscribe" style="width:600px;height:438px;"> 
            &lt;/dt&gt;<dd>Figure: Highlight the keyword and click the Unsubscribe button to make a link for subscribers to unsubscribe themselves.</dd></dl>4. Click <br>             **Next** to create all email activities in Microsoft CRM 2013.
5. Now you have to wait while the emails send out:
    * **Bad Example - Microsoft CRM Outlook** for outgoing email, then you need to open your Microsoft Outlook, so the email activities can be promoted to Outlook and sent out. This method is slow because of the synchronization process between CRM and Microsoft Outlook and you need to leave outlook open during the entire process.
    * **Bad Example - Email router** for outgoing email, then those email activities will be sent out automatically by Email router. This method is our preferred method of sending the newsletter, CRM email router can be configured to send out newsletters immediately and the user doesn't have to open Outlook while the emails are being processed. As per Crm tip of the day (https://crmtipoftheday.com/979/start-planning-farewell-party-for-email-router/) the email router is now deprecated
    * **Good Example - Server side sync** for outgoing email, then those email activities will be sent out automatically by server side sync. This method is our preferred method of sending the newsletter, CRM Server side sync can be configured to send out newsletters immediately and the user doesn't have to open Outlook while the emails are being processed.
