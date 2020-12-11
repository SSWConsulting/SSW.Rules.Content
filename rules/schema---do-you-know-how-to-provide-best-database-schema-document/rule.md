---
type: rule
archivedreason: 
title: Schema - Do you know how to provide best database schema document?
guid: d2aab625-6ce6-4e66-94f6-e6f1f54efe2f
uri: schema---do-you-know-how-to-provide-best-database-schema-document
created: 2019-11-22T22:47:26.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 99
  title: Christian Morford-Waite
related: []

---


<p>​​​​​​​​You should not provide a database schema via several screen captures - it has little information about the details. A well-formatted Word document may be providing more details information, but it is not easy to maintain the document to keep it up-to-date. The best way is to automatically generate your document with a tool.<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p>We recommend and use <a href="https://www.ssw.com.au/ssw/Standards/DeveloperGeneral/SQLservertools.aspx#SqlDoc">Red-Gate SQL Doc</a> to produce chm help files or html pages of the database schema. SQL Doc also allows you to run via the command line so you can include the generation in your build process to be automatically created.</p><p>We have also have used other available tools in the past, such as <a href="https://www.ssw.com.au/ssw/Standards/DeveloperGeneral/SQLservertools.aspx#ApexSqlDoc">Apex SQL Doc</a>.​<br></p><p>Alternatively, you can use SQL Management Studio to generate a Database diagram.<br>1.	Connect to your database using SQL Server Management Studio<br>2.	Create a new Database Diagram, by right-clicking <strong>Database Diagrams</strong></p><dd class="ssw15-rteElement-FigureNormal"><dl class="ssw15-rteElement-ImageArea"><img src="SqlDiagramNew.png" alt="" style="margin:5px;" /></dl>Figure: New Database Diagram<br></dd><p>3.	A popup will appear. Shift-Click to select all the tables then click <strong>Add</strong></p><dl class="ssw15-rteElement-ImageArea"><img src="SqlDiagramSelectingTables.png" alt="" style="margin:5px;width:391px;" /></dl><dd class="ssw15-rteElement-FigureNormal">Figure: Selecting tables for diagram<br></dd><p>4.	You will see tables populate behind the dialogue box, once complete click <strong>Close</strong></p><dl class="ssw15-rteElement-ImageArea"><img src="SqlDiagramTablesPopulated.png" alt="" style="margin:5px;width:428px;" /></dl><dd class="ssw15-rteElement-FigureNormal">Figure: Tables populated<br></dd><p>5.	Click off the tables in the diagram and <strong>Ctrl+A</strong> to Select all<br>6.	Right-Click one of the tables in the diagram and perform the following<br></p><blockquote style="margin:0px 0px 0px 40px;border:none;padding:0px;"><p>a.	​Select <strong>Table View | Standard</strong> from the menu<br></p><p>b.	​​Select <strong>Autosize Selected Tables</strong> from the menu <br></p><dl class="ssw15-rteElement-ImageArea"><img src="SqlDiagramStandardAutoSize.png" alt="" style="margin:5px;width:532px;" /></dl><dd class="ssw15-rteElement-FigureNormal">Figure: Changing the database table diagram to Standard View and Autosize​<br></dd></blockquote><p>7.	Right-click the diagram background and select <strong>Show Relationship Labels</strong></p><dl class="ssw15-rteElement-ImageArea"><img src="SqlDiagramShowRelationshipLabels.png" alt="" style="margin:5px;width:298px;" /></dl><dd class="ssw15-rteElement-FigureNormal">Figure: Show Relationship Labels<br></dd><p>8.	Move the tables around so that the Relationship Labels are clearly visible.<br></p><p><strong>Note: </strong>You will need to screenshot the diagram as using the copy to clipboard function removes the “Allow Nulls” checkmarks.<br><br></p><dl class="ssw15-rteElement-ImageArea"><img src="SqlDiagramNorthwindSchema.png" alt="" style="margin:5px;width:688px;" /></dl><dd class="ssw15-rteElement-FigureNormal">Figure: Northwind Database Schema<br></dd><p><br><br></p><p><br><br></p>


