---
type: rule
title: Do you use the right character for replaceable text placeholders?
uri: placeholder-for-replaceable-text
authors:
  - title: Aman Kumar
    url: https://www.ssw.com.au/people/aman-kumar
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
created: 2022-07-29T17:13:28.570Z
redirects:
  - how-to-indicate-replaceable-text
guid: 3c146b39-4bb1-4da1-845a-2f4d936d19ec

---

Email templates are an awesome way to help people save time writing emails. Often the template needs to indicate a piece of text that should be replaced with custom content. When you need to identify text that should be replaced (e.g. in an email template), it's important to use a consistent way of indicating the replaceable text with a placeholder.

Use a consistent character to make it clear which piece of text should be substituted.
            
<!--endintro-->

However, everyone has their own preferences about which placeholder character to use 🥸

For example:
- Adam Cogan is used to xxx
- SQL developers are used to [ ]
- Word Mail Merge users are used to « »
- API and React developers are used to { }
- Angular developers are used to {{ }}

Let's see these in action:
- The quick brown fox xxx over the lazy dog
- The quick brown fox [ action ] over the lazy dog
- The quick brown fox « action » over the lazy dog
- The quick brown fox { action } over the lazy dog
- The quick brown fox {{ action }} over the lazy dog

[Angular interpolation uses {{ and }} as a delimiter](https://angular.io/guide/interpolation). They indicate a variable and we think this is a very clear way to indicate that something needs to be replaced because it is very uncommon to see this syntax outside of Angular code.

`[]` are commonly used to label things. On sensitive emails, the text `[Sec: Official]` gets appended or prefixed to the subject, for example.

Using `[]` for replaceable text can be confusing since there is already the common usage for labelling.

So, SSW uses double curly brackets instead of square brackets to indicate replaceable text.

Replaceable text is often seen in email templates:

::: email-template  
|          |     |
| -------- | --- |
| To:      | \[Client email\] |
| Subject: | \[Project name\] - Test please |  
::: email-content  

### Hi \[Client name\],  

I've been working on \[Project name\] and just deployed version \[Version number\] with the latest requirements.

1. Test please - \[Link\]

Regards,  
\[Your name\]
:::  
:::  
::: bad  
Figure: Bad example - Using square brackets for replaceable text
:::

::: email-template  
|          |     |
| -------- | --- |
| To:      | {{Client email}} |
| Subject: | {{Project name}} - Test please |  
::: email-content  

### Hi {{Client name}},  

I've been working on {{Project name}} and just deployed version {{Version number}} with the latest requirements.

1. Test please - {{Link}}

Regards,  
{{Your name}}
:::  
:::  
::: good  
Figure: Good example - Using double curly brackets for replaceable text
:::

