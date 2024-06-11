---
seoDescription: When to use User Controls? Master recurring or shared logic and promote code reuse with these reusable UI elements.
type: rule
title: Do you know when to use User Controls?
uri: do-you-know-when-to-use-user-controls
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
created: 2014-03-14T02:45:00.000Z
guid: 38779435-f4d8-42eb-89e6-f8c24293a876
---

User controls allow you to have groups of elements which can be placed on forms.

<!--endintro-->

❌ **Bad**: User controls can be really misused and placed in forms where they shouldn't be. An example of that is shown below, under the components directory the user controls placed and used only _once_ at a time during the application flow. There is much more coding responsibility on the developer to load those controls correctly one at a time inside the main form.

::: bad
![Figure: Bad example - All the forms in the application are user controls](badusercontrols.gif)
:::

::: bad
![Figure: Bad example - All of the controls on this form are on a user control, but are only used once](badusercontrol.gif)
:::

✅ **Good**: User Controls are best used for recurring or shared logic either on the same form or throughout the application. This encourages code reuse, resulting in less overall development time (especially in maintenance). Example, the figure below shows the good use of User Controls, the address control is repeated three times but coded once.

::: good
![Figure: Good example - User controls are only used for shared controls](goodusercontrol.gif)
:::

::: good
![Figure: Good example - The Address User Control is repeated](usercontrol.gif)
:::

**Exception**: User controls can be made for tab pages (e.g Tools | Options) and search pages. This allows the breakdown of complex forms, and development by different developers.

::: ok
![Figure: User controls are OK in tab pages (exception)](usercontrolintabform.jpg)
:::

### Summary

✅ The pros of User Controls are:

- You can use a user control more than once on the same form eg. Mailing Address, Billing Address
- You can reuse logic in the code behind the controls e.g. Search control
- User controls are less prone to visual inheritance errors
- When used in a form with multiple tab pages - and each tab page potentially having a lot of controls, it is possible to put each tabpage into a separate user control
- Reduce lines of generated code in the designer by splitting it into multiple files
- Allow multiple persons to work on different complex tabpages

❌ However the cons are:

- You lose the **AcceptButton** and **CancelButton** properties from the Designer eg. OK, Cancel, Apply. Therefore the OK, Cancel and Apply buttons cannot be on User Controls
