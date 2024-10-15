---
seoDescription: Make check-in policies easier by selecting recent work items using a "Recent" query that returns the last changed work item.
type: rule
archivedreason:
title: Do you know to make using Check-in Policies easier (by adding a 'Recent' Query)?
guid: dcd8280d-f7cc-4609-8c66-c4527955b0dd
uri: do-you-know-to-make-using-check-in-policies-easier-by-adding-a-recent-query
created: 2011-11-18T03:52:51.0000000Z
authors:
  - title: David Klein
    url: https://ssw.com.au/people/david-klein
    noimage: true
  - title: Justin King
    url: https://ssw.com.au/people/justin-king
  - title: Ryan Tee
    url: https://ssw.com.au/people/ryan-tee
    noimage: true
  - title: Tristan Kurniawan
    url: https://ssw.com.au/people/tristan-kurniawan
related: []
redirects:
  - do-you-know-to-make-using-check-in-policies-easier-(by-adding-a-recent-query)
---

When you use Check-in policies you often will need to select a work item that you selected recently

<!--endintro-->

![Figure: When you use Check-in policies you often will need to select a work item that you selected recently](SelectARecentWorkItem.jpg)

Make this easy on yourself by adding a query 'Recent'.

1. Create a work item query that returns you the last changed work item

   ![Figure: Add a query just for your associated check ins](AddQuery.jpg)

2. Just copy the 'Tasks - My' query
3. Add the sort date of 'Changed Date' sorted by descending

   <![Figure: The query should be sorted by 'Changed Date'](SortedByChangedDate.jpg)

4. Use that query on your check ins and you find the relevant work item easily
