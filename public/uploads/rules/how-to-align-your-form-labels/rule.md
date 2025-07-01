---
seoDescription: Discover the pros and cons of top-aligned, left-aligned, right-aligned, and material labeling options for optimal form completion rates.
type: rule
archivedreason: null
title: Do you know how to align form labels?
guid: 968f93bd-a497-41b1-8c49-774a3b182494
uri: how-to-align-your-form-labels
created: 2020-09-16T17:06:51.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Tiago Araujo
    url: https://ssw.com.au/people/tiago-araujo
  - title: Rebecca Liu
    url: https://ssw.com.au/people/rebecca-liu
related: 
  - do-you-know-how-to-arrange-forms
  - data-entry-forms-for-web
  - use-adaptive-placeholders-on-your-forms
redirects:
  - do-you-know-how-to-align-your-form-labels
---

There are different ways to align your form labels and each has its own pros and cons.

<!--endintro-->

## 1. Left-aligned

When labels are left-aligned, the spacing between labels and input fields becomes inconsistent. The excessive visual distance between the labels and their corresponding input fields is a problem.

**✅ Pros**

* Easy to scan labels, especially if you have a lot of optional labels
* Takes a little more attention to fill in, so useful for complicated forms that require accuracy

**❌ Cons**

* Horizontal space, unlike vertical space, is not limitless, and an unintended horizontal scrollbar is the first sin of web development
* Slowest completion times
* Poor multilanguage support
* Not even very good responsive support

::: bad
![Figure: Bad example - Inconsistent spacing between labels and input fields](labels-left-aligned.png)
:::

## 2. Right-aligned

Right-aligning labels ensures a consistent visual distance between the labels and their corresponding fields across the form. This strengthens the association between them, as objects placed closer together are perceived as related.

However, the inconsistent spacing on the left side of the forms makes it harder to scan the fields, leading to user discomfort and slower completion of lengthy forms.

**✅ Pros**

* Best at linking label and form
* Good completion rates on small, common forms (i.e. Login, Sign up)

**❌ Cons**

* Hardest to read and scan
* Poor multilanguage support
* Poor responsive support

::: ok
![Figure: OK example - If aligning labels inline is necessary, opt for right-aligned labels](labels-right-aligned.png)
:::

## 3. Top-aligned

In addition to being more visually appealing, placing labels above the input fields minimizes the visual distance between the label and the input field, creating a stronger cognitive association and enabling faster user response.

The downside of this alignment is that it increases the overall height of the form.

**✅ Pros**

* Easiest to process
* Fastest completion times
* Good for multiple languages

**❌ Cons**

* Takes up a lot of vertical space
* Makes a long-form look even longer

::: ok
![Figure: OK example - Top-aligned labels are space-efficient, making it adaptable to all resolutions](labels-top-aligned.png)
:::

## 4. Adaptive placeholders

[Adaptive placeholders](/use-adaptive-placeholders-on-your-forms) are form labels that become into placeholders and vice-versa, depending on which fields have been filled or not. The placeholder is placed inside the form and slides up on focus and after field is filled. It gives the form a great UX.

**✅ Pros**

* Best for readability
* Best for visual connectivity
* Best for completion rates
* Decent multilanguage support
* Decent responsive support

**❌ Cons**

* Time-consuming to implement. Need to consider the cost/benefit
* Not always available on 3rd party platforms, like Wufoo or Microsoft Forms

::: good
![Figure: Good example - Using adaptive placeholders](adaptative-labels.gif)
:::

---

You can find more useful information and examples in this nice article: [Form design best practices](https://pratikhegde.medium.com/form-design-best-practices-801ceaaf9b67).
