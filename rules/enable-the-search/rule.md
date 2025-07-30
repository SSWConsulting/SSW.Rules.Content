---
seoDescription: Enable search functionality in Outlook Web App (OWA) by ensuring Microsoft Exchange Search service is running and configuring the IndexEnabled parameter for the mailbox database.
type: rule
title: Do you enable the search in OWA?
uri: enable-the-search
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T03:40:00.000Z
guid: 0e902951-0ab8-41e2-acfa-8230ddea5ac4
---

If search is not enabled you will get this message in OWA:

::: greybox
"Search results may take a long time to appear because Microsoft Exchange Search is unavailable. Results will not include matches in the email body."
:::

<!--endintro-->

This is how you fix it:

**To diagnose Exchange Search issues**

1. Is the MSExchangeSearch service started on the Mailbox server? If Yes, go to Step 2. If No, use the Services MMC snap-in to verify that the MSExchangeSearch service is running:
   - Click **Start**, and then click **Control Panel**
   - In **Control Panel**, double-click **Administrative Tools**
   - In **Administrative Tools**, double-click **Services**
   - Verify that the **Microsoft Exchange Search Indexer** service is started
2. Is the _IndexEnabled_ parameter configure to true for the mailbox database of the user? Run the following command in the Exchange Management Shell to verify that the _IndexEnabled_ flag is configure to true: **Get-MailboxDatabase |ft Name,IndexEnabled**
3. Run the **Test-ExchangeSearch** command for the user: Test-ExchangeSearch -Identity username[at]ssw.com.au
4. Check Event Viewer for search-related error messages. Check the **Source: MSExchangeSearch Indexer** and **msftesql-Exchange** events. For more information, follow the link on the event log

**To Rebuild the Full-Text Index Catalog Using the ResetSearchIndex.ps1 Script**

1. Start the Exchange Management Shell.
2. _ResetSearchIndex.ps1 -force -all_  
   Wait a couple of minutes to the index be created
3. Run the command to verify if the index was created  
   _GetSearchIndexForDatabase -All_
