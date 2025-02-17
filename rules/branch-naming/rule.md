---
type: rule
tips: ""
title: Do your branches have a naming convention?
seoDescription: Using effective branch naming conventions with PBI numbers, descriptive names, and structured formats to enhance collaboration and traceability.
uri: branch-naming
authors:
  - title: Christian Morford-Waite
    url: https://ssw.com.au/people/christian-morford-waite
related:
  - do-you-know-when-to-branch-in-git
  - clear-meaningful-names
created: 2025-01-02T15:40:00.000Z
guid: a97fa64d-7684-4220-8042-0b3be889aa9d
---

Have you ever looked at the list of branches in your repository and not know what they were for?

Consistent naming conventions in source control systems help improve collaboration, clarity, and organization across teams. Using meaningful branch names with PBI numbers enhances traceability and reduces [merge debt](/merge-debt).

<!--endintro-->

Always remember to:

- **Include a PBI number** - This makes it easy to track the purpose of the branch, reduces confusion, and provides context
- **Use lowercase kebab style naming** - Keeps the name easy to read and compatible with a wide range of systems
- **Be descriptive** - Clearly indicate the purpose or content of the branch
- **Keep it short** - Use concise yet meaningful names
- **Extra: Use categories for improved organization** - If your repository has many branches or you want to keep them organized, adding a prefix such as "feature", "bugfix", or "hotfix" is beneficial

::: info
**Note:** Release branches should always include a prefix (e.g., release/) to distinguish them from other branch types and keep them organized.
:::

---

::: greybox
* SomeUser-patch-3   
* fix-styling-issue  
* redirects   
* update-package-version   
* fix-stuff
:::
::: bad
Figure: Bad example - Poorly named branches missing PBI numbers
:::

::: greybox
* 1463-collection-categories   
* 1506-fix-storage-variable-yaml   
* 1299-update-third-party-dependencies
:::
::: ok
Figure: OK example - Branches with PBI numbers and meaningful names
:::

::: greybox
* feature/3421-add-search-functionality
* bugfix/4578-fix-date-formatting-issue
* hotfix/9845-patch-payment-api-timeout
* release/2.3.1
:::
::: good
Figure: Good example - Branches with category prefixes
:::

::: greybox
{{ CATEGORY }}/{{ PBI NUMBER }}-{{ DESCRIPTION }}   
:::
::: good
Figure: Good example - Recommended naming format
:::

## ❌ Avoid using `SomeUser-patch-1`

GitHub's automatically generated branch names like patch-1, patch-2, etc., are convenient for quick edits but lack context, making it difficult to identify the changes introduced. These branches are often used for typo fixes or minor documentation updates that are immediately raised as pull requests. 

To improve clarity, use a descriptive name instead, such as `fix-readme-typo` instead of `patch-1`.
