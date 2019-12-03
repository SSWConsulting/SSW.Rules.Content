---
type: rule
archivedreason: 
title: Schema - Do you know how to provide best database schema document?
guid: d2aab625-6ce6-4e66-94f6-e6f1f54efe2f
uri: how-to-provide-best-database-schema-document
created: 2019-11-22T22:47:26.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Christian Morford-Waite
  url: https://ssw.com.au/people/christian-morford-waite
related: []
redirects:
- schema-do-you-know-how-to-provide-best-database-schema-document

---


<p>​​​​​​​​You should not provide a database schema via several screen captures - it has little information about the details. A well-formatted Word document may be providing more details information, but it is not easy to maintain the document to keep it up-to-date. The best way is to automatically generate your document with a tool.<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p>We recommend and use&#160;<a href="https&#58;//www.ssw.com.au/ssw/Standards/DeveloperGeneral/SQLservertools.aspx#SqlDoc">Red-Gate SQL Doc</a>&#160;to produce chm help files or html pages of the database schema. SQL Doc also allows you to run via the command line so you can include the generation in your build process to be automatically created.</p><p>We have also have used&#160;other available tools in the past, such as&#160;<a href="https&#58;//www.ssw.com.au/ssw/Standards/DeveloperGeneral/SQLservertools.aspx#ApexSqlDoc">Apex SQL Doc</a>.​<br></p><p>Alternatively, you can use SQL Management Studio to generate a Database diagram.<br>1. Connect to your database using SQL Server Management Studio<br>2. Create a new Database Diagram, by right-clicking <strong>Database Diagrams</strong></p><dd class="ssw15-rteElement-FigureNormal"><img src="/PublishingImages/SqlDiagramNew.png" alt="" style="margin&#58;5px;" /><br>Figure&#58; New Database Diagram<br></dd><p>3. A popup will appear. Shift-Click to select all the tables then click <strong>Add</strong></p><p><strong></strong><b><img src="/PublishingImages/SqlDiagramSelectingTables.png" alt="" style="margin&#58;5px;width&#58;391px;" /><br></b></p><dd class="ssw15-rteElement-FigureNormal">Figure&#58; Selecting tables for diagram<br></dd><p>4. You will see tables populate behind the dialogue box, once complete click <strong>Close</strong></p><p><strong></strong><b><img src="/PublishingImages/SqlDiagramTablesPopulated.png" alt="" style="margin&#58;5px;width&#58;428px;" /><br></b></p><dd class="ssw15-rteElement-FigureNormal">Figure&#58; Tables populated<br></dd><p>5. Click off the tables in the diagram and <strong>Ctrl+A</strong> to Select all<br>6. Right-Click one of the tables in the diagram and perform the following<br></p><blockquote style="margin&#58;0px 0px 0px 40px;border&#58;none;padding&#58;0px;"><p>a. ​Select <strong>Table View | Standard</strong> from the menu<br></p><p>b. ​​Select <strong>Autosize Selected Tables</strong> from the menu&#160;<br></p><p><img src="/PublishingImages/SqlDiagramStandardAutoSize.png" alt="" style="margin&#58;5px;width&#58;532px;" /><br></p><dd class="ssw15-rteElement-FigureNormal">Figure&#58; Changing the database table diagram to Standard View and Autosize​<br></dd></blockquote><p>7. Right-click the diagram background and select <strong>Show Relationship Labels</strong></p><p><strong></strong><b><img src="/PublishingImages/SqlDiagramShowRelationshipLabels.png" alt="" style="margin&#58;5px;width&#58;298px;" /><br></b></p><dd class="ssw15-rteElement-FigureNormal">Figure&#58; Show Relationship Labels<br></dd><p>8. Move the tables around so that the Relationship Labels are clearly visible.<br></p><p><strong>Note&#58;&#160;</strong>You will need to&#160;screenshot&#160;the diagram as using the copy to clipboard function removes the “Allow Nulls” checkmarks.<br><br></p><p><img src="/PublishingImages/SqlDiagramNorthwindSchema.png" alt="" style="margin&#58;5px;width&#58;688px;" /><br></p><dd class="ssw15-rteElement-FigureNormal">Figure&#58; Northwind Database Schema<br></dd><p><br><br></p><p><br><br></p>


