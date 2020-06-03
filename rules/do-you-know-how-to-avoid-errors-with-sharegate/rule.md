---
type: rule
title: Do you know how to avoid errors (with Sharegate)?
uri: do-you-know-how-to-avoid-errors-with-sharegate
created: 2018-01-17T23:18:42.0000000Z
authors:
- id: 69
  title: Jean Thirion

---



<span class='intro'> Even if you get rid of unsupported content before migration, your first dry-run migrations are very likely to include errors. Here are the most common errors and how to fix them.<br> </span>

<h3 class="ssw15-rteElement-H3">Document ID Service</h3><p>
   <strong>Error&#58;</strong> Document ID Service feature cannot be automatically activated. Please activate the feature manually from the Site Collection Administration page.</p><p>
   <strong>Solution&#58;</strong> Active Document ID feature on SharePoint online (target).</p><p>
   <strong>Source&#58;</strong> <a href="https&#58;//support.share-gate.com/hc/en-us/articles/115000643448">https&#58;//support.share-gate.com/hc/en-us/articles/115000643448</a></p><h3 class="ssw15-rteElement-H3">MicroFeed</h3><p>
   <strong>Error&#58;</strong> Copying the content from a MicroFeed list is not supported.<br>Copying the content to a MicroFeed list is not supported.</p><p>
   <strong>Solution&#58;</strong> Clean up all “MicroFeed&quot; lists as they are not supported to be migrated to the cloud.</p><p>
   <strong>Source&#58; </strong> <a href="https&#58;//support.share-gate.com/hc/en-us/articles/115000600227">https&#58;//support.share-gate.com/hc/en-us/articles/115000600227</a>&#160;</p><dl class="image"><dt> <img src="/PublishingImages/errors-micro-feed-migration.png" alt="errors-micro-feed-migration.png" style="width&#58;750px;" /></dt><dd>Figure&#58; errors due to micro feed migration</dd></dl> 
<h3 class="ssw15-rteElement-H3">​Lookup fields</h3><p>
   <strong>Error&#58;</strong> Property Receipt&#58; The following values are unavailable&#58; 'XXXXX'. Please specify another value.</p><p>
   <strong>Solution&#58;</strong> Disable circular references for lookup fields.</p><h3 class="ssw15-rteElement-H3">Calculated columns</h3><p>
   <strong>Error&#58;</strong> The formula of a calculated column cannot contain volatile functions like Today and Me.</p><p>
   <strong>Solution&#58;</strong> Remove Calculated columns using “Me&quot; or “Today&quot; markups (unsupported)</p><p>
   <strong>Source&#58;</strong> <a href="https&#58;//support.share-gate.com/hc/en-us/articles/115000600047-The-formula-of-a-calculated-column-cannot-contain-volatile-functions-like-Today-and-Me">https&#58;//support.share-gate.com/hc/en-us/articles/115000600047-The-formula-of-a-calculated-column-cannot-contain-volatile-functions-like-Today-and-Me</a>.</p><h3 class="ssw15-rteElement-H3">External Content Types</h3><p>
   <strong>Error&#58;</strong> Entity (External Content Type) cannot be found with Namespace = 'xxxxxxxxx', Name = 'xxxxx'.</p><p>
   <strong>Solution&#58;</strong> Enable/Configure External Content Types if needed on destination (target) .</p><h3 class="ssw15-rteElement-H3">Orphan users</h3><p>
   <strong>Error&#58;</strong> Property 'xxx'&#58; The following users and groups were not found&#58; XXXXX The current user has been assigned.</p><p>
   <em>OR</em></p><p>Property Target Audiences&#58; The Target Audience 'xxxxxxxxxxxxxx' could not be found.</p><p>
   <strong>Solution&#58;</strong> The error won't stop the migration of the item, but to get rid of it, the missing user needs to be present in target directory (it can be disabled though).</p><h3 class="ssw15-rteElement-H3">Too many Requests</h3><p>
   <strong>Error&#58;</strong> The remote server returned an error&#58; (429).</p><p>
   <strong>Solution&#58;</strong> Re-run content migration migrate them. Big items are likely to give this error multiple times. If this happens, simply use content migration for these specific items on a separate migration task.</p><h3 class="ssw15-rteElement-H3">Custom pages</h3><p>
   <strong>Error&#58;</strong> Warning for version 1.0&#58; Unable to convert WebPart&#58; The content of the WebPart is not in a WebPart Zone for page 'xxxxxxxxxxxxxxxxxxxx'.</p><p>
   <em>OR</em><em>&#160;</em></p><p>
   <strong>Error&#58;</strong> Unable to recover source WebParts&#58; You are not authorized to perform the requested operation.</p><p>
   <em>OR</em></p><p>
   <strong>Error&#58;</strong> This page contains WebParts for which the correct zone could not be found. They have been assigned to the default zone, and may need to be edited manually.</p><p>
   <strong>Solution&#58;</strong> Get rid of SharePoint Designer customization on webpart pages.</p><h3 class="ssw15-rteElement-H3">Managed metadata</h3><p>
   <strong>Warning&#58;</strong> This item has values in managed metadata columns which are not supported by the Insane Mode.</p><p>
   <strong>Solution&#58;</strong> Remove managed metadata on folders.</p><h3 class="ssw15-rteElement-H3">ASPX Pages</h3><p>
   <strong>Warning&#58;</strong> The Insane Mode does not support copying ASPX pages. The copy will continue without using Insane Mode.</p><p>
   <strong>Solution&#58;</strong> you should manually check ASPX pages for errors after migration.</p><p>​<br></p>


