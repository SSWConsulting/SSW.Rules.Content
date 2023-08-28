---
type: rule
archivedreason: 
title: Schema - Do you know how to provide best database schema document?
guid: d2aab625-6ce6-4e66-94f6-e6f1f54efe2f
uri: how-to-provide-best-database-schema-document
created: 2019-11-22T22:47:26.0000000Z
authors:
- title: Adam Cogan
  url: /people/adam-cogan
- title: Christian Morford-Waite
  url: /people/christian-morford-waite
related: []
redirects:
- schema-do-you-know-how-to-provide-best-database-schema-document

---

You should not provide a database schema via several screen captures - it has little information about the details. A well-formatted Word document may be providing more details information, but it is not easy to maintain the document to keep it up-to-date. The best way is to automatically generate your document with a tool.

<!--endintro-->

We recommend and use [Red-Gate SQL Doc](https://www.ssw.com.au/ssw/Standards/DeveloperGeneral/SQLservertools.aspx#SqlDoc) to produce chm help files or html pages of the database schema. SQL Doc also allows you to run via the command line so you can include the generation in your build process to be automatically created.

We have also have used other available tools in the past, such as [Apex SQL Doc](https://www.ssw.com.au/ssw/Standards/DeveloperGeneral/SQLservertools.aspx#ApexSqlDoc).

Alternatively, you can use SQL Management Studio to generate a Database diagram.
1.	Connect to your database using SQL Server Management Studio
2.	Create a new Database Diagram, by right-clicking  **Database Diagrams**
 **<img src="SqlDiagramNew.png" alt="" style="margin:5px;">Figure: New Database Diagram
** 
3.	A popup will appear. Shift-Click to select all the tables then click  **Add**
![](SqlDiagramSelectingTables.png) **Figure: Selecting tables for diagram
** 
4.	You will see tables populate behind the dialogue box, once complete click  **Close**
![](SqlDiagramTablesPopulated.png) **Figure: Tables populated
** 
5.	Click off the tables in the diagram and  **Ctrl+A** to Select all
6.	Right-Click one of the tables in the diagram and perform the following


> a.	Select  **Table View | Standard** from the menu
> 
> b.	Select  **Autosize Selected Tables** from the menu
> <img src="SqlDiagramStandardAutoSize.png" alt="" style="margin:5px;width:532px;"> **Figure: Changing the database table diagram to Standard View and Autosize
> **


7.	Right-click the diagram background and select  **Show Relationship Labels**
![](SqlDiagramShowRelationshipLabels.png) **Figure: Show Relationship Labels
** 
8.	Move the tables around so that the Relationship Labels are clearly visible.

**Note:** You will need to screenshot the diagram as using the copy to clipboard function removes the “Allow Nulls” checkmarks.
![](SqlDiagramNorthwindSchema.png) **Figure: Northwind Database Schema
**
