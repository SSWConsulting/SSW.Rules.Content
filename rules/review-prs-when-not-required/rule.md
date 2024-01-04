---
type: rule
title: Do you still review Pull Requests when you are not a required viewer?
guid: 2e3f7d09-8004-4de5-a393-b8341e123534
uri: review-prs-when-not-required
created: 2023-10-06T00:00:00.0000000Z
authors:
- title: Gordon Beeming
  url: https://ssw.com.au/people/gordon-beeming
- title: Matt Goldman
  url: https://ssw.com.au/people/matt-goldman
related: 
- use-branch-protection
- checked-by-xxx
redirects: 
- still-review-pull-requests-when-you-are-not-a-required-viewer

---

As a repository maintainer you would generally setup a branch policy which may include a certain number of reviewers before a pull request can be completed, this could also include that certain reviewers are required instead of this being wide open to just anybody. This is a great way to ensure that code is reviewed before it is merged into the main branch.

However, this does not mean that you should not review pull requests that you are not required to review.

<!--endintro-->

Let's take a look at some of the benefits of reviewing pull requests, even if you are not a required reviewer.

As a junior developer, you may not feel comfortable reviewing a senior developer's code, but you should. You may not be able to provide any feedback around standards and best practices, but you can ask questions. This is a great way to learn and understand why the senior developer did something a certain way.

When you ask questions in a pull request, you are giving the author the opportunity to take a step back and think about what they have done and how they've done it, explain their thought process and potentially where you could learn more about the approach. Alternatively, you could point out a different way of achieving the same result which could be a better approach and they could change their PR.

* ✅ You could learn something new
* ✅ The author could learn something new
* ✅ Congrats... you've just created some micro-documentation that may never have existed before

The more people have approved a pull request, the more confidence you can have that more people in the team have looked at and agree that the code should be merged into the branch. This is effectively the same approach as getting a "Checked by xxx" on an email, see [Do you use 'Checked by xxx'?](/checked-by-xxx/).

* ✅ Shows the team you understand and agree with the code changes
