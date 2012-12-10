---
type: rule
title: Customization - Do you enable your contacts to have more than the default 3 email addresses and phone numbers?
uri: customization---do-you-enable-your-contacts-to-have-more-than-the-default-3-email-addresses-and-phone-numbers
created: 2012-12-10T20:02:07.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> Out of the box CRM4 only enables a contact to have 3 phone numbers (home, business and mobile) + 3 email addresses (but only one visible). A customization that almost everyone needs is to remove this limitation (to allow contacts to have an unlimited amount of phone numbers and email addresses). </span>

 <dl class="badImage">
          <dt>
            <img border="0" src="/SoftwareDevelopment/RulesToBetterCRMForDevelopers/PublishingImages/contact1.jpg" alt="" />
          </dt>
          <dd>Figure&#58; Bad example - Out of the box a contact can only have 3 phone numbers and
              1 email address</dd>
        </dl>
        <p>
          There are a few customizations needed to get the SSW Contact Makeover&#58;
        </p>
        <ul>
          <li>Show some hidden fields </li>
          <li>Make some form changes to move to a new tab </li>
          <li>Make a CRM frame (to add in a subform) </li>
          <li>Add some entities </li>
          <li>Add some form java script to hide the core Contact Details? tab when a user is
            entering a new contact </li>
        </ul>

        <dl class="goodImage">
          <dt>
            <img border="0" src="/SoftwareDevelopment/RulesToBetterCRMForDevelopers/PublishingImages/contact3.jpg" alt="" />
          </dt>
          <dd>Figure&#58; Good example - Enable the hidden fields and move it to a new tab. And now
              a Contact has 3 email addresses and phone numbers </dd>
        </dl>
        <dl class="goodImage">
          <dt>
            <img border="0" src="/SoftwareDevelopment/RulesToBetterCRMForDevelopers/PublishingImages/contact2.jpg" alt="" />
          </dt>
          <dd>Figure&#58; Good example - After adding an entity, you add a frame show the unlimited
              contact details (phone, fax, email etc)
          </dd>
        </dl>
        <p>
          <span>Q&#58; So what is the end result? </span>
          <br>
          <span>A&#58; The end user experience to add a phone number is .. </span>
          <br>
        </p>
        <dl class="image">
          <dt>
            <img border="0" src="/SoftwareDevelopment/RulesToBetterCRMForDevelopers/PublishingImages/contact4.jpg" alt="" />
          </dt>
          <dd>Figure&#58;&#160; Step 1&#58; Double-click the contact (or right-click the contact and
              select Open) Open</dd>
        </dl>

        <dl class="image">
          <dt>
            <img border="0" src="/SoftwareDevelopment/RulesToBetterCRMForDevelopers/PublishingImages/contact5.jpg" alt="" />
          </dt>
          <dd>Figure&#58;&#160; Step 2&#58; Select the tab 'More Contact Details' </dd>
        </dl>
        <br>
        <dl class="image">
          <dt>
            <img border="0" src="/SoftwareDevelopment/RulesToBetterCRMForDevelopers/PublishingImages/contact6.jpg" alt="" />
          </dt>
          <dd>Figure&#58;&#160; Step 3&#58; Click the button 'New Contact Detail' </dd>
        </dl>
        <dl class="image">
          <dt>
            <img border="0" src="/SoftwareDevelopment/RulesToBetterCRMForDevelopers/PublishingImages/contact7.jpg" alt="" />
          </dt>
          <dd>Figure&#58;&#160; Step 4&#58; Enter the details and click button 'Save and Close' (top
              left) </dd>
        </dl>



