---
seoDescription: Mastering forms with intuitive navigation by including "Back" and "Undo" buttons to streamline interactions and enhance user experience.
type: rule
title: Do you include "Back" and "Undo" buttons on every form?
uri: include-back-and-undo-buttons-on-every-form
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
created: 2014-03-14T00:22:00.000Z
guid: 3fbae7db-7cec-4daa-8371-47261cd6117b
---

Following on from including a URL, almost every form should have a Back and an Undo button which takes you back to the previous screen, or reverses the last action. This is just like Outlook (see figure below), it has a Back button to take you to the previous folder and an Undo button.

<!--endintro-->

::: good
![Figure: Good example - Back & Undo buttons in Outlook Advanced toolbar](outlookviewbar.jpg)
:::

**Notes:**

- "Back" button should only be implemented if different views can be shown in the same window
- Don't put "Undo" buttons on non data entry forms such as a Print Preview form

The list of forms/URLs and the order in which they have been accessed should be stored in a DataSet held in memory (like IE) - not saved to disk.

For example:

| **Menu**    | **Action**                                                       | **Undo**             | **Back**    |
| ----------- | ---------------------------------------------------------------- | -------------------- | ----------- |
| Cut         | Remember: Remember Text and Cursor Position <br>Cut To Clipboard | Return to Remember   | n/a         |
| Save Record | Remember old values <br>Execute procCustomerSave <br>Close Form  | Return to Old values | Reopen form |

Sample code implementation in the [SSW .NET Toolkit](https://ssw.com.au/ssw/NETToolkit).
