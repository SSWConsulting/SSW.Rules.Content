---
type: rule
title: Do you standardize AD group names?
seoDescription: Standardize AD group names to simplify management and reduce
  confusion, using a consistent format that includes entity, resource, or
  service information.
uri: do-you-standardise-ad-group-names
authors:
  - title: Chris Briggs
    url: https://ssw.com.au/people/chris-briggs
  - title: Stanley Sidik
    url: https://ssw.com.au/people/stanley-sidik
  - title: Chris Schultz
    url: https://ssw.com.au/people/chris-schultz/
related:
  - groups-in-microsoft-365
redirects:
  - do-you-standardize-ad-group-names
created: 2015-02-16T00:13:41.000Z
archivedreason: null
guid: 6681c17d-fa8f-4187-8bed-a0df63f0e90c
---

The use of standardized group names is a simple yet crucial step towards easier management. Reducing the number of AD groups will make it simpler to manage and allow new staff to figure out what's what faster.

**You can save yourself countless confused conversations by standardizing AD Group Names.**

<!--endintro-->

::: info
Warning: Be very careful if you are renaming groups - permissions can break, especially if the group is sync'd to Entra ID (formerly Azure AD).
:::

For example, this is a list of AD groups associated with products:

::: greybox
SSWSugarLearningAlerts\
 Alerts CodeAuditor\
 SEC_SSW-LinkAuditor-Devs\
 timepro-devs
:::
::: bad
Figure: Bad Example – With no consistency, it is difficult to know the correct name for an AD group
:::

::: greybox
SSWSugarLearningAlerts\
 SSWCodeAuditorAlerts\
 SEC_SSWLinkAuditorDevs\
 SEC_SSWTimeProDevs
:::
::: good
Figure: Good Example – By standardizing the names of AD groups it saves confusion
:::

::: info
**Note:** For large organizations, a better way is to use a type of group (eg. Local or Global)... then the entity it is associated to… then the resource (or service).

**Examples:**

- **L-LocalGroupName-SYD-EntityName-SP-Sharepoint-** becomes **L-SYD-SP-SSW-Users**
- **G-GlobalGroupName-SYD-EntityName-SP-Sharepoint-** becomes **G-SYD-SP-SSW-Users**
:::

### Types of groups

It is also important to differentiate between Distribution groups (or other groups with mail enabled), and Security groups. Distribution groups should have names that are clear, that work well for an email address - for example, **SSWRulesDevs**. Security groups should have the prefix It is **SEC\_**, so that it is clear they are security groups (and cannot receive email), e.g. **SEC_VPNUsers.**
