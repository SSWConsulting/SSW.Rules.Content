---
seoDescription: TypeScript infers types for you most of the time, except when initializing variables or function parameters.
type: rule
archivedreason:
title: Do you describe types sparsely?
guid: 8ee9d1a7-4f85-4548-83fa-13d702b45be4
uri: describe-types-sparsely
created: 2016-04-28T19:44:54.0000000Z
authors:
  - title: Steve Leigh
    url: https://ssw.com.au/people/steve-leigh
related: []
redirects:
  - do-you-describe-types-sparsely
---

This comes down to personal preference, but there are only a few times when you must define a type in TypeScript, for example:

1. When initializing a variable with an ambiguous value (eg. null)
2. Function parameters

Of course, there are also times when you may want to be more explicit – you may want to have an interface as a function return value instead of the class, for example.

<!--endintro-->

The rest of the time, rely on TypeScript to infer the type for you.

![Figure: Except for the input parameter, TypeScript can infer all the types for this function](describe.png)
