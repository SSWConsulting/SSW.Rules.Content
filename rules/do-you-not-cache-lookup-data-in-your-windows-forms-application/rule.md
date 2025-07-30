---
seoDescription: Do not cache lookup data in your Windows Forms application to avoid unnecessary database look-ups and minimize potential issues with synchronizing data.
type: rule
title: Do you not cache lookup data in your Windows Forms application?
uri: do-you-not-cache-lookup-data-in-your-windows-forms-application
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T05:36:00.000Z
guid: d6ed5fd4-de1c-4b8e-b3f7-3e86b6ac7a6f
---

To avoid unnecessary database look-ups, many developers cache lookup tables when creating a windows application. There are issue  that can arise as a result, mainly to do with the synching of the lookup data. If the database administrator decides to change the lookup tables, there is bound to be a user online using a static old version of the lookup data. This may result in sql exception, and data corruption.

<!--endintro-->

**Exception #1:** If the application can be taken offline where the users will not access the database for a finite time, then it is recommended that you cache lookup data. However, we do not recommend caching of non-lookup data, i.e. products, clients or invoices.

**Note:** This is a different scenario to complete offline caching; offline caching is recommended and should be implemented (e.g outlook & IE - [Work Offline].  
However, this rule is about combo boxes and list views which contain less than 100 records. There is not much benefit to caching lookup data as there is much more coding involved.

**Exception #2:** If the application contains minor non-critical data. (eg. If you allow the user to customize the text displayed on forms (some people prefer 'Customer' while some prefer 'Client') and this is stored in a database)

Depending on the frequency of this data being changed (and if the change is user dependant), you may want to:

- Low frequency: Place an option to change this data in the application's installation process
- High frequency: Cache the data and provide an option to refresh all cached data or disable caching all together. (e.g menu items View-&gt;'Refresh All' and Tools-&gt;'Options'-&gt;'Disable Caching').

We would love to be proved wrong on this rule. We have 1000s of users on some of our applications, we have tried caching lookup data and we ended up with a lot more code containing exception handling and table refreshing than its benefit.
