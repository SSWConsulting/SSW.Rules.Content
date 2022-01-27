---
type: rule
archivedreason: Deprecated
title: Do you know how to send newsletter in Microsoft CRM 2013?
guid: 511bb081-084a-49d2-8c58-f64714978ade
uri: do-you-know-how-to-send-newsletter-in-microsoft-crm-2013
created: 2013-03-13T14:14:13.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ulysses Maclaren
  url: https://ssw.com.au/people/ulysses-maclaren
related: []
redirects: []

---

Email newsletters can be sent and responses can be tracked using Microsoft Dynamic CRM 2013:

<!--endintro-->

There is more than one way to distribute a newsletter through CRM, such as through Campaigns and Quick Campaigns. The way detailed below is the simplest method, using Quick Campaigns.

1. Find contacts that you will send the newsletters to. 
      
The first time - use 
       **Advanced Find** in CRM 2013, then save it as a System View. In the example below, we're only interested in New Zealand contacts.
Subsequent times - Use the  **System View** , so everyone is using the same list.

![Figure: From the CRM home screen, hover your mouse over “Workplace”, and then click “Contacts” in the menu that drops down](crm01.png)  

![Figure: From the “Activities” page, click “…” | “Advanced Find”. This will activate a pop-up.](crm02.png)  

![Figure: Select Contacts at Look For and specify a set of criteria to search for newsletter contacts](crm03.png)  

![Figure: then select "Results" to bring up contacts which match your search query](crm04 - results.png)  

![Figure: The result contacts that will get newsletter: these contacts allow us to "Send Marketing Material" and have a New Zealand email address or living country is New Zealand](crm05 - contacts list.png)  
2. First time only, save this as a System View. You will need a SysAdmin for this.
3. Create the newsletter in Microsoft CRM 2013 using a 
             **Quick Campaign** 
![Figure: Select "For All Records on All Pages" to create a Quick Campaign from the current contact list. This will bring up a Quick Campaign Wizard](crm06 - create quick campaign.png)  


![Figure: Click Next and then specify the name of the quick campaign.](crm07 - name quick campaign.png)  

![Figure: Select the Activity Type and Owner.](crm08- own quick campaign.png)  

![Figure: Fill in newsletter content.](crm09 - add content.png)  
    Use your preferred browser to view the content of the newsletter, select all (or use "Ctrl" + "A") and then copy and paste it in the Quick Campaign text area.

![Figure: Highlight the keyword and click the Unsubscribe button to make a link for subscribers to unsubscribe themselves.](crm10 - unsubscribe.png)  
4. Click 
             **Next** to create all email activities in Microsoft CRM 2013.
5. Now you have to wait while the emails send out:
    * **Bad Example - Microsoft CRM Outlook** for outgoing email, then you need to open your Microsoft Outlook, so the email activities can be promoted to Outlook and sent out. This method is slow because of the synchronization process between CRM and Microsoft Outlook and you need to leave outlook open during the entire process.
    * **Bad Example - Email router** for outgoing email, then those email activities will be sent out automatically by Email router. This method is our preferred method of sending the newsletter, CRM email router can be configured to send out newsletters immediately and the user doesn't have to open Outlook while the emails are being processed. As per Crm tip of the day (https://crmtipoftheday.com/979/start-planning-farewell-party-for-email-router/) the email router is now deprecated
    * **Good Example - Server side sync** for outgoing email, then those email activities will be sent out automatically by server side sync. This method is our preferred method of sending the newsletter, CRM Server side sync can be configured to send out newsletters immediately and the user doesn't have to open Outlook while the emails are being processed.
