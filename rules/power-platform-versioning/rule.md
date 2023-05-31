---
type: rule
title: Do you version Power Platform solutions before deploying?
uri: power-platform-versioning
authors:
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
created: 2023-05-31T00:33:53.607Z
guid: 59161602-c554-4098-8fc2-b9adf4ee1228

---

If you're not versioning Power Platform Apps before each deployment, you could be setting yourself up for a world of confusion. A lack of versioning can lead to difficulties in tracking changes, resolving issues, and managing the development lifecycle.

The solution is straightforward: Add a version to your Power Platform Apps before every deploy. This way, you can keep track of what functionality is contained in a particular solution release.

<!--endintro-->

## The Version Format
It's not enough to simply add a version number; the format of the version number is equally crucial. We recommend using the format Year.Month.Day.Iteration because it helps to accurately track the release, providing a chronological snapshot of the deployment history.

For example, if you're deploying the second iteration of a solution on the 31st of May 2023, the version number would be **2023.05.31.02**. This format immediately communicates when the version was deployed and how many iterations were released on the same day.

## The Description
Adding a comment to the description with the version number, the author, and a short description provides additional context for each version. This practice aids in communication among team members and serves as a reference point for future troubleshooting or development work.

An example of a good description would be: **Version 2023.05.31.02 - John Doe - Added new form validation rules**. This description provides clear information about the version number, who made the changes, and a brief summary of what those changes were.

## Practical Examples
Let's consider two scenarios - one following these rules, and one not.

::: greybox
Bob is a Power Platform developer. He makes changes to a Power App and deploys it without adding a version number or updating the description. A week later, a user reports an issue that emerged after Bob's changes. However, Bob can't remember exactly what changes he made, and without a version number or updated description, it's difficult for him and his team to trace back the changes and fix the issue.
:::
::: bad
Figure: Bad example - Bob didn't use a version number and it came back to bite him
:::

::: greybox
Alice also works as a Power Platform developer. When she makes changes to a Power App, she adds a version number following the Year.Month.Day.Iteration format before deploying. She also updates the description with the version number, her name, and a summary of the changes. When a user reports an issue related to her changes, Alice and her team can easily trace back to the version that caused the problem. They can quickly understand what changes were made and by whom, enabling them to efficiently resolve the issue.
:::
::: good
Figure: Good example - Alice versioned her solution nicely and she was able to resolve reported issues quickly and easily
:::

In conclusion, consistently versioning your Power Platform solutions before deploying, using a clear and informative format, and updating the description with relevant details will significantly improve your change management, issue resolution, and overall development process. Remember that good practices today save troubleshooting time tomorrow.    
