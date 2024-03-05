---
type: rule
title: "Do you write the word 'email' in the correct format?"
uri: do-you-write-the-word-email-in-the-correct-format
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - spelling-do-you-write-the-word-email-in-the-correct-format
created: 2014-12-17T05:54:22.000Z
archivedreason: Replaced by [https://www.ssw.com.au/rules/avoid-common-mistakes](/rules/avoid-common-mistakes)
guid: acb77e0d-7594-41d6-8dd9-37e687d25e49
---

Do you spell 'email' correctly?

<!--endintro-->

There is one correct way to spell 'email' and many incorrect ones. The common incorrect ones are:

* EMail
* e-mail

Lower Case with dash (or hyphen):

::: greybox
&lt;p&gt;Your <mark>e-mail</mark> address must match your confirm <mark>e-mail</mark> address&lt;/p&gt;

:::

::: bad
Bad example: Using 'e-mail' in your text  
:::

::: greybox
&lt;p&gt;Your <mark>email</mark> address must match your confirm <mark>email</mark> address&lt;/p&gt;

:::

::: good
Good example: Using 'email' instead

:::

Upper Case with capital M:

```html
<input class="form-control" data-val="true" data-val-required="The EMail field is required." id="EMail" name="EMail" placeholder="EMail" type="email" value="" data-cip-id="EMail" autocomplete="off">
```

::: bad
Bad example : 'EMail' used as a placeholder and in the validation message  
:::

```html
<input class="form-control" data-val="true" data-val-required="The Email field is required." id="Email" name="Email" placeholder="Email" type="email" value="" data-cip-id="Email" autocomplete="off">
```

::: good
Good example: Use 'Email' instead

:::

We have a rule in [SSW Code Auditor](https&#58;//www.ssw.com.au/ssw/codeauditor/) and [SSW Link Auditor](https&#58;//sswlinkauditor.com/) to check for this.
