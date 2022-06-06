---
type: rule
archivedreason: 
title: Do you know how to automate event signup processes?
guid: 62526932-5a88-4d38-b130-2079885200ab
uri: how-to-automate-event-signup-processes
created: 2017-02-27T00:36:43.0000000Z
authors:
- title: Ulysses Maclaren
  url: https://ssw.com.au/people/ulysses-maclaren
related: []
redirects:
- do-you-know-how-to-automate-event-signup-processes

---

You should automate signup processes using [Zapier](https://zapier.com/).

<!--endintro-->

This is the process of a soon-to-be attendee Mr. Northwind signing up for an event:

1. Mr. Northwind visits one of the event pages. E.g. angularhackday.com
2. After selecting a city and date, they press "Register now"
3. Then registers for the event on Eventbrite

This is the according internal process:

1. A Zapier Zap puts his data into a list in Active Campaign and enriches it with tags (e.g. Angular, 2-Day-Angular-Melbourne-Mar-17)
2. Mr. Northwind’s data is sent to a custom web hook receiver (his phone number, email address, full name, and tags are taken from Active Campaign), which adds it to our CRM
