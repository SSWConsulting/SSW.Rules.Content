---
type: rule
archivedreason: 
title: Scheduling - Do you know how to book developers for a project?
guid: 30fa45f9-d065-4f87-ba96-4ad52ae4468b
uri: scheduling---do-you-know-how-to-book-developers-for-a-project
created: 2012-12-06T13:32:15.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 4
  title: Ulysses Maclaren
related: []

---

It is the responsibility of Account Managers to book developers for known client work, however anyone can book a developer, including the developer themselves. Also if a developer notices they should be booked, but there's nothing in their calendar, and they can't figure out the below, as a minimum they should ask the Account Manager to book them.

To book a developer:
<dl class="image">&lt;dt&gt;
      <img alt="Create new appointment in CRM" src="ServiceCalendar2013.jpg" style="width:95%;">
   &lt;/dt&gt;<dd>Figure: Using the Service Calendar, you can see who is and is not available at a given time</dd></dl>
There are a few different ways of booking developers for project work, either via Outlook or the browser.

<!--endintro-->

### Option 1: Use the Outlook Calendar and "Set Regarding" (recommended)

Prerequisite: [https://rules.ssw.com.au/dynamics-crm-install-the-dynamics-365-app-for-outlook](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=31d6b133-8ed2-4ef4-b0b8-33bfebd85d10)

This is generally the easiest way for developers to book themselves in as they don't need to leave outlook and 90% of the steps will already be familiar to them.

1. Create a new Outlook (in the Desktop or Web client) appointment and give it a relevant subject
2. Select required resources if there are other people working with you or if you're booking for someone else
    1. Note: if you're booking for someone else, just have them in the To box of the appointment. If you're booking yourself AND someone else, have both of you in the To box.
3. Set the time and location for your appointment
4. Set the recurrence if it’s more than 1 day of work
5. Click "Dynamics 365" on the ribbon which will open a side panel and click on "Set Regarding" then search select the company that you want to book the developers to work on (this is the step that syncs it with CRM)

<dl class="image">&lt;dt&gt; <img src="Dynamics1.jpg" alt="Dynamics1.jpg" style="margin:5px;width:750px;height:299px;"> <br>&lt;/dt&gt;<dd>Figure: A complete appointment booking Brendan to work for SSW for 5 days</dd><dd><span style="color:#cc4141;font-family:" segoe="" ui",="" "trebuchet="" ms",="" tahoma,="" arial,="" verdana,="" sans-serif;font-size:18px;font-weight:normal;"=""><br></span></dd><dd><span style="color:#cc4141;font-family:" segoe="" ui",="" "trebuchet="" ms",="" tahoma,="" arial,="" verdana,="" sans-serif;font-size:18px;font-weight:normal;"="">Opti</span><span style="color:#cc4141;font-family:" segoe="" ui",="" "trebuchet="" ms",="" tahoma,="" arial,="" verdana,="" sans-serif;font-size:18px;font-weight:normal;"="">on 2: C</span><span style="color:#cc4141;font-family:" segoe="" ui",="" "trebuchet="" ms",="" tahoma,="" arial,="" verdana,="" sans-serif;font-size:18px;font-weight:normal;"="">R</span><span style="color:#cc4141;font-family:" segoe="" ui",="" "trebuchet="" ms",="" tahoma,="" arial,="" verdana,="" sans-serif;font-size:18px;font-weight:normal;"="">M Activity Appointments </span></dd></dl>
This is a backup option for anyone who doesn't have access to Outlook with the CRM add-in.

1. Create new appointment in Dynamics 365 Online

<dl class="ssw15-rteElement-ImageArea"><img src="Dynamics-Calendar-App.jpg" alt="Dynamics-Calendar-App.jpg" style="color:#333333;margin:5px;width:750px;height:348px;"><span style="color:#555555;font-weight:bold;">F</span><span style="color:#555555;font-weight:bold;">i</span><span style="color:#555555;font-weight:bold;">gure: Click Appointment to create a new appointment in CRM</span><span style="color:#555555;font-weight:bold;"><dl class="ssw15-rteElement-ImageArea"><span style="color:#555555;font-weight:bold;"><br></span></dl></span></dl>
1. Set the Subject
2. Select the resources that you want to book
3. Select the client that you want to book the developers to work on
4. Set the location
5. Set the Start and End times
6. If the booking is for more than 1 day, click “Recurrence” and set the frequency


Tip: If you do not want the to block your calendar, you can change the orgainzer and owner to the developer you are booking. It will still track to the Service Calendar, but wont add it to your personal calendar, only the developers.
<dl class="image">&lt;dt&gt; <img src="Dynamics-Appointment.jpg" alt="Dynamics-Appointment.jpg" style="margin:5px;width:750px;height:367px;"> <br>&lt;/dt&gt;<dd>Figure: A complete CRM Appointment for a 1-day booking<br></dd></dl>
### Adding Tentative Bookings


Sometimes you may want to reserve a consultant for an appointment but are not able to confirm with the client immediately. In this case, create a Tentative Booking which reserves the consultant for the period of the booking without assigning them to the client account. The purpose of a Tentative Booking is to reserve a consultant and trigger a conversation between Account Managers if the consultant is required on confirmed client work over the same period.

To create a Tentative Booking:

1. Follow the same steps above to create the Appointment
2. Instead of choosing a client account for 'Set Regarding', choose the company (E.g. "ssw.pencilledin").


**Tip:** Create a "Booked In Days" Report and make the Tentative Bookings display obviously (E.g. A grey color), so Account Managers can easily see it if they need to use that time.

### Adding Internal Bookings


If a developer is needed for non-billable work (E.g. Urgent internal work), or travelling to teach public training events, their time should be blocked out so it shows as unavailable for client work.

To book someone for internal work:

1. Follow the same steps as above to create the Appointment
2. Instead of choosing a client account for "Set Regarding", choose your own company (E.g. "SSW").



![Internally Booked days show as black and Pencilled In days show as grey](2020-03-20_10-49-19.png)


 **
** 

### Using a separate Oulook calendar to book appointments


If you have a lot of staff, it can be useful to use a separate calendar to make your bookings to stop them from covering your every day calendar making it hard to read.

Unfortunately, you cannot use a sub-folder to track appointments in Outlook. You need to create a whole new email account and then add it to your Outlook folder.

For example at SSW we use the account crmtimeprosync@ssw.com.au to add appointments to our Service Calendar, and add them through the SSWBookings calendar in Outlook:
<dl class="ssw15-rteElement-ImageArea"><img src="Appointments tracked from Outlook desktop.png" alt="Appointments tracked from Outlook desktop.png" style="margin:5px;width:700px;height:250px;"> <strong>Figure: Appointments tracked from with Outlook desktop</strong> <br><br></dl>
**How to set it up**
 **For OWA** 
Open browser’s incognito mode | go to https://outlook.office.com | logon with the crmtimeprosync@ssw.com.au account
 
 **For Outlook Desktop** 
     Go to Files | Add an account | Restart Outlook once it completes 
<dl class="ssw15-rteElement-ImageArea"><img src="Add account.jpg" alt="Add account.jpg" style="margin:5px;width:700px;height:204px;"></dl>
**Figure: Add crmtimeprosync@ssw.com.au to your Outlook** 

 **
** 


please note you will need to get the password from your friendly SysAdmins.
