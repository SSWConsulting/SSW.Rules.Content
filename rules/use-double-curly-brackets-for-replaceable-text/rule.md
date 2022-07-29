---
type: rule
title: Do you use double curly brackets for replaceable texts?
uri: how-to-indicate-replaceable-text
authors:
  - title: Aman Kumar
    url: https://www.ssw.com.au/people/aman-kumar
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
created: 2022-07-29T17:13:28.570Z
guid: 3c146b39-4bb1-4da1-845a-2f4d936d19ec
---
Use double curly brackets instead of square brackets for replaceable texts.
            
<!--endintro-->

Angular uses `{{}}` to indicate a variable and we think this is a very clear way to indicate that something needs to be changed because it is very uncommon to see this syntax outside of angular code.

`[]` are used to label things. E.g. On sensitive emails, the text `[Sec: Official]` gets appended or prefixed to the subject.

So people may get confused since there are two different meanings.

### Email Template  
::: email-template  
|          |     |
| -------- | --- |
| To:      | \[Client email\] |
| Subject: | \[Project name\] - Test please |  
::: email-content  

### Hi \[Client name\],  

I've been working on \[Project name\] and just deployed \[Version number\] with the latest requirements.

1. Test please - \[Link\]

Regards,  
\[Your name\]
:::  
:::  
::: bad  
Figure: Bad example - Using square brackets for replaceable texts
:::

### Email Template  
::: email-template  
|          |     |
| -------- | --- |
| To:      | {{Client email}} |
| Subject: | {{Project name}} - Test please |  
::: email-content  

### Hi {{Client name}},  

I've been working on {{Project name}} and just deployed {{Version number}} with the latest requirements.

1. Test please - {{Link}}

Regards,  
{{Your name}}
:::  
:::  
::: good  
Figure: Good example - Using double curly brackets for replaceable texts
:::

