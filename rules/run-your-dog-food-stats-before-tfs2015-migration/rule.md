---
type: rule
archivedreason: 
title: Do you run your dog food stats (before TFS 2015 migration)?
guid: db69f69b-a073-4537-908d-52add92cac8a
uri: run-your-dog-food-stats-before-tfs2015-migration
created: 2015-08-12T16:38:41.0000000Z
authors: []
related: []
redirects:
- do-you-run-your-dog-food-stats-(before)1
- do-you-run-your-dog-food-stats-before1

---

Run the excellent DogFoodStats queries:

- For TFS 2010 - from Grant Holliday - [TFS2010: SQL Queries for TFS Statistics](https://web.archive.org/web/20150921185130/http://blogs.msdn.com/b/granth/archive/2009/10/23/tfs2010-sql-queries-for-tfs-statistics.aspx)   .

- For TFS 2012 – update from Erin Dormier -[TFS Internal Usage Statistics – 1st Half CY 2013](https://devblogs.microsoft.com/devops/tfs-internal-usage-statistics-1st-half-cy-2013-2/)

<!--endintro-->

While the above scripts are intended for older versions of TFS, many of the SELECT statements also work with TFS 2013 Update 4.

The above scripts give you some great information about the details of our collections you can use for comparison afterwards.

Make sure you record these statistics so you can compare them after the upgrade.

:::greybox
Recent Users: 33

Users with Assigned Work Items: 145

**Warning: **Null value is eliminated by an aggregate or other SET operation.

Version Control Users: 244

Total Work Items: 20608

Areas and Iterations: 1838

Work Item Versions: 93298

Work Item Attachments: 11331

Work Item Queries: 12768

Files: 694604

Compressed File Sizes: 18042

Uncompressed File Sizes: 36315

Checkins: 53297

Shelvesets: 381

Merge History: 846922

Pending Changes: 906

Workspaces: 259

Local Copies: 4197458

Command Execution Count

Checkin               27

Get                   578

Shelve                96

Upload                162

VCDownloadHandler     1403

GetWorkItem           558

QueryWorkitems        830

Update                272
:::
**Figure: Example result of DogFoodStats on our TFS 2010 instance**
