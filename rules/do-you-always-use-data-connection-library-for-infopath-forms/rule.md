---
type: rule
archivedreason: 
title: Do you always use Data Connection Library for InfoPath forms?
guid: ed35bc0a-f67d-4c7a-b6a4-769e97a4f1d2
uri: do-you-always-use-data-connection-library-for-infopath-forms
created: 2009-05-27T14:19:06.0000000Z
authors:
- title: John Liu
  url: https://ssw.com.au/people/john-liu
related:
- do-you-always-set-infopath-compatibility-mode-to-design-for-both-rich-and-web-client-forms
redirects: []

---

SharePoint allows you to create a Data Connection Library to hold all the connection information that Forms and Excel services can utilize.

You should always use a Data Connection Library.

<!--endintro-->

Data Connection Library provides a central location for defining all the connections to various data sources within your company.

* It allows you to change the data source definition in one place, without having to worry about changing the same definition in 50 forms and excel spreadsheets.
* A centralized data connection library also helps your users to locate data easily.
* Your users don't want to know the intricate details on how to get a particular data - they just want the data and have the form working!  So if you as the administrator provides it for them, they will love you, they will use it, and you will have an easier time managing your SharePoint site!

Everyone wins!
