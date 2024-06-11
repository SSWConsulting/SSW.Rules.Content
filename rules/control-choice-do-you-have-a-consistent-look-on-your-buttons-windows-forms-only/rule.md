---
seoDescription: Windows Forms application design best practices emphasize consistent button styles to create a cohesive user experience.
type: rule
archivedreason: Deprecated
title: Control Choice - Do you have a consistent look on your buttons? (Windows Forms Only)
guid: 1179d3e8-bafe-4b3c-b772-f31aa8ab8dfc
uri: control-choice-do-you-have-a-consistent-look-on-your-buttons-windows-forms-only
created: 2012-11-27T08:56:29.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - control-choice-do-you-have-a-consistent-look-on-your-buttons-(windows-forms-only)
---

**Question:** What is wrong with this Picture?

![Figure: What is wrong?](../../assets/InconsistentButtonStyles.jpg)

<!--endintro-->

**Answer:** There are three different types of buttons in the Application:

- _Next &gt;_ - Default Window Style
- _Preview_ - .NET Flat Style
- _Cancel_ - Window XP Style

![Figure: Even labels need to use FlatStyle.System. Can you spot the wrong label?](../../assets/BadDivider.gif)

See our [Rules to Better Windows Forms to implement XP Themes in .NET](http://www.ssw.com.au/ssw/Standards/Rules/RulesToBetterWindowsForms.aspx#XPThemes).
