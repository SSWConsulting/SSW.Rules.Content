---
type: rule
title: General - Standards Watchdog - Do you help everyone to learn the rules?
uri: general---standards-watchdog---do-you-help-everyone-to-learn-the-rules
created: 2009-03-10T07:08:39.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> ​​​​​​​​&quot;An ounce of prevention is worth a pound of cure&quot; goes the saying. Having a strict coding standard is prevention. To create good code you must have good standards, such as commenting standards, naming standards, versioning standards and more. 
<br> </span>

<dl class="image"><dt> <img src="/PublishingImages/fb339f_Watchdog.jpg" alt="Watchdog.jpg" style="margin&#58;5px;width&#58;380px;height&#58;243px;" /> </dt><dd> Figure&#58; Be a fearsome Standards Watchdog</dd><p>Every member of a team plays an important role in maintaining standards. Whether it's my code or someone else's, I always keep an eye out for mistakes.</p><p>When I come across an error, I never just fix it, as the developer who made it is likely to make it again. I write an email to the person explaining what has been done wrong and how to do the right thing. I CC the manager so they are aware of the situation.</p><p>Of course, with everyone doing this in the office, it's not a matter of finger pointing, we all truly work together to write better code.</p>When you notice someone doing the wrong thing<ul><li>First time just send an email with a pointer to the rule</li><li>Second time, have a very quick chat with them</li><li>Third time call them in and give them a formal talk about it</li></ul><p>If you don't have the confidence to talk to the person, send an email from info. The important thing is to talk about it at the time.&#160;</p><p>Clearly, this standard does not just apply to writing better code, it applies to <strong>all company standards</strong>. Standards are important because they ensure your experience at work is consistent and enjoyable. For example, if there was no standard to stack the dishes in the dishwasher when you were finished using them, dishes would build up and create a big mess in the kitchen!</p><p>Equally important is your responsibility to ensure that others are doing their best to maintain and follow the standards. Remember,&#160;It can be just as important for someone’s professional development to give feedback as it is to receive it. Being able to communicate feedback in an&#160;effective and professional manner can benefit you in any career.&#160;<br><br></p><p class="ssw15-rteElement-GreyBox"><b>To&#58;</b> Peter<br><b>CC&#58;</b> Adam (Manager)<br>​<br>Dear Peter,<br><br>While you were away, I came across a page called ApplicationForm.aspx which was giving an error&#58;&#160;<br>'The conversion of a char data type to a&#160;datetime&#160;data type resulted in an out-of-range&#160;datetime&#160;value.'&#160;<br>This happened when I entered '13/06/2002' into&#160;a the&#160;'Start Date' field of the form.<br>The error occurs because you are not using the default language of the server which is 'English' - for the users of this database FRDC. This is the same as US English format of Months first, then Days, then a four digit Year (mm/dd/yyyy). Instead, you used 'British English' on the FRDC database which has a format of dd/mm/yyyy. Please use the standard as per&#160;Rules to Better SQLServer Databases, Rule 1200 (Middle Tier Section)<br>Please note that whilst inserting data from your Front End application, you should not use the format dd/mm/yyyy.&#160;Instead&#160;you should use&#160;yyyy/mm/dd<br><br>Let's fix it together when we get to work tomorrow.<br><br>Cheers, DDK</p> <br></dl><dd class="ssw15-rteElement-FigureNormal"> Figure&#58; Make sure you let your client know if you find a standards violation</dd>


