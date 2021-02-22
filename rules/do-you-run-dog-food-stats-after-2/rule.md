---
type: rule
archivedreason: 
title: Do you run Dog Food Stats (After)?
guid: 4eb538fc-5a30-4cc3-9a13-62e0a8ddd9be
uri: do-you-run-dog-food-stats-after-2
created: 2015-08-13T13:00:01.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-run-dog-food-stats-(after)-(2)
- do-you-run-dog-food-stats-after
- do-you-run-dog-food-stats-(after)

---

Running the [DogFoodStats](https&#58;//devblogs.microsoft.com/bharry/team-foundation-dogfood-stats/) queries over the new TFS 2015 server is a good way to see if the upgrade was successful.

You should check the new values against the [stats you recorded from your TFS 2013 Update 4 databases](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=381d8269-1d39-45e2-baea-23c9eff46693).

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

CheckIn                 164
Get                        474
Shelve                    63
Upload                   115
VCDownloadHandler    949
GetWorkItem          491
QueryWorkitems       601
Update               240

:::
 **Figure: Example DogFoodStats after the upgrade
**
