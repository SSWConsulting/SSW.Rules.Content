---
type: rule
archivedreason: 
title: Do you know how to automate event signup processes?
guid: 62526932-5a88-4d38-b130-2079885200ab
uri: do-you-know-how-to-automate-event-signup-processes
created: 2017-02-27T00:36:43.0000000Z
authors:
- title: Ulysses Maclaren
  url: https://ssw.com.au/people/ulysses-maclaren
related: []
redirects:
- how-to-automate-event-signup-processes

---

You should automate signup processes using [Zapier](https&#58;//zapier.com/).




<!--endintro-->

This is the process of a soon-to-be attendee Mr. Northwind signing up for an event:



1. Mr. Northwind visits one of the event pages, e.g. [http://xamarinhackday.com/](http&#58;//xamarinhackday.com/)
2. He presses sign up on [http://xamarinhackday.com/register/](http&#58;//xamarinhackday.com/register/)
3. After selecting a city, he presses register now on [http://xamarinhackday.com/sydney/](http&#58;//xamarinhackday.com/sydney/)
4. He registers for the event on Eventbrite, e.g. [https://www.eventbrite.com/e/xamarin-hack-day-sydney-tickets-20718021159?aff=erelexpmlt](https&#58;//www.eventbrite.com/e/xamarin-hack-day-sydney-tickets-20718021159?aff=erelexpmlt)





This is the according internal process:

1. A Zapier Zap puts his data into a list in Active Campaign and enriches it with tags (e.g. Angular, 2-Day-Angular-Melbourne-Mar-17)
2. Mr. Northwind’s data is sent to a custom web hook receiver (his phone number, email address, full name, and tags are taken from Active Campaign), which adds it to our CRM
