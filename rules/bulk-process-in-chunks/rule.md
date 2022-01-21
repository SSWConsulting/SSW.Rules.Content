---
type: rule
title: Do you bulk process in chunks?
uri: bulk-process-in-chunks
authors:
  - title: Bryden Oliver
    url: https://www.ssw.com.au/people/bryden-oliver
created: 2021-12-13T17:26:26.666Z
guid: c2b997a9-0119-4360-80bb-744c9f5b0f84
---
Databases are slow at doing bulk updates. It's generally significantly faster to break bulk processing down into manageable chunks. It also avoids other database users experiencing significant blocking issues.

<!--endintro-->

Linq include the Chunk method to make this process nice and easy.

```
var productIds = context.ProductIds;
foreach(var chunk in productIds.Chunk(10))
{
    // Do stuff
}
```