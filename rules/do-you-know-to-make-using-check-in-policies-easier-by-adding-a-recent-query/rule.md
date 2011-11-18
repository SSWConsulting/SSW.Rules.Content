---
type: rule
archivedreason: 
title: Do you know to make using Check-in Policies easier (by adding a 'Recent' Query)?
guid: dcd8280d-f7cc-4609-8c66-c4527955b0dd
uri: do-you-know-to-make-using-check-in-policies-easier-by-adding-a-recent-query
created: 2011-11-18T03:52:51.0000000Z
authors:
- id: 22
  title: David Klein
- id: 5
  title: Justin King
- id: 17
  title: Ryan Tee
- id: 6
  title: Tristan Kurniawan
related: []

---


This field should not be null (Remove me when you edit this field).
<br><excerpt class='endintro'></excerpt><br>
<dl><dt><img alt="Select A Recent Work Item" src="/TFS/RulesToBetterVersionControlwithTFS(AKASourceControl)/PublishingImages/SelectARecentWorkItem.jpg" /></dt>
<dd>Figure&#58; When you use Check-in policies you often will need to select a work item that you selected recently </dd></dl>
<ol>Make this easy on yourself by adding a query 'Recent' <li>Create a work item query that returns you the last changed work item <dl><dt><img alt="Add a query" src="/TFS/RulesToBetterVersionControlwithTFS(AKASourceControl)/PublishingImages/AddQuery.jpg" /></dt>
<dd>Figure&#58; Add a query just for your associated check ins </dd></dl></li>
<li>Just copy the 'Tasks - My' query </li>
<li>Add the sort date of 'Changed Date' sorted by descending <dl><dt><img alt="Sorted the query by 'Changed Date' " src="/TFS/RulesToBetterVersionControlwithTFS(AKASourceControl)/PublishingImages/SortedByChangedDate.jpg" /></dt>
<dd>Figure&#58; The query should be sorted by 'Changed Date' </dd></dl></li>
<li>Use that query on your check ins and you find the relevant work item easily </li></ol>



