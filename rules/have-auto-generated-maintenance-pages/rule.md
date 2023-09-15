---
type: rule
archivedreason: 
title: Do you have auto-generated maintenance pages on every project ?
guid: 13cf7a86-c170-438a-8072-d894b12e5f8d
uri: have-auto-generated-maintenance-pages
created: 2016-11-28T18:52:32.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-have-auto-generated-maintenance-pages-on-every-project

---

Nowadays, most application are dealing with Data. And it would be nice to have maintenance pages to manage data (select, insert, update and delete).

We recommend you create the maintenance pages by netTiers. [netTiers](https://github.com/netTiers/netTiers/wiki/Getting-Started) is a set of open source code templates used in CodeSmith for object-relational mapping. It automatically generates a personalized Data Tiers application (on a base of a SQL Server Database) in just a few minutes. With the application it generated, you can manage data of a web application easily and efficiently.

Please follow these steps to create your maintenance pages.

<!--endintro-->

1. [Download](http://www.codesmithtools.com/) CodeSmith.
2. Download .netTiers and extract to a folder (e.g., C:\Program Files\NetTiers)
3. Install CodeSmith.
4. Run C:\Program Files\NetTiers\NetTiers.cst.
5. Set requires properties following instructions.

![Figure: Properties Window](NetTiersConfig.jpg)  
6. Generate.
7. Open the solution.
8. Build it and run it in IE.
9. Congratulations! It's up and running.

![Figure: The application is running](RunNorthwind.jpg)  


Code Smith enables to do this generate with a single command. If you want to generate it again, just run this command.


```bash
cs D:\DataDavidBian\Personal\New12345\NetTiers.csp
```

Figure: An example of command line of Code Smith for NorthWind
We recommend you put this command in a file called "\_Regenerate.bat" and add it in the solution in case you will generate it again in future.
