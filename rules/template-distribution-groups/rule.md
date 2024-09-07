---
seoDescription: Learn how to avoid email template headaches by using distribution groups instead of individual names, and discover the benefits of managing roles with ease.
type: rule
title: Email Templates - Do you use distribution groups instead of individuals?
uri: template-distribution-groups
authors:
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
created: 2022-05-23T23:41:13.679Z
guid: a2379859-dc7f-499a-88a7-d6961ac0da07
---

Email templates are an important way to communicate standard emails that should be sent. Usually, these emails need to be sent to a specific person. It is easy to fall into the trap of addressing the templates to that person. This method leads to problems because when that person needs to change, there could be hundreds of locations to change and those locations may not be visible.

So, what are the solutions?

<!--endintro-->

### Point to a role

Instead of an individual, it is better to address the name of a role. For example, if the person is in charge of the product then you might call them "The Product Champion". This title, means that if the responsible person changes then it is a matter of changing who "The Product Champion" is rather than updating that person everywhere in your system.

The problem is that people may have difficulty finding out who "The Product Champion" is, or they may have to navigate your intranet to find them.

### Use a distribution group

So, the gold standard is to setup a [distribution group](https://docs.microsoft.com/en-us/exchange/recipients-in-exchange-online/manage-distribution-groups/manage-distribution-groups) that represents this role. Using the distribution group, people know what email to send to immediately, and the responsible people can be swapped out easily.

#### Managing people assigned to distribution groups

When you create and manage the distribution group, try to keep in mind who is going to be included in the distribution group.

If the group is to be used in the "To" field of an email then start the group with "The" and limit it to just one person (e.g. TheProductChampion). That way, the person can be directly addressed in the email as per [who to put in the "To:" field](/do-you-know-who-to-put-in-the-to-field).

If the group will be used in the "Cc" field of an email, then try to end it with an "s" to indicate it is a plural (e.g. AccountManagers). That way people know they shouldn't use this group for the "To:" field.

#### Keeping distribution groups up-to-date

To make sure distribution groups are always up-to-date it is also important to have a regular script that runs to check for empty distribution groups that need updates.

::: bad
![Figure: Bad example - Someone is directly addressed](badexamplepiersaddresseddirectlyredbox.png)
:::

::: ok
![Figure: OK example - A moniker is used](okayexampleproductchampionmonikerusedredbox.png)
:::

::: good
![Figure: Good example - A distribution group is used](goodexampleproductchampiondistributiongroupusedredbox.png)
:::
