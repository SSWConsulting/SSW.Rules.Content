---
type: rule
title: Do you know Blazor doesn't support stopping event propogation?
uri: blazor-does-not-support-stopping-event-propogation
authors:
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
created: 2022-08-17T18:40:42.796Z
guid: 8744a176-c690-43a2-abd8-6a48ab0725b5
---
Workaround - When you have two fields and you want to handle tabbing out of the last one to do some stuff and save.

* If you handle onkeydown the value isn't set yet
* If you handle onkeyup it triggers on the first field instead of the last one

<!--endintro-->

To solve the issue change the binding to `@bind:event="oninput"` so the value is captured before key down. 

The reason is due to the problem outlined in [Keyup event behavior on tab](https://stackoverflow.com/questions/18020098/keyup-event-behavior-on-tab).

There are various workarounds such as using eventPropogation in JavaScript: [Catching TAB key press with keyup](https://stackoverflow.com/questions/37144885/catching-tab-key-press-with-keyup).

However, eventPropogation is not supported in Blazor as per [this comment on Compiler support for @oneventname:preventDefault and @oneventname:stopPropagation](https://github.com/dotnet/aspnetcore/issues/14517#issuecomment-559184498)

So, to prevent this issue an OnInput binding lets the value be set before the keydown event is triggered.

This workaround can cause unexpected side effects if you have a custom setter so you shouldn't do that in tandem with this.
