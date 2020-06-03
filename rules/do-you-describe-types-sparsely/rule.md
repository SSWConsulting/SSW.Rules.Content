---
type: rule
title: Do you describe types sparsely?
uri: do-you-describe-types-sparsely
created: 2016-04-28T19:44:54.0000000Z
authors:
- id: 55
  title: Steve Leigh

---



<span class='intro'> <p class="p1">This comes down to personal preference, but there are only a few times when you must define a type in TypeScript, for example&#58;</p><ol class="ol1"><li class="li1">When initializing a variable with an ambiguous value (eg. null)</li><li class="li1">Function parameters​</li></ol><p class="p1">Of course, there are also times when you may want to be more explicit – you may want to have an interface as a function return value instead of the class, for example.​</p> </span>

<p>The rest of the time, rely on TypeScript to infer the type for you.</p><dl class="image"><dt><img src="/PublishingImages/describe.png" alt="describe.png" />​</dt><dd>Figure&#58; Except for the input parameter, TypeScript can infer all the types for this function​</dd></dl>


