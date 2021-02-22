---
type: rule
archivedreason: 
title: Do you know how to avoid errors (with Sharegate)?
guid: 9b82b277-d300-4340-8276-eb496c819e36
uri: how-to-avoid-errors-sharepoint-migration-with-sharegate
created: 2018-01-17T23:18:42.0000000Z
authors:
- title: Jean Thirion
  url: https://ssw.com.au/people/jean-thirion
related: []
redirects:
- do-you-know-how-to-avoid-errors-with-sharegate
- do-you-know-how-to-avoid-errors-(with-sharegate)

---

Even if you get rid of unsupported content before migration, your first dry-run migrations are very likely to include errors. Here are the most common errors and how to fix them.

<!--endintro-->

### Document ID Service

**Error:** Document ID Service feature cannot be automatically activated. Please activate the feature manually from the Site Collection Administration page.

**Solution:** Active Document ID feature on SharePoint online (target).

**Source:** https://support.share-gate.com/hc/en-us/articles/115000643448

### MicroFeed

**Error:** Copying the content from a MicroFeed list is not supported.
Copying the content to a MicroFeed list is not supported.

**Solution:** Clean up all “MicroFeed" lists as they are not supported to be migrated to the cloud.

**Source:** https://support.share-gate.com/hc/en-us/articles/115000600227

![Figure: errors due to micro feed migration](errors-micro-feed-migration.png)  

### Lookup fields

**Error:** Property Receipt: The following values are unavailable: 'XXXXX'. Please specify another value.

**Solution:** Disable circular references for lookup fields.

### Calculated columns

**Error:** The formula of a calculated column cannot contain volatile functions like Today and Me.

**Solution:** Remove Calculated columns using “Me" or “Today" markups (unsupported)

**Source:** https://support.share-gate.com/hc/en-us/articles/115000600047-The-formula-of-a-calculated-column-cannot-contain-volatile-functions-like-Today-and-Me.

### External Content Types

**Error:** Entity (External Content Type) cannot be found with Namespace = 'xxxxxxxxx', Name = 'xxxxx'.

**Solution:** Enable/Configure External Content Types if needed on destination (target) .

### Orphan users

**Error:** Property 'xxx': The following users and groups were not found: XXXXX The current user has been assigned.

*OR*

Property Target Audiences: The Target Audience 'xxxxxxxxxxxxxx' could not be found.

**Solution:** The error won't stop the migration of the item, but to get rid of it, the missing user needs to be present in target directory (it can be disabled though).

### Too many Requests

**Error:** The remote server returned an error: (429).

**Solution:** Re-run content migration migrate them. Big items are likely to give this error multiple times. If this happens, simply use content migration for these specific items on a separate migration task.

### Custom pages

**Error:** Warning for version 1.0: Unable to convert WebPart: The content of the WebPart is not in a WebPart Zone for page 'xxxxxxxxxxxxxxxxxxxx'.

*OR*

**Error:** Unable to recover source WebParts: You are not authorized to perform the requested operation.

*OR*

**Error:** This page contains WebParts for which the correct zone could not be found. They have been assigned to the default zone, and may need to be edited manually.

**Solution:** Get rid of SharePoint Designer customization on webpart pages.

### Managed metadata

**Warning:** This item has values in managed metadata columns which are not supported by the Insane Mode.

**Solution:** Remove managed metadata on folders.

### ASPX Pages

**Warning:** The Insane Mode does not support copying ASPX pages. The copy will continue without using Insane Mode.

**Solution:** you should manually check ASPX pages for errors after migration.
