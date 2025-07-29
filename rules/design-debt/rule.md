---
type: rule
title: Do you know how to avoid design debt?
seoDescription: Making ad-hoc UI changes without a designer leads to design debt. Learn how to prevent inconsistencies and poor UX by following a better workflow.
uri: design-debt
authors:
  - title: Micaela Blank
    url: https://www.ssw.com.au/people/micaela-blank
  - title: Betty Bondoc
    url: https://www.ssw.com.au/people/betty-bondoc
  - title: Tiago Araujo
    url: https://www.ssw.com.au/people/tiago-araujo
created: 2025-04-23T11:45:00.000Z
related:
  - design-system
  - less-is-more
  - request-a-test-please
  - technical-debt
  - underlined-links
archivedreason: null
guid: e0d0ea3b-9b9f-465a-8da8-54f6f7280790
---

It’s tempting to fix small UI issues on the fly - change a button size, adjust some spacing, or tweak a color. But those “quick wins” often turn into long-term losses, leading to a messy, inconsistent UI that confuses users and slows development.

<!--endintro-->

Design debt is like technical debt: shortcuts that seem efficient in the moment create chaos down the line. Without a shared system, visual inconsistencies multiply, developers second-guess design intent, and user experience suffers.

## What causes design debt?

It usually starts with innocent intentions:

* _"Just added a quick icon"_
* _"Tightened the padding a bit"_
* _"Didn't want to bother design - it's small"_

We’ve all done it. But enough of these add up fast. Before you know it, the product starts to feel inconsistent, design is out of sync, and developers redo work they thought was already done.

## Why design debt matters

### 🚨 Why it happens

* Rushed timelines or MVP mindset ("we'll fix it later")
* No shared design system
* Designers and developers working in silos
* Unclear product direction or pivots

### 📉 Why it’s a problem

* Hurts user trust and usability
* Makes the product feel messy or inconsistent
* Slows future development and design
* Causes rework and team friction

### 🧹 How to manage it

* Run regular UX audits and design reviews
* Maintain a living design system or component library
* Include UI refactoring in your roadmap
* Document design decisions with clear rationale

## How to prevent design debt

**Before you code**, ask yourself:

1. **Will users see this change?**

   * **No** → You can proceed without design input
   * **Yes** → Go to Step 2

2. **Is this UI component or pattern already in the [design system](https://www.ssw.com.au/rules/design-system/)?**  

   * **Yes** → Great! Use the existing pattern. You’re done — go ahead and code
   * **No** → This is a new or modified UI — proceed to Step 3

3. **How large is the visual or UX impact?**

   * **Large changes** (e.g. new modal, major layout, navigation shift) → **Create a PBI for a designer to action in the future**

     **Tip:** Tag the PBI as `needs-design` or `minor-UI` depending on impact.

   * **Small changes** (e.g. padding, color tweak, icon alignment) → **You can get a test pass from someone on the Design Masters list**

### More ways to prevent design debt

* Screenshot your change and post it in the PBI before merging
* Ask for a quick "test please" from a designer 👀 on spacing, alignment, and component use
* Loop in design early on bigger stuff (e.g. layout or feature changes)
* After merge, let design know if you created something reusable
  
## Example –  Picking a pretty colour

::: bad
![Figure: Bad example – A light green background is used for the "open" badge. This color doesn’t appear elsewhere in the design and causes low contrast, which affects accessibility. See [Do you use enough color contrast?](/color-contrast)](design-debt-bad.png)
:::

::: good
![Figure: Good example – This issue was flagged with a designer. They used an accessible color and updated the design system to include the missing design component](design-debt-good.png)
:::

## Treat design like code

Every visual tweak changes the product - just like changing a line of code. So follow process, get the right people involved, and respect the system. 🤖
