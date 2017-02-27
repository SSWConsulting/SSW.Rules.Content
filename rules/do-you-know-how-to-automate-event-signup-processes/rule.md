---
type: rule
title: Do you know how to automate event signup processes?
uri: do-you-know-how-to-automate-event-signup-processes
created: 2017-02-27T00:36:43.0000000Z
authors:
- id: 4
  title: Ulysses Maclaren

---



<span class='intro'> At SSW we automate signup processes using <a href="https&#58;//zapier.com/">Zapier</a>.<br> </span>

<p>This is the process of&#160;a&#160;soon-to-be attendee&#160;Mr. Northwind signing up for a SSW event&#58;<br></p><p></p><ol><li>Mr. Northwind visits one of SSW’s event pages, e.g. <a href="http&#58;//xamarinhackday.com/">http&#58;//xamarinhackday.com/</a><br></li><li>He presses sign up on <a href="http&#58;//xamarinhackday.com/register/">http&#58;//xamarinhackday.com/register/</a><br></li><li>After selecting a city, he presses register now on <a href="http&#58;//xamarinhackday.com/sydney/">http&#58;//xamarinhackday.com/sydney/</a><br></li><li>He registers for the event on Eventbrite, e.g. <a href="https&#58;//www.eventbrite.com/e/xamarin-hack-day-sydney-tickets-20718021159?aff=erelexpmlt">https&#58;//www.eventbrite.com/e/xamarin-hack-day-sydney-tickets-20718021159?aff=erelexpmlt​</a><br></li></ol><div><br></div><p class="ssw15-rteElement-P">This is the according SSW internal process&#58;<br></p><ol><li>A Zapier Zap puts his data into a list in Active Campaign and enriches it with tag​s&#160;(e.g.&#160;Angular, 2-Day-Angular-Melbourne-Mar-17)<br></li><li>Mr. Northwind’s data is sent to a custom web hook​ receiver​ (his phone number, email address, full name, and tags are taken from Active Campaign), which adds it to our CRM<br></li></ol><br><p></p>


