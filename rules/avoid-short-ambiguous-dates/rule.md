---
type: rule
tips: ""
title: Do you avoid short or ambiguous dates?
seoDescription: Prevent confusion and tampering by avoiding short or ambiguous date formats. Always use full numbers for day, month, and yeay
uri: avoid-short-ambiguous-dates
authors:
  - title: Harkirat Singh
    url: https://github.com/0xharkirat
related:
  - dates-do-you-keep-date-formats-consistent-across-your-application
created: 2025-09-11T12:20:00.000Z
guid: 050f797a-c163-45f2-bc5e-f6820688eb8e
---
If you sign a document and write a date like `2/2/12`, you’ve unintentionally left the door open for someone to modify it. That date could easily be turned into `12/12/2012`, or something else entirely — and you’d never know. It's a small habit, but writing dates properly can prevent fraud, confusion, and embarrassment.

<!--endintro-->

### Always use full numbers:

✅ Use: `12/02/2012`  
✅ Better: `2012-02-12` (ISO standard)

### ❌ Avoid short or ambiguous formats:

- `2/2/12` – vulnerable to tampering and misreading
- `8/9/25` – is that August 9th or September 8th?
- `2/3` – you’re not doing yourself any favors

::: greybox
Signed: 2/2/12
:::
::: bad
Figure: Bad Example – Anyone can change this to say something completely different, e.g. 12/12/2012
:::

::: greybox
Signed: 12/02/2012
:::
::: good
Figure: Good Example – Two-digit day/month and four-digit year removes ambiguity and protects integrity
:::

### Format for clarity and integrity

- **Day:** Always two digits (`01` to `31`)
- **Month:** Always two digits (`01` to `12`)
- **Year:** Always four digits (e.g. `2025` – unless you're from the future after year 9999)

> A document is only as reliable as the details on it. Don't let a shortcut make it questionable.

This rule isn't just about style — it's about **trust**. Whether it's a legal contract, client invoice, or project brief, using full numeric dates ensures:

- The date can't be easily altered
- Readers across regions (US, AU, EU) understand it clearly
- The document remains valid long into the future

Take the extra 3 seconds — it’s worth it.
