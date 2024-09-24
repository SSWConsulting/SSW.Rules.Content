---
type: rule
title: Do you use the right character for replaceable text placeholders?
uri: placeholder-for-replaceable-text
authors:
  - title: Aman Kumar
    url: https://www.ssw.com.au/people/aman-kumar
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
  - title: Adam Cogan
    url: https://www.ssw.com.au/people/adam-cogan
  - title: Ulysses Maclaren
    url: https://www.ssw.com.au/people/ulysses-maclaren
created: 2022-07-29T17:13:28.570Z
redirects:
  - how-to-indicate-replaceable-text
guid: 3c146b39-4bb1-4da1-845a-2f4d936d19ec

---

Email templates are an awesome way to help people save time writing emails. Often the template needs to indicate a piece of text that should be replaced with custom content. When you need to identify text that should be replaced (e.g. in an email template), it's important to use a consistent way of indicating the replaceable text with a placeholder.

Use a consistent character to make it clear which piece of text should be substituted.
            
<!--endintro-->

`youtube: https://youtu.be/uFLnYo_z6Pw`

**Video: Choose the Best Text Placeholders (3 min)**

However, everyone has their own preferences about which placeholder character to use 🥸

For example:
- SSW Rules historically used xxx
- SSW Intranet | Sales templates use ❌❌❌
- SSW GitHub Sprint Templates use ✏️xxx
- SQL developers are used to [ ]
- Word Mail Merge users are used to « »
- API and React developers are used to { }
- Angular developers are used to {{ }}
- Visual Studio code reviewers are used to TODO:

Let's see these in action:
- The quick brown fox xxx over the lazy dog
- The quick brown fox ❌❌❌ over the lazy dog
- The quick brown fox ✏️xxx over the lazy dog
- The quick brown fox [ action ] over the lazy dog
- The quick brown fox « action » over the lazy dog
- The quick brown fox { action } over the lazy dog
- The quick brown fox {{ action }} over the lazy dog
- The quick brown fox {{ ACTION }} over the lazy dog (currently the standard in SugarLearning and SSW Rules)
- The quick brown fox TODO:action over the lazy dog

### More info on the origins

`[]` are commonly used to label things. On sensitive emails, the text `[Sec: Official]` gets appended or prefixed to the subject, for example.

Using `[]` for replaceable text can be confusing since there is already the common usage for labelling.

{ } are used frequently in popular APIs like [Microsoft Graph](https://learn.microsoft.com/en-au/graph/api/resources/users?view=graph-rest-beta), [Microsoft PowerPlatform](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/samples/webapiservice-query-data) [Facebook](https://developers.facebook.com/docs/marketing-api/conversions-api/using-the-api), [Riot](https://developer.riotgames.com/apis), [Amazon](https://developer-docs.amazon.com/sp-api/docs/product-pricing-api-v0-reference) and also in [React](https://reactjs.org/docs/introducing-jsx.html)

[Angular interpolation uses {{ and }} as a delimiter](https://angular.io/guide/interpolation). They indicate a variable and we think this is a very clear way to indicate that something needs to be replaced because it is very uncommon to see this syntax outside of Angular code.

So, double curly brackets are recommended instead of square brackets to indicate replaceable text.

**In certain places such as Sales templates, you cannot afford to miss a single placeholder**

Of course, if you want to make it even more obvious then highlight the text in yellow... however you can't do it in many places like Microsoft Forms... so another option is to use an emoji like the ✏️ or to make it super obvious the three ❌❌❌

Another way to draw attention to text is to make the placeholder all caps.

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
| To:      | {{ CLIENT EMAIL }} |
| Subject: | {{ PROJECT NAME }} - Test please |  
::: email-content  

### Hi {{ CLIENT NAME }},  

I've been working on {{ PROJECT NAME }} and just deployed version {{ VERSION NUMBER }} with the latest requirements.

1. Test please - {{ LINK }}

Regards,  
{{ YOUR NAME }}
:::  
:::  
::: good  
Figure: Good example - Using double curly brackets for replaceable text... with spaces, and words in UPPERCASE 
:::

