---
type: rule
archivedreason: 
title: Do you setup web application for internal and external access
guid: 5724bda1-f138-449a-9a9f-38fb2f9ef752
uri: setup-web-application-for-internal-and-external-access
created: 2016-05-20T06:15:03.0000000Z
authors:
- title: Mark Liu
  url: https://ssw.com.au/people/mark-liu
related: []
redirects:
- do-you-setup-web-application-for-internal-and-external-access

---

- default zone should be over http, this is so search can access it over non-secure connection
- default zone should not be accessible outside of internal network
- extend the web application to an internet zone, this should be https to provide secure connection

- this section should be extended with strategy to work with reverse proxy.

<!--endintro-->

Reverse proxy handle https connection to client, and connects to SharePoint via http to reduce https overhead on SharePoint

SharePoint also needs to support https for internal traffic, if I click on a link to HTTPS it should work internally

For this scenario to work, web application needs to be extended 2 to 3 different zone

**Default**  (http for internal and search)

**Internet**  (http for reverse proxy)

**Intranet**  (https for internal https link)
