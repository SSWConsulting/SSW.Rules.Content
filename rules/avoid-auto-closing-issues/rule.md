---
seoDescription: "Avoid closing GitHub Issues prematurely by not linking them to PRs—use alternative terms instead of 'closes' or 'fixes.'"
type: rule
title: Do you avoid linking issues to PRs in GitHub?
uri: avoid-auto-closing-issues
authors:
  - title: Brady Stroud
    url: https://www.ssw.com.au/people/brady-stroud
  - title: Gordon Beeming
    url: https://www.ssw.com.au/people/gordon-beeming
created: 2023-07-17T08:40:45.591Z
guid: 97504e80-fe64-427b-9a66-2b6508689411

---

GitHub provides a way to link issues to PRs. This is useful to see what PRs are associated with what issues. However, when you make this link, the issue will close when the PR is merged.

This is not a good idea because it can cause Issues to be closed prematurely. This can lead to confusion and lost work.

Luckily, GitHub provides a way to avoid this auto-closing behavior by using alternative terms when linking issues to PRs.

<!--endintro-->

Issues should not be closed until all the tasks are complete and have a done comment as per [closing PBIs with context](/close-pbis-with-context/).

::: bad
![Figure: Bad example - Linking Issues to PRs might cause premature closing](bad-link-issues-prs.png)
:::

### Disabling auto-close at the repository level

If your team prefers to keep the linking functionality but disable the auto-close behavior, repository administrators can now turn this off in the repository settings:

1. Go to **Settings** | **General**
2. Scroll down to the **Issues** section
3. Deselect **Auto-close issues with merged linked pull requests**

See [Managing the automatic closing of issues in your repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-auto-closing-issues) for more details.
