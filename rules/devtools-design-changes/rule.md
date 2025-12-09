---
type: rule
archivedreason:
title: Do you walk through UI changes using DevTools and screen recordings?
seoDescription: Designers often struggle to explain small UI tweaks to developers. Instead of vague messages or screenshots, use DevTools and a short recording to clearly demonstrate the changes.
guid: a7201bd1-965d-4854-877b-25952fb94a74
uri: devtools-design-changes
created: 2025-12-09T18:00:00.000Z
authors:
  - title: Alex Blum
    url: https://www.ssw.com.au/people/alex-blum/
  - title: Tiago Araujo
    url: https://www.ssw.com.au/people/tiago-araujo/
related:
  - change-from-x-to-y
  - do-you-cater-to-your-audience
  - communication-do-you-go-beyond-text-when-using-teams-zoom-skype-chat
  - do-you-use-chrome-devtools-device-mode-to-design-and-test-your-mobile-views
  - css-changes
  - keep-developers-away-from-design-work
  - hand-over-mockups-to-developers
---

Designers often struggle to explain small UI tweaks to developers using just words or screenshots. A request like "make the button pop" or "this feels off" can be interpreted in many ways. Without clear direction, developers are forced to guess, which leads to delays, frustration, and wasted effort on both sides.

Teams at SSW have found that sharing short DevTools recordings significantly reduces design–dev iteration time – sometimes cutting down a 30-minute meeting to a 2-minute video.

<!--endintro-->

### Show, don't tell – record small changes using DevTools

Instead of describing your design tweaks, demonstrate them. Use your browser's DevTools (e.g. Chrome or Edge) to live-edit the UI. Adjust padding, font size, colors, or layout styles directly in the browser. While doing this, record your screen and voice – so the developer can see exactly what you changed and why.

This method gives the developer precise information in context – reducing ambiguity and miscommunication.

::: greybox
The designer sends a Teams message to the developer:\
"Can you make this button look better?"
:::

::: bad
Figure: Bad example – Vague request with no specific guidance. The developer is left guessing what "better" means.
:::

::: greybox
The designer opens DevTools, increases the button padding from 5px to 15px, and changes the background color. They record the change using YakShaver and explain:\
"I'm adding more padding to make it easier to click, and darkening the color for contrast."
:::

::: good
Figure: Good example – The designer demonstrates and explains the change, giving the dev everything they need to implement it.
:::

### Tools that make this easy

* **Browser DevTools (F12)** – Use the "Elements" and "Styles" panels to adjust HTML and CSS on the fly.
* **YakShaver** – An SSW internal tool that records your screen and voice, and generates a task from the recording using AI. Super useful for quick handovers.
* **Microsoft Teams** – Start a meeting with yourself and hit "Record" to capture your screen and voice.
* **Loom / Zoom / OBS** – Any screen recorder works – just keep it short and clear.

> Tip: Don't overcomplicate it – even a 2-minute video can save a lot of back-and-forth.

### Why this works

* **Clarity** – The dev sees the exact change in place, eliminating guesswork.
* **Efficiency** – Avoids multiple rounds of clarification.
* **Precision** – CSS values and HTML structure are visible – no ambiguity.
* **Collaboration** – You're making the dev's life easier (and your own).

---

### When to use this technique

This technique is best for **small, visual changes** like:

* Adjusting padding/margins
* Tweaking text, colors, or spacing
* Changing alignment or hierarchy
* Proposing alternate layout ideas

::: info
**Note:** If your changes are significant (e.g. new components or complex interactions), consider instead:

* Creating a wireframe in Figma
* Prototyping the functionality with AI-assisted code
:::

---

### Bonus tips for designers

| Tip                        | Description |
|---------------------------|-------------|
| **Narrate your intent**   | Speak while recording: *"I'm increasing the font-size from 24px to 32px to improve readability."* |
| **Keep recordings short** | Aim for 1–3 minutes. Focus on one issue per video. |
| **Speak their language**  | Editing in DevTools doesn't require deep coding knowledge, but learning the basics helps a lot. |
| **Be direct**             | Developers love it when designers provide specific, actionable feedback. |
