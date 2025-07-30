---
seoDescription: Pedantic approach to button design improves user experience and accessibility by providing mnemonics for easy navigation.
type: rule
archivedreason:
title: Being Pedantic - Do your buttons have a mnemonic?
guid: 5efb94c3-e91f-4a8c-87ba-b1bc76edf533
uri: being-pedantic-do-your-buttons-have-a-mnemonic
created: 2012-11-27T09:25:36.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []
---

A mnemonic for a button is the letter which has an underscore, and the user can press the button using `Alt-<char>`.

<!--endintro-->

::: bad  
![Figure: Bad example - All buttons without Mnemonic](../../assets/BadMem.gif)  
:::

::: good  
![Figure: Good example - All buttons with Mnemonic - user can easily choose which button they want without a click](../../assets/GoodMem.gif)  
:::

In Windows Applications, it is quite easy to assign a mnemonic to a button with the "&" character.

So for the case above, the text would be:

```cs
btnAbout.Text = "&About"
```

::: info
Learn more about the [Mnemonic property on Windows Desktop](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.label.usemnemonic?view=windowsdesktop-7.0&WT.mc_id=WDIT-MVP-33518).
:::
