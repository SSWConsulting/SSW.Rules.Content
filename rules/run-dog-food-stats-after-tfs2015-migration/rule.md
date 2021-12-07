---
type: rule
archivedreason: 
title: Do you run Dog Food Stats (after) for TFS 2015 migration?
guid: 4eb538fc-5a30-4cc3-9a13-62e0a8ddd9be
uri: run-dog-food-stats-after-tfs2015-migration 
created: 2015-08-13T13:00:01.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-run-dog-food-stats-(after)-(2)
- do-you-run-dog-food-stats-after-2

---

Running the [DogFoodStats](https://devblogs.microsoft.com/bharry/team-foundation-dogfood-stats/) queries over the new TFS 2015 server is a good way to see if the upgrade was successful.

You should check the new values against the [stats you recorded from your TFS 2013 Update 4 databases](/run-your-dog-food-stats-before).

<!--endintro-->

* a. On your TFS 2015 databases, run the DogFoodStats queries and save the results.
* b. Check that the numbers are the same or very close.  Note any big differences.


**Note:**  The numbers may not be identical due to schema changes.

::: greybox
Recent Users
31

Users with Assigned Work Items
144

Version Control Users
244

Total Work Items
20608

Areas and Iterations
1838

Work Item Versions
93300

Work Item Attachments
11332

Work Item Queries
12768

Compressed File Sizes
21230

Uncompressed File Sizes
39504

Checkins
53302

Shelvesets
386

Merge History
846922

Pending Changes
947

Workspaces
259

Local Copies
4197428

CheckIn              164  
Get                  474  
Shelve               63  
Upload               115  
VCDownloadHandler    949  
GetWorkItem          491  
QueryWorkitems       601  
Update               240  

:::
**Figure: Example DogFoodStats after the upgrade**
