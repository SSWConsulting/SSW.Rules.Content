---
type: rule
archivedreason: 
title: Customization - Do you enable your contacts to have more than the default 3 email addresses and phone numbers?
guid: 8f91c1c2-5746-4142-b46a-11ef7d2d322b
uri: customization-do-you-enable-your-contacts-to-have-more-than-the-default-3-email-addresses-and-phone-numbers
created: 2012-12-10T20:02:07.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

Out of the box CRM4 only enables a contact to have 3 phone numbers (home, business and mobile) + 3 email addresses (but only one visible). A customization that almost everyone needs is to remove this limitation (to allow contacts to have an unlimited amount of phone numbers and email addresses). 
<!--endintro-->


::: bad  
![Figure: Bad example - Out of the box a contact can only have 3 phone numbers and               1 email address](contact1.jpg)  
:::

There are a few customizations needed to get the SSW Contact Makeover:

* Show some hidden fields
* Make some form changes to move to a new tab
* Make a CRM frame (to add in a subform)
* Add some entities
* Add some form java script to hide the core Contact Details? tab when a user is
            entering a new contact



::: good  
![Figure: Good example - Enable the hidden fields and move it to a new tab. And now               a Contact has 3 email addresses and phone numbers](contact3.jpg)  
:::


::: good  
![Figure: Good example - After adding an entity, you add a frame show the unlimited               contact details (phone, fax, email etc)](contact2.jpg)  
:::

Q: So what is the end result? 
A: The end user experience to add a phone number is ..

![Figure:  Step 1: Double-click the contact (or right-click the contact and               select Open) Open](contact4.jpg)  

![Figure:  Step 2: Select the tab 'More Contact Details'](contact5.jpg)  


![Figure:  Step 3: Click the button 'New Contact Detail'](contact6.jpg)  

![Figure:  Step 4: Enter the details and click button 'Save and Close' (top               left)](contact7.jpg)
