---
seoDescription: Data migration prioritizes key data imports to ensure a successful transition from legacy systems.
type: rule
archivedreason:
title: Data Migration - Do you prioritize the data that is to be imported?
guid: c227fdd7-a501-4434-ba98-fc53b1c95502
uri: data-migration-do-you-prioritize-the-data-that-is-to-be-imported
created: 2012-12-10T19:27:51.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []
---

### Step 1 - What data?

1. Don't take all the data for the first release - Usually there are huge amounts
   of data in legacy systems - take only the most important firstly.
2. Using the planning spreadsheets included with the [Microsoft CRM Data Migration Pack](https://docs.microsoft.com/en-us/dynamics365/business-central/admin-migrate-customer-data) - they are excellent for specifying data migration
   field mappings.

### Step 2 - Sync or import?

1. Syncing and keeping the old system live is the preferred option
2. Consider writing .NET callouts - or consider Scribe Insight

<!--endintro-->
