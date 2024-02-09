---
type: rule
archivedreason: Replaced by [https://www.ssw.com.au/rules/design-web-pages-to-work-on-mobile-and-tablets-screens-aka-responsive-web-design](/rules/design-web-pages-to-work-on-mobile-and-tablets-screens-aka-responsive-web-design)
title: Does your application's interface fit in a small screen resolution?
guid: 2e41f20a-377a-4142-95c7-b64cd5177871
uri: does-your-applications-interface-fit-in-a-small-screen-resolution
created: 2012-11-27T02:02:11.0000000Z
authors: []
related: []
redirects: []

---

One side effect of having busy forms is that it doesn't scale down.

<!--endintro-->

Each user prefers to have their own resolution. You must check if your controls will fit on the user's screen. Think about on which computers your application will run, and what devices will display it. To be on the safe side, it is advisable to fit your controls on a 1024 x 768px screen. Our projector has that resolution and it may well be used for presenting your application to the client.

::: bad  
![Figure: Bad example - Form is too large to fit inside 1024x768px resolution](../../assets/InterfaceResBadExample.jpg)  
:::

::: good  
![Figure: Good example - Form fits inside any screen resolution](../../assets/InterfaceResGoodExample.jpg)  
:::

The potential solutions for this problem are:

1. Reorder and move the controls around on the form.
2. Implement Tab pages.
3. Use a wizard type interface, with Next, Back and Finish.
4. Create multiple forms each containing a subset of the controls.
5. Create a menu based form where the items are categories that some form controls fall under.
Similar to VS. Net's Tools -&gt; Options.
6. Hide unimportant controls and add the option to show them if necessary

See [Adam Cogan - Microsoft is onto something here](http://www.adamcogan.com/2012/11/18/microsoft-is-onto-something-here) from 2012:

> I am amazed how good the split screen is so you can be reading email while continuing to watch that movie.
 One thing developers need to be aware of when building apps, is to consider the size for the different resolutions in particular when an application is snapped. On the Surface, the snap view divides the screen up into ¼ and ¾, but this will be different on different devices (actually the snap view is always 342 pixels) so you really need to get into responsive designing. For a good user experience, keep the left snap view for reading, not interactive stuff like filling in forms.
 The great thing for developers is the way you test. With Visual Studio 2012, the emulator simulates the Surface perfectly.

::: good
![Figure: The Surface screen allows you to place two apps side by side](SurfaceScreen.jpg)
:::
