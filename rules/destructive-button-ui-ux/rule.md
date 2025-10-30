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
  - enforce-the-text-meaning-with-icons-and-emojis
  - do-you-avoid-ok-buttons-and-use-the-specific-action-as-labels-instead
  - do-you-make-users-intuitively-know-how-to-use-something
created: 2025-10-03T11:52:00.000Z
guid: 5108d3ab-432f-4dbf-8bbf-02065d8661de

---

Accidentally deleting important data can be a disaster for your users and your support team. A poorly placed or unclear destructive action can result in irreversible mistakes, lost data, and frustrated users.

These actions need to be carefully designed with strong visual cues, clear labels, and proper safeguards.

<!--endintro-->

## Use red for danger consistently

Destructive buttons should always stand out with a **red color**. This is a well-established visual convention that immediately signals danger to users.

* Use red **only** for destructive actions (not warnings or generic alerts)
* Avoid using red buttons for neutral or positive actions

::: bad img-medium  
![Figure: Bad example - Wrong color for a destructive button](destruction-button-bad-color.png)
:::

::: good img-medium  
![Figure: Good example - Red is the right color for a destructive button](destruction-button-good-color.png)
:::

::: info
**Note:** If red is your branding primary color, you may use red for positive or neutral actions, as long as:

* The context clearly communicates a positive intent (e.g., “Submit”, “Continue”, “Book now”)
* Consistency is maintained across all UI elements
* Ensure destructive actions are visually differentiated through contrast and hierarchy. E.g. A different tone of red and an appropriate icon
:::

## Use the right icon in the right position

Icons make buttons faster to recognize and reduce ambiguity. A trash can icon next to the label reinforces the nature of the action.

* Always use the trash can (`🗑️`) or appropriate destructive icon
* Place the icon **to the left** of the button label
* Avoid ambiguous or abstract icons (E.g. Broom icon (`🧹`) is used for “clear all” or “clean up", not "delete". Cross icon (`❌`) means “cancel” or "wrong", not "delete")

::: bad  
![Figure: Bad example - Cross icon usually means "Cancel" and should be avoided for permanent deletion. The button is also missing a text label](destruction-button-bad-icon.png)  
:::  

::: good  
![Figure: Good example -  Button has a Trash/Bin icon positioned to the left of the text labe](destruction-button-good-icon.png)
:::

## Position destructive buttons with care

Placing a destructive button next to a primary action (e.g. "Save" or "Confirm") is dangerous. Users may misclick due to proximity.

* Place destructive buttons away from primary actions
* Use space or visual separation between them
* Make destructive buttons less prominent (except when the primary purpose is deletion)

::: bad  
![Figure: Bad example - "Delete" and "Save" are too close together, which can lead to accidental clicks](destruction-button-bad-positioning.png)
:::

::: good  
![Figure: Good example - "Delete" button in red, with the right icon, and visually isolated from safe actions](destruction-button-good-positioning.png)
:::

## Ask for confirmation when necessary

Not every delete action needs a popup, but if the data is important or irreversible, you should ask the user to confirm.

Use confirmations when:

* Deleting data that can’t be recovered (e.g. a database record or user profile)
* The user might not realize the consequences

::: good  
![Figure: Good example - Confirming a destructive action](destruction-button-good-confirmation.png)
:::

::: info
**Tip:** Avoid overusing confirmations as they lead to [alert fatigue](https://www.magicbell.com/blog/alert-fatigue).
:::

## Use tooltips

Sometimes you might have a UI with limited space that doesn’t allow text labels.

For **icon-only** destructive buttons (for example, a red trash icon in a table row), always provide a tooltip on hover or focus.

::: good  
![Figure: Good example - Tooltip gives clarity to an icon-only destructive button](destruction-button-good-tooltip.png)
:::

## Ensure accessibility and keyboard navigation

Don't rely solely on color to convey meaning — red may be hard to distinguish for users with color blindness.

* Include a label, not just an icon
* Make sure buttons can be navigated and triggered via keyboard
* Support screen readers with `aria-label="Delete project"` or similar

---

## Summary of best practices

| **Element**        | **Best practice**                                                 |
|--------------------|-------------------------------------------------------------------|
| **Color**          | Use red for destructive buttons                                   |
| **Label**          | Always include a text label (e.g. "Delete", "Remove")             |
| **Icon**           | Use a trash can or similar, to the left of label                  |
| **Placement**      | Isolate from primary/positive actions                             |
| **Confirmation**   | Use when deletion is permanent or high-risk                       |
| **Accessibility**  | Don't rely on color; support keyboard and screen readers          |

---

For more guidance on destructive actions in UI design:

* [NNG: Confirmation Dialogs Can Prevent User Errors — If Not Overused](https://www.nngroup.com/articles/confirmation-dialog/)
* [Microsoft Design: Commanding Destructive Actions](https://learn.microsoft.com/en-us/windows/apps/design/controls/buttons#destructive-commands)

---

::: greybox

## Bug reports examples

Check out how SSW manages UI bugs across our many products and teams using [YakShaver](https://yakshaver.ai/). Smarter workflows. Fewer distractions.

### 1. For YakShaver - UI Bug

`youtube: https://www.youtube.com/embed/NE2vPXZpRXo`
**Video: ✨ UI Update - Relocate Delete Project Button (1 min)**

* [Watch on YouTube](https://www.youtube.com/watch?v=NE2vPXZpRXo) (1 min)  
* [YakShaver UX Issue \#3034](https://github.com/SSWConsulting/SSW.YakShaver/issues/3034)  

---

### 2. For TinaCMS - UI Bug

`youtube: https://www.youtube.com/embed/VNQhcBZzys0`
**Video: 🐛 Bug - UI Button Color and Behavior Consistency (1 min)**

* [Watch on YouTube](https://www.youtube.com/watch?v=VNQhcBZzys0) (1 min)  
* [TinaCMS UX Issue \#6076](https://github.com/tinacms/tinacms/issues/6076)

:::
