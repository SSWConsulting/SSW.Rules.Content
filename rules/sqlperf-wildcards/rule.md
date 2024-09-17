---
seoDescription:  Do you avoid avoid using wildcards at the start of a string?
type: rule
archivedreason:
title: Do you avoid avoid using wildcards at the start of a string?
guid: 55f74e51-c405-40a4-905a-f0f6163c79ee
uri: sqlperf-wildcards
created: 2024-07-25T07:26:54.0000000Z
authors:
  - title: Bryden Oliver
    url: https://ssw.com.au/people/bryden-oliver
related:
  - sqlperf-reduce-table-size
  - sqlperf-select-required-columns
  - sqlperf-verify-indexes-used
  - sqlperf-avoid-implicit-type-conversions
  - sqlperf-use-and-instead-of-or
  - sqlperf-minimise-large-writes
---

Using a wildcard at the start of a string match can cause performance problems with queries. Find out more.

<!--endintro-->

`youtube: https://www.youtube.com/embed/mDWsG3P947E`  
**Video: Avoid wildcards at the start of filters for SQL performance | Bryden Oliver (4 min)**

If you have a table that is indexed on a string column and then you use a query like:

```sql
SELECT * FROM Users WHERE Name LIKE '% Oliver'
```

Then have a think about whether the index can be used to efficiently to find the result.
Unfortunately not, because the index is based on the first letter, then the second letter and so on of the column value. But in this case that's the bit that can be anything.

But there is a simple solution if this is a pattern that your application requires regularly. Basically create a new column (for instance ReverseName) and reverse the text in that column. Then you can write a query like

```sql
SELECT * FROM Users WHERE ReverseName LIKE Reverse('% Oliver')
```

As long as there is an index on the ReverseName column then suddenly this query can use the index to do a seek, dramatically reducing the amount of IO required by the query.
