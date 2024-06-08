---
type: rule
archivedreason: 
title: Do you run Test-SPContentDatabase before migration
guid: 9f201185-9e45-4def-a87c-65471653f57f
uri: run-test-spcontentdatabase-before-actual-migration
created: 2016-05-19T08:05:06.0000000Z
authors:
- title: William Yin
  url: https://ssw.com.au/people/william-yin
related: []
redirects:
- do-you-run-test-spcontentdatabase-before-migration

---

**Assumption:**

1. You have already installed the customized wsp package you know.
2. You have restored the content database to SQL server
3. You haven't attach the content database yet.


It is strongly recommend to run a pre-migration check on the content database before attaching it to trigger the migration process.

<!--endintro-->

 **Steps:** 

1. Run SharePoint PowerShell Console as administrator
2. Run the command below

```bash
Test-SPContentDatabase - name WSS_Content_DB  - webapplication http://sitename
```
3. Check the output log, ensure there isn't any errors.
