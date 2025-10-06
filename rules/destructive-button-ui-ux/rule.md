---
type: rule
tips: ""
title: Do you follow best UI practices for destructive buttons?
seoDescription: Learn the best UI/UX practices for designing destructive buttons, including placement, color, icons, confirmation steps, and accessibility.
uri: destructive-button-ui-ux
authors:
  - title: Micaela Blank
    url: https://www.ssw.com.au/people/micaela-blank
  - title: Tiago Araujo
    url: https://ssw.com.au/people/tiago-araujo
related:
  - hamburger-menu
created: 2025-10-03T11:52:00.000Z
guid: 5108d3ab-432f-4dbf-8bbf-02065d8661de

---

Accidentally deleting important data can be a disaster for your users and your support team. A poorly placed or unclear destructive action can result in irreversible mistakes, lost data, and frustrated users. These actions need to be carefully designed with strong visual cues, clear labels, and proper safeguards.

<!--endintro-->

## Use a consistent color - red for danger

Destructive buttons should always stand out with a **red color**. This is a well-established visual convention that immediately signals danger to users.

* Use red **only** for destructive actions (not warnings or generic alerts)
* Avoid using red buttons for neutral or positive actions

::: info
**Note:** If red is your branding primary color, you may use red for positive or neutral actions, as long as:

* The context clearly communicates a positive intent (e.g., “Submit”, “Continue”, “Book now”)
* Consistency is maintained across all UI elements
* Ensure destructive actions are visually differentiated through contrast and hierarchy. E.g. A darker red, outlined button, and an appropriate icon.
:::

## Use the right icon in the right position

Icons make buttons faster to recognize and reduce ambiguity. A trash can icon next to the label reinforces the nature of the action.

* Always use the trash can (`🗑️`) or appropriate destructive icon
* Place the icon **to the left** of the button label
* Avoid ambiguous or abstract icons

::: greybox
[Delete file 🧹]
:::
::: bad  
Figure: Bad example - Broom icon is used for “clear all” or “clean up,” not delete single item + is on the right  
:::

::: greybox
[❌ Delete file]
:::
::: bad  
Figure: Bad example - Cross icon should be avoided for permanent deletion, as it usually means “cancel”
:::

::: greybox
[🗑️ Delete file]
:::
::: good  
Figure: Good example - Trash/Bin icon clearly reinforces the label + is on the left  
:::

## Position destructive buttons with care

Placing a destructive button next to a primary action (e.g. "Save" or "Confirm") is dangerous. Users may misclick due to proximity.

* Place destructive buttons away from primary actions
* Use space or visual separation between them
* Make destructive buttons less prominent (except when the primary purpose is deletion)

::: greybox
[🗑️ Delete] [Save]
:::
::: bad  
Figure: Bad example - Delete and Save too close together can lead to accidental clicks
:::

::: greybox
[Cancel] [Save] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [🗑️ Delete Account]
:::
::: good  
Figure: Good example - Destructive button is separated visually from safe actions
:::

## Ask for confirmation when necessary

Not every delete action needs a popup, but if the data is important or irreversible, you should ask the user to confirm.

Use confirmations when:

* Deleting data that can’t be recovered (e.g. a database record or user profile)
* The user might not realize the consequences

💡 Use specific confirmation messages like:

::: greybox
Are you sure you want to permanently delete this file? This action cannot be undone.
:::
::: good  
Figure: Good example - Confirming a destructive action
:::

::: info
**Tip:** Avoid overusing confirmations — they lead to [alert fatigue](https://www.magicbell.com/blog/alert-fatigue).
:::

## Use tooltips or hover explanations

For icons-only destructive buttons (e.g. a red trash icon in a table), always provide a tooltip on hover or focus.

::: greybox
**Hover text:** "Delete this row permanently"
:::
::: good  
Figure: Good example - Tooltip gives clarity to an icon-only destructive button
:::

## Ensure accessibility and keyboard navigation

Don't rely solely on color to convey meaning — red may be hard to distinguish for users with color blindness.

* Include a label, not just an icon
* Make sure buttons can be navigated and triggered via keyboard
* Support screen readers with `aria-label="Delete project"` or similar

---

## Summary of best practices

| Element              | Best Practice                                                  |
|----------------------|----------------------------------------------------------------|
| Color                | Use red for destructive buttons                                |
| Label                | Always include a text label (e.g. "Delete", "Remove")          |
| Icon                 | Use a trash can or similar, to the left of label               |
| Placement            | Isolate from primary/positive actions                          |
| Confirmation         | Use when deletion is permanent or high-risk                    |
| Accessibility        | Don't rely on color; support keyboard and screen readers       |

---

For more guidance on destructive actions in UI design:

* [NNG: Confirmation Dialogs Can Prevent User Errors — If Not Overused](https://www.nngroup.com/articles/confirmation-dialog/)
* [Material Design: Error & Destructive Actions](https://m3.material.io/foundations/error-handling/overview)
* [Microsoft Design: Commanding Destructive Actions](https://learn.microsoft.com/en-us/windows/apps/design/controls/buttons#destructive-commands)
