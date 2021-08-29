---
type: rule
archivedreason: 
title: Do you allow multiple options rather than forcing a best fit?
guid: ba5a75e4-a372-4369-bd05-7e9510fd8592
uri: allow-multiple-options
created: 2021-07-01T20:47:00.0000000Z
authors:
- title: Piers Sinclair
  url: https://ssw.com.au/people/piers-sinclair
related: []
redirects:
  - storing-all

---

As a developer, we don't always think of the importance of the reporting that the business and marketing professionals use years down the track. It is so easy to give a data entry form a combo box, when a multi-checked list would be a better choice...

<!--endintro-->

::: bad
![Figure: Bad example - Able to select only one Project Type on Dynamics](storing-all-bad.png)
:::

::: good
![Figure: Good example - Able to select multiple Skills from combo box on Dynamics](storing-all-good.png)
:::

Case in point, a project form that has a field called "Skill” (that includes technologies). When a user is entering their project the technologies used may include some Angular, heaps of .NET, and a database like Cosmos DB. When you only have one choice, the obvious thing they can do, is pick the technology that they presume will take up the most development time. Maybe they choose .NET and never think of it again.

Then the problem is later down the track... there is no record of the front end (being Angular) nor the database (being Cosmos DB). Then you have the poor marketing people making uninformed decisions, spending their promotional $$$ based on missing data. If they can't tell which front end tech is growing or dying, they are spending money like a crapshoot in the casino!

These bad decision have enormous impacts on the growth of the business! 🔥

`youtube: https://www.youtube.com/watch?v=5eXx67EY_y4`

`youtube: https://www.youtube.com/watch?v=wLR0e48gou0`

