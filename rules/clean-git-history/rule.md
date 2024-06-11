---
seoDescription: Maintaining a clean and transparent Git history is crucial for codebase readability and understanding changes made over time.
type: rule
title: Do you have a clean git history?
uri: clean-git-history
authors:
  - title: Gordon Beeming
    url: https://www.ssw.com.au/people/gordon-beeming/
  - title: Daniel Mackay
    url: https://ssw.com.au/people/daniel-mackay
related:
  - use-squash-and-merge-for-open-source-projects
  - write-a-good-pull-request
redirects: []
created: 2024-02-22T00:00:00.000Z
guid: af3e6656-97b6-424c-b608-be3dd004ba89
---

Maintaining a clean git history is important for readability and understanding the changes that have been made to a codebase. This is especially important when working in a team, as it allows you to see the changes that have been made to a file over time, and who made them. This can be useful for debugging, and for understanding why a particular change was made.

Things that create a good git history include:

<!--endintro-->

- Granularity of commits
- Descriptive commit messages
- Easy to maintain (i.e. easily revert an entire feature)
- Never lose history

## Squashing Pull Requests

`youtube: https://www.youtube.com/watch?v=0chZFIZLR_0`
**Video: Git MERGE vs REBASE: Everything You Need to Know (4 min)**

Squashing commits is the process of combining multiple commits into a single commit. This allows for the repository history to reflect changes to the application over time, rather than individual commits making up a feature which can be hard to follow as they give little context to the feature that the commit is being added for.

## Good Pull Request titles

When creating a pull request, it's important to have a clear and descriptive title. This is important when looking back at the git history, as it allows you to see at a glance what changes were made in a particular pull request.

## Preserving file history

Often developers will move files around and have major changes to the contents leading to the file history being lost as the the operation will be seen as a delete and add file because of the differences in contents.

This can be avoided by using the `git mv` command to move files, or by breaking up the operation into smaller chunks i.e.: change content and then move the file as separate commits.\
[📝 Git Tips - Making structural and content changes (4 min)](https://www.youtube.com/watch?v=u0CtXbQ-ggY)

## Merging multiple repositories

Sometimes you have a system that was designed in multiple repositories, and you want to merge them back together. This can be a complex process, but it's important that you know what to do when this situation comes up in order to not lose history.

:::greybox
**Source tip**

The process of a source tip is to stop using source code from 1 repository as of certain date, and start using it from another repository.

This process leads to a situation where you have a couple of projects/folders of code all being added to a repository as a new commit, and developers would need to look in an alternate place to see the history of that portion of the codebase.
:::
:::bad
Figure: Bad example
:::

:::greybox
**Merge multiple repository histories into one**

It's important when combining git repositories that you bring all the history with you. This means that even if the files were added physically to a new repository today, developers will be able to see all the commits originally created in the original repository.
:::
:::good
Figure: Good example
:::

## Writing descriptive commit messages

It's important to have descriptive names for commits so that you can easily keep track of what was achieved after each commit was applied. Knowing what was achieved when the commits were made will make it easier to retroactively squash related commits as you'll know what work was done. In addition having descriptive commit messages makes it easier for a reviewer to see what you were trying to achieve in your pull request.

Read more about [writing descriptive commit messages](/use-emojis-in-your-commits).

## Conclusion

Maintaining a clean git history is important for readability and understanding the changes that have been made to a codebase over the lifetime of the repository.

Below is a summary of the things that create a good git history and the methods to achieve them:

|                               | Granularity of commits | Descriptive commit messages | Easy to maintain | Never lose history |
| ----------------------------- | ---------------------- | --------------------------- | ---------------- | ------------------ |
| Squashing Pull Requests       | ✅                     | ✅                          | ✅               |                    |
| Good Pull Request titles      |                        | ✅                          | ✅               |                    |
| Preserving file history       |                        |                             | ✅               | ✅                 |
| Merging multiple repositories |                        |                             | ✅               | ✅                 |
