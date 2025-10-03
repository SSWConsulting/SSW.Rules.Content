---
seoDescription: Make your website WCAG compliant to ensure equal access for all users, regardless of abilities or navigation methods.
type: rule
archivedreason:
title: Do you make your website WCAG compliant?
guid: 853e4258-83f4-4aad-b333-e8449cf7f239
uri: wcag-compliance
created: 2023-12-22T05:06:33.0000000Z
authors:
  - title: Jayden Alchin
    url: https://www.ssw.com.au/people/jayden-alchin/
  - title: Josh Berman
    url: https://www.ssw.com.au/people/josh-berman/
  - title: Luke Cook
    url: https://www.ssw.com.au/people/luke-cook/
related:
  - descriptive-links
  - color-contrast
  - seo-tools
redirects: []
---

The internet has become a part of daily life, but not everyone uses it in the same way. **Web Content Accessibility Guidelines (WCAG)** are a set of formal standards aimed to address this problem.

Accessibility isn't just about compliance - it's about improving the usability of your product for everyone. Whilst essential for people with permanent sensory, motor, or cognitive impairments, it also improves the experience for users with temporary or situational limitations.

<!--endintro-->

Making your website accessible ensures equal access, better usability, and improved SEO.

`youtube: https://www.youtube.com/watch?v=QWPWgaDqbZI`
**Video: The Internet's Accessibility Problem - and How to Fix It (13 min)**

## An overview of WCAG standards

The [Web Content Accessibility Guidelines](https://www.w3.org/WAI/standards-guidelines/wcag/) are international standards developed by the WW3C's Web Accessibility Initiative (WAI). They define how to make web content more accessible to people with disabilities.

These guidelines are constantly reviewed and updated to make the web a more accessible place. Each version release has its own focus, and moves with evolving technologies. The current latest set of guidelines is the [WCAG 2.2](https://www.w3.org/TR/WCAG22/), released in December 2024.

## The 4 principles (POUR)

WCAG consists of 4 high-level principles. Each principle is broken down into a number of sub-criteria.

### 1. Perceivable

Information must be presented in a way users can perceive:

* **Text Alternatives (1.1):** Provide text alternatives for non-text content
* **Time-based Media (1.2):** Provide alternatives and captions for multimedia and time-based content
* **Adaptable (1.3):** Present content in different ways without losing information or structure
* **Distinguishable (1.4):** Making it easier for users to see and hear content, including separating foreground from background (E.g Color contrast - [Do you meet color contrast requirements for accessibility?](/rules/color-contrast/))

### 2. Operable

User Interface components and navigation must be operable:

* **Keyboard Accessible (2.1):** Ensure all functionality can be operated via a keyboard
* **Enough Time (2.2):** Provide users enough time to read and complete tasks
* **Seizures and Physical Reactions (2.3):** Do not design content that is known to cause seizures or physical discomfort
* **Navigable (2.4):** Create a navigable and intuitive user interface
* **Input Modalities (2.5):** Ensure compatibility with input methods beyond just a keyboard

### 3. Understandable

Information and the operation of the user interface must be understandable:

* **Readable (3.1):** Make content readable and understandable
* **Predictable (3.2):** Create a consistent and predictable user interfaces
* **Input Assistance (3.3):** Help users avoid and correct errors

### 4. Robust

Content must be robust enough that it can be interpreted by a wide variety of user agents, including assistive technologies:

* **Compatible (4.1):** Optimize compatibility with current and future technologies

## WCAG accessibility example

Suppose we want to create a simple button on our site.

::: bad
![Figure: Bad example - Lacks accessibility](./bad-example-accessibility.png)
:::

This fails numerous guidelines:

* **Criteria 2.1.1:** Not operable by keyboard
* **Criteria 4.2.1:** No accessible role/ name (for screen readers)
* **Criteria 1.3.1:** Using div for a button breaks semantic structure

::: good
![Figure: Good example - Correct accessibility](./good-example-accessibility.png)
:::

Improving on the previous example, this button passes:

* **Criteria 2.1.1:** Keyboard focus and activation are built-in
* **Criteria 4.1.2:** The button role and label are exposed to assistive tech
* **Criteria 1.3.1:** Correct semantic element conveys structure and purpose

## Conformance Levels

WCAG defines three levels of conformance to these guidelines: A, AA, and AAA. They stack - meaning each higher level includes all requirements of the one below it.

* **Level A** is a must-have
* **Level AA** is a should-have (common target)
* **Level AAA** represents maximized accessibility

## How can you improve accessibility?

| Role       | Actions |
|------------|---------|
| **Designers**  | - Use accessible colour palettes and check contrast ratios (4.5:1 minimum for body text)<br>- Ensure font sizes are readable<br>- Clearly indicate focus states<br>- Design with text alternatives in mind |
| **Developers** | - Write semantic HTML (e.g., `<button>` not `<div>` for buttons)<br>- Use ARIA only when necessary<br>- Ensure full keyboard navigation<br>- Maintain logical tab order |
| **Testers**    | - Run automated checks (axe, Lighthouse)<br>- Test with keyboard only<br>- Test with a screen reader (NVDA, VoiceOver)<br>- Verify form error handling |

## Tools for testing accessibility

### Lighthouse

Lighthouse is an automated auditing tool by Google that runs inside Chrome Devtools to check a website's performance, accessibility, best practices, and SEO. It's automated accessibility checks are based on WCAG, and it uses rules from axe-core.

It is best used for performance and accessibility review before release. Although it only covers ~20-30% of accessibiltiy checks because many need manual testing.

![Figure: Lighthouse in DevTools](./lighthouse-in-devtools.png)

### axe DevTools

Similarly, axe DevTools is a browser extension and testing toolkit powered by axe-core, using the same accessibility engine used in Lighthouse. It is used to find and fix accessibility issues during development. However, unlike lighthouse, it allows guided and manual testing for things automation can't fully check (e.g., meaningful ink text, focus order, screen reader experience).

![axe DevTools Example](./axe-devtools-example.png)

## Key terms

The following are some key concepts that can help make WCAG easier to understand.

* **WCAG versioning** - The guidelines are updated at irregular intervals so it's important to be clear which version you're referencing. E.g. [WCAG 2.2.](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22)
* **Success criteria** - Each WCAG principle contains sub-categories which themselves contain specific success criteria. This means when you reference a success criterion it will have a number like "2.4.1: Bypass Blocks"
* **WAI-ARIA** (Web Accessibility Initiative - Accessible Rich Internet Applications) - A specification of semantic requirements for assistive technologies like screen readers
