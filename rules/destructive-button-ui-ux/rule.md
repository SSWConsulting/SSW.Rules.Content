---
type: rule
tips: ""
title: Do you follow best practices for destructive buttons in your UI?
seoDescription: Learn the best UI/UX practices for designing destructive
  buttons, including placement, color, icons, confirmation steps, and
  accessibility.
uri: destructive-button-ui-ux
authors:
  - title: ""
related:
  - hamburger-menu
  - null
created: 2025-10-03T11:52:00.000Z
guid: 5108d3ab-432f-4dbf-8bbf-02065d8661de
---
Accidentally deleting important data can be a disaster for your users and your support team. A poorly placed or unclear destructive action can result in irreversible mistakes, lost data, and frustrated users. These actions need to be carefully designed with strong visual cues, clear labels, and proper safeguards.

<!--endintro-->

## Use a consistent color scheme - red for danger

Destructive buttons should always stand out with a **red background color**. This is a well-established visual convention that immediately signals danger to users.

- Use red **only** for destructive actions (not warnings or generic alerts)
- Avoid placing red buttons next to neutral or positive actions without spacing


## Add a trash can icon (or similar)

Icons make buttons faster to recognize and reduce ambiguity. A trash can icon next to the label reinforces the nature of the action.

- Always use the trash can (`🗑️`) or appropriate destructive icon
- Place the icon **to the left** of the button label
- Avoid ambiguous or abstract icons

::: greybox
🗑️ Delete file
:::
::: good  
Figure: Good example - Icon is to the left and clearly reinforces the label
:::

## Position destructive buttons with care

Placing a destructive button next to a primary action (e.g. Save or Confirm) is dangerous. Users may misclick due to proximity.

**Best practices:**

- Place destructive buttons away from primary actions
- Use space or visual separation between them
- Make destructive buttons less prominent (except when the primary purpose is deletion)

::: greybox
[Cancel] [Save Changes] &nbsp;&nbsp;&nbsp; [🗑️ Delete Account]
:::
::: good  
Figure: Good example - Destructive button is separated visually from safe actions
:::

::: greybox
[🗑️ Delete] [Save]
:::
::: bad  
Figure: Bad example - Delete and Save too close together can lead to accidental clicks
:::

## Ask for confirmation — but only when necessary

Not every delete action needs a popup, but if the data is important or irreversible, you should ask the user to confirm.

**Use confirmations when:**

- Deleting data that can’t be recovered (e.g. a database record or user profile)
- The user might not realize the consequences

Avoid overusing confirmations — they lead to **alert fatigue**.

💡 Use specific confirmation messages like:

::: greybox
Are you sure you want to permanently delete this file? This action cannot be undone.
:::

**More from Nielsen Norman Group on this:**  
[NNG - Confirming Destructive Actions](https://www.nngroup.com/articles/destructive-actions/)

## Use tooltips or hover explanations

For icons-only destructive buttons (e.g. a red trash icon in a table), always provide a tooltip on hover or focus.

::: greybox
Hover text: "Delete this row permanently"
:::
::: good  
Figure: Good example - Tooltip gives clarity to an icon-only destructive button
:::

## Ensure accessibility and keyboard navigation

Don’t rely solely on color to convey meaning — red may be hard to distinguish for users with color blindness.

- Include a label, not just an icon
- Make sure buttons can be navigated and triggered via keyboard
- Support screen readers with `aria-label="Delete project"` or similar

## Summary of best practices

| Element              | Best Practice                                                  |
|----------------------|----------------------------------------------------------------|
| Color                | Use red exclusively for destructive buttons                    |
| Icon                 | Use a trash can or similar, to the left of label               |
| Label                | Always include a text label (e.g. "Delete", "Remove")          |
| Placement            | Separate from primary/positive actions                         |
| Confirmation         | Use only when deletion is permanent or high-risk               |
| Accessibility        | Don’t rely on color; support keyboard and screen readers       |

---

For more guidance on destructive actions in UI design:

- [NNG: Confirming Destructive Actions](https://www.nngroup.com/articles/confirmation-dialog/)
- [Material Design: Error & Destructive Actions](https://m3.material.io/foundations/error-handling/overview)
- [Microsoft Design: Commanding Destructive Actions](https://learn.microsoft.com/en-us/windows/apps/design/controls/buttons#destructive-commands)
