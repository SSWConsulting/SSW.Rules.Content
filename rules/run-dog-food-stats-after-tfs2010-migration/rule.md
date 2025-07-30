---
seoDescription: Check if TFS 2010 migration was successful by running "Dog Food" stats and comparing numbers with previous results.
type: rule
archivedreason:
title: Do you run Dog Food Stats (after TFS 2010 migration)?
guid: e2472404-8058-45f7-96e1-ddb6a8bdb49f
uri: run-dog-food-stats-after-tfs2010-migration
created: 2009-11-08T02:01:52.0000000Z
authors: []
related: []
redirects:
  - do-you-run-dog-food-stats-(after)
  - do-you-run-dog-food-stats-after
---

Running the "Dog Food" stats on your new TFS 2010 server is a good way to see if the upgrade was successful. You should check the new values against the [stats you noted down from your TFS 2008 server](/do-you-run-your-dog-food-stats-before1).

<!--endintro-->

1. On TFS2010, run the DogFoodStats queries and save the results
2. Compare the numbers are the same
   **Note:** Number will differ slightly (usually increases as TFS2010 checks in a few more items)
   **Note:** Grant Holliday has never published exactly why they are not the same.

::: greybox

### TFS2008

-- Files:

1 <mark>28052</mark>

2 <mark>335168</mark>

-- Compressed file size:

11837952896

-- Uncompressed file sizes:

24868196032

-- Areas & Iterations:

<mark>1096</mark>
:::
**Figure: Have a look at the dogfoodstats you ran before**

::: greybox

### TFS2010

-- Areas and Iterations:

<mark>1096</mark>

-- Files:

<mark>347629</mark>

-- Compressed File Sizes:

11296

-- Uncompressed File Sizes:

23723
:::
**Figure: You should get the same number or more for your TFS2010 server. We’re not worried unless it’s slightly less**
