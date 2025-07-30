---
seoDescription: Educate developers on permission granting processes and best practices to ensure secure and efficient resource access.
type: rule
title: Do you know how to educate your developers?
uri: educate-your-developer
authors:
  - title: Ash Anil
    url: https://www.ssw.com.au/people/ash-anil-anil/
related:
  - warn-then-call
created: 2024-03-05T04:17:56.338Z
guid: d0b5fc44-9396-4a93-9ab2-4c1111e6959c
---

To ensure that developers have a clear understanding of how permissions are granted, it's important to educate them on the process.

<!--endintro-->

User sends an email with a task to grant access to a resource and SysAdmins grant it. A developer wouldn't know how a SysAdmin granted the permission.

::: bad
![Bad Example - Issac wouldn't how he was added to GitHub](2024-03-05_16-34-15.jpg)
:::

As a SysAdmin, call a developer on Teams and share the screen to show how you would grant permission to a resource. Warn them before calling as per [Calling - Do you warn then call?](/warn-then-call/)

## Steps to effectively educate your developers

- Start by explaining the importance of granting permissions correctly and securely.
- Show developers how to navigate to the appropriate access control section in the relevant platform (e.g., Azure, AWS, SharePoint).
- Demonstrate how to select the specific resource or application for which permissions need to be granted.
- Emphasize the principle of least privilege and guide developers on granting only the necessary permissions.
- Provide examples of common scenarios where specific permissions are required and explain how to grant them.
- Encourage developers to ask questions and seek clarification during the process.
